import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Main from '@/components/pages/Main'
import About from '@/components/pages/About'
import All from '@/components/pages/All'
import Author from '@/components/pages/Author'
import Search from '@/components/pages/Search'
import Archive from '@/components/pages/Archive'
import Aspects from '@/components/pages/Aspects'
import MainDiscussion from '@/components/pages/Discussion/Main'
import AddDiscussion from '@/components/pages/Discussion/Add'
import MainProfile from '@/components/pages/Profile/Main'
import DeleteProfile from '@/components/pages/Profile/DeleteAccount'
import MainProfileEducation from '@/components/pages/Profile/Education/Main'
import EditProfileEducation from '@/components/pages/Profile/Education/Edit'
import MainProfileAreasOfKnowledge from '@/components/pages/Profile/AreasOfKnowledge/Main'
import EditProfileAreasOfKnowledge from '@/components/pages/Profile/AreasOfKnowledge/Edit'
import FavoritesProfile from '@/components/pages/Profile/Favorites'
import HistoryProfile from '@/components/pages/Profile/History'
import LogoutProfile from '@/components/pages/Profile/Logout'
import RewardsProfile from '@/components/pages/Profile/Rewards'
import SettingsProfile from '@/components/pages/Profile/Settings'
import PrivacyPolicy from '@/components/pages/PrivacyPolicy'
import TermsOfUse from '@/components/pages/TermsOfUse'
import PageNotFound from '@/components/pages/PageNotFound'

export function createRouter() {
  return new Router({
    mode: 'history',
    routes: [
      { path: '/', name: 'Main', component: Main },

      { path: '/reset_password', name: 'ResetPassword', component: Main },
      { path: '/confirm_email', name: 'ConfirmEmail', component: Main },

      { path: '/oauth/vk', name: 'OAuthVk', component: Main },
      { path: '/oauth/google', name: 'OAuthGoogle', component: Main },
      { path: '/oauth/facebook', name: 'OAuthFacebook', component: Main },

      { path: '/about', name: 'About', component: About },
      { path: '/all', name: 'All', component: All },
      { path: '/author/:id', name: 'Author', component: Author },
      { path: '/search', name: 'Search', component: Search },
      { path: '/aspects', name: 'Aspects', component: Aspects },
      { path: '/archive', name: 'Archive', component: Archive },
      { path: '/discussion/add', name: 'DiscussionAdd', component: AddDiscussion },
      { path: '/discussion/:id', name: 'Discussion', component: MainDiscussion },
      { path: '/profile/logout', name: 'Logout', component: LogoutProfile },
      { path: '/profile/settings', name: 'Settings', component: SettingsProfile },
      { path: '/profile/rewards', name: 'Rewards', component: RewardsProfile },
      { path: '/profile/history', name: 'History', component: HistoryProfile },
      { path: '/profile/favorites', name: 'Favorites', component: FavoritesProfile },
      { path: '/profile/delete', name: 'Delete', component: DeleteProfile },
      { path: '/profile/education', name: 'MainEducation', component: MainProfileEducation },
      { path: '/profile/education/edit', name: 'EditEducation', component: EditProfileEducation },
      { path: '/profile/areas-of-knowledge', name: 'MainAreasOfKnowledge', component: MainProfileAreasOfKnowledge },
      { path: '/profile/areas-of-knowledge/edit', name: 'EditAreasOfKnowledge', component: EditProfileAreasOfKnowledge },
      { path: '/profile/:id', name: 'MainProfile', component: MainProfile },
      { path: '/terms-of-use', name: 'TermsOfUse', component: TermsOfUse },
      { path: '/privacy-policy', name: 'PrivacyPolicy', component: PrivacyPolicy },
      { path: '*', component: PageNotFound }
    ]
  })
}