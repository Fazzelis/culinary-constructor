<template>
  <div class="catalog">
    <div class="catalog__container container">
      <div class="catalog__info">
        <h1 class="catalog__title title">Каталог</h1>
        <span class="catalog__counter"
          >Найдено рецептов: {{ totalCount }}</span
        >
      </div>
      <dish-list :dishList="dishList" />
      <div class="catalog__pagination pagination">
        <my-button-s
          v-for="page in visiblePages"
          :key="page"
          class="pagination__item"
          :class="{ active: page === currentPage, dots: page === '...' }"
          @click="page !== '...' && goPage(page)"
        >
          {{ page }}
        </my-button-s>
      </div>
    </div>
  </div>
</template>

<script>
import { API_URL } from "../api.config";
import SvgTagIngredient from "../assets/icons/SvgTagIngredient.vue";
import SvgTagTime from "../assets/icons/SvgTagTime.vue";
import DishList from "../components/DishList.vue";
import MyButtonS from "../components/UI/MyButtonS.vue";

export default {
  components: { SvgTagIngredient, SvgTagTime, MyButtonS, DishList },
  data() {
    return {
      page: 1,
      limit: 5,
      totalPages: 0,
      totalCount: 0,
      dishList: [],
    };
  },
  methods: {
    async getDishList() {
      try {
        const response = await fetch(
          `${API_URL}/dish/all?page=${this.page}&page_size=${this.limit}`
        );
        const result = await response.json();
        this.dishList = result.dishes;
        this.totalPages = result.pagination.total_pages;
        this.totalCount = result.pagination.total_count
      } catch (e) {
        console.log("Ошибка получения списка блюд: ", e);
      }
    },
    async goPage(pageNum) {
      try {
        const response = await fetch(
          `${API_URL}/dish/all?page=${pageNum}&page_size=${this.limit}`
        );
        const result = await response.json();
        this.dishList = result.dishes;
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } catch (e) {
        console.log("Ошибка получения списка блюд: ", e);
      }
    },
  },
  computed: {
    visiblePages() {
      const total = this.totalPages;
      const current = this.currentPage;
      const delta = 2;
      const range = [];
      const rangeWithDots = [];
      let l;

      for (let i = 1; i <= total; i++) {
        if (
          i === 1 ||
          i === total ||
          (i >= current - delta && i <= current + delta)
        ) {
          range.push(i);
        }
      }

      for (let i of range) {
        if (l) {
          if (i - l === 2) {
            rangeWithDots.push(l + 1);
          } else if (i - l !== 1) {
            rangeWithDots.push("...");
          }
        }
        rangeWithDots.push(i);
        l = i;
      }

      return rangeWithDots;
    },
  },
  mounted() {
    this.getDishList();
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
