import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
Vue.config.devtools = true
import modules from './store/modules'

export function createStore () {
  return new Vuex.Store({
    state () {
      return {
        menu: false,
        dialog: false,
        alertMessage: '',
        alertType: null
      }
    },
    mutations: {
      openMenu(state, status) {
        state.menu = status
      },
      openDialog(state, payload){
        state.dialog = true
        if(typeof payload === 'string'){
          state.alertMessage = payload
          return
        }
        if(payload.hasOwnProperty('type')){
          state.alertMessage = payload.message
          state.alertType = payload.type
        }else{
          state.alertMessage = payload.message
        }

      },
      closeDialog(state){
        state.dialog = false
        state.alertMessage = ''
        state.alertType = null
      },
      setDialog(state, payload){
        state.dialog = payload
      },
    },

    actions: {
    },

    modules
  })
}
