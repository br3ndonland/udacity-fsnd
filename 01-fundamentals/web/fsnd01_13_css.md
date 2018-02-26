Lesson 13: CSS syntax
=====================

**Udacity Full Stack Web Developer Nanodegree program**

Part 01. Programming fundamentals and the web

Project 02. Build a portfolio site

Brendon Smith | br3ndonland

---

## Lesson

1. Getting Started With CSS

    Intro by James Parks

2. What is CSS?

    **Cascading style sheets.** Webpage styling. Sometimes you may load a website and just see a plain text outline. It is lacking CSS.

    If you want to try removing the style from the Youtube homepage yourself, follow these instructions: *see [Developer Tools](#developer-tools) below*

3. Quiz: CSS or HTML?
    
    This was easy. The website with styling is the one with css.

4. CSS Rulesets

    James showed Coca-Cola's website. 

    - All css begins with a **ruleset.** The ruleset has two parts:
        + **Selector:** selects the HTML elements to style
        + **Declaration block:** describes the style to apply to HTML.
    - CSS rulesets can be included in the HTML `<head></head>` inside the `<style type="text/css"></style>` tags.

5. Quiz: CSS Syntax

    I got the answer quickly. I first thought it would be `<title></title>`, but that didn't work, and I realized the title was an `<h1></h1>`. 

    ```html
    <!DOCTYPE html>

    <!-- Instructions: Change the color of "Hello, world!" to green. -->

    <html>
    <head>
        <title>Quiz - Hello, world!</title>
        <style>
            p {
                color: blue;
            }        
            /* add CSS here */
            h1 {
                color: green;
            }
        </style>
    </head>
    <body>
        <h1>Hello, world!</h1>
        <p>Are you ready for your first challenge?</p>
        <p>Let's add some style to this webpage!</p>
    </body>
    </html>
    ```


6. Comments

    Comments
    Let's take a quick diversion to cover something useful: code comments.

    A comment is a human-readable message inside code. Comments are usually surrounded by or preceded by special characters that instruct computers to completely ignore whatever text is inside the comment. Comments are great because they allow you, the developer, to leave clarifying messages and instructions for other developers (as well as your future self!). Every programming language gives you the ability to write comments.

    Comments are also useful when you're testing your code. Rather than deleting potentially useful chunks of code, you can comment them out, getting the same effect without the risk of accidentally losing work!

    CSS Comments
    You saw a CSS comment in the code from your previous quiz:

    ```css
    p {
        color: blue;
    }        
    /* add CSS here */
    h1 {
        color: red;
    }
    ```
    The line /* add CSS here */ is a comment. CSS comments are surrounded by an opening /* and a closing */. You must use both. The comment made it clear to you where you needed to add your code and it did not affect the style of the page in any way.

    HTML Comments
    You can write comments in HTML too! Here's how they look.

    ```html
    <!-- This is a comment -->
    <div class="example">Words, words, words.</div>
    ```
    You must surround your HTML comments with a starting `<!-- and a closing -->`.

    Now, back to CSS.


7. Quiz: Tag Selectors

    Including a tag selector like `<p></p>` will affect all paragraphs within `<p></p>` tags.


8. Attributes and Selectors

    tag selector

    ```css
    h1 {
      color: green;
    }
    ```

    `class` attribute selector
    **Classes are flexible and powerful. The same class can be used in multiple HTML elements, and HTML elements can have multiple classes. This allows you to subdivide instances of the same class. Most web developers prefer classes over IDs, because they organize the HTML and because they can be used as CSS selectors.**

    ```css
    <p id="site-description">favorite books</p>
    <hr>
    <h2 class="book-title">Robinson Crusoe</h2>
    ```
    **To select an HTML class to style with CSS, type a period followed by the name of the class:**
    ```css
    .book-summary {
      color: blue;
    }
    ```

    `id` attribute selector
    **IDs should be used sparingly. An HTML element can have only one ID, and IDs can be used only once per page (in one element).**
    **To select an ID, use a pound sign followed by the name:**
    ```css
    #site-description {
      color: red;
    }
    ```
    

9. Quiz: Using Selectors

    Instructions — Which HTML elements match the given CSS statement?
    ```css
    .right {
       text-align: right;
    }
    ```

    - `<div class="right"></div>` yes
    - `<a href="#" class="leftright"></a>` no, no space between left and right
    - `<button id="right"></button>` no, it's an id not a class
    - `<p class="highlight module right"></p>` yes, multiple classes can be selected if separated by spaces, and order does not matter.


10. Udacity Front End Feedback Extension
    
    Already got it

11. Quiz: Writing Selectors


    <html>
    <div class="index--markdown--2I2Ir ureact-markdown "><h1 id="writing-selectors">Writing Selectors</h1>
    <p>At this point, you should be familiar with the basic structure of a CSS statement. Every CSS statement is made up of a <strong>selector</strong> and a <strong>declaration block</strong>. The selector tells the browser what HTML element we want to style and the declaration block tells the browser what styles need to be applied to that HTML.</p>
    <p><img src="http://udacity.github.io/fend/lessons/L3/problem-set/05-writing-selectors/css-statement.png" alt="css statement"></p>
    <p><em>The basic structure of a CSS statement</em></p>
    <p>For this quiz, I want you to focus exclusively on the selector part of a CSS statement. To do this, I've created a webpage that is lacking style. The webpage already has ids and classes added to the HTML, but it's missing the right selectors to add the style.</p>
    <pre><code class="lang-html"><span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">id</span>=<span class="hljs-value">"menu"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">h1</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"item"</span>&gt;</span>Chicken Clay Pot<span class="hljs-tag">&lt;/<span class="hljs-title">h1</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">img</span> <span class="hljs-attribute">src</span>=<span class="hljs-value">"img/clay-pot.jpg"</span> <span class="hljs-attribute">alt</span>=<span class="hljs-value">"clay pot"</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"picture"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">p</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"description"</span>&gt;</span>Crispy rice baked in clay pot topped with chicken and vegetables<span class="hljs-tag">&lt;/<span class="hljs-title">p</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    </code></pre>
    <pre><code class="lang-css"><span class="hljs-comment">/* missing id */</span> <span class="hljs-rules">{
      <span class="hljs-rule"><span class="hljs-attribute">text-align</span>:<span class="hljs-value"> center</span></span>;
    }</span>
    <span class="hljs-comment">/* missing class */</span> <span class="hljs-rules">{
      <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> red</span></span>;
    }</span>
    <span class="hljs-comment">/* missing class */</span> <span class="hljs-rules">{
      <span class="hljs-rule"><span class="hljs-attribute">border-radius</span>:<span class="hljs-value"> <span class="hljs-number">5px</span></span></span>;
    }</span>
    <span class="hljs-comment">/* missing class */</span> <span class="hljs-rules">{
      <span class="hljs-rule"><span class="hljs-attribute">font-style</span>:<span class="hljs-value"> italic</span></span>;
    }</span>
    </code></pre>
    <p>It's your job to download the webpage and fill-in the missing selectors. If you do it right, your webpage should end up looking like this...</p>
    <p><img src="http://udacity.github.io/fend/lessons/L3/problem-set/05-writing-selectors/clay-pot-solution.jpg" alt="writing selectors solution"></p>
    <h2 id="how-to-complete-this-quiz">How to Complete this Quiz</h2>
    <ol>
    <li>Download the zip file called <code>writing-selectors.zip</code> from the resources section or from <a target="_blank" href="http://udacity.github.io/fend/lessons/L3/problem-set/05-writing-selectors/writing-selectors.zip">here</a>.</li>
    <li>Open <code>index.html</code> and turn on the <a target="_blank" href="https://classroom.udacity.com/nanodegrees/nd001/parts/0011345403/modules/742847927175460/lessons/7323812069/concepts/73256617910923">Udacity Feedback Chrome Extension</a>.</li>
    <li>Edit <code>index.html</code> and add the missing id and class selectors within the <code>&lt;style&gt;</code> tags (alternatively, you can use Developer Tools to add the missing id and class selectors to pass all the tests).</li>
    <li>When you've successfully added the correct selectors, copy and paste the code that appears into the next page to finish!</li>
    </ol>
    <p>When you're ready to get started, click "Skip to Quiz".</p>
    </div>
    </html>

    **Got it on my first try!**
    **Completed code:**

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Writing Selectors Quiz</title>
        <!-- the next line loads the tests for the Udacity Feedback extension -->
        <meta name="udacity-grader" content="http://udacity.github.io/fend/lessons/L3/problem-set/05-writing-selectors/tests.json">
        <style>
            #menu {
                text-align: center;
            }
            .item {
                color: red;
            }
            .picture {
                border-radius: 5px;
            }
            .description {
                font-style: italic;
            }
        </style>
    </head>
    <body>
        <div id="menu">
            <h1 class="item">Chicken Clay Pot</h1>
            <img src="img/clay-pot.jpg" alt="clay pot" class="picture">
            <p class="description">Crispy rice baked in clay pot topped with chicken and vegetables</p>
        </div>
    </body>
    </html> 
    ```



12. Quiz: Using CSS References

    Instructions — Use CSS References to answer the questions below.

    - *What CSS property is used to italicize text?* font-style
    - *What CSS property is used to underline text?* text-decoration
    - *What CSS property is used to uppercase text?* text-transform
    - *What CSS property is used to bold text?* font-weight

    [Mozilla MDN CSS Fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts)

13. Developer Tools

    *see [Developer Tools](#developer-tools) below*

14. Developer Tools on Different Browsers
15. Quiz: Using Developer Tools
16. CSS Units

    CSS uses absolute (pixels, mm, cm, in) and relative (percentages, em, vw, vh) units.

17. Quiz: Units in CSS

    Instructions — Add the following changes to the webpage:

    - *set the first div's width to 100px (pixels)*
    - *set the second div's height to 200px (pixels)*
    - *set the third div's margin to 1em*
    - *set the fourth div's font-size to 2em*

    ```html
    <!DOCTYPE html>

    <!-- Instructions: Add the following changes to this webpage:

    - set the first div's width to 100px (pixels)
    - set the second div's height to 200px (pixels)
    - set the third div's margin to 1em
    - set the fourth div's font-size to 2em

    -->

    <html>
    <head>
        <title>Quiz - Units in CSS</title>
        <style>
            .first {
                width: 100px;
            }
            .second {
                height: 200px;
            }
            .third {
                margin: 1em;
            }
            .fourth {
                font-size: 2em;         
            }
        </style>
    </head>
    <body>
        <div class="first"></div>
        <div class="second"></div>
        <div class="third">Hammock ex plaid nulla. Nihil stumptown gastropub, dreamcatcher gochujang franzen cillum cliche keffiyeh pop-up pug small batch knausgaard. Fanny pack elit you probably haven't heard of them before they sold out. Sint elit tofu et veniam irony 3 wolf moon. VHS slow-carb trust fund chartreuse wolf. Qui sed dreamcatcher cronut, hoodie fixie normcore. Gochujang dolor consectetur post-ironic.</div>
        <div class="fourth">Hammock ex plaid nulla. Nihil stumptown gastropub, dreamcatcher gochujang franzen cillum cliche keffiyeh pop-up pug small batch knausgaard. Fanny pack elit you probably haven't heard of them before they sold out. Sint elit tofu et veniam irony 3 wolf moon. VHS slow-carb trust fund chartreuse wolf. Qui sed dreamcatcher cronut, hoodie fixie normcore. Gochujang dolor consectetur post-ironic.</div>
    </body>
    </html>
    ```

    **The quiz was throwing an error even though I had all the code correct.**

18. CSS Colors

    - Color is light. All light is a combination of red, green, blue.
    - RGB values are written as 0-255, with 255 being 100% presence of that color.
    - Hexadecimal: FF is equivalent to 255, or 100% presence of light.
    - Color pickers are a fast way to get the hex code.


    How Hexadecimal Works

    - [The Hexadecimal Numeral System](https://en.wikipedia.org/wiki/Hexadecimal)
    - [Hex to RGB Convertor](http://hex.colorrrs.com/)


19. Quiz: Identifying Colors

    shorthand can be used to identify colors, like `color: #00f` for blue

