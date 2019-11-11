<template>
  <div class="center">
    <section class="section-form">
      <div class="h2 m-hid"><h1>{{$lang.profile.eduTitle}}</h1></div>
      <div class="ed_block">
        <div class="form_block_title block_title m-show"><span class="icon-cab1"></span>{{$lang.profile.eduTitle}}</div>
        <form>
          <div class="ed_block_cols">
            <div class="ed_block_left">
              <div class="form_block LK_form_block">
                <router-link to="/profile/education/edit" class="btn btn-bord-blue"><span class="icon-edit"></span> {{$lang.profile.edit}}</router-link>
                <table class="card_info">
                  <tr><th>{{$lang.profile.country}}:</th><td>{{ profile_education.country || 'Не заполнено' }}</td></tr>
                  <tr><th>{{$lang.profile.city}}:</th><td>{{ profile_education.city || 'Не заполнено' }}</td></tr>
                  <tr><th>{{$lang.profile.uni}}:</th><td>{{ profile_education.high_school || 'Не заполнено' }}</td></tr>
                  <tr><th>{{$lang.profile.date}}:</th><td>{{ profile_education.graduation_date || 'Не заполнено' }}</td></tr>
                  <tr><th>{{$lang.profile.fuc}}:</th><td>{{ profile_education.faculty || 'Не заполнено' }}</td></tr>
                  <tr><th>{{$lang.profile.spec}}:</th><td>{{ profile_education.speciality || 'Не заполнено' }}</td></tr>
                </table>
              </div>
            </div>
            <div class="ed_block_right">
              <div class="card_verif"><span class="icon-check" v-show="profile_education.is_verified"></span>{{profile_education.is_verified ? $lang.profile.confirm : $lang.profile.notConfirm}}:</div>
              <div class="add_file js-bg" v-if="profile_education.scan_url.length > 0">
                <img :src="$baseUrl + profile_education.scan_url" alt="foto"/>
              </div>
            </div>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "EducationMain",

  computed: {
    ...mapState('auth', ['auth']),
    ...mapState('profile', ['profile', 'profile_education']),
  },

  methods: {
    ...mapActions('profile', ['getUserEducation'])
  },

  mounted () {
    return this.getUserEducation(this.auth.id).catch(err =>{alert(err.message)})
  }
}
</script>

<style scoped>

</style>
