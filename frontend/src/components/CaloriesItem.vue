<template>
  <div class="calories">
    <div class="calories__item">
      <span class="calories__name">{{ item.name }}</span>
      <div class="calories__icon">
        <component :is="iconComponent" />
      </div>
      <div class="calories__counter">
        <span class="calories__counter calories__counter--m">{{ item.counterNum }}</span>
        <span class="calories__counter calories__counter--s">{{ item.counterText }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import SvgCalories from '../assets/icons/SvgCalories.vue';
import SvgCarbs from '../assets/icons/SvgCarbs.vue';
import SvgFats from '../assets/icons/SvgFats.vue';
import SvgProtein from '../assets/icons/SvgProtein.vue';

export default {
  components: {SvgCalories, SvgCarbs, SvgFats, SvgProtein},
  props: {
    item: {
      type: Object,
      required: true
    },
    iconComponent: { type: Object, required: true }
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