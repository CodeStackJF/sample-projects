<script setup></script>

<template>
  <HeaderComponent />
  <div class="container">
    <router-view />
  </div>
</template>

<script>
  import HeaderComponent from '@/components/HeaderComponent.vue'

  export default {
    components: {
      HeaderComponent
    }
  }
</script>

<style scoped></style>
