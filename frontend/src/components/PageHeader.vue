<template>
  <header class="page-header">
    <div class="page-header__container container">
      <div class="page-header__logo">
        <SvgLogo />
      </div>
      <nav class="page-header__nav">
        <ul class="page-header__list">
          <li class="page-header__item">
            <router-link to="/" class="page-header__link"
              >Конструктор</router-link
            >
          </li>
          <li class="page-header__item">
            <router-link to="/catalog" class="page-header__link"
              >Каталог рецептов</router-link
            >
          </li>
        </ul>
      </nav>
      <MyInput />
    </div>
  </header>
</template>

<script>
import SvgLogo from "../assets/icons/SvgLogo.vue";
import MyInput from "./UI/MyInput.vue";

export default {
  components: { SvgLogo, MyInput },
};
</script>

<style lang="less">
.page-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100;
  padding-block: 10px;
  height: 80px;

  &::before {
    content: "";
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    @supports (backdrop-filter: blur(20px)) {
      background-color: @header;
      backdrop-filter: blur(20px);
    }
  }

  &__container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-block: 5px;
  }

  &__logo {
    color: @orange;
    z-index: 101;
  }

  &__list {
    display: flex;
    column-gap: 30px;
  }

  &__link {
    position: relative;
    user-select: none;

    &::before {
      content: "";
      position: absolute;
      bottom: -2px;
      left: -4px;
      width: 0;
      height: 1px;
      transition: 0.3s;
    }

    &:hover {
      &::before {
        background-color: @light;
        width: calc(100% + 8px);
      }
    }

    &:focus-visible {
      outline: 1px solid @orange;
      border-radius: 2px;
      outline-offset: 6px;
    }

    &:active,
    &--active,
    &.router-link-exact-active {
      color: @orange;

      &:hover {
        &::before {
          background-color: @orange;
        }
      }
    }
  }
}
</style>
