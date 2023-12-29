import { createRouter, createWebHistory } from "vue-router";
import PostsList from "@/components/PostsList.vue";
import Post from "@/components/PostView.vue";
import Login from "@/components/LoginComponent.vue";
import Register from "@/components/RegisterComponent.vue";
import Logout from "@/components/LogoutComponent.vue";

const routes = [
  { path: "/", component: PostsList },
  { path: "/login", name: "login", component: Login },
  { path: "/register", name: "register", component: Register },
  { path: "/logout", name: "logout", component: Logout },
  { path: "/post/:id", name: "post", component: Post },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;