import {
  GetProfileId,//*
  GetCurrentProfile, //*
  GetProfileEducation,//*
  EditProfileEducation,//*
  EditProfileEducationScan,//*
  GetUsersTop,//*
  ToggleDiscusionAuthorFav,//*
  ToggleDiscusionAuthorLike,//*
  EditPassword,//*
  EditEmail,//*
  ChangeAvatar,//*
  GetAllAspects,//*
  ToggleAspects, //*
  GetDiscussionsFav, //*
  ToggleDiscusionFav, //*
  GetFavoritesAuthors, //*

} from '@/api'

export default {
  namespaced: true,

  state: {
    profile: null,
    profile_rewards: [],
    profile_knowledge: [],
    profile_education: {
      country: '',
      city: '',
      high_school: '',
      faculty: '',
      speciality: '',
      graduation_date: '',
      scan_url: '',
      is_verified: false
    },
    profile_current: {
      avatar_url: null,
      fullname: '',
      i_like: false,
      id: null,
      is_confirmed: false,
      is_favorite: false,
      total_likes: 0
    },
    all_aspects: [],
    favorite_aspects: [],
    favoritesDiscussion: [],
    favoritesDiscussions: [],
    favoritesAspect: [],
    usersTop: [],
    favoritesAuthors: [],
    paginationSetting: {
      total_pages: null,
      total_items: null,
      items_per_page: null,
    }
  },

  mutations: {
    setFavoritesDiscussionAuthors(state, items) {
      state.favoritesAuthors = items
    },//*
    setAllAspects(state, { page, items }) {
      state.all_aspects.push({ page, items })
    },//*
    UpdateAspects(state, { id, is_favorite, page }) {
      state.all_aspects.find((asp, index) => {
        if (asp.page == page) {
          state.all_aspects[index].items.find((a, i) => {
            if (a.id == id) {
              state.all_aspects[index].items[i].is_favorite = is_favorite
            }
          })
        }
      })
    },//*
    setUserProfile(state, profile) {
      state.profile = profile
    },//*
    //setUserKnowledges
    setCurrentProfile(state, payload) {
      state.profile_current = payload
    },//*
    setUserEducation(state, education) {
      state.profile_education = education
    },//*
    setUserTop(state, payload) {
      state.usersTop = payload
    },
    setFavoritesDiscussion(state, disc) {
      state.favoritesDiscussions = disc
    }, //*
    addCustomAspect(state, aspect) {
      state.favorite_aspects.push(aspect)
    },//*
    replaceDiscusionAuthorFav(state, { id, is_favorite }) {
      state.usersTop.find((author, index) => {
        if (author.id == id) {
          state.usersTop[index].is_favorite = is_favorite
        }
      })
    },//*
    replaceDiscusionAuthorLike(state, { id, i_like, total_likes }) {
      state.usersTop.find((author, index) => {
        if (author.id == id) {
          state.usersTop[index].i_like = i_like
          state.usersTop[index].total_likes = total_likes
        }
      })
      if (state.favoritesAuthors.length) {
        state.favoritesAuthors.find((author, index) => {
          if (author.id == id) {
            state.favoritesAuthors[index].i_like = i_like
            state.favoritesAuthors[index].total_likes = total_likes
          }
        })
      }
    },//*
    deleteFavoritesDiscussion(state, id) {
      state.favoritesDiscussions.find((disc, index) => {
        if (disc.id == id) {
          state.favoritesDiscussions.splice(index, 1)
        }
      })
    }, //*
    cleareFavoritesDiscussions(state) {
      state.favoritesDiscussions = []
    }, //*
    cleareFavoritesDiscussionAuthors(state) {
      state.favoritesAuthors = []
    }, //*
    setPaginationSetting(state, { total_pages, total_items, items_per_page }) {
      state.paginationSetting = { total_pages, total_items, items_per_page }
    },//*
    removeFavoritesDiscussionAuthors(state, id) {
      state.favoritesAuthors.find((author, i) => {
        if (author.id == id) {
          state.favoritesAuthors.splice(i, 1)
        }
      })
    }

  },

  actions: {
    toggleDiscusionAuthorFav(ctx, id) {
      return ToggleDiscusionAuthorFav(id).then(res => {
        return res.data
      })
    },//*
    toggleDiscusionAuthorLike(ctx, id) {
      return ToggleDiscusionAuthorLike(id).then(res => {
        return res.data
      })
    },//*
    GetAllAspects({ commit, state }, page = 1) {
      if (state.all_aspects.length == 0) {
        return GetAllAspects(page).then(res => {
          commit('setAllAspects', { items: res.data.items, page })
          commit('setPaginationSetting', {
            total_pages: res.data.total_pages,
            total_items: res.data.total_items,
            items_per_page: res.data.items_per_page,
            itemsPerPage: 1
          })
          return res.data
        })
      } else if (!state.all_aspects.some(item => {
        return item.page == page
      })) {
        return GetAllAspects(page).then(res => {
          commit('setAllAspects', { items: res.data.items, page })
          return true
        })
      }
    },//*
    toggleAspects(context, id) {
      return ToggleAspects(id)
    },//*
    getUserProfile(store, id) {
      return GetProfileId(id)
        .then(response => {
          store.commit('setUserProfile', response.data)
          return response
        })
    },//*
    getUserKnowledges({ commit }, id) {
      return commit + id
    },//* not api
    getCurrentProfile({ commit }) {
      return GetCurrentProfile().then(res => {
        commit('setCurrentProfile', res.data)
      })
    },//*
    editUserEducation({ commit }, { id, data }) {
      return EditProfileEducation({ id, data }).then(res => {
        commit('setUserEducation', res.data)
        return res
      })
    },//*
    editUserEducationScan(ctx, { id, scan }) {
      return EditProfileEducationScan({ id, scan })
    },//*
    getUserEducation({ commit }, id) {
      return GetProfileEducation(id)
        .then(response => {
          if (Object.keys(response.data).length > 1) {
            commit('setUserEducation', response.data)
            return response
          }

        })
    },//*
    getUsersTop({ commit }, topFilter = 1) {
      return GetUsersTop(topFilter).then(res => {
        commit('setUserTop', res.data.items)
      })
    },//*
    EditPassword(ctx, data) {
      return EditPassword(data)
    },//*
    EditEmail(ctx, data) {
      return EditEmail(data)
    },//*
    ChangeAvatar(ctx, data) {
      return ChangeAvatar(data)
    },//*
    getFavoritesDiscussion({ commit }, page) {
      GetDiscussionsFav(page).then(res => {
        commit('setFavoritesDiscussion', res.data.items)
      })
    },//*
    getFavoritesDiscussionAuthors({ commit }, page) {
      return GetFavoritesAuthors(page).then(res => {
        commit('setFavoritesDiscussionAuthors', res.data.items)
        return res.data
      })
    },//*
    deleteFavoritesDiscussion({ commit }, id) {
      return ToggleDiscusionFav(id).then(res => {
        commit('deleteFavoritesDiscussion', res.data.id)
        return res.data.id
      })
    }, //*


  }
}
