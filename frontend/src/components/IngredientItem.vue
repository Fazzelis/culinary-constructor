<template>
  <li
    class="ingredient"
    @click="$emit('toggleIngredient', ingredient)"
    :class="{
      'ingredient--selected': selectedIngredients.includes(ingredient.id),
    }"
    :style="{ '--ingredient-color': color }"
  >
    {{ ingredient.name }}
  </li>
</template>


<script>
export default {
  props: {
    ingredient: {
      type: Object,
      required: true,
    },
    selectedIngredients: {
        type: Object,
        required: true,
    },
    color: {
      type: String,
      default: '#000000'
    }
  },
};
</script>


<style lang="less">
.ingredient {
    position: relative;
    display: inline-block;
    padding: 30px 20px 15px 20px;
    background-color: @light;
    color: @black;
    font-family: @font;
    border-radius: 12px;
    cursor: pointer;

    &::before {
      content: "";
      position: absolute;
      top: 15px;
      left: 20px;
      width: 20px;
      height: 10px;
      background-color: var(--ingredient-color);
      transition: 0.3s;
    }

    &--selected {
      &::before {
        background-color: @light;
      }
      background-color: var(--ingredient-color);
    }
    &:hover {
      &::before {
        width: calc(100% - 40px);
      }
    }
  }
</style>