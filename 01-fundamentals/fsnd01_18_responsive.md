Lesson 18: Starting Small
========================

**Udacity Full Stack Web Developer Nanodegree program**

Part 01. Programming fundamentals and the web

Project 02. Build a portfolio site

Brendon Smith | br3ndonland

---

# Lesson

1. Defining the Viewport

    The Viewport defines the area of the screen that the browser can render content to.

2. Pixels, pixels and moar pixels!

    - "A pixel isn't always a pixel."
    - **Browsers report width in Device Independent Pixels (DIPs). DIPs take up the same amount of space, regardless of the device's pixel density.**
    - The browser must be told that the site was designed to work on a small screen, or it will render the page at full DIPs as if it were on a desktop.

3. Quiz: Pixelation

    - Pixel measurements in web development are complicated.
    - Tech specs typically refer to hardware pixels, so a 1080p mobile screen will have 1920px x 1080px.

4. Quiz: Calculating DPR

    - **Device Pixel Ratio (DPR)** of 2: one DIP for every two hardware pixels.

5. Quiz: What's the difference?

    - *why would a site with the same HTML and CSS render differently on two devices?* -> Viewport may need to be set, and DPR may be different.

6. Quiz: Calculating CSS Pixels
    
    - Right! Divide 1920px by 2 and you get a viewport width of 960 CSS pixels.

7. Quiz: How wide is the viewport?

    We just calculated the DIPs for each device, given hardware pixels and DPR.

8. Setting the Viewport
    
    - Udacity: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
    - The viewport tag is actually not standardized yet. See [MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Mobile/Viewport_meta_tag). 

9. Quiz: Setting the Viewport

    - We added a viewport to Cameron's website to make it responsive.
    - See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta) for a refresher on the meta tag.

10. Large Fixed Width Elements

    - Need to have images resize with the viewport.
    - Use relative units (100%). 
    - I used relative units in the General Assembly Dash website projects.

11. Max-width on elements

    Include a catch-all in your CSS:
    ```css
    img, embed, object, video {
        max-width: 100%;
    }
    ```

12. Quiz: Relative Sizes
13. Tap Target Sizes

    - Tap targets need to be large enough to be easy to hit on mobile devices.
    - CSS pixels: 48 px x 48 px is generally large enough for tap targets.

14. Quiz: Tap Targets

    ```css
    nav a, button {
        min-width: 48px;
        min-height: 48px;    
    }
    ```

15. Start Small

    - Design your site with the smallest screen in mind first.
    - `#PerfMatters`

16. Quiz: Project Part 1

    I downloaded the files and edited in Sublime text instead of Chrome Dev Tools so I could save the changes easily.

    a. *add meta viewport tag:* copy and paste `<meta name="viewport" content="width=device-width, initial-scale=1.0">` into the HTML head
    b. *single column and relative widths:* replace `float` in top-level element CSS with `display: block;`, add `width: 100%`
    c. *touch targets:* modified the `.nav_item` CSS to include ` min-width: 48px; min-height: 48px;`
    d. *test across different viewports:* done

    My solution actually looks better than the Udacity solution. 

    - My header nav buttons are centered on mobile devices, like iPhone 5, their buttons are not.
    - Their header doesn't extend the full width of the device

17. Project Solution - Long

    I didn't need to watch this because I got the solution on my own.

18. Lesson Summary