Lesson 16: Floats
=================

**Udacity Full Stack Web Developer Nanodegree program**

Part 01. Programming fundamentals and the web

Project 02. Build a portfolio site

Brendon Smith | br3ndonland

---

## Lesson

1. Intro

    Floats originally came on the scene to help web developers mimic print layouts. 

2. Floats

    **Floats allow you to embed images within blocks of text, while not disturbing the overall layout of the page. They are outside the normal flow.**


    <html>
    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>First off, floats are not a positioning value. They are a wholly different flow on the page created by a new property, <code>float</code>.</p>
    <p>Nowadays, floats are commonly used to create grid-based layouts, like Udacity's catalog, but they originally came on the scene to solve a very different class of problems. Let's take a quick history lesson so that the quirks of <code>float</code> seem less quirky :)</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57bc9609_screen-shot-2016-08-23-at-13.25.12/screen-shot-2016-08-23-at-13.25.12.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Get used to spotting grids! They're all over the web. Here are some of the grids on our catalog page (as of 23 August 2016). You can easily break down these grids further.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><h3 id="why-do-floats-exist-">Why Do Floats Exist?</h3>
    <p>Remember that the web began as a way to display, share and find text documents. Early websites mimicked printed text. The <code>float</code> property gave developers the ability to add images that sit within text, much like inset images in newspaper articles.</p>
    <p><code>float</code> creates a new flow on the page with a unique behavior:</p>
    <blockquote>
    <h3 id="normal-flow-line-boxes-respect-the-boundaries-of-floated-elements-but-normal-flow-block-elements-ignore-floats-">Normal flow line boxes respect the boundaries of floated elements, but normal flow block elements ignore floats.</h3>
    </blockquote>
    <p>This lets you embed images within a block of text without affecting the overall layout of the page. Let me show you an example.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57bc96a7_screen-shot-2016-08-23-at-11.45.28/screen-shot-2016-08-23-at-11.45.28.png" class="index--image--1wh9w" style="width: 526.337px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The two images appear to be floating inside the text.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>You’ve probably seen something like this before. <a target="_blank" href="http://udacity.github.io/fend/fend-refresh/lesson6-part2/float-left-example.html">This site</a> demonstrates the original purpose of floats.</p>
    <p>The Carl Sagan image is styled as <code>float: left</code> and the Pale Blue Dot image is <code>float: right</code>.</p>
    <p>The inline text wraps around the images, which seem to be floating in the page's text. The block paragraph elements, on the other hand, ignore the floats and take up as much space as they normally would. If you open developer tools, you'll see that the paragraphs extend behind the images.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57bc9719_screen-shot-2016-08-23-at-13.33.12/screen-shot-2016-08-23-at-13.33.12.png" class="index--image--1wh9w" style="width: 526.337px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Paragraphs ignore the floats.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Here's the HTML behind this example. Nothing fancy here except the two <code>float</code> properties.</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Float Example<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        <span class="hljs-tag">body</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> <span class="hljs-number">640px</span></span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">margin</span>:<span class="hljs-value"> <span class="hljs-number">0</span> auto</span></span>;
        }</span>
        <span class="hljs-tag">img</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">height</span>:<span class="hljs-value"> <span class="hljs-number">200px</span></span></span>;
        }</span>
        <span class="hljs-class">.left</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">margin-right</span>:<span class="hljs-value"> <span class="hljs-number">8px</span></span></span>;
        }</span>
        <span class="hljs-class">.right</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> right</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">margin-left</span>:<span class="hljs-value"> <span class="hljs-number">8px</span></span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">h1</span>&gt;</span>Carl Sagan<span class="hljs-tag">&lt;/<span class="hljs-title">h1</span>&gt;</span>

      <span class="hljs-tag">&lt;<span class="hljs-title">p</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-title">p</span>&gt;</span>

      <span class="hljs-tag">&lt;<span class="hljs-title">img</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"left"</span> <span class="hljs-attribute">src</span>=<span class="hljs-value">"images/Carl_Sagan_Planetary_Society.jpg"</span> <span class="hljs-attribute">alt</span>=<span class="hljs-value">"Carl Sagan by NASA/JPL [Public domain], via Wikimedia Commons"</span>&gt;</span>

      <span class="hljs-tag">&lt;<span class="hljs-title">p</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-title">p</span>&gt;</span>

      <span class="hljs-tag">&lt;<span class="hljs-title">img</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"right"</span> <span class="hljs-attribute">src</span>=<span class="hljs-value">"images/256px-PaleBlueDot.jpg"</span> <span class="hljs-attribute">alt</span>=<span class="hljs-value">"Pale Blue Dot - Earth as seen through one of Saturn's rings"</span>&gt;</span>

      <span class="hljs-tag">&lt;<span class="hljs-title">p</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-title">p</span>&gt;</span>

      <span class="hljs-tag">&lt;<span class="hljs-title">p</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-title">p</span>&gt;</span>

      <span class="hljs-tag">&lt;<span class="hljs-title">p</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-title">p</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre><p>Developers eventually realized the float flow has some unique properties that make it perfect for creating responsive, grid-based layouts. Keep going to see how.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>
    </html>


