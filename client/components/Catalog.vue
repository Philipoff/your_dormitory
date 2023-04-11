<template>
  <div class="catalog">
    <div class="catalog-header">Каталог общежитий</div>
    <div
        class="catalog-cards"
        v-for="(dorm, index) in $props.dormitories"
        :key="index"
    >
      <DormCard :dormitory="dorm"></DormCard>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    dormitories: Array,
  }
}
</script>

<style scoped>
  .catalog-header {
    font-size: 32px;
    margin-bottom: 30px;
  }
</style>