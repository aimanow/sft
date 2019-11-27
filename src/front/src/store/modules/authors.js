import {GetAuthorDiscussions} from '@/api'

export default {
  namespaced: true,
  state: {
    authors_discussion: [],
    paginationSetting:{
      total_pages: null,
      total_items: null,
      items_per_page: null,
    }
  },
  mutations: {
    clereAuthorsDiscussions(state){
      state.authors_discussion = []
      state.paginationSetting = {
        total_pages: null,
        total_items: null,
        items_per_page: null,
      }
    },
    setAuthorsDiscussions(state, payload){
      state.authors_discussion.push({items: payload.items, page: payload.page})
      state.paginationSetting = {
        total_pages: payload.total_pages,
        total_items: payload.total_items,
        items_per_page: payload.items_per_page,
      }
    }
  },
  actions:{
    getAuthorDiscussions({commit}, {id, page}){
      return GetAuthorDiscussions({id, page}).then(res => {
        commit('setAuthorsDiscussions', res.data)
        return res.data
      })
    }
  }

}
