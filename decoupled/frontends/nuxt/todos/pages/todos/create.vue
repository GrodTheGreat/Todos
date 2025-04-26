<script setup lang="ts">
import { ref } from "vue";
import type { TextInput } from "~/types/types";

const title = ref<TextInput>(undefined);
const description = ref<TextInput>(undefined);

function create() {}
</script>

<template>
  <main>
    <h1>Create Todo</h1>
    <form action="" method="post">
      <fieldset>
        <legend>New Todo</legend>
        <div>
          <label for="title">Title</label>
          <input type="text" name="title" id="title" v-model="title" required />
        </div>
        <div>
          <label for="description">Description</label>
          <textarea
            name="description"
            id="description"
            v-model="description"
          ></textarea>
        </div>
        <button type="submit" @click.prevent="create">Create</button>
      </fieldset>
    </form>
  </main>
</template>
