<template>
  <div class="calories">
    <div class="calories__item">
      <span class="calories__name">{{ calories.name }}</span>
      <div class="calories__icon">
        <slot></slot>
      </div>
      <div class="calories__counter">
        <span class="calories__counter calories__counter--m">{{ calories.counterNum }}</span>
        <span class="calories__counter calories__counter--s">{{ calories.counterText }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    calories: {
      type: Object,
      required: true
    }
  }
}
</script>

<style lang="less">
.calories {
  &__item {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    row-gap: 12px;
  }

  &__name {
    font-size: 14px;
  }

  &__icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 64px;
    aspect-ratio: 1;
    border-radius: 50%;
    background-color: @orange;
  }

  &__counter {
    display: flex;
    flex-direction: column;
    align-items: center;

    &--m {
      font-size: 24px;
    }

    &--s {
      font-size: 16px;
    }
  }
}
</style>