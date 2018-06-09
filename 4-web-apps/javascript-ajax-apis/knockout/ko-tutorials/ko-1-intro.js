// This is a simple *viewmodel* - JavaScript that defines the data and behavior of your UI
function AppViewModel () {
  this.firstName = ko.observable('Bert')
  this.lastName = ko.observable('Bertington')

  this.fullName = ko.computed(() =>
    `${this.firstName()} ${this.lastName()}`, this)

  this.capitalizeLastName = () => {
    let currentVal = this.lastName() // Read the current value
    this.lastName(currentVal.toUpperCase()) // Write back a modified value
  }

  this.lowercaseLastName = () => {
    let currentVal = this.lastName()
    this.lastName(currentVal.toLowerCase())
  }
}

// Activates knockout.js
ko.applyBindings(new AppViewModel())
