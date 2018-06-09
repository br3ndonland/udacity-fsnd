// Require modules to run file from Node.js outside of browser
const fetch = require('node-fetch')

const fetchFoursquare = async () => {
  try {
    const url = 'https://api.foursquare.com/v2/lists/5af879722b9844322f1aba96'
    const params = {
      client_id: 'client_id',
      client_secret: 'client_secret',
      v: '20180528'
    }
    const query = fetch(`${url}?&client_id=${params.client_id}&client_secret=${params.client_secret}&v=${params.v}`)
    const data = await (await query).json()
    // Console log data
    console.group('Foursquare list')
    console.group('Metadata')
    console.log(`Response code: ${data.meta.code}`,
      `\nList name: ${data.response.list.name}`,
      `\nList URL: ${data.response.list.canonicalUrl}`,
      `\nList author: ${data.response.list.user.firstName} ${data.response.list.user.lastName}`,
      `\nList description: ${data.response.list.description}`)
    console.groupEnd('Metadata')
    console.group('Venues')
    const items = data.response.list.listItems.items
    const venueNames = items.map(item => item.venue.name)
    console.log(venueNames)
    const venueNamesForEach = items.forEach(item => {
      let name = item.venue.name
      console.log(name)
    })

    const venueCities = items.map(item => item.venue.location.city)
    console.log(venueCities)
    // const cities = venueCities.reduce()
    const venueCitiesForEach = items.forEach(item => {
      let city = item.venue.location.city
      console.log(city)
    })
    const cities = new Set(items.map(item => item.venue.location.city))
    let array = Array.from(cities)
    console.log(array)
    const venueInfo = items.map(item => {
      let name = item.venue.name
      console.log(`${item.venue.name}, ${item.venue.location.formattedAddress[0]}, ${item.venue.location.formattedAddress[1]}, lat: ${item.venue.location.lat}, lng: ${item.venue.location.lng}`)
      let canonicalUrl = `https://foursquare.com/v/${item.venue.name.toLowerCase().replace(/[^a-zA-Z\s]/g, '').replace(/\s/g, '-')}/${item.venue.id}`
      let googleUrl = `https://www.google.com/maps/search/?api=1&query=${escape(item.venue.name)}&query=${item.venue.location.lat},${item.venue.location.lng}`
      console.log(canonicalUrl, `\n`, googleUrl)
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
  } catch (e) {
    throw Error(e)
  }
}

fetchFoursquare()
