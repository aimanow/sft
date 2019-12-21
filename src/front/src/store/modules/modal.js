export default {
  namespaced: true,

  state: {
    modals: []
  },

  mutations: {
    add(state, modal) {
      state.modals.push(modal)
    },

    closeAllModal(state) {
      state.modals = []
    },

    remove(state, num) {
      state.modals.splice(num, 1)
    }
  },

  actions: {
    addModal(ctx, {name, data}) {
      ctx.commit('add', {
        name,
        data
      })
    },

    closeModal(ctx, name) {
      for (let i = ctx.state.modals.length - 1; i >= 0; i--) {
        let modal = ctx.state.modals[i]
        if (modal.name === name) {
          ctx.commit('remove', i)
        }
      }
    },

    openLoginModal(ctx) {
      ctx.dispatch('addModal', {
        name: 'Login',
        success: () => {
        },

        cancel: () => {

        }
      })
    }
  }
}
