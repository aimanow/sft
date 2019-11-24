import axios from 'axios'

function Request () {
  const baseURL = 'http://localhost:5000/api/public'
  return axios.create({ baseURL, withCredentials: true })
}

let request = Request();

export function Login (data) {
  let form = new FormData()
  form.append('email', data.email)
  form.append('password', data.password)
  return request.post('/access/auth', form)
    .then(response => {
      //request = Request(response.data.result.token)
      return response
    })
    .catch(err =>{
		return err
		//alert(err.response.data.message)
	})
}//*
export function Logout (){
  return request.post('/access/logout')
}//*
export function Register (data) {
  let form = new FormData()
  form.append('email', data.email)
  form.append('fullname', data.fullname)
  form.append('password', data.password)

  return request.post('/access/registration', form)

}//*
export function GetProfileId (id) {
  return request.get(`/profiles/${id}`)
}//*
export function GetCurrentProfile () {
  return request.get(`/profiles/current`)
}//*
export function GetProfileEducation (id) {
  return request.get(`/profiles/${id}/education`)
}//*
export function EditPassword(data){
  const baseURL = 'http://37.252.1.151:5000/api/public';
  return request.post(`/profiles/current/security/password`, data,
    {
      baseURL,
      withCredentials: true,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'x-www-form-urlencoded',
      }
    })
}//*
export function EditEmail(data){
  let form = new FormData();
  form.append('email', data.new_email)
  return request.post("/profiles/current/security/email", form)
}//*
export function ChangeAvatar({profile_id, avatar}){
  let form = new FormData();
  form.append("avatar", avatar)

  return request.put(`/profiles/${profile_id}/avatar`, form,
  {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'multipart/form-data',
    }
  })
}//*
export function EditProfileEducation ({id, data}){
  return request.put(`/profiles/${id}/education`, data,
    {
      headers:{
          'Content-Type': 'application/json',
      }
    })
}//*
export function EditProfileEducationScan ({id, scan}){
  let form = new FormData();
  form.append("scan", scan)
  return request.put(`/profiles/${id}/education/scan`, form,
    {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
      }
    }
  )
}//*
export function ToggleAspects (id) {
  return request.post(`/aspects/${id}/favorite`)
}//*
export function GetFavoritesAuthors(page){
  return request.get(`/profiles?location=favorites&page=${page}`)
}//*
export function ToggleDiscusionFav(id){
    return request.post(`/discussions/${id}/favorite`)
}//*
export function ToggleDiscusionAuthorFav(id){
  return request.post(`/profiles/${id}/favorite`)
}// *
export function ToggleDiscusionFreeze(id){
  return request.post(`/discussions/${id}/freeze`)
}// *
export function ToggleDiscusionAuthorLike(id){
  return request.post(`/profiles/${id}/likes`)
}// *
export function CreateAspects (payload) {
  return request.post(`/aspects`, payload, {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    }
  })
} //*
export function CreateAspectsImage ({id, image}) {
  let form = new FormData();
  form.append("image", image)
  return request.put(`/aspects/${id}/image`, form, {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'multipart/form-data"',
    }
  })
} //*
export function GetFilteredDiscussion(query){
  return request.get(`/discussions?q=${query}&location=all&sort=last&page=1`)
}//*
export function GetAllDiscussion(page){
  return request.get(`/discussions?location=all&sort=last&page=${page}`)
}//*
export function CreateNewDiscussion (data) {
  return request.post(`/discussions`, data,
    {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
  })
} //*
export function PostDiscussionArgements({id, form}){
  return request.post(`/discussions/${id}/arguments`, form, {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    }
  })
}//*
export function PostDiscussionThesis({id, form}){
  return request.post(`/arguments/${id}/theses`, form, {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    }
  })
}//*
export function CreateDiscussionArguments (data) {
  return request.post(`/discussions`, data,
    {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
  })
} //*
export function PutDiscussionImage({id, image}){
  request.put(`/discussions/${id}/image`, image, {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'multipart/form-data"',
    }
  })
} //*
export function GetDiscussions () {
  return request.get('/discussions')
} //* not ready
export function DeleteDiscussion(id){
  return request.delete(`/discussions/${id}`)
}//*
export function DeleteAspect(id){
  return request.delete(`/aspects/${id}`)
}//*
export function GetAuthorDiscussions ({id, page}) {
  return request.get(`/discussions?author=${id}&location=all&sort=last&page=${page}`)
} //*
export function GetDiscussion (id) {
  return request.get('/discussions/' + id)
} //*
export function GetDiscussionsTop () {
  return request.get(`/discussions?location=all&sort=popular&page=1`)
} //*
export function GetDiscussionsLast () {
  return request.get(`/discussions?location=all&sort=last&page=1`)
}//*
export function GetDiscussionsFav (page) {
  return request.get(`/discussions?location=favorites&sort=last&page=${page}`)
}//*
export function GetCurrentDiscussions (id) {
  return request.get(`/discussions/${id}`)
} //*
export function GetThesisIdComments(id){
    return request.get(`/theses/${id}/comments?page=1`)
}//*
export function AddThesisFile({id, file}){
  let form = new FormData();
  file.forEach(file => {form.append("files[]", file)})
  return request.post(`/theses/${id}/attachments/files`, form,
    {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
      }
    } )
}//*
export function AddThesisLink({id, link}){
  let form = new FormData();
  link.forEach(link => {form.append("links[]", link)})
  return request.post(`/theses/${id}/attachments/links`, form, {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'multipart/form-data',
    }
  } )

}//*

export function GetDiscussionArguments (id) {
  return request.get('/discussions/' + id + '/arguments')
} //*
// export function GetDiscussionAspects (id) {
//   return request.get('/aspects/' + id)
// } //*
export function GetAllAspects (page=1) {
  return request.get(`/aspects?&page=${page}`)
} //*
export function GetAspects (payload) {
  return request.get(`/aspects?q=${payload}&page=1`)
} //*

export function GetArguments (id) {
  return request.get(`/arguments/${id}`)
} //*

export function GetArgumentThesis (id) {
  return request.get(`/arguments/${id}/theses?page=1`)
} //*
export function PatchtThesisVotes (id, data) {
  return request.patch(`/theses/${id}/votes`, data,
    {
      headers:{
        'Content-Type': 'application/json'
      }
    })
} //*

export function AddDiscussionArguments (id, data) {
  return request.post(`/discussions/${id}/arguments`, data)
} //*

export function GetUsersTop () {
  return request.get(`/profiles/top_rated`)
}//*

export function DeleteUser (id) {
  return request.delete(`/profiles/${id}`)
}//*
