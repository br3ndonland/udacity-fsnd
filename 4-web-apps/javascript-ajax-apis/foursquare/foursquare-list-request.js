// Require modules to run file from Node.js outside of browser
const request = require('request') // https://github.com/request/request

request({
  url: 'https://api.foursquare.com/v2/lists/5af879722b9844322f1aba96',
  method: 'GET',
  qs: {
    client_id: 'client_id',
    client_secret: 'client_secret',
    v: '20180528'
  }
},
(err, res, body) => {
  if (err) {
    console.error(err)
  } else {
    const data = JSON.parse(body)
    // Console log data
    console.group('Foursquare list')
    console.group('Metadata')
    console.log(`Response code: ${data.meta.code}`,
      `\nList name: ${data.response.list.name}`,
      `\nList author: ${data.response.list.user.firstName} ${data.response.list.user.lastName}`,
      `\nList description: ${data.response.list.description}`)
    console.groupEnd('Metadata')
    console.group('Venues')
    const items = data.response.list.listItems.items
    // Iteration methods to return venue info
    const list = items.map(item => {
      console.log(`${item.venue.name}, ${item.venue.location.address}, ${item.venue.location.city}`)
    })
    // Alternative for...of iteration method
    // for (const item of items) {
    //   console.log(`${item.venue.name}, ${item.venue.location.address}, ${item.venue.location.city}`)
    // }
    // Alternative forEach iteration method
    // items.forEach(item => {
    //   console.log(`${item.venue.name}, ${item.venue.location.address}, ${item.venue.location.city}`)
    // })
    console.groupEnd('Venues')
    console.groupEnd('Foursquare list')
  }
})
