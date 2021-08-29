import { axiosWithJWT, error401Handler } from "../../services/api.service";

export default {
  state: {
    lessonDetails: null,
    stepDetails: null,
  },
  mutations: {
    updateStepDetails(state, stepDetails) {
      state.stepDetails = stepDetails;
    },
    updateLessonDetails(state, lessonDetails) {
      state.lessonDetails = lessonDetails;
    },
  },
  actions: {
    async fetchStepDetails({ commit }, { lesson_id, step_id }) {
      const { data } = await axiosWithJWT
        .get(`/lesson/${lesson_id}/step/${step_id}/`)
        .catch((err) => {
          error401Handler(err);
        });
      commit("updateStepDetails", data);
    },
    async fetchLessonDetails({ commit }, id) {
      const { data } = await axiosWithJWT
        .get(`/lesson/${id}`)
        .catch((err) => error401Handler(err));
      commit("updateLessonDetails", data);
    },
  },
  getters: {
    stepDetails: function(state) {
      return state.stepDetails;
    },
    lessonDetails: function(state) {
      return state.lessonDetails;
    },
    allStepsIds: function(state) {
      return state.lessonDetails.steps;
    },
    testFromStep: function(state) {
      return state.stepDetails.test;
    },
  },
};
