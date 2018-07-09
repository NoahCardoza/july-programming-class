// this will save us some typing later
// so when we call api.get('/price')
// we will really call api.get('http://51.38.128.213:3000' + '/price')
const api = axios.create({
  baseURL: 'http://51.38.128.213:3000'
})

// We are using this to save typing
const thenGetValue = p => p.then(r => r.data.value)
// => thenGetValue(api.get(...)) == api.get(...).then(r => r.data.value)

const getBtcPrice = () => thenGetValue(api.get('/price'))
const getBalance = () => thenGetValue(api.get('/balance'))
const getMyBtc = () => thenGetValue(api.get('/btc'))

// Here we are storing all of the elements we are going to use throught the
// program. ui stands for "user interface"
const ui = {
  btcPrice: document.querySelector('#btc-price'),
  token: document.querySelector('#token'),
  saveToken: document.querySelector('#save-token'),
  tokenForm: document.querySelector('#token-form'),
  tokenError: document.querySelector('#token-error'),
  app: document.querySelector('#app'),
  amount: document.querySelector('#amount'),
  buy: document.querySelector('#buy'),
  sell: document.querySelector('#sell'),
  balance: document.querySelector('#balance'),
  btc: document.querySelector('#btc'),
  log: document.querySelector('#log'),
}

function updateUi(){
  // both getBalance and getMyBtc return Promises
  // Promise.all will wait till both are resloved before running
  // the function we attach to it
  Promise.all([getBalance(), getMyBtc()]).then(([balance, btc]) => {
    // updates the ui
    ui.balance.innerText = balance
    ui.btc.innerText = btc
  })
}

// setInterval will run the function we pass it every X milliseconds
setInterval(function () {
   getBtcPrice().then(price => {
     ui.btcPrice.innerText = price
   })
// X = 1000ms = 1s
}, 1000);

ui.saveToken.addEventListener('click', () => {
  // This part looks complicated but it is just the way axios works.
  // https://github.com/axios/axios#custom-instance-defaults
  api.defaults.headers.common['Authorization'] = "Bearer " + ui.token.value
  api.get('/balance')
    .then(({ data }) => {
      // If the token was valid we hide the input and button
      ui.tokenForm.style = 'display: none;'
      // and other half of the app
      ui.app.style = 'display: block;'
      // this will get and set the btc and bank balance in the page
      updateUi()
    })
    .catch(() => {
      // if we encountered an error we unhide the error message
      ui.tokenError.style = 'display: block;'
    })
})

function appendToLog(text) {
  // this just creates a new div element with JS
  const div = document.createElement('div')
  // sets the text
  div.innerText = text
  // and appends the div (which is just a programmery way to say added to the end of)
  // the log element
  ui.log.appendChild(div)
}


// this both select paths within an object
const getMessage = r => r.data.message
// getMessage({
//  data: {
//    message: 42
//  }
// }) == 42
const getErrorToMessage = r => getMessage(r.response)

// this will run the function below when we click the buy button
ui.buy.addEventListener('click', () => {
  // we get the number the user has in the input field
  const amount = ui.amount.value
  // `/buy?amount=${ amount }` is called string interpolation
  // `/buy?amount=${ amount }` == '/buy?amount=' + amount
  api.get(`/buy?amount=${ amount }`)
    // this will either return the success message or the error message
    .then(getMessage)
    .catch(getErrorToMessage)
    // this will append it to the log
    .then(appendToLog)
    // this will get the new number of btc and USD the user owns
    .then(updateUi)
})

// this will run the function below when we click the sell button
ui.sell.addEventListener('click', () => {
  // we get the number the user has in the input field
  const amount = ui.amount.value
  api.get(`/sell?amount=${ amount }`)
    // this will either return the success message or the error message
    .then(getMessage)
    .catch(getErrorToMessage)
    // this will append it to the log
    .then(appendToLog)
    // this will get the new number of btc and USD the user owns
    .then(updateUi)
})
