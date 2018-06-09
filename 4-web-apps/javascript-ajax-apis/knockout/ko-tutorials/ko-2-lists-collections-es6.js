// Class to represent a row in the seat reservations grid
function SeatReservation (name, initialMeal) {
  const self = this
  self.name = name
  self.meal = ko.observable(initialMeal)

  self.formattedPrice = ko.computed(() => {
    const price = self.meal().price
    return price ? '$' + price.toFixed(2) : 'None'
  })
}

// Overall viewmodel for this screen, along with initial state
function ReservationsViewModel () {
  const self = this

  // Non-editable catalog data - would come from the server
  self.availableMeals = [
    { mealName: 'Standard (sandwich)', price: 0 },
    { mealName: 'Premium (lobster)', price: 34.95 },
    { mealName: 'Ultimate (whole zebra)', price: 290 }
  ]

  // Editable data
  self.seats = ko.observableArray([
    new SeatReservation('Steve', self.availableMeals[0]),
    new SeatReservation('Bert', self.availableMeals[0])
  ])

  // Computed data
  self.totalSurcharge = ko.computed(() => {
    let total = 0
    for (let i = 0; i < self.seats().length; i++) { total += self.seats()[i].meal().price }
    return total
  })

  // Operations
  self.addSeat = () => {
    self.seats.push(new SeatReservation('', self.availableMeals[0]))
  }
  self.removeSeat = seat => { self.seats.remove(seat) }
}

ko.applyBindings(new ReservationsViewModel())
