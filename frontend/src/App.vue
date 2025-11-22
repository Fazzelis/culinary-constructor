<template>
  <div>
    <PageHeader />
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
import PageHeader from "./components/PageHeader.vue";

export default {
  components: { PageHeader },
};
</script>

<style lang="less">

</style>