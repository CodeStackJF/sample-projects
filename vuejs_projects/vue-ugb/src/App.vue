<script setup></script>

<template>
  <NavBarHeader />
  <div class="container" style="margin-top: 20px; border: solid 1px black">
    <router-view />
  </div>
</template>

<style scoped></style>


<script>
import NavBarHeader from '@/components/NavBarHeader.vue';

export default {
  components: {
    NavBarHeader
  },
  setup() {
    
  },
}
</script>
