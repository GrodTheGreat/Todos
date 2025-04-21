<script setup lang="ts">
const route = useRoute();
</script>

<template>
  <p>This is Todo {{ route.params.id }}</p>
</template>