3. Many Floats

    Floats stack together in order. `float:right` will align rightmost first, `float:left` will align left first.

4. Floats in Parents Quiz

    Floated elements stay within their containers' width, but not necessarily the height.

5. Clearing
    
    **We went through two strategies for avoiding conflicts between floats and other normal flow elements. Block formatting with `overflow: auto`, or any value other than `visible`, forces the elements to respect the boundaries of the float. Clearing takes it further, and basically inserts a line break after the float with `clear: left, right, or both`.**

    <html>
    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Remember, floats are outside the normal flow. In the previous quiz, you saw that despite the fact that the child float had a height, the parent <em>did not have a height</em>!</p>
    <blockquote>
    <h3 id="float-children-are-not-involved-in-the-box-size-calculation-of-normal-flow-parents-">Float children are <em>not</em> involved in the box-size calculation of normal flow parents.</h3>
    </blockquote>
    <p>If a container only contains a float child, the container will <em>not</em> have a height by default - the height has to be set some other way, such as with normal flow content or the <code>height</code> property.</p>
    <p>This makes sense in some ways, but it's surprising in others. Given what you know about interactions between the normal flow and the float flow, you shouldn't be surprised that normal flow block elements ignore the size of child float elements when calculating box size. However, if you were, say, creating a page layout using floats, it would be reasonable to assume that a sibling to a parent element with float children would respect the boundaries of the children.</p>
    <p>Let me show you.</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Parent with Siblings and Float Children<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">link</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">'https://fonts.googleapis.com/css?family=Source+Sans+Pro'</span> <span class="hljs-attribute">rel</span>=<span class="hljs-value">'stylesheet'</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">'text/css'</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        - <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">box-sizing</span>:<span class="hljs-value"> border-box</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-family</span>:<span class="hljs-value"> <span class="hljs-string">'Source Sans Pro'</span>, sans-serif</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-weight</span>:<span class="hljs-value"> bold</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-size</span>:<span class="hljs-value"> <span class="hljs-number">14pt</span></span></span>;
        }</span>
        <span class="hljs-class">.bordered</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2px</span> solid <span class="hljs-hexcolor">#2e3d49</span></span></span>;
        }</span>
        <span class="hljs-class">.child</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#15A222</span></span></span>;
        }</span>
        <span class="hljs-class">.sibling</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#D16906</span></span></span>;
        }</span>
        <span class="hljs-class">.left</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered parent"</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered child left"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered child left"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered sibling"</span>&gt;</span>Sibling to the parent<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre><p>At a glance, the HTML seems to say that the sibling, <code>.sibling</code>, will be displayed below the parent and its children. Of course, that's not true. Here's how it looks.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57bf1886_screen-shot-2016-08-25-at-11.06.44/screen-shot-2016-08-25-at-11.06.44.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>While the sibling is below the parent, it isn't below the parent's child float elements.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>If you're using floats to create a layout (as you will be soon), this is undesired behavior. There are a few ways to work around it and force elements in the normal flow to respect the boundaries of floats.</p>
    <h3 id="strategy-1-block-formatting-contexts">Strategy 1: Block Formatting Contexts</h3>
    <p>This strategy forces normal flow <strong>siblings</strong> to respect the boundaries of floats. Elements with a block formatting context (remember those from last lesson!) may not overlap floats.</p>
    <p>This rule originally protected elements like <code>&lt;table&gt;</code>, which create their own block formatting context, from being invaded by floats. The reasoning behind this is that you wouldn't want a random image to push aside all the text inside a carefully built table.</p>
    <p>You can take advantage of this rule - if you force elements to establish a block formatting context, they'll respect the boundaries of the float.</p>
    <p>In <a target="_blank" href="http://udacity.github.io/fend/fend-refresh/lesson6-part2/float-block-formatting.html">this example</a>, I'm using the <code>overflow</code> property to set a block formatting context (any value other than <code>visible</code>, including <code>auto</code>, forces an element to take on a block formatting context).</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Block Formatting Context<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        - <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">box-sizing</span>:<span class="hljs-value"> border-box</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-family</span>:<span class="hljs-value"> <span class="hljs-string">'Source Sans Pro'</span>, sans-serif</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-weight</span>:<span class="hljs-value"> bold</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-size</span>:<span class="hljs-value"> <span class="hljs-number">14pt</span></span></span>;
        }</span>
        <span class="hljs-class">.child</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#15A222</span></span></span>;
        }</span>
        <span class="hljs-class">.bordered</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2px</span> solid <span class="hljs-hexcolor">#2e3d49</span></span></span>;
        }</span>
        <span class="hljs-class">.block-context</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">overflow</span>:<span class="hljs-value"> auto</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#D16906</span></span></span>;
        }</span>
        <span class="hljs-class">.left</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"parent"</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"child left"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"child left"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered block-context"</span>&gt;</span>New context<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57bf3e2e_screen-shot-2016-08-25-at-13.51.08/screen-shot-2016-08-25-at-13.51.08.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>There's no overlap between the new context and the two float children.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>With <code>overflow: auto</code>, the "new context" element respects the boundaries of the two children. No overlap! Try toggling <code>overlap: auto</code> to see what happens if it isn't applied.</p>
    <p>You can take this a step further with a property called <code>clear</code>.</p>
    <h3 id="strategy-2-clearing">Strategy 2: Clearing</h3>
    <p>By default, line boxes clear out space for float elements. "Clear," in this case, means that they move out of the way for floats. You can control how siblings interact with floats with <code>clear</code>.</p>
    <p><code>clear: left</code> indicates that the top of the element must be below any left floated elements that appear before this one in the document. <code>clear: right</code> acts the same, but with right floated elements. <code>clear: none</code> means that there are no restrictions; this is the default value.</p>
    <p><code>clear: both</code> is interesting - it indicates that the element must be below <em>any</em> floated elements that appear earlier in the document.</p>
    <p>Let me demonstrate. There are four examples in this HTML.</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Block Formatting Context<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        - <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">box-sizing</span>:<span class="hljs-value"> border-box</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-family</span>:<span class="hljs-value"> <span class="hljs-string">'Source Sans Pro'</span>, sans-serif</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-weight</span>:<span class="hljs-value"> bold</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-size</span>:<span class="hljs-value"> <span class="hljs-number">14pt</span></span></span>;
        }</span>
        <span class="hljs-comment">/*
           `:nth-child` and `:not` (below) are pseudo-classes:
            https://developer.mozilla.org/en-US/docs/Web/CSS/pseudo-classes
        */</span>
        <span class="hljs-tag">div</span><span class="hljs-pseudo">:nth-child(even)</span><span class="hljs-pseudo">:not(</span><span class="hljs-class">.left</span>)<span class="hljs-pseudo">:not(</span><span class="hljs-class">.right</span>) <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#128FC2</span></span></span>;
        }</span>
        <span class="hljs-tag">div</span><span class="hljs-pseudo">:nth-child(odd)</span><span class="hljs-pseudo">:not(</span><span class="hljs-class">.left</span>)<span class="hljs-pseudo">:not(</span><span class="hljs-class">.right</span>) <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#15A222</span></span></span>;
        }</span>
        <span class="hljs-class">.bordered</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2px</span> solid <span class="hljs-hexcolor">#2e3d49</span></span></span>;
        }</span>
        <span class="hljs-class">.left</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#FD9F0E</span></span></span>;
        }</span>
        <span class="hljs-class">.right</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> right</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#FD9F0E</span></span></span>;
        }</span>
        <span class="hljs-class">.clear-left</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">clear</span>:<span class="hljs-value"> left</span></span>;
        }</span>
        <span class="hljs-class">.clear-right</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">clear</span>:<span class="hljs-value"> right</span></span>;
        }</span>
        <span class="hljs-class">.clear-both</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">clear</span>:<span class="hljs-value"> both</span></span>;
        }</span>
        <span class="hljs-class">.wide</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> <span class="hljs-number">40%</span></span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-comment">&lt;!-- example 1 --&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered left"</span>&gt;</span>Left ← Left ← Left<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered clear-left"</span>&gt;</span>This element has been clear left'ed.<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>

      <span class="hljs-comment">&lt;!-- example 2 --&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered right"</span>&gt;</span>Right → Right → Right<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered clear-right"</span>&gt;</span>This element has been clear right'ed.<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>

      <span class="hljs-comment">&lt;!-- example 3 --&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"left bordered"</span>&gt;</span>Left ← Left ← Left<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered"</span>&gt;</span>Not cleared at all!<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>

      <span class="hljs-comment">&lt;!-- example 4 --&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered left wide"</span>&gt;</span>Left ← Left ← Left ← Really wide.<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered right wide"</span>&gt;</span>Right → Right → Right. Really wide.<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered clear-both"</span>&gt;</span>This element has been clear both'ed.<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57bf3e61_screen-shot-2016-08-25-at-13.52.06/screen-shot-2016-08-25-at-13.52.06.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>There is clearly a difference to the behaviors of different clears. (Sorry for the bad pun :P)</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>There's one more technique: the clearfix. But before we get to it, I want you to practice clearing floats.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>
    </html>


