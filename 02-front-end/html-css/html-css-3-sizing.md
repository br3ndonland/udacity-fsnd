# Sizing

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Lesson](#lesson)
  - [01. Guess the Render Game](#01-guess-the-render-game)
  - [02. James' Solution](#02-james-solution)
  - [03. Cameron's Solution](#03-camerons-solution)
  - [04. Who's the Winner](#04-whos-the-winner)
  - [05. Boxes, Boxes Everywhere](#05-boxes-boxes-everywhere)
  - [06. Boxes on the Web](#06-boxes-on-the-web)
  - [07. The Box Model](#07-the-box-model)
  - [08. Quiz: Border-Box](#08-quiz-border-box)
  - [09. Changing Boxes](#09-changing-boxes)
  - [10. Quiz: Box Model Sizing](#10-quiz-box-model-sizing)
  - [11. Containers](#11-containers)
  - [12. Quiz: Relative Widths](#12-quiz-relative-widths)
  - [13. Inline Boxes](#13-inline-boxes)
  - [14. Semantic Elements](#14-semantic-elements)
  - [15. Types of Elements](#15-types-of-elements)
  - [16. Quiz: Element Research](#16-quiz-element-research)
  - [17. Outro](#17-outro)

## Lesson

### 01. Guess the Render Game

> Welcome, this lesson is all about elements and how to size them.

James and Cameron play the "render game." They create a bunch of HTML files, exchange them, and challenge each other to render (sketch) the sites based on the HTML.

### 02. James' Solution

### 03. Cameron's Solution

Different HTML elements have different default sizes. For example, the footer takes the entire width of the page, and usually contains info about who made the page.

### 04. Who's the Winner

Cameron wins.

> Semantic elements are just much, much easier to read.

### 05. Boxes, Boxes Everywhere

**Visual design, print or digital, is based on a series of boxes.**

Key points:

- **You can take any design and turn it into a box.**
- **There are many kinds of boxes with many different purposes.**

### 06. Boxes on the Web

- The two key options for display properties are `display: block`, which takes up as much width as possible, and `display: inline`, which only takes up as much width as needed. Height is content-based.
- a `<div></div>` is the most generic display property.
- `d3.js` is a library for creating web graphics. They show an example of a Circos plot (chord diagram).
  - [d3.js Gallery](https://github.com/d3/d3/wiki/Gallery)
  - [d3.js Chord Diagram](http://bl.ocks.org/mbostock/4062006)

### 07. The Box Model

- **Content**
- **Padding**
- **Border**
- **Margin**

James also pointed out the `box-sizing: content-box` code. Normally, the `width` doesn't include padding and border, so if you set width to 800px, then add 50px each for padding and border, you're now at 1000px wide. To get around this, you can use `box-sizing: border-box;` which will include both padding and border in the width and height of the element. `box-sizing: border-box;` does not include margin.

### 08. Quiz: Border-Box

`box-sizing: border-box;` does not include margin.

### 09. Changing Boxes

- Boxes have default properties, called user-agent styles.
- Height is content-based.

### 10. Quiz: Box Model Sizing

Instructions:

> Finish the CSS to create this block element's box model.

<details>
  <summary>Solution</summary>

```css
.box-model {
  width: 175px;
  height: 175px;
  padding: 50px;
  margin: 20px;
}
```

</details>

### 11. Containers

The sizes of child elements will be influenced by the parent elements. The parent elements are also called **containers**.

### 12. Quiz: Relative Widths

### 13. Inline Boxes

Inline elements will wrap when they exceed the container width.

### 14. Semantic Elements

Excessive use of `<div></div>` can lead to "div soup." This technically works, but is not semantically ideal. HTML is intended to be a markup language, so it describes a document. Use semantic elements instead. Semantic elements have the additional benefit of enhancing Search Engine Optimization (SEO). The Googlebot can more easily extract information.

Instructor notes

> Semantic elements can really help improve your website's search engine optimization. If you want to learn more about SEO, I recommend checking out [Moz's Beginners Guide to SEO](https://moz.com/beginners-guide-to-seo).
>
> Want to learn more about surfing the web with a screen reader? Here's a [quick video](https://classroom.udacity.com/courses/ud882/lessons/3574748851/concepts/37757186550923) from our [course on Responsive Images](https://udacity.com/courses/ud882). The video focuses on images but there are some great links if you've never tried a screen reader before.

### 15. Types of Elements

> You have many different kinds of elements at your disposal. Almost all of them are either block or inline with the major differences being their default CSS styles. Check it out, [here’s a list](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).
>
> The elements for [content sectioning](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Content_sectioning) are good for laying out things on the page. Notice that a lot of these have requirements for what should be inside the element, for example, an `<article>` typically includes a heading as a child element.
>
> [Text content](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Text_content) is good for text. There are a few from here that you’ve seen before, but there are some new ones as well.
>
> There are also [inline text semantics](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Inline_text_semantics). You’ll see familiar elements like `<em>` and `<span>`, but you’ve got others like `<code>`, which displays code in a monospace font. Also `<data>`, `<progress>`, `<time>`, and others.
>
> There are other categories, but take a look at the last category, a [graveyard of old elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Obsolete_and_deprecated_elements). This is evidence of the way the web used to be. Don’t use these. They might work, but they aren’t guaranteed to continue working because they are no longer supported. Stick with the other elements and you’ll be fine.
>
> For the next quiz, you'll be asked to research these elements in order to select which ones should be used on an example website. Press "Next" to continue to the quiz.

### 16. Quiz: Element Research

The quiz took me a few tries. They were looking for `<nav></nav>` for the links at the top, and `<article></article>` for the sections. The sidebar was `<aside></aside>`.

### 17. Outro

[(Back to TOC)](#table-of-contents)