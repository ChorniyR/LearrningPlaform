import axios from 'axios'

export default {
  state: {
    courses: [],
    currentCourse: null,
  },
  mutations: {
    updateCourses(state, courses){
      state.courses = courses
    },
    updateCurrentCourse(state, course){
      state.currentCourse = course
    }
  },
  actions: {
    async fetchCourses({commit}){
      axios.get('courses/', {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access-token')}`
        }
      })
      .then(r => r.data.results)
      .then(courses => {
        commit('updateCourses', courses)
      })
    },
    async fetchDetails({commit}, id){
      axios.get(`/courses/${id}`, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access-token')}`
        }
      })
      .then(r => r.data)
      .then(course => {
        commit('updateCurrentCourse', course)
      })
    }    
  },
  getters: {
    allCourses: function(state){
      return state.courses
    },
    currentCourse: function (state) {
      return state.currentCourse      
    }
  }
}