6. Clear Quiz

    Just had to add `clear: left;`.

7. Pseudo-elements

    **Pseudo-elements are created with CSS and rendered like HTML.**

    <html>
    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Before we get into the third technique for clearing, you need a quick primer on something called a <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements">pseudo-element</a>.</p>
    <h3 id="pseudo-elements">Pseudo-elements</h3>
    <p>The DOM is mutable (changeable). The magic of JavaScript (which you'll probably be learning about soon) is that it allows you to modify the DOM on the fly, effectively changing the way a live site renders.</p>
    <p>CSS can also mutate the DOM using something called a <strong>pseudo-element</strong>. A pseudo-element is an element that is actually <em>created with CSS</em> and then rendered like a normal element. Let me show you <a target="_blank" href="http://udacity.github.io/fend/fend-refresh/lesson6-part2/pseudoelements.html">an example</a>.</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Pseudo-elements Example<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">link</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">'https://fonts.googleapis.com/css?family=Source+Sans+Pro'</span> <span class="hljs-attribute">rel</span>=<span class="hljs-value">'stylesheet'</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">'text/css'</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        - <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">box-sizing</span>:<span class="hljs-value"> border-box</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-family</span>:<span class="hljs-value"> <span class="hljs-string">'Source Sans Pro'</span>, sans-serif</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-weight</span>:<span class="hljs-value"> bold</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-size</span>:<span class="hljs-value"> <span class="hljs-number">14pt</span></span></span>;
        }</span>
        <span class="hljs-class">.bordered</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2px</span> solid <span class="hljs-hexcolor">#2e3d49</span></span></span>;
        }</span>
        <span class="hljs-class">.child</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#15A222</span></span></span>;
        }</span>
        <span class="hljs-class">.child</span><span class="hljs-pseudo">:after</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">content</span>:<span class="hljs-value"> <span class="hljs-string">'Pseudo-element!'</span></span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">display</span>:<span class="hljs-value"> block</span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"parent"</span>&gt;</span>Parent
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"child bordered"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre><p>Here's how it looks.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57c0b060_screen-shot-2016-08-26-at-16.10.32/screen-shot-2016-08-26-at-16.10.32.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Notice that the pseudo-element is inside the child.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The pseudo-element is created with <code>:after</code> inside the CSS on the element that I want to mutate. Another option would be <code>:before</code>. You can see that <code>:after</code> is rendered as a child of <code>.child</code> because it shares the background color of <code>.child</code> and is rendered inside the child's border. If you open developer tools, you'll also see that it's inside the child.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57c0b1cb_screen-shot-2016-08-26-at-16.16.37/screen-shot-2016-08-26-at-16.16.37.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>More evidence that the pseudo-element is rendered as a child.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>In effect, the pseudo-element is extra content that is added to the element. Without the <code>content</code> property, the pseudo-element <em>disappears</em>! Watch.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><div class="video-atom--video--1rflY" style="width: 100%;"><div><div><div class="youtube-player--youtube-player--1kyG7"><div class="youtube-player--embed-responsive-16x9--x203G youtube-player--_embed-responsive--wS2qC"><span><iframe class="embed-responsive-item" frameborder="0" allowfullscreen="1" title="YouTube video player" width="640" height="360" src="https://www.youtube.com/embed/he7CrLqZPf4?showinfo=0&amp;rel=0&amp;autohide=1&amp;vq=hd720&amp;hl=en-us&amp;cc_load_policy=0&amp;enablejsapi=1&amp;origin=https%3A%2F%2Fclassroom.udacity.com&amp;widgetid=21" id="undefined"></iframe></span></div></div></div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><div style="text-align: center; color: #afafaf; font-size: 14px; margin-top: 15px;">One click and it's gone!</div></div></div></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>You can, of course, style pseudo-elements with whatever CSS properties you'd like. In this case, I added <code>display: block</code> so that the pseudo-element would take its own line. If you remove it, you'll see that it behaves like an inline element instead.</p>
    <p>Pseudo-elements are useful in a many situations. I find myself using them most off as accents. For instance, the green ✓ and red ✗ that appear in the Udacity Feedback widget are <code>:before</code> pseudo-elements! [<em>Accurate with the current build of the widget as of August 2016.</em>]</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57c0b826_screen-shot-2016-08-26-at-16.14.53/screen-shot-2016-08-26-at-16.14.53.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>A pseudo-element in the wild!</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Keep going to see how a pseudo-element can be used to clear floats.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>
    </html>

