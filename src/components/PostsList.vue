<template>
  <div>
    <h1>Список постов</h1>
    <div v-if="posts.length === 0">Нет постов</div>
    <div v-for="post in posts.results" :key="post.id" class="post-item">
      <router-link :to="'/post/' + post.id"><h2>{{ post.title }}</h2></router-link>
      <p>{{ post.content }}</p>
    </div>
    <form v-if="isAdmin" @submit.prevent="createPost" class="post-form">
      <h2>Создать новый пост</h2>
      <div>
        <label for="title">Заголовок:</label>
        <input type="text" id="title" v-model="newPost.title" required/>
      </div>
      <div>
        <label for="content">Содержание:</label>
        <textarea id="content" v-model="newPost.content" required></textarea>
      </div>

      <button type="submit">Создать пост</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
      isAdmin: this.$cookies.get('isSuperuser') === 'true',
      newPost: {
        title: '',
        content: '',
      },
      authToken: this.$cookies.get('authToken'),
    };
  },
  methods: {
    async loadPosts() {
      try {
        const response = await axios.get('/api/posts/');
        this.posts = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке постов', error);
      }
    },

    async createPost() {
      try {
        if (this.isAdmin) {
          const headers = {
            'X-CSRFToken': this.$cookies.get('csrftoken'),
            'Authorization': this.authToken,
          };

          await axios.post('/api/posts/', this.newPost, { headers });
          await this.loadPosts();
          this.newPost = { title: '', content: '' };
        } else {
          console.error('Недостаточно прав для создания поста. Требуются права суперпользователя.');
        }
      } catch (error) {
        console.error('Ошибка при создании поста', error);
      }
    },
  },
  mounted() {
    this.loadPosts();
  },
};
</script>

<style scoped>
.post-item {
  margin-bottom: 20px;
  border: 1px solid #ccc;
  padding: 10px;
}

.post-form {
  margin-top: 20px;
  border: 1px solid #ccc;
  padding: 10px;
  max-width: 400px;
}

.post-form div {
  margin-bottom: 10px;
}

.post-form label {
  display: block;
  margin-bottom: 5px;
}

.post-form input,
.post-form textarea {
  width: 100%;
  padding: 5px;
  box-sizing: border-box;
}
</style>
