// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import AppComponent from './App/index.vue'

Vue.config.productionTip = false

/* eslint-disable no-new */
const vm = new Vue({
    el: '#app',
    components: {
        app: AppComponent,
    },
    render: h => h('app'),
})
vm.init()