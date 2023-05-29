<template>
  <div class="catalog">
    <div class="catalog-header section-header">Каталог общежитий</div>
    <div
        class="catalog-cards"
        v-for="dorm in $props.dormitories"
        :key="dorm.id"
    >
        <DormCard
            class="dormCard"
            :dormitory="dorm"
            @click="$router.push({path: `/dorm_info/${dorm.id}`, name: 'dorm_info-id', params: { id: dorm.id }})"
        ></DormCard>
    </div>
  </div>
</template>

<script>
import DormCard from "./DormCard";
export default {
  components: {DormCard},
  props: {
    dormitories: Array,
  }
}
</script>

<style scoped>
  .dormCard:hover{
    cursor: pointer;
  }

</style>