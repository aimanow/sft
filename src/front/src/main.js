import Vue from 'vue';
import App from './App.vue';
import axios from 'axios';
import router from './router';
import store from './store/store.js';
import Lang from 'vuejs-localization';

const VueScrollTo = require('vue-scrollto');
import '@/assets/scss/style.scss';
import 'vuetify/src/stylus/app.styl';
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
});

Vue.use(VueScrollTo, {
  offset: -90
});
Lang.requireAll(require.context('@/lang', true, /\.js$/));

// init modules
Vue.use(Lang, { default: 'ru' });
const baseURL = 'http://localhost:5000/api/public';
Vue.prototype.$axios = axios.create({ baseURL, withCredentials: true });
Vue.prototype.$baseUrl = "http://localhost:5000";
Vue.config.productionTip = false;


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
