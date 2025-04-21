<script setup lang="ts">
import type { Todo } from "~/types/todo";

const props = defineProps<{ todo: Todo }>();
</script>

<template>
  <div>
    <NuxtLink :to="`/todos/${todo.id}`">{{ todo.title }}</NuxtLink>
    <button>Delete</button>
  </div>
</template>
