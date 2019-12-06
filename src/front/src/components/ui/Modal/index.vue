<template>
  <div>
    <div class="overlay" :class="{ open: modals.length }"></div>

    <MainLogin v-if="activeModal && activeModal.name === 'Login'" :modal="activeModal"/>
    <MainRegister v-if="activeModal && activeModal.name === 'Register'" :modal="activeModal"/>

    <MainForgotPassword v-if="activeModal && activeModal.name === 'ForgotPassword'" :modal="activeModal"/>
    <MainPasswordRecovery v-if="activeModal && activeModal.name === 'PasswordRecovery'" :modal="activeModal"/>

    <RewardsInfo v-if="activeModal && activeModal.name === 'RewardsInfo'" :modal="activeModal"/>
    <DiscussionAddAspects v-if="activeModal && activeModal.name === 'DiscussionAddAspects'" :modal="activeModal"/>
    <ModalArgument v-if="activeModal && activeModal.name === 'ModalArgument'" :modal="activeModal" :id="modals[0].data"/>
    <DiscussionComplaints v-if="activeModal && activeModal.name === 'DiscussionComplaints'" :modal="activeModal"/>
    <DiscussionGraph v-if="activeModal && activeModal.name === 'DiscussionGraph'" :modal="activeModal"/>
    <Chart v-if="activeModal && activeModal.name === 'Chart'" :modal="activeModal"/>
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-text>
          <v-alert :value="true" :color="alertColor" :icon="alertIcon" outline>
            {{alertMessage}}
          </v-alert>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" flat @click="closeDialog"> Ok</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <OAuthVK v-if="activeModal && activeModal.name === 'OAuthVK'" :modal="activeModal"/>
    <OAuthGoogle v-if="activeModal && activeModal.name === 'OAuthGoogle'" :modal="activeModal"/>
    <OAuthFacebook v-if="activeModal && activeModal.name === 'OAuthFacebook'" :modal="activeModal"/>

    <AspectEdit v-if="activeModal && activeModal.name === 'AspectEdit'" :modal="activeModal"/>

  </div>
</template>

<script>
import MainLogin from './Main/Login'
import MainRegister from './Main/Register'

import MainForgotPassword from './Main/ForgotPassword'
import MainPasswordRecovery from './Main/PasswordRecovery'

import RewardsInfo from './Rewards/Info'

import DiscussionAddAspects from './Discussion/Add'
import Chart from './Chart/Main'
import ModalArgument from './Discussion/ModalArgument'
import DiscussionComplaints from './Discussion/Complaints'
import DiscussionGraph from './Discussion/Graph'

import OAuthVK from './OAuth/OAuthVK'
import OAuthFacebook from './OAuth/OAuthFacebook'
import OAuthGoogle from './OAuth/OAuthGoogle'

import AspectEdit from './Discussion/AspectEdit'

import { mapState } from 'vuex'

export default {
  name: 'Modal',

  components: {
    MainLogin,
    MainRegister,

    MainForgotPassword,
    MainPasswordRecovery,

    Chart,
    RewardsInfo,
    DiscussionAddAspects,
    ModalArgument,
    DiscussionComplaints,
    DiscussionGraph,

    OAuthVK,
    OAuthGoogle,
    OAuthFacebook,

    AspectEdit
  },
  methods: {
    closeDialog() {
      this.$store.commit('closeDialog')
    }
  },

  computed: {
    ...mapState('modal', ['modals']),
    ...mapState(['alertMessage']),
    dialog: {
      get() {
        return this.$store.state.dialog
      },
      set(newValue) {
        this.$store.commit('setDialog', newValue)
      }
    },
    alertColor() {
      if (this.$store.state.alertType) {
        return this.$store.state.alertType
      } else {
        return 'error'
      }
    },
    alertIcon() {
      if (this.$store.state.alertType) {
        return 'check_circle'
      } else {
        return 'warning'
      }
    },
    activeModal() {
      if (this.modals.length) {
        return this.modals[this.modals.length - 1]
      }
      return false
    }
  }
}
</script>

<style>
  .v-alert {
    font-size: 24px;
  }
</style>
