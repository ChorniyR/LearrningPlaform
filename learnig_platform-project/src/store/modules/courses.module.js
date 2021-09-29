import { axiosWithJWT, error401Handler } from "../../services/api.service";

export default {
  state: {
    courses: [],
    myCourses: [],
    currentCourse: null,
  },
  mutations: {
    updateCourses(state, courses) {
      state.courses = courses;
    },
    updateCurrentCourse(state, course) {
      state.currentCourse = course;
    },
    updateMyCourses(state, myCourses) {
      state.myCourses = myCourses;
    },
  },
  actions: {
    async fetchCourses({ commit }) {
      const { data } = await axiosWithJWT
        .get("courses/")
        .catch((error) => error401Handler(error));

      commit("updateCourses", data.results);
    },
    async fetchDetails({ commit }, id) {
      const { data } = await axiosWithJWT
        .get(`/courses/${id}`)
        .catch((error) => error401Handler(error));

      commit("updateCurrentCourse", data);
    },
    async fetchMyCourses({ commit }) {
      const { data } = await axiosWithJWT
        .get("/courses/my/")
        .catch((error) => error401Handler(error));

      commit("updateMyCourses", data[0].course);
    },
  },
  getters: {
    allCourses: function(state) {
      return state.courses;
    },
    currentCourse: function(state) {
      return state.currentCourse;
    },
    myCourses: function(state) {
      return state.myCourses;
    },
  },
};
