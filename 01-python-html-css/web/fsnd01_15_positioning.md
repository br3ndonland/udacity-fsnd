Lesson 15: Positioning
======================

**Udacity Full Stack Web Developer Nanodegree program**

Part 01. Programming fundamentals and the web

Project 02. Build a portfolio site

Brendon Smith | br3ndonland

---

# Lesson

1. Intro

    Positioning elements is a lot like Tetris. It's easy to learn the basics, but mastery requires practice.

    Web developers don't spend time memorizing positioning syntax.

    Strategies:

    - **Make good guesses**
    - **Read documentation**
    - **test, fix, iterate** to get it right. 

    I appreciate that they are teaching us how to think like programmers, rather than simply showing us.

2. Normal Flow


    Instructor notes:
    <html>
    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The Game of Positions starts with this CSS property: <code>position</code>.</p>
    <blockquote>
    <h3 id="-position-static-"><code>position: static;</code></h3>
    </blockquote>
    <p>Let's start with an analogy. Take a look at the image below. The arrows show how currents <strong>flow</strong> around the Australian continent.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://lh3.googleusercontent.com/3D_WvaIJ1mBEISeNuSxiNYn6ixEYmrZv6mZBTOSbWqPZogUt8DcJdp_KSl0pMMETNBhWL6JrFJBYrWmtkDE=s0#w=550&amp;h=358" class="index--image--1wh9w" style="width: 550px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>© Commonwealth of Australia 2013 [CC BY 3.0 au (<a target="_blank" href="http://creativecommons.org/licenses/by/3.0/au/deed.en">http://creativecommons.org/licenses/by/3.0/au/deed.en</a>)], via Wikimedia Commons</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>An object floating in the oceans around Australia (<a target="_blank" href="https://en.wikipedia.org/wiki/Friendly_Floatees">like a rubber ducky</a>) would follow the path of the <a target="_blank" href="https://en.wikipedia.org/wiki/Ocean_current">currents</a>.</p>
    <p>The Game of Positions actually can be played with a few different sets of rules, which we sometimes call <strong>flows</strong> because of the way most developers think of elements flowing into place as if they were being pushed by a force, much like the currents flowing around Australia (and every other landmass, for that matter).</p>
    <p>So, how does this look with CSS?</p>
    <pre><code><span class="hljs-class">.default</span> <span class="hljs-rules">{
        <span class="hljs-rule"><span class="hljs-attribute">position</span>:<span class="hljs-value"> static</span></span>;
    }</span>
    </code></pre><p>The default position is <code>static</code>, which gets called the <strong>normal flow</strong>. This is what you’ve been using in all of your sites so far. The <code>relative</code>, <code>absolute</code> and <code>fixed</code> flows are variations of the normal flow.</p>
    <h3 id="how-the-normal-flow-works">How the Normal Flow Works</h3>
    <p>The way elements will move in the normal flow depends on their display state as <code>block</code> elements or <code>inline</code> elements.</p>
    <ol>
    <li>Block elements are aligned <strong>vertically</strong>.</li>
    <li>Inline elements are aligned <strong>horizontally</strong>.</li>
    </ol>
    <video width="100%" autoplay="" loop="">
      <source src="https://s3.amazonaws.com/content.udacity-data.com/courses/fend/normal-flow3.mp4" type="video/mp4">
      Your browser does not support the video tag. <a href="https://s3.amazonaws.com/content.udacity-data.com/courses/fend/normal-flow3.mp4" target="_blank">Click here to see the animation.</a>
    </video>

    <p><em>(Elements don’t actually have a starting point on the screen. I picked the bottom middle arbitrarily.  Depending on the flow that you’re using, you might do better thinking that your elements are coming in from the bottom left, or bottom right, or appearing randomly!)</em></p>
    <p>Notice how the <code>&lt;div&gt;</code>s (block elements) stack vertically while the <code>&lt;span&gt;</code>s (inline elements) stack horizontally.</p>
    <hr>
    <p>Let's look at another example. Here is some HTML:</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Sample Normal Flow<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css"> <span class="hljs-comment">/* nothing but colors, widths and margins */</span> </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span>&gt;</span>block<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span>&gt;</span>block<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span>&gt;</span>block<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">span</span>&gt;</span>span <span class="hljs-tag">&lt;/<span class="hljs-title">span</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">span</span>&gt;</span>span <span class="hljs-tag">&lt;/<span class="hljs-title">span</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">span</span>&gt;</span>span<span class="hljs-tag">&lt;/<span class="hljs-title">span</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span>&gt;</span>block<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre><p>And here is the <a target="_blank" href="http://udacity.github.io/fend/fend-refresh/lesson6/normal-flow/keynote-sample.html">resulting website</a>:</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/578533c5_screen-shot-2016-07-12-at-13.15.23/screen-shot-2016-07-12-at-13.15.23.png" class="index--image--1wh9w" style="width: 560px;"></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Take a look at the way the block elements line up.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><div class="video-atom--video--1rflY" style="width: 100%;"><div><div><div class="youtube-player--youtube-player--1_HuD"><div class="youtube-player--embed-responsive-16x9--3bmQJ youtube-player--_embed-responsive--VSOkY"><span><iframe class="embed-responsive-item" frameborder="0" allowfullscreen="1" title="YouTube video player" width="640" height="360" src="https://www.youtube.com/embed/r50ZR9DIe0I?showinfo=0&amp;rel=0&amp;autohide=1&amp;vq=hd720&amp;hl=en-us&amp;cc_load_policy=0&amp;enablejsapi=1&amp;origin=https%3A%2F%2Fclassroom.udacity.com&amp;widgetid=71" id="undefined"></iframe></span></div></div></div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><div style="text-align: center; color: #afafaf; font-size: 14px; margin-top: 15px;">The left edges of block elements line up.</div></div></div></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Block elements are laid out vertically. Their left outer edges will line up with their parent’s left outer edges. Even though these blocks do not take up the full width of the page, they still stack.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><div class="video-atom--video--1rflY" style="width: 100%;"><div><div><div class="youtube-player--youtube-player--1_HuD"><div class="youtube-player--embed-responsive-16x9--3bmQJ youtube-player--_embed-responsive--VSOkY"><span><iframe class="embed-responsive-item" frameborder="0" allowfullscreen="1" title="YouTube video player" width="640" height="360" src="https://www.youtube.com/embed/lk4ZyO5lqgA?showinfo=0&amp;rel=0&amp;autohide=1&amp;vq=hd720&amp;hl=en-us&amp;cc_load_policy=0&amp;enablejsapi=1&amp;origin=https%3A%2F%2Fclassroom.udacity.com&amp;widgetid=73" id="undefined"></iframe></span></div></div></div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><div style="text-align: center; color: #afafaf; font-size: 14px; margin-top: 15px;">Inline elements push together side by side.</div></div></div></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Inline elements are laid out horizontally inside their parents.  The left edge of an element’s line box will touch the right edge of the preceding element’s line box.</p>
    <p>If a line box is too big for a line, it wraps around to the next line.</p>
    <p>And that’s it! The rules of the positioning game are pretty simple by themselves, but they can get complicated when they start building on each other. For instance, take a look at how the spans end up on a line of their own. The block elements seem to treat the inline elements <em>as a whole</em> like a block. There's an interesting reason for this which you'll encounter later in this lesson.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>
    </html>


