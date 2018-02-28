import Vue from 'vue'
import Vuetify from 'vuetify'
import store from '~/store'
import router from '~/router'
import { i18n } from '~/plugins'
import App from '~/components/App'
import '~/components'

Vue.use(Vuetify)

Vue.config.productionTip = true
Vue.prototype.$baseURL = window.location.href.split('/').slice(0,4).join('/')+'/'

new Vue({
  el: '#app',
  i18n,
  store,
  router,
  ...App
})