8. Clearfix

    **Clearfix resizes a normal flow parent element to fit the floats inside it.**

    <html>
    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Back to technqiues for clearing, here's the third.</p>
    <h3 id="strategy-3-clearfix">Strategy 3: Clearfix</h3>
    <p>Once more, let's look at the HTML of the normal flow parent with a float child and a normal flow sibling.</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Parent with Siblings and Float Children<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">link</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">'https://fonts.googleapis.com/css?family=Source+Sans+Pro'</span> <span class="hljs-attribute">rel</span>=<span class="hljs-value">'stylesheet'</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">'text/css'</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        - <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">box-sizing</span>:<span class="hljs-value"> border-box</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-family</span>:<span class="hljs-value"> <span class="hljs-string">'Source Sans Pro'</span>, sans-serif</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-weight</span>:<span class="hljs-value"> bold</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-size</span>:<span class="hljs-value"> <span class="hljs-number">14pt</span></span></span>;
        }</span>
        <span class="hljs-class">.bordered</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2px</span> solid <span class="hljs-hexcolor">#2e3d49</span></span></span>;
        }</span>
        <span class="hljs-class">.left</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
        }</span>
        <span class="hljs-class">.child</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#15A222</span></span></span>;
        }</span>
        <span class="hljs-class">.sibling</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#D16906</span></span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered parent"</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered child left"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered child left"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered sibling"</span>&gt;</span>Sibling to the parent<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57c1c4a4_screen-shot-2016-08-25-at-11.06.44/screen-shot-2016-08-25-at-11.06.44.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>I'm sure you remember this.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>There is a commandment for software developers:</p>
    <blockquote>
    <h3 id="thou-shalt-always-write-code-that-runs-the-way-it-reads-">Thou shalt always write code that runs the way it reads.</h3>
    </blockquote>
    <p>I've also seen this <a target="_blank" href="http://stackoverflow.com/questions/876089/who-wrote-this-programing-saying-always-code-as-if-the-guy-who-ends-up-maintai">written as</a>:</p>
    <blockquote>
    <h3 id="always-code-as-if-the-guy-who-ends-up-maintaining-your-code-will-be-a-violent-psychopath-who-knows-where-you-live-">Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.</h3>
    </blockquote>
    <p>As a developer, you should always strive to write your code as clearly as possible. Keep surprises to a minimum. The example above breaks the commandment because the HTML seems to indicate that <code>.sibling</code> will be rendered underneath <code>.parent</code> and all of its children, but that's not what happens.</p>
    <p>The third technique to clear floats, clearfix, combines aspects of the first two. The goal of the clearfix is to make a normal flow parent resize its box model to fit all of the floats inside it. There are two general techniques to do so.</p>
    <ol>
    <li>Add an element with <code>clear: both</code> to the end of a parent. This ensures that the last element is a normal flow element that has been pushed below all the floats.</li>
    <li>Turn the parent into a block formatting context with an <code>overflow</code> property other than <code>visible</code>. The block formatting context respects the boundaries of floats and ensures the parent's box model encompasses float children.</li>
    </ol>
    <p>The first technqiue by itself, adding an HTML element with <code>clear: both</code>, violates the commandment of code clarity; HTML should be restricted to rendered content. However, applying the same technique with a pseudo-element works nicely. Here's how it looks.</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Clearfix Example<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">link</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">'https://fonts.googleapis.com/css?family=Source+Sans+Pro'</span> <span class="hljs-attribute">rel</span>=<span class="hljs-value">'stylesheet'</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">'text/css'</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        - <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">box-sizing</span>:<span class="hljs-value"> border-box</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-family</span>:<span class="hljs-value"> <span class="hljs-string">'Source Sans Pro'</span>, sans-serif</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-weight</span>:<span class="hljs-value"> bold</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-size</span>:<span class="hljs-value"> <span class="hljs-number">14pt</span></span></span>;
        }</span>
        <span class="hljs-class">.bordered</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2px</span> solid <span class="hljs-hexcolor">#2e3d49</span></span></span>;
        }</span>
        <span class="hljs-class">.clearfix</span><span class="hljs-pseudo">:after</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">content</span>:<span class="hljs-value"> <span class="hljs-string">''</span></span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">clear</span>:<span class="hljs-value"> both</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">display</span>:<span class="hljs-value"> table</span></span>;
        }</span>
        <span class="hljs-class">.left</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
        }</span>
        <span class="hljs-class">.parent</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#89D0E5</span></span></span>;
        }</span>
        <span class="hljs-class">.child</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#15A222</span></span></span>;
        }</span>
        <span class="hljs-class">.sibling</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#D16906</span></span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered parent clearfix"</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered child left"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered child left"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered sibling"</span>&gt;</span>Sibling to the parent<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre><p>(I added a background color to <code>.parent</code> to make it stand out more.)</p>
    <p>Here's how it looks!</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57c1c5ea_screen-shot-2016-08-27-at-11.54.55/screen-shot-2016-08-27-at-11.54.55.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>No surprises! Now the site reflects the structure of the HTML.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>This clearfix actually uses both technqiues - the pseudo-element has a block formatting context, forcing it to stay outside the bounds of the floats, and it clears both left and right floats.</p>
    <p>Here's how the second technique, giving the parent a block formatting context, looks.</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Clearfix Example<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">link</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">'https://fonts.googleapis.com/css?family=Source+Sans+Pro'</span> <span class="hljs-attribute">rel</span>=<span class="hljs-value">'stylesheet'</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">'text/css'</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        - <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">box-sizing</span>:<span class="hljs-value"> border-box</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-family</span>:<span class="hljs-value"> <span class="hljs-string">'Source Sans Pro'</span>, sans-serif</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-weight</span>:<span class="hljs-value"> bold</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-size</span>:<span class="hljs-value"> <span class="hljs-number">14pt</span></span></span>;
        }</span>
        <span class="hljs-class">.bordered</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2px</span> solid <span class="hljs-hexcolor">#2e3d49</span></span></span>;
        }</span>
        <span class="hljs-class">.clearfix</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">overflow</span>:<span class="hljs-value"> auto</span></span>;
        }</span>
        <span class="hljs-class">.left</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
        }</span>
        <span class="hljs-class">.parent</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#89D0E5</span></span></span>;
        }</span>
        <span class="hljs-class">.child</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#15A222</span></span></span>;
        }</span>
        <span class="hljs-class">.sibling</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#D16906</span></span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered parent clearfix"</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered child left"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered child left"</span>&gt;</span>Child<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"bordered sibling"</span>&gt;</span>Sibling to the parent<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57c1c66d_screen-shot-2016-08-27-at-11.56.59/screen-shot-2016-08-27-at-11.56.59.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>This works too!</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The result is the same! That's good news.</p>
    <p>You just saw that there are two techniques to accomplish the same task. At this point, you should be asking yourself if one technique is better than the other. Great question. Keep going to the next quiz to investigate the side effects of clearfixes.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>
    </html>

