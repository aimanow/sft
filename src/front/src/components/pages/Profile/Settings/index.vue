<template>
  <div class="center">
    <section class="section-form">
      <div class="h2 m-hid"><h1>{{$lang.profile.setTitle}}</h1></div>
      <div class="LK_block">
        <div class="LK_avatar">
          <div class="add_file">
            <div class="jq-file file-link">
              <div class="jq-file__name"><span class="icon-link2"></span>{{$lang.profile.addFile}}</div>
              <div class="jq-file__browse"><span class="icon-link"></span></div>
              <input type="file" class="file-link" value="$lang.profile.addFile" @change="changeAvatar">
            </div>
            <div class="LK_avatar_txt">{{$lang.profile.addAvatar}}</div>
          </div>
        </div>
        <div class="LK_form_block form_block">
          <div class="form_block_title block_title"><span class="icon-cab6"></span>{{$lang.profile.changPass}}</div>
          <div class="LK_form">
            <form @submit.prevent="changePassword">
              <div class="form_row">
                <label>{{$lang.profile.oldPass}}:</label>
                <div class="form_el">
                  <input type="password" class="t-inp" placeholder="********" v-model="old_password" required>
                  <!-- <a href="#" class="look_link"><span class="icon-eye"></span></a> -->
                </div>
              </div>
              <div class="form_row">
                <label>{{$lang.profile.newPass}}:</label>
                <div class="form_el">
                  <input type="password" class="t-inp" placeholder="********" v-model="new_password" required>
                  <!-- <a href="#" class="look_link"><span class="icon-eye"></span></a> -->
                </div>
              </div>
              <div class="form_row">
                <label>{{$lang.profile.reNewPass}}:</label>
                <div class="form_el">
                  <input type="password" class="t-inp" placeholder="********" v-model="re_new_password" required>
                  <!-- <a href="#" class="look_link"><span class="icon-eye"></span></a> -->
                </div>
              </div>
              <div class="form_btn"> <input type="submit" class="btn" :value="$lang.profile.changePassBut"/></div>
            </form>
          </div>
        </div>
      </div>
      <div class="LK_form_block form_block">
        <div class="form_block_title block_title"><span class="icon-mail2"></span>{{$lang.profile.changeEmail}}</div>
        <div class="LK_form">
          <form @submit.prevent="changeEmail">
            <div class="form_cols">
              <!-- <div class="form_cols_item">
                <div class="form_row">
                  <label>{{$lang.profile.oldEmail}}</label>
                  <div class="form_el">
                    <input v-model="old_email" type="text" class="t-inp" required>
                  </div>
                </div>
              </div> -->
              <div class="form_cols_item">
                <div class="form_row">
                  <label>{{$lang.profile.newEmail}}</label>
                  <div class="form_el">
                    <input v-model="new_email" type="text" class="t-inp" required>
                  </div>
                </div>
              </div>
            </div>
            <div class="form_btn"> <input type="submit" class="btn" :value="$lang.profile.changeEmailBut"/></div>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState, mapActions, mapMutations } from 'vuex'

export default {
  name: "Settings",
  data() {
    return {
      old_email: '',
      new_email: '',
      old_password: '',
      new_password: '',
      re_new_password: '',
    }
  },
  computed: {
    ...mapState('auth', ['auth'])
  },

  methods: {
    ...mapActions('profile', ['EditPassword', 'EditEmail','ChangeAvatar']),
    ...mapMutations('auth', ['login','updateAvatar']),
    changeEmail () {
      this.EditEmail({
        new_email: this.new_email,
      })
        .then(response => {
          this.$store.commit('openDialog', {type: 'success', message: response.data})
        })
        .catch(err =>{
          if (err.response){
            this.$store.commit('openDialog', err.response.data)
          }else { this.$store.commit('openDialog', err.message)}
        })
    },
    changePassword () {
      if (this.new_password !== this.re_new_password) return this.$store.commit('openDialog', 'Пароли не идеинтичны')
      let form = new FormData();
        form.append("old_password", this.old_password)
        form.append("new_password", this.new_password)
            this.$axios.post('/profiles/current/security/password', form ).then(()=>{
              this.$store.commit('openDialog', {type: 'success', message: "Your Parol has been successfully chanhe"})
            }).catch(err => {
              if (err.response){
                this.$store.commit('openDialog', err.response.data)
              }else { this.$store.commit('openDialog', err.message)}
            })
    },
    changeAvatar (e) {
      let avatar = e.target.files[0];
      this.ChangeAvatar({
        profile_id: this.auth.id,
        avatar,
      })
        .then(response => {
          if (response.status !== 200) return;
            this.$axios.get('/profiles/current').then(res => {
              this.updateAvatar()
                if(res.status == 200){
                  let auth = res.data;
                  this.login(auth);
                }
            })
        })
    }
  }
}
</script>

<style scoped>

</style>
