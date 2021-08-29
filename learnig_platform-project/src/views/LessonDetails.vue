<template>
<q-page-container>
  <q-virtual-scroll
    :items="heavyList"
    virtual-scroll-horizontal
  >
    <template v-slot="{ item, index }">
      <div :key="index" class="row items-center">
        <q-separator v-if="index === 0" vertical spaced />

        <q-avatar v-if="item.avatar === true" class="bg-black text-white q-my-md">
          {{ index % 10 + 1 }}
        </q-avatar>

        <q-item
          v-else
          dense
          clickable
        >
          <q-item-section>
            <q-item-label>
              #{{ index }} - {{ item.label }}
            </q-item-label>
          </q-item-section>
        </q-item>

        <q-separator vertical spaced />
      </div>
    </template>
  </q-virtual-scroll> 

  <div class="data">
  <p>
    {{stepDetails}}
  </p>
  <p>
    {{lessonDetails}}
  </p>
  <p>
    {{lessonDetails && stepDetails.steps}}
  </p>
  </div>
   </q-page-container>
</template>



<script>
import { mapActions, mapGetters } from 'vuex'

const maxSize = 10000
const heavyList = []

for (let i = 0; i < maxSize; i++) {
  heavyList.push({
    label: 'Option ' + (i + 1),
    avatar: i % 5 === 0
  })
}

export default {
  name: 'TestDetails',
  methods: {
    ...mapActions(["fetchStepDetails", "fetchLessonDetails"])
  },
  computed: mapGetters(["stepDetails", "lessonDetails", "allStepsIds", "testFromStep"]),
  setup () {
    return {
      heavyList
    }
  },
  mounted () {
    this.fetchStepDetails({lesson_id: 1, step_id:1})  
    this.fetchLessonDetails(1)
  }
}
</script>
