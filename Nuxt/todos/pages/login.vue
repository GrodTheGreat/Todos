<script setup lang="ts">
import { ref } from "vue";
import type { TextInput } from "~/types/types";

const username = ref<TextInput>(undefined);
const password = ref<TextInput>(undefined);

function login() {}
</script>

<template>
  <main>
    <h1>Login</h1>
    <form action="/login" method="post">
      <fieldset>
        <legend>Login</legend>
        <div>
          <label for="username">Username</label>
          <input type="text" name="username" id="username" v-model="username" />
        </div>
        <div>
          <label for="password">Password</label>
          <input
            type="password"
            name="password"
            id="password"
            v-model="password"
          />
        </div>
        <button type="submit" @click.prevent="login">Login</button>
      </fieldset>
    </form>
  </main>
</template>
