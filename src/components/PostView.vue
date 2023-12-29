<template>
  <div>
    <h2>{{ post.title }}</h2>
    <p>Содержимое поста: {{ post.content }}</p>
    <p>Дата публикации: <b>{{ post.created_at }}</b></p>

    <h3>Комментарии</h3>
    <div v-if="comments.length > 0">
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          {{ comment.text }} , Дата публикации: {{ comment.created_at }})
        </li>
      </ul>
    </div>
    <p v-else>No comments yet.</p>

    <div v-if="isLoggedIn" class="comment-block">
      <textarea v-model="newCommentText" placeholder="Оставьте свой комментарий"></textarea>
      <button @click="handleAddComment">Добавить комментарий</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    isLoggedIn: Boolean,
  },
  data() {
    return {
      post: {},
      comments: [],
      newCommentText: "",
    };
  },
  created() {
    const postId = this.$route.params.id;
    this.loadPost(postId);
    this.loadComments(postId);
  },
  methods: {
    loadPost(postId) {
      axios.get(`/api/posts/${postId}`)
          .then(response => {
            this.post = response.data;
          })
          .catch(error => {
            console.error("Ошибка загрузки поста:", error);
          });
    },
    loadComments(postId) {
      axios.get(`/api/posts/${postId}`)
          .then(response => {
            this.comments = response.data.comments;
          })
          .catch(error => {
            console.error("Ошибка загрузки комментариев:", error);
          });
    },
    handleAddComment() {
      const postId = this.$route.params.id;
      this.addComment(postId);
    },
    addComment(postId) {
      console.log('isLoggedIn:', this.isLoggedIn);
      if (this.isLoggedIn) {
        const csrfToken = this.$cookies.get('csrftoken');
        const authToken = this.$cookies.get('authToken');

        const headers = {
          'X-CSRFToken': csrfToken,
          'Authorization': authToken,
        };
        console.log(authToken)

        axios.post(`/api/posts/${postId}/comment/`, {text: this.newCommentText}, {headers})
            .then(() => {
              this.loadComments(postId);
              this.newCommentText = "";
            })
            .catch(error => {
              console.error("Ошибка создания комментария:", error);
            });
      } else {
        console.error("Пользователь не авторизован. Нельзя оставить комментарий.");
        this.$router.push({name: "login"});
      }
    },
  },
};
</script>

<style>
textarea {
  margin: auto auto 20px;
  width: 500px;
}

.comment-block {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
}

button {
  margin-top: 20px;
  cursor: pointer;
}

ul {
  list-style: none;
  width: 600px;
  margin: auto;
}
</style>
