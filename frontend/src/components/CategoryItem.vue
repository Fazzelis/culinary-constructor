<template>
  <div class="category">
    <button
      type="button"
      class="category__name"
      :class="{ 'category__name--rotate': !openCategories[category.id] }"
      @click="$emit('toggleCategory', category.id)"
    >
      {{ category.name }}
      <SvgTriangle />
    </button>
    <transition name="category-list">
      <ul
        class="category__list"
        v-show="openCategories[category.id]"
        v-if="categoryIngredients"
      >
        <IngredientItem
          v-for="ingredient in categoryIngredients.ingredients"
          :key="ingredient.id"
          :ingredient="ingredient"
          :selectedIngredients="selectedIngredients"
          :color="categoryIngredients.color"
          @toggleIngredient="$emit('toggleIngredient', ingredient)"
        />
      </ul>
    </transition>
  </div>
</template>

<script>
import SvgTriangle from "../assets/icons/SvgTriangle.vue";
import IngredientItem from "./IngredientItem.vue";

export default {
  components: { SvgTriangle, IngredientItem },
  props: {
    category: {
      type: Object,
      required: true,
    },
    categoryIngredients: {
      type: [Object, null, undefined],
      default: null,
    },
    openCategories: {
      type: Object,
      required: true,
    },
    selectedIngredients: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="less">
.category {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  row-gap: 40px;

  &__name {
    column-gap: 8px;
    color: @light;
    font-family: @font;
    font-weight: 400;
    font-size: 32px;
    line-height: 1.25;

    svg {
      color: @orange;
      transition: all 0.3s;
    }

    &--rotate {
      svg {
        transform: rotate(180deg);
      }
    }
  }

  &__list {
    display: flex;
    column-gap: 60px;
    row-gap: 30px;
    flex-wrap: wrap;
  }
}

.category-list-move,
.category-list-enter-active,
.category-list-leave-active {
  transition: all 0.4s ease;
}
.category-list-enter-from,
.category-list-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}
</style>