20. Quiz: Style an Image


    My code: got it on the first try!

    ```html
    <!DOCTYPE html>

    <!-- Instructions: Replicate the same styling seen in the kitten image below. -->

    <html>
    <head>
        <title>Style an Image Quiz</title>
        <style>
            .kitten-image {
                border: thick dashed;
                border-color: #fa8072;
                border-radius: 5px;
                -webkit-box-shadow: 10px 10px 22px 0px rgba(0,0,0,0.1);
                -moz-box-shadow: 10px 10px 22px 0px rgba(0,0,0,0.1);
                box-shadow: 10px 10px 22px 0px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <!-- Image credit: Nicolas Suzor, https://www.flickr.com/photos/nicsuzor/ - via Flickr, Creative Commons. -->
            <img src="http://udacity.github.io/fend/lessons/L3/problem-set/02-style-an-image/kitten.jpg" alt="kitten" class="kitten-image">
    </body>
    </html>
    ```

    Instructor code:

    ```css
    .kitten-image {
      border: 5px dashed salmon;
      border-radius: 5px;
      cursor: pointer;
      box-shadow: 5px 5px 20px #ccc;
    }
    ```

21. Quiz: Style the Font

    My code

    ```html
    <!DOCTYPE html>

    <!-- Instructions: Replicate the same styling seen in the Udacity text below. -->

    <html>
    <head>
        <title>Style the Font Quiz</title>
        <style>
            .udacity-text {
                font-family: arial;
                font-size: 60px;
                color: #8001ff;
                text-decoration: underline;
                text-transform: uppercase;
            }
        </style>
    </head>
    <body>
        <h1 class="udacity-text">udacity</h1>
    </body>
    </html>
    ```

