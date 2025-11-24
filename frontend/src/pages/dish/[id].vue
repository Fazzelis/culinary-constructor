<template>
  <div class="dish">
    <div class="dish__container container">
      <h1 class="dish__title title">{{ dish.name }}</h1>
      <div class="dish__body">
        <img
          :src="dish.img"
          alt=""
          width="450"
          height="350"
          class="dish__img"
        />
        <div class="dish__info">
          <div class="dish__info-block1">
            <div class="dish__description">
              <p>{{ dish.description }}</p>
            </div>
            <MyButton class="dish__btn">Сохранить</MyButton>
          </div>
          <div class="dish__info-block2">
            <h2 class="dish__subtitle">Энергетическая ценность</h2>
            <div class="dish__calories">
              <CaloriesItem v-for="calories in dish.caloriesList" :key="calories.id" :calories="calories">
                <SvgSquirrels />
              </CaloriesItem>
            </div>
          </div>
        </div>
      </div>
      <div class="dish__ingredients">
        <h2 class="dish__subtitle">Ингредиенты</h2>
        <ul class="dish__ingredients-list">
          <DishIngredientItem
            v-for="ingredient in dish.ingredients"
            :key="ingredient.id"
            :ingredient="ingredient"
          />
        </ul>
      </div>
      <div class="dish__reciepe">
        <ul class="dish__reciepe-list">
          <ReciepeItem
            v-for="reciepe in dish.reciepeList"
            :key="reciepe.id"
            :reciepe="reciepe"
          />
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import SvgSquirrels from "../../assets/icons/SvgSquirrels.vue";
import CaloriesItem from "../../components/CaloriesItem.vue";
import DishIngredientItem from "../../components/DishIngredientItem.vue";
import ReciepeItem from "../../components/ReciepeItem.vue";
import MyButton from "../../components/UI/MyButton.vue";

export default {
  components: {
    MyButton,
    SvgSquirrels,
    CaloriesItem,
    DishIngredientItem,
    ReciepeItem,
  },
  data() {
    return {
      dish: {
        id: 1,
        img: '/dish1_big.png',
        name: "Паста болоньезе",
        description:
          "Блюдо итальянского происхождения, разновидность сервировки пасты, а также используемый при такой сервировке мясной соус Блюдо итальянского происхождения, разновидность сервировки пасты, а также используемый при такой сервировке ",
        caloriesList: [
          {
               id: 1,
               name: 'белки',
               counterNum: 31,
               counterText: 'грамм' 
          },
          {
               id: 1,
               name: 'белки',
               counterNum: 31,
               counterText: 'грамм' 
          },
          {
               id: 1,
               name: 'белки',
               counterNum: 31,
               counterText: 'грамм' 
          },
          {
               id: 1,
               name: 'белки',
               counterNum: 31,
               counterText: 'грамм' 
          },
        ],
        ingredients: [
          {
            id: 1,
            name: "Мясной фарш",
            counter: "500 г.",
          },
          {
            id: 1,
            name: "Мясной фарш",
            counter: "500 г.",
          },
          {
            id: 1,
            name: "Мясной фарш",
            counter: "500 г.",
          },
          {
            id: 1,
            name: "Мясной фарш",
            counter: "500 г.",
          },
        ],
        reciepeList: [
          {
            id: 1,
            step: 1,
            text: "В сковороде на растительном масле обжарить мелко нарезанный лук и чеснок до характерного запаха.",
          },
          {
            id: 1,
            step: 1,
            text: "В сковороде на растительном масле обжарить мелко нарезанный лук и чеснок до характерного запаха.",
          },
          {
            id: 1,
            step: 1,
            text: "В сковороде на растительном масле обжарить мелко нарезанный лук и чеснок до характерного запаха.",
          },
        ],
      },
    };
  },
};
</script>

<style lang="less">
.dish {
  &__container {
    display: flex;
    flex-direction: column;
    row-gap: 60px;
  }

  &__body {
    display: flex;
    column-gap: 30px;
  }

  &__img {
    width: 450px;
    height: 350px;
    object-fit: fill;
    border-radius: 24px;
  }

  &__info {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  &__info-block1 {
    display: flex;
    align-items: flex-start;
    column-gap: 60px;
  }

  &__description {
    font-size: 16px;
    line-height: 1.25;
    max-width: 560px;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: normal;
  }

  &__btn {
    padding-block: 16px;
  }

  &__info-block2 {
    display: flex;
    flex-direction: column;
    align-items: center;
    row-gap: 30px;
  }

  &__calories {
    display: flex;
    column-gap: 60px;
  }

  &__ingredients {
    display: flex;
    flex-direction: column;
    row-gap: 30px;
    max-width: 800px;
    width: 100%;
    margin-inline: auto;
  }

  &__ingredients-list {
    display: flex;
    flex-direction: column;
    row-gap: 16px;
    padding: 20px;
    background-color: @white-bg;
    border-radius: 12px;
  }

  &__reciepe-list {
    display: flex;
    flex-direction: column;
    row-gap: 30px;
  }

  &__subtitle {
    text-align: center;
  }
}
</style>
