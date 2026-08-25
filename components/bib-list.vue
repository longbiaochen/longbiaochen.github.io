<template>
  <ol id="list">
    <li v-for="(item, itemIndex) in filteredItems" :key="itemKey(item, itemIndex)">
      <span class="series"><strong>[{{item.series}}'{{item.date}}]</strong></span>
      <span v-for="(author, aidx) in item.creators" :key="'a-' + itemIndex + '-' + aidx">
        <span :class="author.firstName">{{author.firstName}} {{author.lastName}}, </span>
      </span>
      <span class="title">{{item.title}},</span>
      <span class="proc" v-if="item.itemType=='conferencePaper'"> </span>
      <span class="publication">{{ venue(item) }}, </span>
      <span class="vol" v-if="item.volume"> vol.{{item.volume}}, </span>
      <span class="issue" v-if="item.issue"> no.{{item.issue}}, </span>
      <span class="pages" v-if="item.pages"> pp.{{item.pages}}, </span>
      <span class="date"> {{item.date}}. </span>
      <span v-for="(tag, tidx) in rankTagsOrdered(item)" :key="'t-' + itemIndex + '-' + tidx">
        <span class="rank">[{{tag.tag}}]</span>
      </span>
      <span class="online" v-if="onlineHref(item)">
        <a :href="onlineHref(item)">[Online]</a>
      </span>
    </li>
  </ol>
</template>

<script>
module.exports = {
  props: ['path', 'source', 'filter'],
  data: function() {
    return {
      items: null
    }
  },
  created: function() {
    var el = document.getElementById('publications-embed');
    if (el && el.textContent) {
      try {
        var data = JSON.parse(el.textContent);
        if (data && data.items && data.items.length) {
          this.items = _.orderBy(data.items, 'date', 'desc');
          return;
        }
      } catch (e) {}
    }
    axios.get(this.path + this.source).then(response => {
      this.items = response.data.items;
      this.items = _.orderBy(this.items, 'date', 'desc')
    });
  },
  methods: {
    itemKey: function(item, index) {
      var id = item && item.key ? item.key : '';
      return id || ((item && item.title) || '') + '|' + ((item && item.date) || '') + '|' + index;
    },
    isRankTag: function(name) {
      var r = ['CCF-A', 'CCF-B', 'CCF-C', 'JCR-I', 'JCR-II', 'JCR-III', 'JCR-IV'];
      return r.indexOf(name) >= 0;
    },
    rankTagOrder: function(name) {
      var order = ['CCF-A', 'CCF-B', 'CCF-C', 'JCR-I', 'JCR-II', 'JCR-III', 'JCR-IV'];
      var i = order.indexOf(name);
      return i >= 0 ? i : 999;
    },
    rankTagsOrdered: function(item) {
      var self = this;
      var tags = _.filter(item.tags || [], function(t) { return self.isRankTag(t.tag); });
      return _.orderBy(tags, [function(t) { return self.rankTagOrder(t.tag); }], ['asc']);
    },
    venue: function(item) {
      return item.publicationTitle || item.proceedingsTitle || '';
    },
    onlineHref: function(item) {
      if (item.DOI) {
        return 'https://doi.org/' + item.DOI;
      }
      if (item.url) {
        return item.url;
      }
      return '';
    }
  },
  computed: {
    filteredItems: function() {
      if (!this.items || !this.items.length) {
        return [];
      }
      if (!this.filter) {
        return this.items;
      }
      var tag = this.filter;
      return _.filter(this.items, function(item) {
        return _.some(item.tags || [], function(t) { return t.tag === tag; });
      });
    }
  }
}
</script>

<style scoped>
.Longbiao {
  font-weight: bold;
}

.series,
.rank {
  color: #C74350;
}

.rank{
  font-weight: bold;
}
</style>