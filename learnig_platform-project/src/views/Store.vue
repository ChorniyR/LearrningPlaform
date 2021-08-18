<template>
<q-page-container>
    <div class="store row justify-around q-mt-xl">
        <q-card dark bordered class="bg-grey-9 my-card q-mb-lg" v-for="course in allCourses" :key="course.id">
            <q-card-section>
                <div class="text-h6">{{course.name}}</div>
            </q-card-section>

        <q-separator dark inset />
            <q-card-section>
                {{ course.description }}
            </q-card-section>
        <q-separator dark inset />

        <q-card-section>
            <q-btn outline color="primary" label="Details" :to="`/details/${course.id}`"></q-btn>
        </q-card-section>
    </q-card>
    </div>
</q-page-container>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
    name: "Store",
    methods: {
        ...mapActions(['fetchCourses'])
    },
    computed: mapGetters(['allCourses']),
    mounted() {
        this.fetchCourses()
    }
}
</script>


