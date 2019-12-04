import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import { createRouter } from './router'
import { createStore } from './store'
import Lang from 'vuejs-localization'
//import VueCircleSlider from 'vue-circle-slider'
const VueScrollTo = require('vue-scrollto')
import '@/assets/scss/style.scss'
//import 'vuetify/lib/src/stylus/components/_app.styl'
//import 'vuetify/lib/src/stylus/components/_progress-circular.styl'
import 'vuetify/src/stylus/app.styl'
import Vuetify, {
  VApp,  // required
  VLayout,
  VFlex,
  VContainer,
  VPagination,
  VProgressCircular,
  VBtn,
  VIcon,
  VCard,
  VCardText,
  VCardActions,
  VSpacer,
  VDialog,
  VSlider,
  VAlert
} from 'vuetify/lib'

Vue.use(Vuetify, {
  components: {
    VApp,
    VLayout,
    VFlex,
    VContainer,
    VPagination,
    VProgressCircular,
    VBtn,
    VIcon,
    VCard,
    VCardText,
    VCardActions,
    VSpacer,
    VDialog,
    VSlider,
    VAlert
  }
})
Vue.use(VueScrollTo, {
  offset: -90
})
Lang.requireAll(require.context('@/lang', true, /\.js$/))

// LANGUAGE AUTO DETECTOR
let userLang = 'en'
if (process.client) {
  userLang = navigator.language || navigator.userLanguage
  try {
    userLang = userLang.split('-')[0]
  } catch (e) {}
  const validLangs = ['ru', 'en', 'de']
  if (validLangs.indexOf(userLang) < 0)
    userLang = 'en'
}
Vue.prototype.$defaultLang = userLang

// init modules
Vue.use(Lang, { default: userLang })
const baseURL = 'https://test.sft.space/api/public'
Vue.prototype.$axios = axios.create({ baseURL, withCredentials: true })
Vue.prototype.$baseUrl = 'https://test.sft.space'
Vue.config.productionTip = false


export async function createApp ({
  beforeApp = () => {},
  afterApp = () => {}
} = {}) {
  const router = createRouter()
  const store = createStore()


  await beforeApp({
    router,
    store,

  })

  const app = new Vue({
    router,
    store,
    render: h => h(App)
  })

  const result = {
    app,
    router,
    store,

  }

  await afterApp(result)

  return result
}
