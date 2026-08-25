<template>
  <div class="card-deck row">
    <!-- ------------------------------------- -->
    <div v-for="(item, idx) in filteredItems" :key="cardKey(item, idx)" class="card" :style="{'max-width': styles.max_width, 'min-width': styles.min_width}">
      <a :href="item.url" class="card-img"><img :src="item.img" class="card-img-top" :alt="item.title || ''" loading="lazy" decoding="async"></a>
      <div class="card-body" :style="{'padding': '0 ' + styles.padding}">
        <h5 class="card-title"> {{item.title}} </h5>
        <h6 class="card-subtitle mb-2 text-muted"> {{item.sub_title}} </h6>
        <div class="card-text">
          <div v-for="(tag, di) in (item.desc || [])" :key="'d-' + idx + '-' + di">{{ tag }}</div>
        </div>
      </div>
      <div v-if="item.button" class="card-footer">
        <a :href="item.url" class="btn btn-primary"> {{item.button}} </a>
      </div>
    </div>
    <!-- --------------------------------------->
  </div>
</template>

<script>
module.exports = {
  props: ['items', 'styles'],
  data: function() {
    return {}
  },
  methods: {
    cardKey: function(item, index) {
      if (item && item.id !== undefined && item.id !== null) {
        return String(item.id);
      }
      return (item && item.url) || (item && item.title) || String(index);
    }
  },
  computed: {
    filteredItems: function() {
      if (!this.items || !this.items.length) {
        return [];
      }
      return _.filter(this.items, function(o) { return !o.hidden; });
    }
  }
}
</script>

<style scoped>
.card-deck {
  margin: -10px -5px;
}

.card {
  margin: 10px !important;
  overflow: hidden;
}

.card-body {
  padding: 0 10px;
}

.card-img {
  padding: 0;
}

.card-img-top {
  width: auto;
  margin-left: 50%;
  transform: translateX(-50%);
  height: 180px;
  padding: 0;
  border-bottom: 1px solid rgba(0, 0, 0, 0.125);
}

.card-title {
  font-weight: bold;
  font-size: 1em;
  text-align: center;
}

.card-subtitle {
  text-align: center;
}

.card-text {
  margin-bottom: 1.5em;
}

.card-footer {
  text-align: center;
}

.card-footer a {
  padding: 0.375rem 0.75rem;
  color: #fff;
  text-decoration: none;
}
</style>
