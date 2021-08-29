import { createStore } from "vuex";
import courses from "./modules/courses.module";
import lessons from "./modules/lessons.module";

export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    courses,
    lessons,
  },
});
