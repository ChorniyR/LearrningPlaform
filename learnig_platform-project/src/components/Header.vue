<template>
  <q-layout view="hHh lpR fFf">
    <q-header bordered class="bg-primary text-white" height-hint="98">
        <q-toolbar>
            <q-toolbar-title>
            <q-avatar>
            <img src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Bananas.svg">
            </q-avatar>
            Courses platform
        </q-toolbar-title>

        <q-btn dense flat round icon="menu" @click="toggleRightDrawer" />
        </q-toolbar>

        <q-tabs align="left">
            <q-route-tab to="/page1" label="Home" />
            <q-route-tab to="/page2" label="Store" />
            <q-route-tab to="/page3" label="Profile" />
        </q-tabs>
    </q-header>

    <q-drawer show-if-above v-model="rightDrawerOpen" side="right" bordered>
       
    </q-drawer>

    <q-page-container>
        <router-view/>
    </q-page-container>

  </q-layout>
</template>

<script>
import { ref } from 'vue'

export default {
    name: "Header",
    setup () {
    const rightDrawerOpen = ref(false)

    return {
        rightDrawerOpen,
        toggleRightDrawer () {
        rightDrawerOpen.value = !rightDrawerOpen.value
      }
    }
  }
}
</script>
