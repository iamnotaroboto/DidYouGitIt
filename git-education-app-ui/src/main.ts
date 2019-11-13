import Vue from 'vue';
import VueMaterial from 'vue-material';
import App from './App.vue';
import router from './router';
import 'vue-material/dist/vue-material.min.css';
import 'vue-material/dist/theme/default.css';
import store from './store';

Vue.config.productionTip = false;
Vue.use(VueMaterial);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
