<template>
  <div id="app">
    <site-header :is-logged-in="isLoggedIn" @logout="logout"/>
    <router-view v-model:is-logged-in="isLoggedIn" :is-admin="isAdmin"/>
  </div>
</template>

<script>
import SiteHeader from '@/components/SiteHeader.vue';

export default {
  name: 'App',
  components: {
    SiteHeader,
  },
  data() {
    return {
      isLoggedIn: false,
      isAdmin: false,
    };
  },
  methods: {
    login(token, isAdmin) {
      localStorage.setItem('token', token);
      this.isLoggedIn = true;
      this.isAdmin = isAdmin;
    },
    logout() {
      localStorage.removeItem('token');
      this.isAdmin = false;
      this.isLoggedIn = false;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
  margin: 50px;
}

h1 {
  font-size: 2em;
  margin-bottom: 20px;
}

textarea {
  width: 100%;
  margin-bottom: 10px;
  padding: 5px;
}

button {
  padding: 5px 10px;
}
</style>
