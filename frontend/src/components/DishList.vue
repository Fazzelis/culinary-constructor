<template>
  <div class="listing">
    <dish-card v-for="dish in dishList" :key="dish.id" :dish="dish" />
  </div>
</template>

<script>
import DishCard from "./DishCard.vue";

export default {
  components: { DishCard },
  props: {
    dishList: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="less">
.listing {
  display: flex;
  flex-direction: column;
  row-gap: 40px;
}
</style>
