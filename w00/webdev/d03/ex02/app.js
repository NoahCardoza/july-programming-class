// const prop = key => obj => obj[key]

const api = axios.create({
  baseURL: 'http://51.38.128.213:3000'
})

setInterval(function () {
  api.get('/price').then(r => {
    document.querySelector('#btcPrice').innerText = r.data.value
  })
}, 1000);

// document.querySelector('#tokenConnect')
// .addEventListener('click', () => {
//   const token = document.querySelector('#tokenConnect')
//   // http://51.38.128.213:3000/balance
//   api.defaults.headers.common.Authorization = 'Bearer ' + token
//   api.get('/balance')
//   .then(prop('data'))
//   .then(prop('value'))
//   .catch()
// })