22. Quiz: Slack Card

    I tried using Chrome Developer tools to edit the Slack card. It was a pain. I wasn't sure how to insert a line break.

23. Quiz: Udacity Site Header

    Again, wasn't really able to save the code because developer tools is difficult to use. It was just formatting a website header.

24. What is a Stylesheet?
    <html>
    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><h1 id="what-is-a-stylesheet-">What is a Stylesheet?</h1>
    <p>In the next quiz, you'll be working with a stylesheet. So what is a stylesheet and why is it important? Well, consider the following question...</p>
    <p><em>What if you wanted to use the same CSS on more than one webpage?</em></p>
    <p>You could just copy all of your CSS from one file and paste it into another, but that seems like a lot of extra work and doesn't scale very well. What if you decide to make changes later? You'd have to change every copy of the CSS!</p>
    <p>There's got to be a better way...</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/5792aac7_better-way-meme/better-way-meme.jpg" class="index--image--1wh9w" style="width: 320px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>There's got to be a better way meme</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>While the process described above works, it's not recommended. Instead, the preferred method is to write your CSS in a file called a <strong>stylesheet</strong> and then link to that file in your HTML.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/5792ab14_side-by-side-html-css/side-by-side-html-css.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Example HTML Document and CSS Stylesheet</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><h2 id="stylesheets">Stylesheets</h2>
    <p>A stylesheet is a file containing the code that describes how elements on your webpage should be displayed.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/5792ab54_example-css-file/example-css-file.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Example CSS File</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>This is no different than what you've been doing before, except the CSS lives in a different file... and you don't have to use the <code>&lt;style&gt;</code> tags anymore. To create a stylesheet, simply add a new file to your project, write some CSS, and save it as <code>name-of-stylesheet.css</code>.</p>
    <h2 id="how-to-link-to-a-stylesheet">How to Link to a Stylesheet</h2>
    <p>Before your webpage can use the stylesheet, you need to link to it. To do this, you'll need to create a <code>&lt;link&gt;</code> to your stylesheet in your HTML. To create a link, simply type the following inside the <code>&lt;head&gt;</code> of your HTML.</p>
    <pre><code class="lang-html"><span class="hljs-tag">&lt;<span class="hljs-title">link</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">"path-to-stylesheet/stylesheet.css"</span> <span class="hljs-attribute">rel</span>=<span class="hljs-value">"stylesheet"</span>&gt;</span>
    </code></pre>
    <p>The <code>href</code> attribute specifies the <strong>path</strong> to the linked resource (you can link to other resources besides stylesheets, more on this later) and the <code>rel</code> attribute names the <strong>relationship</strong> between the resource and your document. In this case, the relationship is a stylesheet. When you're done, it will look something like this...</p>
    <pre><code class="lang-html"><span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>My Webpage<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-comment">&lt;!-- ... --&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">link</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">"path-to-stylesheet/stylesheet.css"</span> <span class="hljs-attribute">rel</span>=<span class="hljs-value">"stylesheet"</span>&gt;</span>
      <span class="hljs-comment">&lt;!-- ... --&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    </code></pre>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>
    </html>

