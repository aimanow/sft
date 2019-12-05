import {
  CreateNewDiscussion,//*
  GetDiscussions,//*
  GetAllDiscussion,//*
  GetDiscussionsTop, //*
  GetDiscussionsLast, //*
  ToggleDiscusionFav,//*
  ToggleDiscusionFreeze,//*
  GetDiscussion,
  //GetDiscussionAspects, // not necassery*
  GetDiscussionArguments, //*
  AddDiscussionArguments
} from '@/api'

export default {
  namespaced: true,

  state: {
    current_discussion: null,
    thesisId: null,
    discussions: [],
    discussion: null,
    discussion_aspects: [],
    selected_aspects: [],
    discussion_arguments: [],
    discussion_argument_new: true,
    argument_id: null,
    argument_thesis: null,
    argument_thesises: {},
    thesises: {},
    resDiscussionArguments: null,
    discussionButton: true,
    searchedDiscusion: [],
    discussionsTop: [],
    discussionsLast: [],
    discussionsAll: [],
    removedFavDisc: [],
    removedFavAuthorDisc: [],
    paginationSetting: {
      total_pages: null,
      total_items: null,
      items_per_page: null,
    }
  },
  mutations: {
    addCustomAspect(state, aspect) {
      state.discussion_aspects.push(aspect)
    },//*
    setCurrentDiscussion(state, payload) {
      state.current_discussion = payload
    },//*
    setThesisId(state, payload) {
      state.thesisId = payload
    },//*
    setArgumentThesises(state, payload) {
      state.argument_thesises[payload.argument_id] = payload.items
      payload.items.forEach((thesis) => {
        state.thesises[thesis.id] = thesis
      })
    },//*
    updateArgumentThesis(state, payload) {
      if (state.argument_thesises[payload.argument_id]) {
        state.argument_thesises[payload.argument_id].find((thesis, index) => {
          if (thesis.id === payload.thesis_id) {
            thesis.votes.mean_x = payload.mean_x
            thesis.votes.mean_y = payload.mean_y
            if (thesis.votes.my_vote == null)
              thesis.votes.my_vote = {}
            thesis.votes.my_vote.x = payload.x
            thesis.votes.my_vote.y = payload.y
            // thesis.message = '123'
          }
        })
      }
    },//*
    setRemovedFavDisc(state, payload) {
      state.removedFavDisc = payload
    },//*
    setRemovedFavAuthor(state, payload) {
      state.removedFavAuthorDisc = payload
    },//*
    setPaginationSetting(state, { total_pages, total_items, items_per_page }) {
      state.paginationSetting = { total_pages, total_items, items_per_page }
    },//*
    setAllDiscusion(state, { page, items }) {
      state.discussionsAll.push({ page, items })
    },//*
    setFilteredDiscusion(state, payload) {
      state.searchedDiscusion = payload
    },//*
    setSelectedAspects(state, payload) {
      state.selected_aspects.push(payload)
    },//*
    deleteSelectedAspects(state, payload) {
      state.selected_aspects = state.selected_aspects.filter(function(item) {
        return item !== payload
      })
    },
    toggleDiscussionButton(state, payload) {
      payload ? state.discussionButton = payload : state.discussionButton = !state.discussionButton
    }, //*
    setDiscussionsList(state, list) {
      state.discussions = list
    },//*
    setDiscussion(state, item) {
      state.discussion = item
    },
    setDiscussionsTop(state, payload) {
      state.discussionsTop = payload.items
    },//*
    replaceDiscussionLast(state, { id, is_favorite }) {
      state.discussionsLast.find((disc, index) => {
        if (disc.id == id) {
          state.discussionsLast[index].is_favorite = is_favorite
        }
      })
    },//*
    replaceDiscussionTop(state, { id, is_favorite }) {
      state.discussionsTop.find((disc, index) => {
        if (disc.id == id) {
          state.discussionsTop[index].is_favorite = is_favorite
        }
      })
    },//*
    replaceDiscussionAll(state, { id, is_favorite, is_frozen, page }) {
      state.discussionsAll.find((disc, index) => {
        if (disc.page == page) {
          state.discussionsAll[index].items.find((d, i) => {
            if (d.id == id) {
              state.discussionsAll[index].items[i].is_favorite = is_favorite
              state.discussionsAll[index].items[i].is_frozen = is_frozen
            }
          })
        }
      })
    },//*
    setDiscussionsLast(state, payload) {
      state.discussionsLast = payload.items
    },//*
    // setDiscussionAspects (store, aspects) {
    //   store.discussion_aspects.push(aspects)
    // },// not necassery*
    replaceDiscussionArgument(state, { id, opinion_ratio }) {
      state.discussion_arguments.find((arg, index) => {
        if (arg.id == id) {
          state.discussion_arguments[index].opinion_ratio = opinion_ratio
        }
      })
    }, //*
    setArgumentId(state, id) {
      state.argument_id = id
    }, //*
    setDiscussionArguments(state, payload) {
      state.discussion_arguments.splice(0, state.discussion_arguments.length)
      payload.items.forEach((item) => {
        state.discussion_arguments.push(item)
      })
      state.resDiscussionArguments = payload
    }, //*
    pushDiscussionArgument(state, payload) {
      state.discussion_arguments.push(payload)
    }, //*
    pushDiscussionThesis(state, payload) {
      state.argument_thesis = null
      state.argument_thesis = payload
    }, //*


  },

  actions: {
    createNewDiscussion(store, data) {
      return CreateNewDiscussion(data) //*
    },
    toggleDiscusionFav(ctx, id) {
      return ToggleDiscusionFav(id).then(res => {
        return res.data
      })
    },//*
    ToggleDiscusionFreeze(ctx, id) {
      return ToggleDiscusionFreeze(id).then(res => {
        return res.data
      })
    },//*
    getDiscussions(store) {
      return GetDiscussions()
        .then(response => {
          store.commit('setDiscussionsList', response.data)
        })
    },

    getDiscussion(store, id) {
      return GetDiscussion(id)
        .then(response => {
          store.commit('setDiscussion', response.data)
          return response
        })
    },//*
    getDiscussionsTop({ commit }) {
      return GetDiscussionsTop().then(res => {
        commit('setDiscussionsTop', res.data)
      })
    },//*
    getDiscussionsLast({ commit }) {
      return GetDiscussionsLast().then(res => {
        commit('setDiscussionsLast', res.data)
      })
    },//*
    getDiscussionsAll({ commit, state }, page) {
      if (state.discussionsAll.length == 0) {
        return GetAllDiscussion(page).then(res => {
          commit('setAllDiscusion', { items: res.data.items, page })
          commit('setPaginationSetting', {
            total_pages: res.data.total_pages,
            total_items: res.data.total_items,
            items_per_page: res.data.items_per_page,
            itemsPerPage: 1
          })
          return res.data
        })
      } else if (!state.discussionsAll.some(item => {
        return item.page == page
      })) {
        return GetAllDiscussion(page).then(res => {
          commit('setAllDiscusion', { items: res.data.items, page })
          return true
        })
      }

    },
    // getDiscussionAspects (store, id) {
    //   return GetDiscussionAspects(id)
    //     .then(response => {
    //       store.commit('setDiscussionAspects', response.data)
    //       return response
    //     })
    // },//*

    getDiscussionArguments(store, id) {
      return GetDiscussionArguments(id)
        .then(response => {
          store.commit('setDiscussionArguments', response.data)
          return response
        })
    },//*

    addDiscussionArguments(store, { id, data }) {
      return AddDiscussionArguments(id, data)
    }
  }
}
