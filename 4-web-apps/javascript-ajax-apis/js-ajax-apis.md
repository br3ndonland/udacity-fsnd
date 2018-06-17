# FSND JavaScript, AJAX, and APIs lessons

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

[br3ndonland](https://github.com/br3ndonland)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Intro to APIs](#intro-to-apis)
  - [Lesson 01. Requests and APIs](#lesson-01-requests-and-apis)
  - [Lesson 02. Building the Move Planner app](#lesson-02-building-the-move-planner-app)
- [JavaScript Design Patterns and Libraries](#javascript-design-patterns-and-libraries)
  - [Lesson 03. Changing expectations](#lesson-03-changing-expectations)
  - [Lesson 04. Refactoring with separation of concerns](#lesson-04-refactoring-with-separation-of-concerns)
  - [Lesson 05. Using an organization library](#lesson-05-using-an-organization-library)
  - [Lesson 06. Learning a new codebase](#lesson-06-learning-a-new-codebase)
- [Google Maps](#google-maps)
  - [Lesson 07. Getting started with the APIs](#lesson-07-getting-started-with-the-apis)
  - [Lesson 08. Understanding API services](#lesson-08-understanding-api-services)
  - [Lesson 09. Using the APIs in practice](#lesson-09-using-the-apis-in-practice)
- [Feedback](#feedback)

## Intro to APIs

### Lesson 01. Requests and APIs

- This part is similar to the [Intro to AJAX](https://www.udacity.com/course/intro-to-ajax--ud110) free course.
- The instructor Cameron inspects Facebook and Twitter with developer tools (network tab, clicking on individual request paths) to show how AJAX is used.

### Lesson 02. Building the Move Planner app

- jQuery
  - Most people use jQuery for AJAX requests (the famous [`$.ajax({})`](https://api.jquery.com/jQuery.ajax/)).
  - In [cs50 web](https://cs50.github.io/web/lectures) during [lecture 05](https://video.cs50.net/web/2018/spring/lectures/5?t=1h10m26s), Brian mentioned that jQuery is not as useful anymore, because many of its functions can be accomplished with standard JavaScript like [`querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) and `querySelectorAll`. It's also a large library, so it's better not to load jQuery if you don't have to.
  - The [Syntax podcast episode 39: Is jQuery dead?](https://syntax.fm/show/039/is-jquery-dead) was also very helpful.
  - The [Asynchronous JavaScript Requests course](https://www.udacity.com/course/es6-javascript-improved--ud356) compares XHR, jQuery and Fetch.
- [jQuery.getJSON()](http://api.jquery.com/jquery.getjson/)
- [jQuery.error()](http://api.jquery.com/error/) method for error handling
- CORS: Cross-Origin Resource Sharing

    >tl;dr CORS works around a sometimes overly-strict browser policy meant to protect servers from malicious requests. CORS is enabled on the server-side, so you won't generally need to worry about it for your code. You do need to know about it though, since some APIs support it, and some do not.

- [NYT article search API](http://developer.nytimes.com/article_search_v2.json)
- [Wikipedia API](http://www.mediawiki.org/wiki/API:Main_page)
- Split up generic and unique HTML to render content as quickly as possible.

---

## JavaScript Design Patterns and Libraries

### Lesson 03. Changing expectations

- From [JavaScript Design Patterns](https://www.udacity.com/course/javascript-design-patterns--ud989) free course
- The instructor Ben Jaffe builds a "cat clicker" app. See [ud989-cat-clicker-andy](https://github.com/udacity/ud989-cat-clicker-andy) and [ud989-retain](https://github.com/udacity/ud989-retain). He uses Sublime Text in the video.
- **Separation of Concerns**: Separate out the different types of files and functions.
- **Model View Controller**: The instructor used "octopus" to represent controller.

#### Resources

>In case you need a refresher on events and event listeners, here are some links.
>
>If you're writing Cat Clicker with vanilla JS (no jQuery), you'll be adding the "click" event with elem.addEventListener().

```javascript
var elem = document.getElementById('my-elem');
elem.addEventListener('click', function(){
  // the element has been clicked... do stuff here
}, false);

```

>If you're using jQuery, you'll be adding the "click" event listener with jQuery.click().

```javascript
$('#my-elem').click(function(e) {
  //the element has been clicked... do stuff here
});

```

#### Closures and Event Listeners

##### The problem

>Let's say we're making an element for every item in an array. When each is clicked, it should alert its number. The simple approach would be to use a for loop to iterate over the list elements, and when the click happens, alert the value of `num` as we iterate over each item of the array. Here's an example:

```js
// clear the screen for testing
document.body.innerHTML = '';
document.body.style.background="white";

var nums = [1,2,3];

// Let's loop over the numbers in our array
for (var i = 0; i < nums.length; i++) {

    // This is the number we're on...
    var num = nums[i];

    // We're creating a DOM element for the number
    var elem = document.createElement('div');
    elem.textContent = num;

    // ... and when we click, alert the value of `num`
    elem.addEventListener('click', function() {
        alert(num);
    });

    // finally, let's add this element to the document
    document.body.appendChild(elem);
};
```

>If you run this code on any website, it will clear everything and add a bunch of numbers to the page. Try it! Open a new page, open the console, and run the above code. Then click on the numbers and see what gets alerted. Reading the code, we'd expect the numbers to alert their values when we click on them.
>
>But when we test it, all the elements alert the same thing: the last number. But why?

##### What's actually happening

>Let's cut out the irrelevant code so we can see what's going on. The comments below have changed, and explain what is actually happening.

```js
var nums = [1,2,3];

for (var i = 0; i < nums.length; i++) {

    // This variable **keeps changing** every time we iterate!
    //  It's first value is 1, then 2, then finally 3.
    var num = nums[i];

    // On click...
    elem.addEventListener('click', function() {

        // ... alert num's value **at the moment of the click**!
        alert(num);

        // Specifically, we're alerting the num variable
        // that's defined **outside** of this inner function.
        // Each of these inner functions are pointing to the
        // same `num` variable... the one that changes on
        // each iteration, and which equals 3 at the end of
        // the for loop.  Whenever the anonymous function is
        // called on the click event, the function will
        //  reference the same `num` (which now equals 3).

    });

};
```

>That's why regardless of which number we click on, they all alert the last value of `num`.

##### How do we fix it

>The solution involves utilizing closures. We're going to create an inner scope to hold the value of `num` **at the exact moment we add the event listener**. There are a number of ways to do this -- here's a good one.
>
>Let's simplify the code to just the lines where we add the event listener.

```js
var num = nums[i];

elem.addEventListener('click', function() {

    alert(num);

});
```

The `num` variable changes, so we have to somehow connect it to our event listener function. Here's one way of doing it. First take a look at this code, then I'll explain how it works.

```js
elem.addEventListener('click', (function(numCopy) {
    return function() {
        alert(numCopy)
    };
})(num));
```

>`(function(numCopy)` is the outer function. We immediately invoke it by wrapping it in parentheses and calling it right away, passing in num. This method of wrapping an anonymous function in parentheses and calling it right away is called an IIFE (Immediately-Invoked Function Expression, pronounced like "iffy"). This is where the "magical" part happens.
>
>We're passing the value of `num` into our outer function. Inside that outer function, the value is known as `numCopy` -- aptly named, since it's a copy of `num` in that instant. Now it doesn't matter that `num` changes later down the line. We stored the value of `num` in `numCopy` inside our outer function.
>
>Lastly, the outer function returns the inner function to the event listener. Because of the way JavaScript scope works, that inner function has access to `numCopy`. In the near future, `num` will increment, but that doesn't matter. The inner function has access to `numCopy`, which will never change.
>
>Now, when someone clicks, it'll execute the returned inner function, alerting `numCopy`.

##### The Final Version

>Here's our original code, but fixed up with our closure trick. Test it out!

```js
// clear the screen for testing
document.body.innerHTML = '';

var nums = [1,2,3];

// Let's loop over the numbers in our array
for (var i = 0; i < nums.length; i++) {

    // This is the number we're on...
    var num = nums[i];

    // We're creating a DOM element for the number
    var elem = document.createElement('div');
    elem.textContent = num;

    // ... and when we click, alert the value of `num`
    elem.addEventListener('click', (function(numCopy) {
        return function() {
            alert(numCopy);
        };
    })(num));

    document.body.appendChild(elem);
};
```

### Lesson 04. Refactoring with separation of concerns

- Refactoring is keeping the core functionality of the code the same, while making improvements to the functionality that will help the code scale. You can either start fresh ("burn it") or "refactor in place."
- The instructor goes through some ways to make the code more efficient.
  - Adding event handlers (listening for click events, etc.)
  - Storing data in the model, not in the view (DOM)
  - Ensuring the model and view never talk directly to each other, but go through the controller.
  - Having multiple views if needed.
- The repo [ud989-cat-clicker-premium-vanilla](https://github.com/udacity/ud989-cat-clicker-premium-vanilla) contains the instructor's refactored code.
- We were also given the [ud989-school-attendance](https://github.com/udacity/ud989-school-attendance) repo, intentionally authored as spaghetti code by Mike Wales, and told to refactor it.
- We also went to the [frontend-nanodegree-resume](https://github.com/udacity/frontend-nanodegree-resume)
 repo, part of the [Intro to JavaScript course](https://www.udacity.com/course/ud803).
- I laughed at the "How to modernize projects" section of the lesson. The instructor says, "Every company has legacy code, even Udacity." That's an understatement. Udacity doesn't keep its own courses updated. They don't even add licenses to their GitHub repos.

### Lesson 05. Using an organization library

- This is where we get into [KnockoutJS](http://knockoutjs.com/).
- KnockoutJS uses MVVM (Model View ViewModel).
- Library vs. Framework:
  - **Libaries are just a bunch of pre-written code.** jQuery is a library. Some of the most common functions addressed by libraries are DOM manipulation and AJAX.
  - **Frameworks give more structure to your code.** They are also sometimes called Organizational Libraries.
- It's not a cop-out to use a library. Engineering is all about taking what's already been done and tested, and using it to build something more.
- Fundamental organizational concepts:
  - **Model**: The data, maybe in JSON for example. Collections are smart arrays filled with models (data).
  - **View**: Pages the users view. Routers are similar (like app routes in Flask).
  - **Controller** (the "octopus"). Also called **ViewModel** for Knockout. Libraries/frameworks that don't fit the MVC paradigm are called MV*.
- **Knockout**
  - ViewModel: Similar to the "octopus" controller concept. Sits between data and DOM.
  - Declarative Bindings: Connect View and ViewModel
  - Automatic UI refresh: Updates view automatically when model changes
  - Dependency tracking: Models can depend on other models
- Knockout notes
  - Knockout is similar to jQuery, but extends the features of jQuery to provide more of an app framework.
  - **Observables** are variables that can automatically update the DOM when the view model changes.
    - [Example](http://jsfiddle.net/rniemeyer/3Lqsx/)

      ```js
      var myNum = 5
      var myNum = ko.observable(5)
      ```

    - Knockout also has smart arrays called [observableArrays](http://knockoutjs.com/documentation/observableArrays.html).
  - **Computed observables** create values when accessed.
    - The instructor started by creating a function

      ```js
      let firstName = 'Ben'
      let lastName = 'Jaffe'
      let fullName = function () {
        return firstName + ' ' + lastName
      }
      ```

    - Note that you could also code the instructor's example above with ES6 template literals and arrow functions.

      ```js
      let firstName = 'Ben'
      let lastName = 'Jaffe'
      let fullName = () => `${firstName} ${lastName}`
      console.log(fullName())
      ```

    - You actually don't even need a function. Not the greatest example.

      ```js
      let firstName = 'Ben'
      let lastName = 'Jaffe'
      let fullName = `${firstName} ${lastName}`
      console.log(fullName)
      ```

    - The instructor then uses `data-bind=""` attributes in the view HTML.
    - Knockout's method of encoding [computed observables](http://knockoutjs.com/documentation/computedObservables.html):

      ```js
      function AppViewModel () {
        this.firstName = ko.observable('Bert')
        this.lastName = ko.observable('Bertington')

        this.fullName = ko.computed(() =>
          `${this.firstName()} ${this.lastName()}`, this)
      }
      ```

    - Note that I included ES6 template literals and arrow functions.
    - The computed observables must be coded as functions. Again, not a great example because you could encode the fullName directly as a template literal.
  - We downloaded the [cat clicker knockout repo](https://github.com/udacity/ud989-cat-clicker-ko-starter) to practice.
- We get into `this`. The instructor uses `var self = this` (I guess with ES6 it would be `let self = this`) to allow reference to the top level `var viewModel` even when within other lower functions.
- **Documentation is important!** There was an interview with a Udacity engineer about the importance of documentation.
- Knockout's website looks several years out of date. The documentation doesn't even have previous/next navigation.

### Lesson 06. Learning a new codebase

- Getting handed a bunch of code and dealing with it.
- We worked with [TodoMVC](http://todomvc.com/), the same app written in many different frameworks. Cool. TodoMVC was created by Addy Osmani at Google. He has also written about [creating Progressive Web Apps (PWAs) with React](https://addyosmani.com/blog/progressive-web-apps-with-react/).
- The instructor Ben Jaffe incorporated TodoMVC into the [ud989-todo-app](https://github.com/udacity/ud989-todo-app) repo. **The instructor's repo hasn't been updated in over three years, no license, no README.**
- Ben goes through the different repo directories. They use Bower (outdated of course) to manage packages. Backbone is an organizational library used to separate concerns.
- Ben and Jacques say, "Always use semicolons." Jacques also says, "Remember kids: Always use tabs." No thanks.
- "Be tofu." Absorb the flavors from the codebase and adapt to the codebase.
- "Be a detective."

---

## Google Maps

### Lesson 07. Getting started with the APIs

- [Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/tutorial)
- This is the [Google Maps APIs course](https://www.udacity.com/course/google-maps-apis--ud864), with instructor Emily Keller from Google NYC. There is a [GitHub repo](https://github.com/udacity/ud864).
- As I went through the lesson, I compared the lesson code with the Maps docs, and added the code to my neighborhood map project.
- Maps are broken up into tiles and zoom levels.
- Emily creates an array and loops over it to drop pins, or [markers](https://developers.google.com/maps/documentation/javascript/markers), on the map. She mentions her favorite dessert place nearby, Rice to Riches.
- She adds [infoWindows](https://developers.google.com/maps/documentation/javascript/infowindows)
- She also adds event listeners to modify the page.
- Maps can be styled. See [Google map style docs](https://developers.google.com/maps/documentation/javascript/examples/maptype-styled-simple) and [SnazzyMaps](https://snazzymaps.com).
- [**Static maps**](https://developers.google.com/maps/documentation/maps-static/intro) are simple and embeddable. They are added through a separate API and may not be applicable to the neighborhood map project.
- Street views use pitch and heading to determine camera angle.
- Geometry library
- Visualization library has heat maps
- Drawing manager can add shapes around an area, and the user can also draw shapes.
  - Calculate area of a shape:

    ```js
    var area = google.maps.geometry.spherical.computeArea(polygon.getPath())
      window.alert(area+" SQUARE METERS")
    })
    ```

### Lesson 08. Understanding API services

- [Geocoding](https://developers.google.com/maps/documentation/geocoding/intro) allows conversion between addresses and lat lng. It takes in a lat lng and returns an address. Reverse geocoding takes an address and returns lat lng.
- The geocoding API can accept HTTP requests, and returns JSON.

  ```text
  https://maps.googleapis.com/maps/api/geocode/outputFormat?parameters
  ```

- Don't confuse geocoding with [geocaching](https://www.geocaching.com/play). I remember when geocaching became popular a few years ago.
- Quiz response: Key and address are needed.
  - >Great job! The address is the only information needed to complete a geocoding request. Alternatively, if Ajay was doing REVERSE geocoding, he would only need to provide the latlng parameter! The KEY is required for authentication. Region is an optional parameter, which will BIAS the results toward a specific region.
- Distance matrix API
- Directions API
  - Quiz: Starting in Florence, Italy, calculate the optimized route to visit Bologna, Genoa, and Venice, stopping in Milan. We used the distance API with the `waypoints` parameter and `optimize:true`.
- The roads API allows snapping to roads with `snapToRoads`.
- Searching for places of interest within the map: See ud864-master/Project_Code_12_FasterIsBetterPlacesAutocompletePart2.html
- [Places library](https://developers.google.com/maps/documentation/javascript/places):
  - [Place details requests](https://developers.google.com/maps/documentation/javascript/places#place_details) return detailed information about places, including hours of operation and user reviews.
  - Each place has its own unique **Place ID.**
  - [**Place IDs**](https://developers.google.com/places/place-id) can be passed like lat lng into the Places web service database.

    ```text
    https://maps.googleapis.com/maps/api/place/details/json?placeid=PLACE_ID&key=YOUR_API_KEY
    ```

  - The JSON returned includes operating hours (including `open_now: true`) and other details.
- Geolocation API
  - The geolocation API can be used to retrieve geolocation info for a device.

### Lesson 09. Using the APIs in practice

## Feedback

These lessons were "part 4" of the Udacity Full Stack Web Developer Nanodegree program. As usual, the lessons didn't really teach me what I needed to know, especially not for Knockout. It was frustrating to be working with Knockout, which is basically like an inferior predecessor to React. Udacity may have held off on including React here because it's a lot to learn, and because they want more customers for their React Nanodegree program. I also found it amusing to look at comments for the lesson videos on YouTube. "You call this a tut? It sucks." I'm inclined to agree.

[(Back to TOC)](#table-of-contents)