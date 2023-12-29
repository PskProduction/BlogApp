<template>
  <div>
    <h2>Выход</h2>
    <button @click="logout">Выйти из аккаунта</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    isLoggedIn: Boolean,
  },
  methods: {
    async logout() {
      try {
        const csrftoken = this.$cookies.get('csrftoken');
        const response = await axios.post('/api/auth/logout/', {}, {headers: {'X-CSRFToken': csrftoken}});

        console.log('Logout successful', response.data);
        this.$emit('update:isLoggedIn', false);
        this.$emit('update:isAdmin',  false);
        this.$router.push('/');
        this.$cookies.remove('authToken');
        this.$cookies.remove('isSuperuser')
      } catch (error) {
        console.error('Logout failed', error.response.data);
      }
    },
  },
};
</script>
