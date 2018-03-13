Lesson 19: Building Up
======================

**Udacity Full Stack Web Developer Nanodegree program**

Part 01. Programming fundamentals and the web

Project 02. Build a portfolio site

Brendon Smith | br3ndonland

---

# Lesson

1. Lesson Intro

    A responsive website applies styles based on the characteristics of the device. In order to make a site fully responsive, we need to think about the entire design.

2. Basic Media Query Intro

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

3. Adding a Basic Media Query

    in the GA_wdi_03_business.html, we created a media query to resize the site on screens <500px. Here, we will set up a media query that activates when the screen is >500px. We add a new stylesheet, and link to it in the site HTML.

    ```html
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" media="screen and (min-width:500px)" href="over500.css">
    ```

    **Stick with `media="screen"` or `media="print"`. Other types didn't gain traction.**

4. Adding a basic media query 2

    - As in the GA_wdi_03_business.html example, we will embed the media query with an `@media` tag. Avoid the `@import` tag "for performance reasons."
    - Weigh the costs between linked CSS (many small http requests) and `@media` (few large http requests)

5. Next Step Media Queries

    - `min-width` and `max-width` are most frequently used.
    - `min-device-width` and `max-device-width` are strongly discouraged. They are based on the size of the total screen, not the viewport.

6. Quiz: Which styles are applied?

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

7. Breakpoints

    A **breakpoint** is the point at which the site changes layout.

8. Breakpoints Pt. II

    Cameron starts with skinnyties.com. He calls the three bar nav icon a "hamburger."

9. Quiz: Number of Breakpoints

    * Example site has two: 500px, 600px
    * Medium.com has two breakpoints, 768px, 992px.

10. Picking Breakpoints

    Breakpoints should not be defined based on a specific device. Define breakpoints based on content.

    > We shouldn't choose breakpoints at all. Instead, we should find them, using our content as a guide.
    
    Scott Yale

11. [Picking Breakpoints 2](https://youtu.be/17XgkPFq6eY)

    * Again, start with smallest first. In all our examples, we have had two breakpoints to create three viewports: small, medium, large.

12. Quiz: Pick a Breakpoint

    * I looked at the content, particularly the tables, and picked 600px as a breakpoint.

13. Complex Media Queries
14. Quiz: What Styles Are Applied?

    <img src="https://www.dropbox.com/s/3qv6qtajd8ns3f1/Screen%20Shot%202017-10-16%20at%206.51.18%20PM.png?dl=1">

15. Grids

    * They mentioned fluid grids, and how Bootstrap is a pre-made fluid grid layout.

16. Flexbox Intro

    Use flexboxes for responsive grid layouts.

17. Flexbox Container
    
    * `display: flex;`. The default flex direction is row.
    * `flex-wrap: wrap;` allows elements to wrap to the next line.

18. Flex Item

    * set order of elements with an `order attribute`

19. Deconstructing a Flexbox Layout
20. Quiz: Deconstructing a Flexbox Layout

    <img src="https://www.dropbox.com/s/8kl5oti33lrb06b/Screen%20Shot%202017-10-16%20at%208.22.20%20PM.png?dl=1">

21. Responsive Design Outro

