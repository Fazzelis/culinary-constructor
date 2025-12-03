<template>
  <button class="button" title="Подобрать рецепты">
    <slot></slot>
  </button>
</template>

<style lang="less">
.button {
  padding: 25px 50px;
  gap: 8px;
  border-radius: 16px;
  border: 3px solid @orange;
  background-color: @orange;

  &:hover {
    background-color: @light;
  }

  &:focus-visible {
    background-color: @light;
  }
}
</style>
