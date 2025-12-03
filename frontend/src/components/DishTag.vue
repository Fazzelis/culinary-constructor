<template>
  <div class="tag">
     <slot></slot>
  </div>
</template>

<style lang="less">
.tag {
  padding: 6px 8px 6px 6px;
  display: flex;
  align-items: center;
  column-gap: 4px;
  background-color: @light;
  color: @beige;
  border-radius: 8px;
  font-size: 14px;

  svg {
    color: @orange;
  }
}
</style>
