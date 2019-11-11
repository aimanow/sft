export default{
  methods: {
    checkFavData(curData, removedData){
      if(curData.length>0 && removedData.length>0){
        let replaceDisc = [];
        curData.filter(d => {
          removedData.forEach(item =>{
            if(item == d.id) return replaceDisc.push(item)
          })
        })
        return replaceDisc
      } else return []
    }
  },
  mounted(){
    let arrTop = this.checkFavData(this.discussionsTop, this.removedFavDisc);
      if(arrTop.length > 0){
        arrTop.forEach(id =>{
          this.$store.commit('discussion/replaceDiscussionTop', {id, is_favorite: false})
        })
      }
    let arrLast = this.checkFavData(this.discussionsLast, this.removedFavDisc);
      if(arrLast.length > 0){
        arrLast.forEach(id =>{
          this.$store.commit('discussion/replaceDiscussionLast', {id, is_favorite: false})
        })
      }
    let arrAutorsTop = this.checkFavData(this.usersTop, this.removedFavAuthorDisc);
      if(arrAutorsTop.length > 0){
        arrAutorsTop.forEach(id =>{
          this.$store.commit('profile/replaceDiscusionAuthorFav', {id, is_favorite: false})
        })
      }
  }
}
