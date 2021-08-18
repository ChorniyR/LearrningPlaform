<template>
<q-page-container>
    <h4>{{ currentCourse && currentCourse.name }}</h4>
</q-page-container>
<q-footer class="fixed-bottom row justify-center">
    <q-btn class="full-width" color="primery" text-color="white" label="Enroll" />
</q-footer>
</template>


<script>
import {mapActions, mapGetters} from 'vuex'


export default {
    name:'CourseDetails',
    methods: {
        ...mapActions(['fetchDetails']),  
    },
    computed: mapGetters(['currentCourse']),
    mounted() {
        this.fetchDetails(this.$route.params.id)
    },
}
</script>

<style lang="sass" >
@import '../styles/quasar.variables.sass'

.q-footer
    background-color: $primary
    height: 100px
</style>
