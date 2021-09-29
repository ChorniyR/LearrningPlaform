import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Store from "../views/Store.vue";
import CourseDetails from "../views/CourseDetails.vue";
import LessonDetails from "../views/LessonDetails.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/store",
    name: "Store",
    component: Store,
  },
  {
    path: "/details/:id",
    name: "CourseDetails",
    component: CourseDetails,
  },
  {
    path: "/lesson/:id/step/:stepId",
    name: "LessonDetails",
    component: LessonDetails,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
