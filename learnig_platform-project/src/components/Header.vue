<template>
    <q-header bordered class="bg-primary text-white" height-hint="98">
        <q-toolbar>
            <q-toolbar-title>
            <q-avatar>
            <img src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Bananas.svg">
            </q-avatar>
            Courses platform
        </q-toolbar-title>            
        </q-toolbar>
        <div class="full-width row  justify-between">
            <q-tabs align="left">
                <q-route-tab to="/" label="Home" />
                <q-route-tab to="/store" label="Store" />
                <q-route-tab to="/page3" label="Profile"/>
            </q-tabs>
            <q-tabs align="right">
                <q-route-tab to="/login" label="Login"/>
            </q-tabs>
        </div>
    </q-header>
</template>

<script>
import { ref } from 'vue'

export default {
    name: "Header",
}
</script>
