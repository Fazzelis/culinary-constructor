<template>
  <button class="button-s" title="Найти блюдо">
    <slot></slot>
  </button>
</template>

<style lang="less">
.button-s {
  padding: 7px;
  gap: 8px;
  border-radius: 4px;
  border: 3px solid @orange;
  background-color: @orange;

  &:hover {
    background-color: @light;

    svg {
      color: @orange;
    }
  }

  &:focus-visible {
    background-color: @light;

    svg {
      color: @orange;
    }
  }
}
</style>
