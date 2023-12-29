<template>
  <header>
    <nav>
      <router-link to="/">Главная</router-link>
      <router-link v-if="!isLoggedIn" to="/login">Вход</router-link>
      <router-link v-if="!isLoggedIn" to="/register">Регистрация</router-link>
      <router-link v-if="isLoggedIn" to="/logout">Выход</router-link>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'SiteHeader',
  props: {
    isLoggedIn: Boolean,
  },
};
</script>

<style>
nav {
  display: flex;
  width: 250px;
  justify-content: space-between;
}
</style>
