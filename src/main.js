import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
// import { createStore } from 'vuex'



loadFonts()

const app = createApp(App)

app.use(router)
  .use(store)
  .use(vuetify)
  .mount('#app')

