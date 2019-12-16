<template>
  <div class="win win-reg" id="win-reg">
    <div class="win_cont">
      <div class="win_title">{{$lang.auth.oauthFacebook}}....</div>
    </div>
    <a @click.prevent="closeAllModal()" class="win_close"><span class="icon-cab7"></span></a>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  name: 'OAuthFacebook',

  props: ['modal'],

  data() {
    return {}
  },

  mounted() {
    this.doLogin()
  },

  methods: {
    ...mapActions('modal', ['addModal', 'closeModal', 'openForgotPassword']),
    ...mapMutations('modal', ['closeAllModal']),
    ...mapMutations(['openDialog']),
    ...mapActions('auth', ['login']),

    windowPopup(options) {
      var screenX = typeof window.screenX != 'undefined' ? window.screenX : window.screenLeft,
        screenY = typeof window.screenY != 'undefined' ? window.screenY : window.screenTop,
        outerWidth = typeof window.outerWidth != 'undefined' ? window.outerWidth : document.body.clientWidth,
        outerHeight = typeof window.outerHeight != 'undefined' ? window.outerHeight : (document.body.clientHeight - 22),
        width = options.width, height = options.height, left = parseInt(screenX + ((outerWidth - width) / 2), 10),
        top = parseInt(screenY + ((outerHeight - height) / 2.5), 10),
        features = ('width=' + width + ',height=' + height + ',left=' + left + ',top=' + top)
      return window.open(options.url, 'oauth', features)
    },

    getOAuthCode(location) {
      let code = null
      try {
        const pathData = {}
        location.search.split('?')[1].split('&').forEach((pd) => {
          const pdS = pd.split('=')
          pathData[pdS[0]] = pdS[1]
        })
        code = pathData['code'] || null
        if (code)
          code = decodeURIComponent(code)
      } catch (e) {
        code = null
      }
      return code
    },

    getOAuthData(location) {
      let data = null
      const code = this.getOAuthCode(location)
      if (!code)
        return data
      data = { oauth: code, provider: 'facebook' }
      return data
    },

    oauth(data) {
      this.login(data)
        .then(success => {
          if (success) {
            this.closeAllModal()
          }
        }).catch((err) => {
        this.closeAllModal()
          if (err.message === 'Request failed with status code 403') {
            this.openDialog(this.$lang.error.authEmailError)
          } else
            this.openDialog(this.$lang.error.authPlainError)
        })
    },

    doLogin() {
      const CLIENT_ID = process.env.VUE_APP_OAUTH_FACEBOOK_ID

      const redirect_uri = window.location.origin+'/oauth/facebook'
      const uri_regex = new RegExp(redirect_uri)

      const url = 'https://www.facebook.com/v5.0/dialog/oauth?client_id=' + CLIENT_ID +
          '&redirect_uri=' + redirect_uri +
          '&scope=email' +
          '&state={"{st=state123abc,ds=123456789}"}'
      let win = this.windowPopup({ width: 720, height: 570, url: url })
      let error = null
      let ok = false
      let watch_timer = setInterval(() => {
        try {
          if (uri_regex.test(win.location)) {
            clearInterval(watch_timer)
            // setTimeout(function() {
            const oauthData = this.getOAuthData(win.location)
            if (oauthData)
              this.oauth(oauthData)
            ok = true
            win.close()
            // }, 500)
          }
        } catch (e) {
          error = e
        }

        if (win.closed) {
          clearInterval(watch_timer)
          if (!ok)
            this.addModal({ name: 'Login' })
        }
      }, 100)
      return error
    }
  }
}
</script>

<style scoped>

</style>
