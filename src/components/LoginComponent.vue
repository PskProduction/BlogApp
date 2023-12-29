<template>
  <div>
    <h2>Вход</h2>
    <form @submit.prevent="login">
      <label for="username">Логин:</label>
      <input type="text" v-model="username" required>

      <label for="password">Пароль:</label>
      <input type="password" v-model="password" required>

      <button type="submit">Войти</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    isLoggedIn: Boolean,
  },
  data() {
    return {
      username: "",
      password: "",
      authToken: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8000/api/auth/login/', {
          username: this.username,
          password: this.password,
        });

        if (response.data && response.data.token) {
          this.$cookies.set('authToken', response.data.token, {expires: '7d'});
          this.$cookies.set('isSuperuser', response.data.is_superuser, {expires: '7d'});

          this.$emit('login', response.data.token);
          this.$emit('update:isLoggedIn', true);
          console.log(response.data.is_superuser);
          this.$router.push('/');
        } else {
          console.error('Login failed. Response data or token is undefined:', response);
        }
      } catch (error) {
        console.error('Login failed', error.response ? error.response.data : error.message);
      }
    },
  },
};
</script>
