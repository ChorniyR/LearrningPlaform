<template>
  <q-layout view="hHh lpR fFf">
    <Header />
    <router-view />
  </q-layout>
</template>

<script>
import { ref } from "vue";
import Header from "./components/Header.vue";

export default {
  name: "LayoutDefault",

  components: {
    Header,
  },

  setup() {
    return {
      leftDrawerOpen: ref(false),
    };
  },
};
</script>
