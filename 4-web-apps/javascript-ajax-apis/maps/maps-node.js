// Require modules to run file from Node.js outside of browser
const fetch = require('node-fetch')
const google = require('@google/maps').createClient({
  key: 'paste_key_here',
  Promise: Promise
})
// Geocode an address.
google.geocode({
  address: '1600 Amphitheatre Parkway, Mountain View, CA'
}, function (err, response) {
  if (!err) {
    console.log(response.json.results)
  }
})

google.geocode({address: '1600 Amphitheatre Parkway, Mountain View, CA'})
  .asPromise()
  .then((response) => {
    console.log(response.json.results)
  })
  .catch((err) => {
    console.log(err)
  })

const mountainView = async () => {
  try {
    let address = '1600 Amphitheatre Parkway, Mountain View, CA'
    let request = fetch(google.geocode(address).asPromise())
    let response = await (await request).json()
    console.log(response)
  } catch (e) {
    throw Error(e)
  }
}
