export default {

  beforeUpdate () {
    for (let slick in this.$refs) {
      if (slick.includes('slick')) {
        this.$refs[slick].destroy()
      }
    }
  },

  updated () {
    this.$nextTick(function () {
      for (let slick in this.$refs) {
        if (slick.includes('slick')) {
          this.$refs[slick].create(this.$refs[slick].options)
        }
      }
    })
  }
}
