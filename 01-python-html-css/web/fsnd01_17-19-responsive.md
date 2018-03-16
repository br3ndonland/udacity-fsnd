# Lessons 17-19: Responsive Design

**Udacity Full Stack Web Developer Nanodegree program**

Part 01. Programming fundamentals and the web

[Responsive Web Design Fundamentals by Google](https://www.udacity.com/course/responsive-web-design-fundamentals--ud893)

Brendon Smith

br3ndonland

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Lesson 17: Responsive Design](#lesson-17-responsive-design)
- [Lesson 18: Starting Small](#lesson-18-starting-small)
- [Lesson 19: Building Up](#lesson-19-building-up)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Lesson 17: Responsive Design

### 17.01. Sites On Mobile

Pete LePage, front-end advocate at Google
Cameron Pittman, course developer at Udacity

Google News uses a fully responsive layout for mobile, and a less responsive version for desktops. They have to maintain the two different versions. The Skinny Ties site is always fully responsive. I also found the creator of the Skinny Ties site, [Gravity Department](http://gravitydept.com/). 


### 17.02. Quiz: Share Your Great & Awful Sites

Responsive sites

* curator.io
* material.io

Instructor answer:

* alistapart.com


### 17.03. Intro to Project

* Cameron mentioned "lessons 2, 4, and 5," which I think is in reference to the standalone responsive design course.
* We will have to make a website responsive.
* Think responsive from the start.


### 17.04. Pan, Zoom, Touch, Ick

### 17.05. Emulators, Simulators and Real Devices

https://www.browserstack.com/


### 17.06. Setting up Chrome's Dev Tools

Click the mobile icon in Chrome's developer tools to view a mobile version.

From [Google](https://developers.google.com/web/fundamentals/):

> The core foundations of a delightful web experience are...
> 
> * **Fast** - It respond quickly to user interactions with silky smooth animations and no janky scrolling.
> * **Integrated** - The user doesn’t have to reach through the browser, it uses the full capabilities of the device to create an experience true to the device.
> * **Reliable** - Load instantly and reliably, never showing the downasaur, even in uncertain network conditions.
> * **Engaging** - Keeps the user coming back to the app with beautifully designed experiences that look and feel natural.
> 
> <img src="img/fsnd01_17_0601-google-hero-2x.png" alt="Google web design graphic" width="75%">

### 17.07. IMPORTANT! Udacity Front End Feedback Extension

### 17.08. Quiz: Device Emulation

We added a custom device emulation into Chrome Developer Tools.


### 17.09. Remote Debugging Intro

Debugging in Chrome for Android


### 17.10. Setup for mobile

* Android developer mode: go to device settings, click on build number seven times (seriously).
* USB debugging: usually in developer options on device. After turning on, connect USB to desktop, 
* Chrome: install chrome canary on desktop, chrome beta on android.


### 17.11. Using dev tools on mobile
### 17.12. Mobile tools for iOS
### 17.13. Lesson 1 Summary

---

## Lesson 18: Starting Small

### 18.01. Defining the Viewport

The Viewport defines the area of the screen that the browser can render content to.


### 18.02. Pixels, pixels and moar pixels!

* "A pixel isn't always a pixel."
* **Browsers report width in Device Independent Pixels (DIPs). DIPs take up the same amount of space, regardless of the device's pixel density.**
* The browser must be told that the site was designed to work on a small screen, or it will render the page at full DIPs as if it were on a desktop.


### 18.03. Quiz: Pixelation

* Pixel measurements in web development are complicated.
* Tech specs typically refer to hardware pixels, so a 1080p mobile screen will have 1920px x 1080px.


### 18.04. Quiz: Calculating DPR

* **Device Pixel Ratio (DPR)** of 2: one DIP for every two hardware pixels.

### 18.05. Quiz: What's the difference?

* *why would a site with the same HTML and CSS render differently on two devices?* -> Viewport may need to be set, and DPR may be different.


### 18.06. Quiz: Calculating CSS Pixels
		
> Right! Divide 1920px by 2 and you get a viewport width of 960 CSS pixels.


### 18.07. Quiz: How wide is the viewport?

We just calculated the DIPs for each device, given hardware pixels and DPR.


### 18.08. Setting the Viewport

* Udacity: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
* The viewport tag is actually not standardized yet. See [MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Mobile/Viewport_meta_tag). 


### 18.09. Quiz: Setting the Viewport

* We added a viewport to Cameron's website to make it responsive.
* See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta) for a refresher on the meta tag.


### 18.10. Large Fixed Width Elements

* Need to have images resize with the viewport.
* Use relative units (100%). 
* I used relative units in the General Assembly Dash website projects.


### 18.11. Max-width on elements

Include a catch-all in your CSS:
```css
img, embed, object, video {
		max-width: 100%;
}
```

### 18.12. Quiz: Relative Sizes

### 18.13. Tap Target Sizes

* Tap targets need to be large enough to be easy to hit on mobile devices.
* CSS pixels: 48 px x 48 px is generally large enough for tap targets.

### 18.14. Quiz: Tap Targets

```css
nav a, button {
		min-width: 48px;
		min-height: 48px;    
}
```


### 18.15. Start Small

* Design your site with the smallest screen in mind first.
* `#PerfMatters`


### 18.16. Quiz: Project Part 1

* I downloaded the files and edited in Sublime text instead of Chrome Dev Tools so I could save the changes easily.
* Steps:
	- *add meta viewport tag:* copy and paste `<meta name="viewport" content="width=device-width, initial-scale=1.0">` into the HTML head
	- *single column and relative widths:* replace `float` in top-level element CSS with `display: block;`, add `width: 100%`
	- *touch targets:* modified the `.nav_item` CSS to include ` min-width: 48px; min-height: 48px;`
	- *test across different viewports:* done
* My solution actually looks better than the Udacity solution:
	- My header nav buttons are centered on mobile devices, like iPhone 5, their buttons are not.
	- Their header doesn't extend the full width of the device


### 18.17. Project Solution - Long

I didn't need to watch this because I got the solution on my own.

### 18.18. Lesson 2 Summary

---

## Lesson 19: Building Up

### 19.01. Lesson Intro

A responsive website applies styles based on the characteristics of the device. In order to make a site fully responsive, we need to think about the entire design.

### 19.02. Basic Media Query Intro

Include an additional stylesheet with a media query. Also see GA_wdi_03_business.html, where I included a media query.

```css
@media (max-width: 500px) {
  h1 {
    font-size: 50px;
    margin-top: 20px;
    line-height: 40px;
  }
  h2 {
    font-size: 20px;
    margin: 20px 0 30px 0;
  }
  div {
    margin: 20px 12px 0 12px;
  }
  p {
    font-size: 12px;
    line-height: 24px;
    width: 90%;
  }
  small {
    font-size: 10px;
  }
}
```

### 19.03. Adding a Basic Media Query

In GA_wdi_03_business.html, we created a media query to resize the site on screens <500px. Here, we will set up a media query that activates when the screen is >500px. We add a new stylesheet, and link to it in the site HTML.

```html
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" media="screen and (min-width:500px)" href="over500.css">
```

**Stick with `media="screen"` or `media="print"`. Other types didn't gain traction.**


### 19.04. Adding a basic media query 2

* As in the GA_wdi_03_business.html example, we will embed the media query with an `@media` tag. Avoid the `@import` tag "for performance reasons."
* Weigh the costs between linked CSS (many small http requests) and `@media` (few large http requests)

### 19.05. Next Step Media Queries

* `min-width` and `max-width` are most frequently used.
* `min-device-width` and `max-device-width` are strongly discouraged. They are based on the size of the total screen, not the viewport.


### 19.06. Quiz: Which styles are applied?

We made some changes to the `<style type="text/css"></style>` section of the `<head></head>` of the sample site, to apply different colors to the <`body></body>` depending on the. Cameron mentioned that it was easier to write the code in Sublime Text and paste it in.

```html
<style type="text/css">
  h1 {
    position: absolute;
    text-align: center;
    width: 100%;
    font-size: 6em;
    font-family: Roboto;
    transition: all 0.5s;
  }
  @media screen and (min-width: 0px) and (max-width: 400px) {
    body {
      background-color: red;
    }
  }
  @media screen and (min-width: 401px) and (max-width: 600px) {
    body {
      background-color: green;  
    }
  }
  @media screen and (min-width: 600px) {
    body {
      background-color: blue;    
    }
  }
</style>
```


### 19.07. Breakpoints

A **breakpoint** is the point at which the site changes layout.


### 19.08. Breakpoints Pt. II

Cameron starts with skinnyties.com. He calls the three bar nav icon a "**hamburger**."


### 19.09. Quiz: Number of Breakpoints

* Example site has two: 500px, 600px
* Medium.com has two breakpoints, 768px, 992px.


### 19.10. Picking Breakpoints

Breakpoints should not be defined based on a specific device. **Define breakpoints based on content.**

> We shouldn't choose breakpoints at all. Instead, we should find them, using our content as a guide.

Scott Yale

### 19.11. Picking Breakpoints 2

[Video](https://youtu.be/17XgkPFq6eY)

Again, start with smallest first. In all our examples, we have had two breakpoints to create three viewports: small, medium, large.


### 19.12. Quiz: Pick a Breakpoint

I looked at the content, particularly the tables, and picked 600px as a breakpoint.


### 19.13. Complex Media Queries

### 19.14. Quiz: What Styles Are Applied?

<img src="img/fsnd01_19_1401.png" alt="Practice with media queries" width="75%">


### 19.15. Grids

They mentioned fluid grids, and how Bootstrap is a pre-made fluid grid layout.


### 19.16. Flexbox Intro

Use flexboxes for responsive grid layouts.


### 19.17. Flexbox Container

* `display: flex;`. The default flex direction is row.
* `flex-wrap: wrap;` allows elements to wrap to the next line.


### 19.18. Flex Item

Set order of elements with an `order attribute`


### 19.19. Deconstructing a Flexbox Layout

### 19.20. Quiz: Deconstructing a Flexbox Layout

<img src="img/fsnd01_19_2001.png" alt="Flexbox layout example" width="75%">


### 19.21. Responsive Design Outro