9. Clearfix Quiz

    **When using `overflow: auto;`, you lose some control over what content is scrollable.**

    <html>
    <div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The two techniques for clearfix are:</p>
    <pre><code><span class="hljs-class">.clearfix</span><span class="hljs-pseudo">:after</span> <span class="hljs-rules">{
      <span class="hljs-rule"><span class="hljs-attribute">content</span>:<span class="hljs-value"> <span class="hljs-string">''</span></span></span>;
      <span class="hljs-rule"><span class="hljs-attribute">clear</span>:<span class="hljs-value"> both</span></span>;
      <span class="hljs-rule"><span class="hljs-attribute">display</span>:<span class="hljs-value"> table</span></span>;
    }</span>
    </code></pre><p>and</p>
    <pre><code><span class="hljs-class">.clearfix</span> <span class="hljs-rules">{
      <span class="hljs-rule"><span class="hljs-attribute">overflow</span>:<span class="hljs-value"> auto</span></span>;
    }</span>
    </code></pre><p>If you were to decide which technique is better just based on the complexity of the two CSS classes, <code>overflow: auto</code> would win. It's much simpler. However, <code>overflow: auto</code> has a side effect. I'm not going to tell you what it is because I want you to figure that out for yourself in this quiz! But first, a little bit of background about <code>overflow</code>.</p>
    <h3 id="overflow">Overflow</h3>
    <p>There are technically three different <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow">overflow properties</a>: <code>overflow</code>, <code>overflow-x</code> and <code>overflow-y</code>. These three properties determine what happens to content if its box model is larger than its parent's box model.</p>
    <p>The default option is <code>visible</code>, which means that the content is always rendered and may extend <em>outside</em> of its parent. Other options include <code>hidden</code>, <code>scroll</code> and <code>auto</code>. <code>hidden</code> does exactly what you think - it clips off any content that extends outside the parent's box model. <code>scroll</code> adds scroll bars to the parent, allowing the user to scroll around the parent element to access all the content. The behavior of <code>auto</code> depends on the browser.</p>
    <p>Keep this in mind as you go through the quiz.</p>
    <h3 id="instructions">Instructions</h3>
    <ol>
    <li>Head to <a target="_blank" href="http://udacity.github.io/fend/fend-refresh/lesson6-part2/clearfix-overflow-quiz.html">this site</a>, which is using the <code>overflow: auto</code> clearfix.</li>
    <li>Open developer tools to determine which of the options below describes what could go wrong with <code>overflow: auto</code>. (Hint, <code>.row</code> has some commented out properties that you should try manipulating.)</li>
    <li>Answer the question below!</li>
    </ol>
    </div>  
    </html>

10. Outro