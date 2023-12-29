<template>
  <head>
    <title>Регистрация</title>
  </head>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <label for="username">Логин:</label>
      <input type="text" v-model="username" required>

      <label for="email">Email:</label>
      <input type="email" v-model="email" required>

      <label for="password">Пароль:</label>
      <input type="password" v-model="password" required>

      <label for="passwordConfirmation">Подтвердите пароль:</label>
      <input type="password" v-model="passwordConfirmation" required>

      <button type="submit">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      passwordConfirmation: "",
    };
  },
  methods: {
    async register() {
      try {
        const csrfToken = this.$cookies.get("csrftoken");

        await axios.post('/api/auth/register/', {
          username: this.username,
          email: this.email,
          password: this.password,
          password2: this.passwordConfirmation,
        }, {
          headers: {
            'X-CSRFToken': csrfToken,
          },
        });

        this.$router.push('/');
      } catch (error) {
        console.error('Registration failed', error.response.data);
      }
    },
  },
};
</script>

<style>
form {
  display: flex;
  flex-direction: column;
  width: 350px;
  margin: auto;
}

input {
  margin-bottom: 10px;
}

button {
  width: 150px;
  margin: auto;
  cursor: pointer;
}
</style>