3. Normal Flow Quiz

    They gave us some CSS and HTML, and we had to predict how the website would look. I got it on my first try.


4. Inline-Block


    Instructor notes:
    <html>
    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>So far, there's been a distinction between inline and block elements. However, there’s a hybrid of the two!</p>
    <pre><code><span class="hljs-class">.example</span> <span class="hljs-rules">{
      <span class="hljs-rule"><span class="hljs-attribute">display</span>:<span class="hljs-value"> inline-block</span></span>;
    }</span>
    </code></pre><blockquote>
    <h3 id="-display-inline-block-elements-can-be-sized-like-block-elements-but-are-laid-out-like-inline-elements-"><code>display: inline-block</code> elements can be sized like block elements but are laid out like inline elements.</h3>
    </blockquote>
    <p>Take a look at this example. Notice that the <code>.random</code> span in the middle of the text has a width and height assigned to it but the span in the <a target="_blank" href="http://udacity.github.io/fend/fend-refresh/lesson6/inline-block/inline-block-example-start.html">resulting website</a> (shown below) acts like a regular inline element - it is rendered as a line-box and the <code>width</code> and <code>height</code> are ignored.</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Inline-Block Example<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        - <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">box-sizing</span>:<span class="hljs-value"> border-box</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-family</span>:<span class="hljs-value"> <span class="hljs-string">'Source Sans Pro'</span>, sans-serif</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-weight</span>:<span class="hljs-value"> bold</span></span>;
        }</span>
        <span class="hljs-class">.inline-block</span> <span class="hljs-rules">{ <span class="hljs-comment">/* hasn't been assigned! */</span>
          <span class="hljs-rule"><span class="hljs-attribute">display</span>:<span class="hljs-value"> inline-block</span></span>;
        }</span>
        <span class="hljs-class">.random</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2px</span> solid <span class="hljs-hexcolor">#2e3d49</span></span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#ecc81a</span></span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> <span class="hljs-number">20em</span></span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">height</span>:<span class="hljs-value"> <span class="hljs-number">40px</span></span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">link</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">'https://fonts.googleapis.com/css?family=Source+Sans+Pro'</span> <span class="hljs-attribute">rel</span>=<span class="hljs-value">'stylesheet'</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">'text/css'</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"container"</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">span</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-title">span</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">span</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"random"</span>&gt;</span>This is a random span.<span class="hljs-tag">&lt;/<span class="hljs-title">span</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">span</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-title">span</span>&gt;</span>
      <span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/578665a4_screen-shot-2016-07-13-at-11.00.13/screen-shot-2016-07-13-at-11.00.13.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Looks like the random span is acting like a normal inline element.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Now, I'll add <code>.inline-block</code> to the <code>.random</code> span. Take a look at <a target="_blank" href="http://udacity.github.io/fend/fend-refresh/lesson6/inline-block/inline-block-example-inline.html">the website now</a> to see how it looks!</p>
    <pre><code>&lt;span <span class="hljs-type">class</span>=<span class="hljs-string">"random inline-block"</span>&gt;This <span class="hljs-keyword">is</span> a random span.&lt;/span&gt;
    </code></pre></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/578666a3_screen-shot-2016-07-13-at-11.04.41/screen-shot-2016-07-13-at-11.04.41.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Now the random span has a defined width and height and still appears in the same line as the rest of the text!</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>You can see that the <code>.random</code> span is mixing the behavior of a block element and an inline element. But what if <code>display: inline-block</code> is applied to a block element, like a <code>&lt;div&gt;</code>?</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Inline-Block Example<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        - <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">box-sizing</span>:<span class="hljs-value"> border-box</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-family</span>:<span class="hljs-value"> <span class="hljs-string">'Source Sans Pro'</span>, sans-serif</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-weight</span>:<span class="hljs-value"> bold</span></span>;
        }</span>
        <span class="hljs-class">.inline-block</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">display</span>:<span class="hljs-value"> inline-block</span></span>;
        }</span>
        <span class="hljs-class">.random</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2px</span> solid <span class="hljs-hexcolor">#2e3d49</span></span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#ecc81a</span></span></span>;
          <span class="hljs-comment">/* no width this time, but you could certainly apply one */</span>
          <span class="hljs-rule"><span class="hljs-attribute">height</span>:<span class="hljs-value"> <span class="hljs-number">40px</span></span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">link</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">'https://fonts.googleapis.com/css?family=Source+Sans+Pro'</span> <span class="hljs-attribute">rel</span>=<span class="hljs-value">'stylesheet'</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">'text/css'</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"container"</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">span</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-title">span</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"random inline-block"</span>&gt;</span>This is a random div.<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"random inline-block"</span>&gt;</span>This is a second random div.<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-title">span</span>&gt;</span>...<span class="hljs-tag">&lt;/<span class="hljs-title">span</span>&gt;</span>
      <span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre><p><a target="_blank" href="http://udacity.github.io/fend/fend-refresh/lesson6/inline-block/inline-block-example-final.html">This is what you'll see</a>:</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/57866835_screen-shot-2016-07-13-at-11.09.20/screen-shot-2016-07-13-at-11.09.20.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Same thing!</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Regardless of the tag, any element with <code>display: inline-block</code> takes on the layout behaviors of an inline element with the sizing behaviors of a block element.</p>
    <p>Now that you've seen inline-block elements, I want to show you a quirk of HTML that shows up from time to time.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>
    </html>


