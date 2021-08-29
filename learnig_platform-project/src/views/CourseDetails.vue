<template>
  <q-page-container>
    <h4>{{ currentCourse && currentCourse.name }}</h4>
      <q-footer class="fixed-bottom row justify-center">
    <q-btn
      class="full-width"
      color="primery"
      text-color="white"
      label="Enroll"
      v-on:click="enroll(currentCourse.id); to='/lesson/1'"
    />
  </q-footer>
  </q-page-container>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import { enroll } from "../services/courses.service"

export default {
  name: "CourseDetails",
  methods: {
    ...mapActions(["fetchDetails"]),
    enroll: (id) => {
      return enroll(id)
    }
  },
  computed: mapGetters(["currentCourse"]),
  mounted() {
    this.fetchDetails(this.$route.params.id);
  },
};
</script>

<style lang="sass">
@import '../styles/quasar.variables.sass'

.q-footer
    background-color: $primary
    height: 60px
</style>
