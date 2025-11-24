<template>
  <li class="reciepe">
    <div class="reciepe__step">
      <span class="reciepe__step-text reciepe__step-text--m">{{ reciepe.step }}</span>
      <span class="reciepe__step-text reciepe__step-text--s">шаг</span>
    </div>
    <div class="reciepe__text">
      <p>{{ reciepe.text }}</p>
    </div>
  </li>
</template>

<script>
export default {
    props: {
        reciepe: {
            type: Object,
            required: true,
        }
    }
}
</script>

<style lang="less">
.reciepe {
  display: flex;
  align-items: center;
  column-gap: 20px;

  &__step {
    padding: 36px 46px;
    background-color: @orange;
    border-radius: 16px;
  }

  &__step-text {
    &--m {
      margin-right: 2px;
      font-size: 48px;
    }

    &--s {
      font-size: 24px;
      color: fade(@light, 60%);
    }
  }

  &__text {
    display: flex;
    align-items: center;
    width: 100%;
    padding: 15px;
    background-color: @white-bg;
    border-radius: 12px;
    min-height: 100px;
  }
}
</style>