5. Why Two Lines?
6. Anonymous Boxes

    I figured this out quickly. He had two boxes that should have been on the same line, but they were on two lines. I viewed the page with developer tools and changed the width to 40%. The two elements were written as separate lines, and the browser interpreted the whitespace, newline, and tab as an **anonymous box**.

    References:

    https://www.w3.org/TR/CSS2/visuren.html#anonymous-block-level
    http://book.mixu.net/css/1-positioning.html#anonymous-box-generation

    Quiz response:

    > Thanks for completing that!
    > Right! Believe it or not, tabs, spaces and newlines in HTML can actually become elements! The resulting elements are called "anonymous boxes," which get created in a number of scenarios. This is just one example of an anonymous box. Usually, anonymous boxes from whitespace don't affect the way a page displays, but this is an example of where they do!

7. Relative Flow

    **Relative flow allows objects to be shifted relative to the other elements in the flow, after elements are laid out in the normal flow.**

    ```css
    .relative {
    position: relative;
    top: 10px;
    left: 10px;
    bottom: 10px; /* redundant if you've already defined top */
    right: 10px; /* redundant if you've already defined left */
    }
    ```

    Instructor notes

    <html>
    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><pre><code>* <span class="hljs-rules">{
        <span class="hljs-rule"><span class="hljs-attribute">position</span>:<span class="hljs-value"> relative</span></span>;
    }</span>
    </code></pre><p>The <strong>relative flow</strong> is a variant of the normal flow and behaves basically the same. But, the relative flow adds some new abilities.</p>
    <blockquote>
    <h3 id="the-relative-flow-allows-you-to-shift-the-position-of-elements-after-they-ve-been-laid-out-in-the-normal-flow-">The <strong>relative flow</strong> allows you to shift the position of elements <em>after</em> they've been laid out in the normal flow.</h3>
    </blockquote>
    <pre><code><span class="hljs-class">.relative</span> <span class="hljs-rules">{
        <span class="hljs-rule"><span class="hljs-attribute">position</span>:<span class="hljs-value"> relative</span></span>;
        <span class="hljs-rule"><span class="hljs-attribute">top</span>:<span class="hljs-value"> <span class="hljs-number">10px</span></span></span>;
        <span class="hljs-rule"><span class="hljs-attribute">left</span>:<span class="hljs-value"> <span class="hljs-number">10px</span></span></span>;
        <span class="hljs-rule"><span class="hljs-attribute">bottom</span>:<span class="hljs-value"> <span class="hljs-number">10px</span></span></span>; <span class="hljs-comment">/* redundant if you've already defined top */</span>
        <span class="hljs-rule"><span class="hljs-attribute">right</span>:<span class="hljs-value"> <span class="hljs-number">10px</span></span></span>; <span class="hljs-comment">/* redundant if you've already defined left */</span>
    }</span>
    </code></pre><p>You can think of these new CSS properties, <code>top</code>, <code>left</code>, <code>bottom</code> and <code>right</code>, as adjustments to the normal flow. Setting any of them to any pixel value will shift the element by that much from where it <em>would</em> have ended up in the normal flow.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><div class="video-atom--video--1rflY" style="width: 100%;"><div><div><div class="youtube-player--youtube-player--1_HuD"><div class="youtube-player--embed-responsive-16x9--3bmQJ youtube-player--_embed-responsive--VSOkY"><span><iframe class="embed-responsive-item" frameborder="0" allowfullscreen="1" title="YouTube video player" width="640" height="360" src="https://www.youtube.com/embed/WghQmLk7tgI?showinfo=0&amp;rel=0&amp;autohide=1&amp;vq=hd720&amp;hl=en-us&amp;cc_load_policy=0&amp;enablejsapi=1&amp;origin=https%3A%2F%2Fclassroom.udacity.com&amp;widgetid=77" id="undefined"></iframe></span></div></div></div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><div style="text-align: center; color: #afafaf; font-size: 14px; margin-top: 15px;"><a href="http://udacity.github.io/fend/fend-refresh/lesson6/relative-flow/shift-two.html" target="_blank">Here is the example</a> from the animation.</div></div></div></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Note that you can use positive and negative pixel values. You aren't changing the width or height, only the position. As you can't shift an element both directions in one axis simultaneously, you should only use one of <code>top</code> and <code>bottom</code> or one of <code>left</code> and <code>right</code> at a time.</p>
    <p>Let's add another <code>&lt;div&gt;</code> and break down this example some more. Here's the HTML to start (notice that <code>position: relative</code> is commented out):</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">html</span> <span class="hljs-attribute">lang</span>=<span class="hljs-value">"en"</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">head</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">meta</span> <span class="hljs-attribute">charset</span>=<span class="hljs-value">"UTF-8"</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">title</span>&gt;</span>Relative Flow Example<span class="hljs-tag">&lt;/<span class="hljs-title">title</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">link</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">'https://fonts.googleapis.com/css?family=Source+Sans+Pro'</span> <span class="hljs-attribute">rel</span>=<span class="hljs-value">'stylesheet'</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">'text/css'</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">style</span>&gt;</span><span class="css">
        - <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">box-sizing</span>:<span class="hljs-value"> border-box</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-family</span>:<span class="hljs-value"> <span class="hljs-string">'Source Sans Pro'</span>, sans-serif</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">font-weight</span>:<span class="hljs-value"> bold</span></span>;
        }</span>
        <span class="hljs-tag">div</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">display</span>:<span class="hljs-value"> inline-block</span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2px</span> solid <span class="hljs-hexcolor">#2e3d49</span></span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> <span class="hljs-number">300px</span></span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">height</span>:<span class="hljs-value"> <span class="hljs-number">50px</span></span></span>;
        }</span>
        <span class="hljs-tag">div</span><span class="hljs-pseudo">:nth-child(even)</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#02b3e4</span></span></span>;
        }</span>
        <span class="hljs-tag">div</span><span class="hljs-pseudo">:nth-child(odd)</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">background-color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#ecc81a</span></span></span>;
        }</span>
        <span class="hljs-class">.shift</span> <span class="hljs-rules">{
          <span class="hljs-comment">/*position: relative;*/</span>
          <span class="hljs-rule"><span class="hljs-attribute">top</span>:<span class="hljs-value"> <span class="hljs-number">10px</span></span></span>;
          <span class="hljs-rule"><span class="hljs-attribute">left</span>:<span class="hljs-value"> <span class="hljs-number">10px</span></span></span>;
        }</span>
        <span class="hljs-class">.relative</span> <span class="hljs-rules">{
          <span class="hljs-rule"><span class="hljs-attribute">position</span>:<span class="hljs-value"> relative</span></span>;
        }</span>
      </span><span class="hljs-tag">&lt;/<span class="hljs-title">style</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">body</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span>&gt;</span>I'm an inline-block div!<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span> <span class="hljs-attribute">class</span>=<span class="hljs-value">"shift"</span>&gt;</span>I'm an inline-block div!<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-title">div</span>&gt;</span>I'm an inline-block div!<span class="hljs-tag">&lt;/<span class="hljs-title">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">body</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>
    </code></pre></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/578e93af_screen-shot-2016-07-19-at-15.53.03/screen-shot-2016-07-19-at-15.53.03.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The normal flow. As all three divs are inline-block, they display in the same line.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p><a target="_blank" href="http://udacity.github.io/fend/fend-refresh/lesson6/relative-flow/shift-three.html">This shows</a> exactly what you'd expect with the normal flow. Now I'll uncomment <code>position: relative</code> in the <code>.shift</code> ruleset, which should change the position of the second <code>&lt;div&gt;</code> (you should try this out with developer tools on your own!).</p>
    <pre><code><span class="hljs-class">.shift</span> <span class="hljs-rules">{
      <span class="hljs-rule"><span class="hljs-attribute">position</span>:<span class="hljs-value"> relative</span></span>;
      <span class="hljs-rule"><span class="hljs-attribute">top</span>:<span class="hljs-value"> <span class="hljs-number">10px</span></span></span>;
      <span class="hljs-rule"><span class="hljs-attribute">left</span>:<span class="hljs-value"> <span class="hljs-number">10px</span></span></span>;
    }</span>
    </code></pre></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/578e9d95_screen-shot-2016-07-19-at-16.37.15/screen-shot-2016-07-19-at-16.37.15.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The relative flow. The second div is in a new position!</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The relatively positioned <code>.shift</code> element moved from its original position down by 10 pixels and right by 10 pixels. Now, it may seem weird that the element moved <em>down</em> when the <code>top</code> property was added, but it makes sense when you consider the <a target="_blank" href="https://en.wikipedia.org/wiki/Coordinate_system">coordinate system</a> that browsers use.</p>
    <p>You're probably familiar with the <a target="_blank" href="https://en.wikipedia.org/wiki/Cartesian_coordinate_system">Cartesian coordinate system</a> from geometry or the <a target="_blank" href="https://en.wikipedia.org/wiki/Polar_coordinate_system">Polar coordinate system</a> from trigonometry. Browsers use a slightly different coordinate system.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/578eb0d1_screen-shot-2016-07-19-at-17.58.34/screen-shot-2016-07-19-at-17.58.34.png" class="index--image--1wh9w" style="width: 556.559px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The coordinate system that browsers use. The vertical axis, y, starts at 0 at the top and gets more positive as you go down, while the horizontal axis, x, starts at 0 on the left and gets more positive as you move right.</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Similar to the Cartesian coordinate system, there are <em>x</em> and <em>y</em> axes. But while the <em>y</em>-axis in the Cartesian system gets more positive as you go <em>up</em>, the <em>y</em>-axis in browsers starts with 0 at the top and gets more positive as you move <em>down</em>.</p>
    <p>Thus, when you set <code>top</code> to a positive number, you're actually moving the element down. And if you make <code>left</code> a positive number, you move the element to the right!</p>
    <!--

    *(Later on, you'll probably encounter a very useful element called the [HTML5 canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) (`<canvas>`). It's essentially a blank slate on the page and you can can draw anything on it with JavaScript. The canvas element follows the same coordinate system! Here's [a sneak peek](https://classroom.udacity.com/courses/ud292/lessons/3163218691/concepts/31699687980923#) from a lesson in the HTML5 Canvas course where I (Cameron) go over the canvas coordinate system.)*

    --></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Did you notice how the third element didn't move in the last example? Even after the second element shifted, the third element stayed in place. You'll be exploring why in the next quiz.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>
    </html>

8. Relative Flow Quiz

    Children of a relative element shift with the parent. Siblings don't shift.

9. Relative Neighbors

    Browsers use a layering system, so some elements will be on top of others.

10. 3D Websites

    > Browsers also have a third dimension: the z-dimension (also known as the z-axis). While x and y run along the computer screen's surface, z is the dimension that extends in to and out of the screen. By adding a third dimension, you can think of elements as appearing on different layers, similar to the kind of layers you would find in image-editing software like Adobe® Photoshop®.
    > 
    > In CSS you can often use the z-index property to control the stacking order of overlapping elements on different layers (but [there are many gotchas!](https://philipwalton.com/articles/what-no-one-told-you-about-z-index/)).

11. Document and Viewport

    - Document is the entire DOM
    - Window is the total visible portion of the DOM
    - Viewport is the portion of the DOM currently shown on the screen

12. Fixed Flow

    `position: absolute` and `position: fixed`

    |  | Relative | Absolute | Fixed |
    |--|----------|----------|-------|
    | **When** |  After normal flow | Before normal flow | Before normal flow |
    | **Positioned relative to...** |  position in normal flow | parent | viewport

13. Fixed Flow Quiz

    I added the following code to the sticky footer CSS:

    ```css
    .sticky-footer {
          background-color: #15C26B;
          width: 100%;
          height: 50px;
          position: fixed;
          bottom: 0px;
    ```

14. Absolute Flow

    > **When Would You Actually Use `position: absolute`?**
    > Frankly, `position: absolute` is best thought of as a last resort. If all the other flows fail, then maybe absolute is your best option. Off the top of my head, I can't actually think of an instance where I wanted to use `position: absolute`. There are, in fact, other CSS techniques for achieving the same kind of shift, of which my favorite is `transform: translate`. ([Transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform) is a more advanced CSS property and it's incredibly powerful. I recommend checking it out).
    > It's good to know what `position: absolute` does, but it's rarely your best positioning option.

15. Inline Formatting

    Horizontal alignment: `text-align`. Left, right, center, justify.

    Vertical alignment: `vertical-align`. 

    > There are two sets of values you can use to change text vertical alignment. The first set focuses on the parent's size, while the second set focuses on the element's line.
    > `vertical-align: text-top`, `vertical-align: text-bottom` and `vertical-align: middle` are options for aligning text to the eponymous locations in the parent.
    > `vertical-align: top` and `vertical-align: bottom` will align with the line instead.
    > Deciding how and when to use vertical-align is usually more of an exercise in trial-and-error than careful consideration.

16. Debugging CSS Part 1
    
    > Simple ideas form the basis of even the most complex system.

    Yes!

    Quiz part 1: add one line of CSS on the .sibling class, to move the "Relative Sibling" box down.

    `vertical-align: top`

17. Debugging CSS Part 2
18. Debugging CSS Solution

    I didn't have the alignment problem the instructor was referring to, so I just moved on.

    I'll just paste the explanation below:

    <html>
    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>As I said earlier, I came across this problem on accident. I'm presenting the solution in an order that's efficient and effective for your understanding, but I want you to know that this is the end product of a lot of experimentation. I spent quite a bit of time in developer tools playing with CSS properties, predicting what would happen before I made a change and then drawing conclusions after. I'm not alone in my approach. Here's a quote from Warren Ouyang, our lead front-end engineer, to whom I gave this problem. After he finished it, he said,</p>
    <blockquote>
    <p>I would love to say I just looked at the code and figured it out, but <strong>I also did a bunch of playing around with it to understand it</strong>.</p>
    </blockquote>
    <p>Here we go!</p>
    <hr>
    <p>Remember, the shift from <code>position: relative</code> happens <em>after</em> the normal flow finishes. Let's start with the normal flow. Ignore <code>position: relative</code> for now.</p>
    <p>Unchecking <code>position: relative</code> gives you this:</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><div class="video-atom--video--1rflY" style="width: 100%;"><div><div><div class="youtube-player--youtube-player--1kyG7"><div class="youtube-player--embed-responsive-16x9--x203G youtube-player--_embed-responsive--wS2qC"><span><iframe class="embed-responsive-item" frameborder="0" allowfullscreen="1" title="YouTube video player" width="640" height="360" src="https://www.youtube.com/embed/7Rc7w1zU0w4?showinfo=0&amp;rel=0&amp;autohide=1&amp;vq=hd720&amp;hl=en-us&amp;cc_load_policy=0&amp;enablejsapi=1&amp;origin=https%3A%2F%2Fclassroom.udacity.com&amp;widgetid=13" id="undefined"></iframe></span></div></div></div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><div style="text-align: center; color: #afafaf; font-size: 14px; margin-top: 15px;">Notice that the layout of two non-relative siblings stays the same!</div></div></div></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Here is your smoking gun. Look at how the text lines up. You've seen this before.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57bb7f71_screen-shot-2016-08-22-at-17.39.27/screen-shot-2016-08-22-at-17.39.27.png" class="index--image--1wh9w" style="width: 560px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Without relative positioning, the text lines up!</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The sibling is an inline box and the "Child" text inside it is its text. As you learned a few pages ago, text will line up with the baseline of a parent. The baseline of the parent is lowered by the extra text inside the relative sibling. As a result, the text of the other siblings is lowered.</p>
    <p>Now, realize that the <em>text</em> lines up, not the whole inline block. Siblings have a defined height, which then extends below the text. The parent extends lower to fit all of the children.</p>
    <p><strong>So where is the gap coming from?</strong> It <em>just so happens</em> that the relative shift puts the <code>.relative</code> div slightly higher than its siblings.</p>
    <p>There's something curious about solving the last problem when you applied <code>vertical-align: top</code> to <code>.sibling</code>. You could have actually solved the problem by applying <code>vertical-align: top</code> to <code>.relative</code> too! <code>vertical-align: top</code> shifts the baseline of the relative element to the top, which means that the parent's baseline is back to the top. As a result, the two other siblings no longer get pushed up. Try it yourself and see what happens!</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>
    </html>

19. Outro

James explained that inline blocks are not the best option for the reasons we saw above.
