<template>
  <div class="dish-card">
    <img :src="dish.img" alt="" class="dish-card__img" width="250" height="150"/>
    <div class="dish-card__body">
      <div class="dish-card__tags">
        <dish-tag>
          <svg-tag-ingredient />
          <span class="tag__info"
            >Ингредиентов: {{ dish.countIngredients }}</span
          >
        </dish-tag>
        <dish-tag>
          <svg-tag-time />
          <span class="tag__info">Время: {{ dish.time }}</span>
        </dish-tag>
      </div>
      <div class="dish-card__info">
        <h2 class="dish-card__name">{{ dish.name }}</h2>
        <div class="dish-card__description">
          <p>{{ dish.description }}</p>
        </div>
      </div>
      <router-link
        class="dish-card__link"
        :to="{ name: 'dish', params: { id: dish.id } }"
        >Посмотреть рецепт</router-link
      >
    </div>
  </div>
</template>

<script>
import SvgTagIngredient from "../assets/icons/SvgTagIngredient.vue";
import SvgTagTime from "../assets/icons/SvgTagTime.vue";
import DishTag from "./DishTag.vue";

export default {
  components: { DishTag, SvgTagIngredient, SvgTagTime },
  props: {
    dish: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="less">
.dish-card {
  display: flex;
  align-items: center;

  &__body {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 15px 30px;
    background-color: @white-bg;
    border: 1px solid @light;
    border-top-right-radius: 12px;
    border-bottom-right-radius: 12px;
  }

  &__img {
    width: 250px;
    height: 150px;
    border-radius: 16px;
  }

  &__tags {
    display: flex;
    column-gap: 10px;
  }

  &__name {
    font-family: @font;
    font-weight: 400;
    font-size: 28px;
    line-height: 1.25;
    margin-bottom: 10px;
    transition: all 0.3s;
  }

  &__description {
    font-size: 16px;
    max-width: 354px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: normal;
  }

  &__name,
  &__description {
    text-align: center;
  }

  &__link {
    color: @light;
    transition: all 0.3s;
    cursor: pointer;

    &:hover {
      color: @orange;
    }
  }
}
</style>
