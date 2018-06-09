// Reusable bindings - ideally kept in a separate file

ko.bindingHandlers.fadeVisible = {
  init: function (element, valueAccessor) {
    // Start visible/invisible according to initial value
    var shouldDisplay = valueAccessor()
    $(element).toggle(shouldDisplay)
  },
  update: function (element, valueAccessor) {
    // On update, fade in/out
    var shouldDisplay = valueAccessor()
    shouldDisplay ? $(element).fadeIn() : $(element).fadeOut()
  }
}

ko.bindingHandlers.jqButton = {
  init: function (element) {
    $(element).button() // Turns the element into a jQuery UI button
  },
  update: function (element, valueAccessor) {
    var currentValue = valueAccessor()
    // Here we just update the "disabled" state, but you could update other properties too
    $(element).button('option', 'disabled', currentValue.enable === false)
  }
}

ko.bindingHandlers.starRating = {
  init: function (element, valueAccessor) {
    $(element).addClass('starRating')
    for (var i = 0; i < 5; i++) { $('<span>').appendTo(element)}

    // Handle mouse events on the stars
    $('span', element).each(function (index) {
      $(this).hover(
        function () { $(this).prevAll().add(this).addClass('hoverChosen') },
        function () { $(this).prevAll().add(this).removeClass('hoverChosen') }
      ).click(function () {
        var observable = valueAccessor() // Get the associated observable
        observable(index + 1) // Write the new rating to it
      })
    })
  },
  update: function (element, valueAccessor) {
    // Give the first x stars the "chosen" class, where x <= rating
    var observable = valueAccessor()
    $('span', element).each(function (index) {
      $(this).toggleClass('chosen', index < observable())
    })
  }
}

// ----------------------------------------------------------------------------
// Page viewmodel

function Answer (text) { this.answerText = text; this.points = ko.observable(1) }

function SurveyViewModel (question, pointsBudget, answers) {
  this.question = question
  this.pointsBudget = pointsBudget
  this.answers = $.map(answers, function (text) { return new Answer(text) })
  this.save = function () { alert('To do') }

  this.pointsUsed = ko.computed(function () {
    var total = 0
    for (var i = 0; i < this.answers.length; i++) { total += this.answers[i].points()}
    return total
  }, this)
}

ko.applyBindings(new SurveyViewModel('Which factors affect your technology choices?', 10, [
  'Functionality, compatibility, pricing - all that boring stuff',
  'How often it is mentioned on Hacker News',
  'Number of gradients/dropshadows on project homepage',
  'Totally believable testimonials on project homepage'
]))
