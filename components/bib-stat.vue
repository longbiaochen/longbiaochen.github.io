<template>
  <div id="statistics">
    <span><mark>CCF-A类（一作及通讯）： {{ccf_a}}</mark></span>
    <span>CCF-B类（一作及通讯）：{{ccf_b}}</span>
    <span>科睿唯安《期刊引证报告》分区（一作及通讯）： I区 {{jcr_i}} II区 {{jcr_ii}} III区 {{jcr_iii}} IV区 {{jcr_iv}}</span>
    <span>总论文数： {{total}}</span>
  </div>
</template>

<script>
module.exports = {
  props: ['path', 'source'],
  data: function() {
    return {
      items: null,
      total: 0,
      recent: 0,
      ccf_a: 0,
      ccf_b: 0,
      jcr_i: 0,
      jcr_ii: 0,
      jcr_iii: 0,
      jcr_iv: 0,
      cn_core: 0
    }
  },
  created: function() {
    var loadItems = function(cb) {
      var el = document.getElementById('publications-embed');
      if (el && el.textContent) {
        try {
          var data = JSON.parse(el.textContent);
          if (data && data.items && data.items.length) {
            cb(data.items);
            return;
          }
        } catch (e) {}
      }
      axios.get(this.path + this.source).then(function(response) {
        cb(response.data.items);
      });
    }.bind(this);
    loadItems(function(items) {
      this.items = items;
      this.total = this.items.length;
      this.recent = _.filter(this.items, function(item) {
        return item.date > 2015;
      }).length;
      function hasTag(item, name) {
        return _.some(item.tags || [], function(t) { return t.tag === name; });
      }
      function countPair(a, b) {
        return _.filter(this.items, function(item) {
          return hasTag(item, a) && hasTag(item, b);
        }).length;
      }
      // CCF-A
      this.ccf_a = countPair.call(this, 'CCF-A', 'FIRST') + countPair.call(this, 'CCF-A', 'CORRESPONDING');
      // CCF-B
      this.ccf_b = countPair.call(this, 'CCF-B', 'FIRST') + countPair.call(this, 'CCF-B', 'CORRESPONDING');
      this.jcr_i = countPair.call(this, 'JCR-I', 'FIRST') + countPair.call(this, 'JCR-I', 'CORRESPONDING');
      this.jcr_ii = countPair.call(this, 'JCR-II', 'FIRST') + countPair.call(this, 'JCR-II', 'CORRESPONDING');
      this.jcr_iii = countPair.call(this, 'JCR-III', 'FIRST') + countPair.call(this, 'JCR-III', 'CORRESPONDING');
      this.jcr_iv = countPair.call(this, 'JCR-IV', 'FIRST') + countPair.call(this, 'JCR-IV', 'CORRESPONDING');
      // Chinese Core
      this.cn_core = _.filter(this.items, function(item) {
        return _.includes(item.extra, '核心期刊');
      }).length;
    }.bind(this));
  },
  computed: {
    filteredItems: function() {
      if (!this.items || !this.items.length) {
        return [];
      }
      return _.filter(this.items, function(item) {
        var jcr = ['JCR-I', 'JCR-II', 'JCR-III', 'JCR-IV'];
        return _.some(item.tags || [], function(t) { return jcr.indexOf(t.tag) >= 0; }) &&
            _.some(item.tags || [], function(t) { return t.tag === 'CORRESPONDING'; });
      });
    }
  }
}
</script>

<style scoped>
#statistics {
  font-style: italic;
}
</style>
