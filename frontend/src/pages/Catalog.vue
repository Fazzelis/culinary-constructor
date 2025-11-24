<template>
  <div class="catalog">
    <div class="catalog__container container">
      <div class="catalog__info">
        <h1 class="catalog__title title">Каталог</h1>
        <span class="catalog__counter"
          >Найдено рецептов: {{ dishList.length }}</span
        >
      </div>
      <dish-list :dishList="dishList" />
      <div class="catalog__pagination pagination">
        <my-button-s class="pagination__item">1</my-button-s>
      </div>
    </div>
  </div>
</template>

<script>
import SvgTagIngredient from "../assets/icons/SvgTagIngredient.vue";
import SvgTagTime from "../assets/icons/SvgTagTime.vue";
import DishList from "../components/DishList.vue";
import MyButtonS from "../components/UI/MyButtonS.vue";

export default {
  components: { SvgTagIngredient, SvgTagTime, MyButtonS, DishList },
  data() {
    return {
      dishList: [
        {
          id: 1,
          img: "/dish1_big.png",
          countIngredients: 3,
          time: "1 час",
          name: "Паста болоньезе",
          description:
            "Блюдо итальянского происхождения, разновидность сервировки пасты, а также используемый при такой сервировке мясной соус",
        },
        {
          id: 2,
          img: "/dish1_big.png",
          countIngredients: 3,
          time: "1 час",
          name: "Паста болоньезе",
          description:
            "Блюдо итальянского происхождения, разновидность сервировки пасты, а также используемый при такой сервировке мясной соус",
        },
      ],
    };
  },
};
</script>

<style lang="less">
.catalog {
  &__container {
    display: flex;
    flex-direction: column;
    row-gap: 60px;
  }

  &__title {
    text-align: center;
  }

  &__info {
    display: flex;
    flex-direction: column;
    align-items: center;
    row-gap: 8px;
  }

  &__pagination {
    margin-inline: auto;
  }
}
</style>
