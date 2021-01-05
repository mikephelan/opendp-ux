import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import  axios from  'axios'
import GSignInButton from 'vue-google-signin-button'

Vue.config.productionTip = false
Vue.use(GSignInButton)
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

new Vue({
  router,
  store,
  render: function (h) { return h(App) }
}).$mount('#app')
