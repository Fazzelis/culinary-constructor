<template>
  <div class="constructor">
    <div class="constructor__container container">
      <h1 class="constructor__title title">Конструктор</h1>
      <div class="constructor__body">
        <CategoryItem
          v-for="category in categories"
          :key="category.id"
          :category="category"
          :openCategories="openCategories"
          :selectedIngredients="selectedIngredients"
          @toggleCategory="toggleCategory"
          @toggleIngredient="toggleIngredient"
        />
      </div>
      <div class="constructor__info">
        <span class="constructor__counter"
          >Выбрано ингредиентов: {{ countIngredients }}</span
        >
        <MyButton @click="log">Подобрать рецепт</MyButton>
      </div>
    </div>
  </div>
</template>

<script>
import SvgTriangle from "../assets/icons/SvgTriangle.vue";
import CategoryItem from "../components/CategoryItem.vue";
import MyButton from "../components/UI/MyButton.vue";

export default {
  components: { SvgTriangle, MyButton, CategoryItem },
  data() {
    return {
      countIngredients: 0,
      openCategories: {},
      selectedIngredients: [],
      categories: [
        {
          id: 1,
          name: "Мясо",
          color: "#FFBDC8",
          ingredients: [
            {
              id: 11,
              name: "Курица",
            },
          ],
        },
        {
          id: 2,
          name: "Овощи",
          color: "#A8F792",
          ingredients: [
            {
              id: 12,
              name: "Помидор",
            },
          ],
        },
        {
          id: 3,
          name: "Фрукты",
          color: "#FFBDC8",
          ingredients: [
            {
              id: 13,
              name: "Яблоко",
            },
          ],
        },
        {
          id: 4,
          name: "Рыба",
          color: "#FFBDC8",
          ingredients: [
            {
              id: 14,
              name: "Форель",
            },
          ],
        },
      ],
    };
  },
  methods: {
    toggleCategory(id) {
      this.openCategories[id] = !this.openCategories[id];
    },
    toggleIngredient(ingredient) {
      const index = this.selectedIngredients.indexOf(ingredient.id);
      if (index === -1) {
        this.selectedIngredients.push(ingredient.id);
      } else {
        this.selectedIngredients.splice(index, 1);
      }
    },
    log() {
      console.log(this.selectedIngredients);
    },
  },
  computed: {
    countIngredients() {
      return this.selectedIngredients.length;
    },
  },
};
</script>

<style lang="less">
.constructor {
  &__container {
    display: flex;
    flex-direction: column;
    row-gap: 60px;
  }

  &__body {
    display: flex;
    flex-direction: column;
    row-gap: 50px;
  }

  &__info {
    display: flex;
    align-items: center;
    column-gap: 40px;
    margin: 0 auto;
  }
}
</style>
