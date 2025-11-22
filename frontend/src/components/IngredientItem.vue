<template>
  <li
    class="category__item"
    @click="$emit('toggleIngredient', ingredient)"
    :class="{
      'category__item--selected': selectedIngredients.includes(ingredient.id),
    }"
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
    }
  },
};
</script>
