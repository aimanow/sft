export default{
  methods: {
    checkFields(){
      if(this.index_active_aspect === null && this.aspectsCount > 3 || this.aspect_ids.length==0){
        this.$store.commit('openDialog', 'Please check Aspects \'Only maximum three aspects can be chosen\''); return false}
      if(this.form.position === null){
        this.$store.commit('openDialog', 'Please check Yes or No');return false}
      if(this.form.thesis.length<10 && this.form.argument.length<10){
        this.$store.commit('openDialog', 'Please check filds thesis and arguments the filds must have at least 10 characters long'); return false}
    }
  }
}
