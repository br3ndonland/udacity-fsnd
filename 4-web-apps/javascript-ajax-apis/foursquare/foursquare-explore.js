const request = require('request')

request({
  url: 'https://api.foursquare.com/v2/venues/explore',
  method: 'GET',
  qs: {
    client_id: 'PASTE_YOUR_KEY_HERE',
    client_secret: 'PASTE_YOUR_SECRET_HERE',
    ll: '42.3495694,-71.0836727',
    query: 'george howell',
    v: '20180323',
    limit: 1
  }
}, function (err, res, body) {
  if (err) {
    console.error(err)
  } else {
    console.log(body)
  }
})