25. Quiz: Link to a Stylesheet

    - downloaded files
    - added link to css into html index with `<link rel="stylesheet" type="text/css" href="css/styles.css">`

26. Outro

## other notes

* [Sass](http://sass-lang.com/) (Syntactically Awesome Style Sheets) extends the functionality of CSS.
* [CSSmatic](http://www.cssmatic.com/) generates CSS features


## Developer tools

* open with cmd+opt+j
* Developer tools allow you to edit webpages live. You can edit each element.
To restore the page, just refresh.
* I worked with developer tools for a little bit. I edited the LeanBox website.

Editing site with developer tools

* How do you add a line break to the CSS? -> right click on the style tag and select "edit as HTML"

Mobile development 

* Click the mobile icon in Chrome's developer tools to view a mobile version.

Saving site with developer tools

* Add folder to workspace
* Map to file system resource: 
    - *How do i do this for the entire site? Is it just for specific files?*
    - I tried searching, but [Stack Overflow](https://stackoverflow.com/questions/6843495/how-to-save-css-changes-of-styles-panel-of-chrome-developer-tools) wasn't very helpful.
    - It looks like you have to download the file, then make modifications. If you have made modifications directly in the browser, and want to save them, I thought you might have to copy the elements and paste them into the desktop file with your text editor. 
    - [Set Up Persistence with DevTools Workspaces](https://developers.google.com/web/tools/setup/setup-workflow)

        > + TL;DR
            * Don't manually copy changes to local files. Use workspaces to persist changes made in DevTools to your local resources.
            * Stage your local files to your browser. Map files to URLs.
            * Once persistent workspaces are set-up, style changes made in the Elements panel are persisted automatically; DOM changes aren't. Persist element changes in the Sources panel instead.
        + Limitations
        As powerful as Workspaces are, there are some limitations you should be aware of.
            * Only style changes in the Elements panel are persisted; changes to the DOM are not persisted.
            * Only styles defined in an external CSS file can be saved. Changes to element.style or to inline styles are not persisted. (If you have inline styles, they can be changed on the Sources panel.)

Deleting elements with developer tools

* Visit https://www.youtube.com/ or any other website of your choice.
* Right click anywhere on the page, and click "Inspect" (on Mac) or "Inspect Element" (Firefox)
* You'll see a panel showing HTML. Inside the <head> element, delete any line that has rel="stylesheet". For example:
    ```html
    <link rel="stylesheet" href="//s.ytimg.com/yts/cssbin/www-core-webp-vflCayM79.css" name="www-core" class="css-httpssytimgcomytscssbinwwwcorewebpvflCayM79css">
    ```

From lesson 15 positioning: You already have the developer tools skills you need to find the .relative element and move it. However, before you start, let me show you a quick trick for finding any element by its selector with Chrome developer tools.

* [Open the DevTools console panel](https://developers.google.com/web/tools/chrome-devtools/debug/console/console-ui?hl=en#opening-the-console).
* Type $('[selector]') and press enter. [selector] can be any CSS selector, so you could have $('.className') or $('#idName'). Notice that you need ' around the selector.
* An HTML element should appear in the console (something like <div class="relative">text</div>). Right-click (or control-click on a Mac) on the element and select Reveal in Elements Panel.
* *I find this to be far more cumbersome than just clicking on the element and selecting inspect.*
