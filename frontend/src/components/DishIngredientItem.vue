<template>
  <li class="dish-ingredient">
    <div class="dish-ingredient__item">
      <span class="dish-ingredient__text">{{ ingredient.name }}</span>
      <span class="dish-ingredient__dots"></span>
      <span class="dish-ingredient__text">{{ ingredient.counter }}</span>
    </div>
  </li>
</template>

<script>
export default {
  props: {
    ingredient: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="less">
.dish-ingredient {
  font-family: monospace;

  &__item {
    display: flex;
  }

  &__text {
    white-space: nowrap;
  }

  &__dots {
    flex-grow: 1;
    border-bottom: 1px dotted @light;
    margin: 0 16px 5px;
  }
}
</style>
