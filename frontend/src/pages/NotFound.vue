<template>
  <div class="notfount">
    <div class="notfound__container container">
      <h1 class="notfound__title title">Блюдо не найдено</h1>
      <img src="/notfound.png" alt="" width="550" height="550">
    </div>
  </div>
</template>

<script>
export default{
    methods: {
        scrollTop() {
            window.scrollTo({ top: 0, behavior: "smooth" });
        }
    },
    beforeMount() {
        this.scrollTop()
    }
}
</script>

<style lang="less">
.notfound {
  &__container {
    display: flex;
    flex-direction: column;
    align-items: center;
    row-gap: 16px;
  }

  &__title {
    text-align: center;
  }
}
</style>
