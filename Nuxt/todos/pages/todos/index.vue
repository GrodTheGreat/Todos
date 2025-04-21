<script setup lang="ts">
import { ref } from "vue";
import type { Todo } from "~/types/todo";

const todos = ref<Todo[]>([
  { id: 1, title: "Todo 1", description: "This is a todo", isComplete: false },
  { id: 2, title: "Todo 2", isComplete: false },
  {
    id: 3,
    title: "Todo 3",
    description: "This is another todo",
    isComplete: true,
  },
]);
</script>
<template>
  <main>
    <h1>All Todos</h1>
    <div>
      <ul>
        <li v-for="todo in todos" :key="todo.id">
          <TodoItem :todo />
        </li>
      </ul>
    </div>
  </main>
</template>
