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
          :categoryIngredients="categoryIngredients[category.id]"
          @toggleCategory="toggleCategory"
          @toggleIngredient="toggleIngredient"
        />
      </div>
      <div class="constructor__info">
        <span class="constructor__counter"
          >Выбрано ингредиентов: {{ countIngredients }}</span
        >
        <MyButton>Подобрать рецепт</MyButton>
      </div>
    </div>
  </div>
</template>

<script>
import { API_URL } from "../api.config";
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
      categories: [],
      categoryIngredients: {},
    };
  },
  methods: {
    async getCategories() {
      try {
        const response = await fetch(`${API_URL}/category`);
        const result = await response.json();
        this.categories = result.categories;
      } catch (e) {
        console.log("Ошибка получения категорий: ", e);
      }
    },
    async toggleCategory(id) {
      this.openCategories[id] = !this.openCategories[id];

      if (this.openCategories[id]) {
        const saveCategory = localStorage.getItem(`${id}`);
        const category = saveCategory ? JSON.parse(saveCategory) : null;

        if (category) {
          this.categoryIngredients = {
            ...this.categoryIngredients,
            [id]: category,
          };
        } else {
          const response = await fetch(
            `${API_URL}/category/ingredients?category_id=${id}`
          );
          const result = await response.json();
          this.categoryIngredients = {
            ...this.categoryIngredients,
            [id]: result,
          };

          localStorage.setItem(`${id}`, JSON.stringify(result));
        }
      }
    },
    toggleIngredient(ingredient) {
      const index = this.selectedIngredients.indexOf(ingredient.id);
      if (index === -1) {
        this.selectedIngredients.push(ingredient.id);
      } else {
        this.selectedIngredients.splice(index, 1);
      }
    },
  },
  computed: {
    countIngredients() {
      return this.selectedIngredients.length;
    },
  },
  mounted() {
    this.getCategories();
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
    row-gap: 40px;
  }

  &__info {
    display: flex;
    align-items: center;
    column-gap: 40px;
    margin: 0 auto;
  }
}
</style>
