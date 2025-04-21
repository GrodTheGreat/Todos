<script setup lang="ts">
import { ref } from "vue";
import type { TextInput } from "~/types/types";

const username = ref<TextInput>(undefined);
const email = ref<TextInput>(undefined);
const givenName = ref<TextInput>(undefined);
const surname = ref<TextInput>(undefined);
const password = ref<TextInput>(undefined);
const confirm = ref<TextInput>(undefined);

function register() {}
</script>

<template>
  <main>
    <h1>Register</h1>
    <form action="/register" method="post">
      <fieldset>
        <legend>Register</legend>
        <div>
          <label for="username">Username</label>
          <input type="text" name="username" id="username" v-model="username" />
        </div>
        <div>
          <label for="email">Email</label>
          <input type="email" name="email" id="email" v-model="email" />
        </div>
        <div>
          <label for="given-name">First Name</label>
          <input
            type="text"
            name="given-name"
            id="given-name"
            v-model="givenName"
          />
        </div>
        <div>
          <label for="surname">Last Name</label>
          <input type="text" name="surname" id="surname" v-model="surname" />
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
        <div>
          <label for="confirm">Confirm Password</label>
          <input type="confirm" name="confirm" id="confirm" v-model="confirm" />
        </div>
        <button type="submit" @click.prevent="register">Register</button>
      </fieldset>
    </form>
  </main>
</template>
