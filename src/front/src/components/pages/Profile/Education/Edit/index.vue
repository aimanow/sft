<template>
  <div class="center">
    <section class="section-form">
      <div class="h2 m-hid"><h1>Образование</h1></div>
      <div class="ed_block" >
        <div class="form_block_title block_title m-show"><span class="icon-cab1"></span>Образование</div>
        <form @submit.prevent="submitEducation">
          <div class="ed_block_cols">
            <div class="ed_block_left">
              <div class="form_block LK_form_block">
                <button type="submit" class="btn btn-bord-blue">Сохранить</button>
                <div class="form_row">
                  <label>Страна:</label>
                  <div class="form_el">
                    <input type="text" class="t-inp" v-model="education.country">
                  </div>
                </div>
                <div class="form_row">
                  <label>Город:</label>
                  <div class="form_el">
                    <input type="text" class="t-inp" v-model="education.city">
                  </div>
                </div>
                <div class="form_row">
                  <label>ВУЗ:</label>
                  <div class="form_el">
                    <input type="text" class="t-inp" v-model="education.high_school">
                  </div>
                </div>
                <div class="form_row">
                  <label>Дата:</label>
                  <div class="form_el">
                    <input type="text" class="t-inp" v-model="education.graduation_date">
                  </div>
                </div>
                <div class="form_row">
                  <label>Факультет:</label>
                  <div class="form_el">
                    <input type="text" class="t-inp" v-model="education.faculty">
                  </div>
                </div>
                <div class="form_row">
                  <label>Специальность:</label>
                  <div class="form_el">
                    <input type="text" class="t-inp" v-model="education.speciality">
                  </div>
                </div>
              </div>
            </div>
            <div class="ed_block_right">
              <div class="card_verif">Подтвердить данные:</div>
              <div class="add_file">
                <div class="jq-file file-link">
                  <div class="jq-file__name"><span class="icon-link2"></span>Прикрепить файл</div>
                  <div class="jq-file__browse"><span class="icon-link"></span></div>
                  <input type="file" class="file-link" value="Прикрепить файл" @change="uploadScan">
                </div>
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
  name: "EducationEdit",

  data () {
    return {
      education: {
        country: "",
        city: "",
        high_school: "",
        faculty: "",
        speciality: "",
        graduation_date: "",
        scan_url: "",
        is_verified: false
      },
      scan: null,
    }
  },

  computed: {
    ...mapState('auth', ['auth']),
    ...mapState('profile', ['profile_education']),
  },

  methods: {
    ...mapActions('profile', ['editUserEducation', 'editUserEducationScan']),

    submitEducation () {
      if(this.scan){
        this.editUserEducationScan({id: this.auth.id, scan: this.scan}).then(()=>{
          this.editUserEducation({id: this.auth.id, data: this.education})
          this.$router.push("/profile/education")
        }).catch(err =>{
          if (err.response){
            this.$store.commit('openDialog', err.response.data)
          }else { this.$store.commit('openDialog', err.message)}
        })
      }else{
          this.editUserEducation({id: this.auth.id, data: this.education}).then(()=>{
            this.$router.push("/profile/education")
          }).catch(err =>{
            if (err.response){
              this.$store.commit('openDialog', err.response.data)
            }else { this.$store.commit('openDialog', err.message)}
          })
      }
    },
    uploadScan (e) {
      console.log(e.target.files[0])
      this.scan = e.target.files[0]
    }
  },
  created(){
    this.education = this.profile_education;
  }

}
</script>

<style scoped>

</style>
