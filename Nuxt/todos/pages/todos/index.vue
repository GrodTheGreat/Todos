<script setup lang="ts">
import { ref } from "vue";
import {
  VBtn,
  VCheckbox,
  VFab,
  VIcon,
  VList,
  VListItem,
} from "vuetify/components";

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
      <v-list lines="two">
        <v-list-item
          v-for="todo in todos"
          :key="todo.id"
          :title="todo.title"
          :subtitle="todo.description"
        >
          <template #prepend>
            <v-checkbox color="primary"></v-checkbox>
          </template>
          <template #append>
            <v-btn>
              <v-icon icon="mdi-pencil" color="warning"></v-icon>
            </v-btn>
            <v-btn>
              <v-icon icon="mdi-delete" color="error"></v-icon>
            </v-btn>
          </template>
        </v-list-item>
      </v-list>
    </div>
    <v-fab icon="mdi-plus" location="right bottom" absolute></v-fab>
  </main>
</template>
