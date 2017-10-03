Udacity full-stack web developer nanodegree
========================

Part 01. Programming fundamentals and the web
========================

Lesson 12: HTML syntax
========================

Brendon Smith | br3ndonland

---

1. Lesson Introduction

    The instructor Cameron starts off talking about massive redwood trees. Trees will be a recurring theme in web development.

2. HTML Structure Part 1

    - Anything within `<>` is a type of HTML element called a **tag**. 
    - Other tags include `<p></p>`, `<h1></h1>`, and `<span></span>`. 
        + `<p></p>` will be on its own, `<span></span>` is inline.
    - There is always an opening and closing tag.
    - The tag, and the content within the tag, is called an **element**.


3. Quiz: Make Your First Element

    **I typed this in Sublime. So much faster with tag autocompletion.**

    ```html
    <span><i>Why do you think you'll be a good web developer?</i></span>

    <p>I am motivated by two primary outcomes in my life: personal growth and positive impact. Web development fulfills both these outcomes.

    I am most happy when I am improving myself. Web development provides an almost unlimited set of tools and skills to be learned, and the resources to learn them. I have enjoyed my web development work so far, and appreciate how quickly I can see myself making progress.

    Web development will also enable me to have a positive impact on the world by building technology tools for science. I am convinced that science is central to our existence as modern intelligent humans, but concerned that we are not doing scientific research effectively. I will be able to deliver improved technology tools that will make science more efficient, reproducible, and sustainable.</p>

    <span><i>Great answer brohan!</i></span>
    ```

    *Congratulations! You made your first element! No issues!*

4. Environments
    
    - The development environment includes all software and code that you're running. The text editor and browser are two key aspects of the development environment.
    - Apple XCode and Microsoft Visual Studio are IDEs. We won't need IDEs for web development because the browser runs the code.



5. Text Editors

    - Sublime text 3
    - Atom
    - Notepad++
    - Emacs
    - Vi/Vim
    - Microsoft Word displays rich text. Never, ever use Word for coding. Code should be written in plain-text ASCII characters.

6. Browsers

    - We will be working with Chrome.
    - They also speak highly of Firefox.

7. Udacity Front End Feedback Extension

    > While writing code in the Udacity classroom is a great way to learn web development, we think it's really important that you practice working with a text editor and a web browser on your own computer. We also think it's incredibly important that you get feedback on your code as you write it. So, we created the Udacity Front End Feedback Extension to give you feedback on your sites as you work on your own computer.
    > 
    > To use the extension, you'll write code in your text editor (doesn't matter which one) and then load your site in Google Chrome (or Mozilla Firefox) with the extension enabled. For some quizzes, the extension will give you a code that you'll copy and paste back into the classroom to let us know that you've finished the quiz successfully.

8. Workflow

    - Edit files in text editor as HTML.
    - Open in browser

9. Quiz: Make All the Headers

    *index.html*

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Headers Quiz</title>
      <!-- the next line loads the tests for the Udacity Feedback extension -->
      <meta name="udacity-grader" content="http://udacity.github.io/fend/fend-refresh/lesson2/problem-set/headers/tests.json">
    </head>
    <body>
      <p>Add your headers below this paragraph element! Add an h1, h2, h3, and h4 to finish the quiz. And make sure every header has text content :)</p>
      <h1>big big header</h1>
      <h2>big header</h2>
      <h3>header 3</h3>
      <h4>hey I'm h4! Don't forget about me!</h4>
    </body>
    </html>
    ```


10. Trees

    - Trees are used in computer science to represent hierarchical data.


11. HTML and Trees

    - HTML uses a tree structure. Content is nested within divs. Div stands for division.

    <img src="https://www.dropbox.com/s/gozg6k2sqvrc2hf/fsnd01_12_html_trees.png?dl=1">


12. Quiz: Spot the Bug

    We looked at ways to correctly format and nest tags.

13. Quiz: Tree to HTML

    Build this: 

    <img src="https://www.dropbox.com/s/g8nfm3h3ledxv2r/sample-tree.png?dl=1">

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Tree to HTML</title>
      <!-- the next line loads the tests for the Udacity Feedback extension -->
      <meta name="udacity-grader" content="http://udacity.github.io/fend/fend-refresh/lesson2/problem-set/tree-to-html/tests.json">
    </head>
    <body>
      <!-- Did you notice that the body tag - the top of the sample tree - is already here? You don't need to add another one. -->
      <!-- Your code goes here! -->
      <h1>Tree to HTML</h1>
      <div>
          <p>I want you to build this tree with HTML.</p>
          <p>Here is another paragraph!</p>
      </div>
    </body>
    </html>
    ```

14. Quiz: HTML Research

    [MDN HTML Element Reference page](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

    ```html
    <p><b>This text should be bold.</b></p>
    <p><i>And this text should have emphasis (italics).</i></p>
    ```

    The b and i are used for other purposes. Recommended alternative tags: 

    ```html
    <p><strong>This text should be bold.</strong></p>
    <p><em>And this text should have emphasis (italics).</em></p>
    ```

15. Quiz: Make a List
    
    > Did you know that web developers spend 90% of their time looking things up?
    > 
    > Ok, I made up that number.
    > 
    > But seriously, making sense of documentation and looking up new techniques and technologies is a huge part of any web developer's work. And that's what I want you to do for this quiz.
    > 
    > Actually, you might find that you can make an `<li>` element appear on the page without putting it inside a `<ul>` or `<ol>`. Just because this works doesn't mean that you should ever do this. It's the equivalent of writing a sentence with bad grammar - most people will probably understand what you mean but some people will get confused. In this case, "people" are browsers and "confused" means "render your website incorrectly."


16. A Guide to Paths

    **I found this guide very interesting. It emphasized how websites are just collections of files on a computer that we call a server.**

    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>You'll soon make a website that displays an image that is stored locally on your computer. In order to display a local image, you need to be able to write a <strong>path</strong>.</p>
    <p><strong>tl;dr</strong> If there is a file called <code>index.html</code> in a directory and there is another directory called <code>example/</code> in the same directory, you can access any files in <code>example/</code> from <code>index.html</code> with the URL (path) <code>example/filename.html</code>, e.g. <code>&lt;a href="example/filename.html"&gt;Example Path&lt;/a&gt;</code>.</p>
    <h2 id="paths">Paths</h2>
    <p>A path is a way of describing where a file is stored.</p>
    <p>Think of it like this:</p>
    <p>Anyone in the world can use the address 1600 Pennsylvania Ave NW, Washington DC, USA 20006 to find the White House. A street address is an absolute path to a location.</p>
    <p>But, if you were at the <a target="_blank" href="https://www.google.com/maps/place/Eisenhower+Executive+Office+Building/@38.8974712,-77.0390948,17z/data=!4m7!1m4!3m3!1s0x89b7b7bcdec17ee3:0xf920b148b3d45e45!2s1600+Pennsylvania+Ave+NW,+Washington,+DC+20500!3b1!3m1!1s0x0000000000000000:0x054470506cffbeb3">Eisenhower Executive Office</a>, you could also use the phrase "next door" to find the White House. "Next door" is a relative path because it depends on your current location.</p>
    <p>There are essentially two domains for paths that you'll need to consider as a web developer: paths to find files on your computer, <strong>local</strong> files, and paths to find files on other computers, <strong>external</strong> files.</p>
    <h3 id="local-paths">Local Paths</h3>
    <p>Computers have folders (also called "directories"). Operating systems like Windows, Mac and Linux organize <em>all</em> of your files into a tree of directories called a <strong>file system</strong>. There's a top-most directory, often called the <strong>root</strong>, that contains all of the other directories. Within the root, there are files and directories. Within those directories are more files and more directories. And within those directories are even more files and directories, and so on.</p>
    <p>Compare this part of the file system on my computer:</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57ed86e8_local-paths/local-paths.png" class="index--image--1wh9w" style="width: 465.5px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Local path directory structure screenshot</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>to a tree diagram showing the same directory structure:</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57ed8715_directory-structure-tree/directory-structure-tree.png" class="index--image--1wh9w" style="width: 465.5px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Tree diagram of directory structure</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Every file has an address, which we call the "path." An absolute path is written in relation to the computer's root directory. For instance, a file in the Documents folder on a Mac has a path that looks like this:</p>
    <pre><code class="lang-text">/Users/cameron/Documents/file.txt
    </code></pre>
    <p><code>file.txt</code> is stored inside <code>Documents/</code>. <code>Users/</code>, <code>cameron/</code> and <code>Documents/</code> are all names of directories. <code>Documents/</code> lives inside <code>cameron/</code> and <code>cameron/</code> lives inside <code>Users/</code>. <code>Users/</code> is inside the root directory, which is represented by the first <code>/</code>. The rest of the <code>/</code> are used to separate directories.</p>
    <p>When you open an HTML file in your browser, you're seeing the absolute path to the file on your computer.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57ed87c3_absolute-path-browser/absolute-path-browser.png" class="index--image--1wh9w" style="width: 465.5px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Absolute Path to index.html</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>This URL will <em>only</em> work for you on your computer. As no one else has your file system, this URL is unique to your computer. If you want other people to be able to access it, then you need an...</p>
    <h3 id="external-paths">External Paths</h3>
    <p>The process of loading a website from a URL like <code>https://www.udacity.com</code> mimics opening an HTML file that you've written and saved to your computer. Every website starts with an HTML file. It just so happens that when you want to visit a website, the HTML file that you want to open lives on a different computer. The computer responsible for giving you a website's files is called a <strong>server</strong>.</p>
    <p>Pointing your browser to <code>https://www.udacity.com</code> sends a request to Udacity's server for the HTML file (and others) that your computer needs to load the Udacity website. You can think of <code>udacity.com</code> as the root path of Udacity's server (computer) that anyone can access (the reality of the situation is actually much more complicated but the general idea is true). Unlike your personal computer (for now!), Udacity's servers run software that <strong>expose</strong> files to the web, which means that they make them available to anyone who wants them. Servers have an <strong>external path</strong> that anyone can access and is the reason why the web works.</p>
    <p>Different websites are just different collections of files. Every website is really just a server (or many servers) with an external address, which we call a URL. Servers store files and send them to computers who request them (the requesting computers are called <strong>clients</strong>).</p>
    <p>There are different <strong>protocols</strong> for serving files, the most common of which on the web are HTTP and HTTPS. When you open a file on your own computer, you're using the file protocol. You don't need to know much more about protocols for now, but if you're interested in learning (a lot!) more about HTTP, check out <a target="_blank" href="https://www.udacity.com/course/networking-for-web-developers--ud256">Networking for Web Developers</a>.</p>
    <h3 id="relative-paths">Relative Paths</h3>
    <p>The relative path is similar to the absolute path, but it describes how to find to a file from a directory that is not the root directory. Like using the phrase "next door" to tell someone how to find the White House from the Eisenhower Executive Office, a relative path takes advantage of the location of one file to describe where another file can be found.</p>
    <p>Relative paths work the same for both local and external paths. Let's break down two examples of absolute paths to see how relative paths work.</p>
    <p><strong>External</strong>:</p>
    <pre><code><span class="hljs-tag">&lt;<span class="hljs-title">a</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">"http://labs.udacity.com/fend/example/hello-world.html"</span>&gt;</span>Hello, world!<span class="hljs-tag">&lt;/<span class="hljs-title">a</span>&gt;</span>
    </code></pre><p><strong>Local</strong>:</p>
    <pre><code><span class="hljs-tag">&lt;<span class="hljs-title">a</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">"/Users/cameron/Udacity/etc/labs/fend/example/hello-world.html"</span>&gt;</span> Hello, world!<span class="hljs-tag">&lt;/<span class="hljs-title">a</span>&gt;</span>
    </code></pre><p><code>href</code> is really just a path to a file.</p>
    <p>Both examples are links to the same file using absolute paths, but the external example would work for anyone and only my computer can use the link in the local example.</p>
    <p>Pay attention to the <code>fend/example/hello-world.html</code> portion of both paths - they mean the same thing.</p>
    <p>Imagine that you are editing <code>/Users/cameron/Udacity/etc/labs/fend/test.html</code>. <code>test.html</code> can reference <code>hello-world.html</code> by describing how to get from it's location in <code>fend/</code> to <code>hello-world.html</code>. The relative path would look like:</p>
    <pre><code>example/hello-world.html
    </code></pre><p>This relative path takes advantage of the fact that <code>test.html</code> and <code>example/</code> are in the same directory.</p>
    <p>But what if I'm editing a file in <code>/Users/cameron/Udacity/etc/labs/</code> and I want to write a path to <code>hello-world.html</code>? In that case, the relative path would be:</p>
    <pre><code class="lang-text">fend/example/hello-world.html
    </code></pre>
    <p>Now that I'm in <code>labs/</code>, not <code>fend/</code>, I have to include <code>fend/</code> in a relative path to <code>hello-world.html</code>.</p>
    <p>To finish this off, let's imagine there are two files:</p>
    <pre><code class="lang-text">http://labs.udacity.com/science/sciences.html
    </code></pre>
    <p>and</p>
    <pre><code class="lang-text">http://labs.udacity.com/science/physics/relativity.html
    </code></pre>
    <p>In order to write a relative path from <code>sciences.html</code> to <code>relativity.html</code>, I only need to include the part of the path that describes how to get from <code>science/</code> to <code>relativity.html</code>:</p>
    <pre><code class="lang-html"><span class="hljs-tag">&lt;<span class="hljs-title">a</span> <span class="hljs-attribute">href</span>=<span class="hljs-value">"physics/relativity.html"</span>&gt;</span>Einstein's Special Relativity<span class="hljs-tag">&lt;/<span class="hljs-title">a</span>&gt;</span>
    </code></pre>
    <p>And that's it! Now it's time to apply your new skills.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>


17. Constructing Links

    Type in a link that points to https://www.google.com and displays as Google.

    <a href="https://www.google.com">Google</a>

18. Quiz: Add an Image

    ```html
        <!--
    Sample image element:

        <img src="http://somewebsite.com/image.jpg" alt="short description">

    How to complete this quiz:

    - Create an image element at the designated spot in the paragraph below.
    - Set the source to: http://udacity.github.io/fend/images/udacity.png
    - Set the alt description to a quick description of the image (maybe something like, "Udacity logo").
    - Play around with the URL! See if you can make a different image appear.
    -->

    <p>
        This is a big paragraph of text about Udacity. Cool. Cool. And here is an image! <!-- put the image element here! --> <img src="http://udacity.github.io/fend/images/udacity.png" alt="Udacity logo"> Here's another question for you: how is the text reacting to the image? Is the image on its own line or is it showing up in the same last as the rest of the text?
    </p>

    ```

19. Quiz: Figures

    The `<figure></figure>` [element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) was new to me.

    There were two ways to complete the quiz. I used option 2.

    Option 1

    ```html
    <img 
      src="redwoods_state_park.jpg"
      alt="Stout Memorial Grove in Jedediah Smith Redwoods State Park">
      <p>
        Stout Memorial Grove in Jedediah Smith Redwoods State Park in 2011 by Chmee2 (Own work) GFDL or CC BY-SA 3.0, via Wikimedia Commons - <a href="https://commons.wikimedia.org/wiki/File%3AStout_Memorial_Grove_in_Jedediah_Smith_Redwoods_State_Park_in_2011_(22).JPG">Source</a>
      </p>
    ```


    Option 2 (adding figure tag)

    ```html
    <figure>
      <img 
      src="redwoods_state_park.jpg"
      alt="Stout Memorial Grove in Jedediah Smith Redwoods State Park">
      <figcaption>Stout Memorial Grove in Jedediah Smith Redwoods State Park in 2011 by Chmee2 (Own work) GFDL or CC BY-SA 3.0, via Wikimedia Commons - <a href="https://commons.wikimedia.org/wiki/File%3AStout_Memorial_Grove_in_Jedediah_Smith_Redwoods_State_Park_in_2011_(22).JPG">Source</a>
      </figcaption>
    </figure>
    ```

    > **Indentation Discussion**
    > 
    > I usually indent child elements inside parents. Notice that the img and figcaption are both indented inside the figure in the solution to option 2. I don't indent when a child element is part of a line or sentence. For instance, I don't indent links because their content is read as part of a sentence.
    > 
    > I also indented the text content inside the p in option 1 and the figcaption in option 2. I did this because the text looks like a big block in my code editor and it's easier to read if it is on its own line.

20. HTML Forms

    I love forms and user input! 

    **Human-Computer Intelligent Interaction**

    [HTML5 input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)

    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Forms are everywhere on the web. Here's a form you filled out when you signed up for Udacity!</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/October/57f808b9_udacity-sign-up/udacity-sign-up.png" class="index--image--1wh9w" style="width: 465.5px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Screenshot of Udacity Sign Up Form</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>And, here's a form I filled out when I ordered a new blender online.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/October/57f80a1e_shipping-form/shipping-form.png" class="index--image--1wh9w" style="width: 404px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Shipping form screenshot</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Forms allow users to interact with your site. Normally, forms take the information submitted by a user and send it somewhere to be processed. The sending and receiving of information using a form will be covered in later courses; however, for this next quiz, you'll learn how to plan out and structure a form given some specifications.</p>
    <p>To do this, you'll first need to know about the different HTML form tags available to you.</p>
    <h3 id="-form-tag"><code>&lt;form&gt;</code> tag</h3>
    <p>The <code>&lt;form&gt;</code> tag will be the parent element that contain all of the code for the form. The form fields, the buttons, etc. need to be enclosed inside these tags.</p>
    <pre><code><span class="hljs-tag">&lt;<span class="hljs-title">form</span> <span class="hljs-attribute">action</span>=<span class="hljs-value">""</span> <span class="hljs-attribute">method</span>=<span class="hljs-value">""</span>&gt;</span>
    <span class="hljs-comment">&lt;!-- stuff goes here --&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-title">form</span>&gt;</span>
    </code></pre><p>the <code>action</code> and <code>method</code> attributes tell the form where and how to send the form data, respectively. You will not need them in this course, so we will leave them blank for now.</p>
    <h3 id="-input-tags"><code>&lt;input&gt;</code> tags</h3>
    <p>The <code>&lt;input&gt;</code> tag lets you add form fields for the user to enter their information. Each input tag will have an attribute called <code>type</code> to indicate what type of form field to put in the form:</p>
    <pre><code>&lt;input <span class="hljs-class"><span class="hljs-keyword">type</span>=</span><span class="hljs-string">"text"</span>&gt;
    </code></pre><input type="text" placeholder="text is awesome" data-com.agilebits.onepassword.user-edited="yes">
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>There are a ton of input types available with HTML5. You can check out the <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input">list</a> here if you're curious. Each different input type changes the type of form field that's rendered on the page. Here's an example using the date, radio, and checkbox input types.</p>
    <pre><code>&lt;input type=<span class="hljs-string">"checkbox"</span>&gt; You can check <span class="hljs-keyword">me</span> off <span class="hljs-keyword">the</span> <span class="hljs-type">list</span>!
    </code></pre><p><input type="checkbox" id="1" value="I am a checkbox"><label for="1"> &nbsp; You can check me off the list! </label></p>
    <pre><code>&lt;input <span class="hljs-class"><span class="hljs-keyword">type</span>=</span><span class="hljs-string">"radio"</span>&gt; <span class="hljs-type">On</span> the radio... oh oh.
    </code></pre><p><input type="radio" id="2" value="I am a radio button"><label for="2"> &nbsp; On the radio... oh oh. </label></p>
    <pre><code>&lt;input <span class="hljs-class"><span class="hljs-keyword">type</span>=</span><span class="hljs-string">"date"</span>&gt;
    </code></pre><input type="date">

    <p><br>
    One particular example that's a little different than the others is the <code>&lt;textarea&gt;</code> tag. It's similar to <code>&lt;input type="text"&gt;</code> but you can use it to create a multi-line text input box for your user.</p>
    <pre><code><span class="hljs-tag">&lt;textarea&gt;</span>
    </code></pre><textarea>Here's a place to write a lot of stuff.</textarea>

    <h3 id="-label-tag"><code>&lt;label&gt;</code> tag</h3>
    <p>A form is no good if your user doesn't know what to put in each box! The <code>&lt;label&gt;</code> tag adds text to an <code>&lt;input&gt;</code> field so the user knows what information is being asked for.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/October/57f81304_example-no-label-form/example-no-label-form.png" class="index--image--1wh9w" style="width: 465.5px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>What am I supposed to type here?</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>For accessibility reasons, it's important to associate each input element with a label. One way to do this is to use the <code>&lt;label&gt;</code> tag. Screen readers and other programs designed for accessibility will help bring focus to an input field and its description when labels are appropriately linked to their input fields using the <code>for</code> and <code>id</code> attributes.</p>
    <pre><code><span class="hljs-tag">&lt;<span class="hljs-title">label</span> <span class="hljs-attribute">for</span>=<span class="hljs-value">"name"</span>&gt;</span>What is your name?<span class="hljs-tag">&lt;/<span class="hljs-title">label</span>&gt;</span> <span class="hljs-tag">&lt;<span class="hljs-title">input</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">"text"</span> <span class="hljs-attribute">id</span>=<span class="hljs-value">"name"</span>&gt;</span> <span class="hljs-comment">&lt;!-- for= and id= are both "name" --&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">label</span> <span class="hljs-attribute">for</span>=<span class="hljs-value">"age"</span>&gt;</span>How old are you?<span class="hljs-tag">&lt;/<span class="hljs-title">label</span>&gt;</span> <span class="hljs-tag">&lt;<span class="hljs-title">input</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">"number"</span> <span class="hljs-attribute">id</span>=<span class="hljs-value">"age"</span>&gt;</span> <span class="hljs-comment">&lt;!-- for= and id= are both "age" --&gt;</span>
    </code></pre><p><label for="name">What is your name?</label> <input type="text" id="name" data-com.agilebits.onepassword.user-edited="yes"></p>
    <p><label for="age">How old are you?</label> <input type="number" id="age" data-com.agilebits.onepassword.user-edited="yes"></p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><h3 id="-button-button-"><code>&lt;button&gt;&lt;/button&gt;</code></h3>
    <p>Finally, the user needs to be able to do something with the data. There are buttons for this!</p>
    <p>HTML5 has the <code>&lt;button&gt;&lt;/button&gt;</code> element. Buttons also have a type (you can read about them <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button">here</a>) so you can specify whether the button submits data or resets (clears) it. Buttons also have the added benefit of being able to display anything in the button by just adding content inside the button tags.</p>
    <pre><code><span class="hljs-tag">&lt;<span class="hljs-title">button</span>&gt;</span>I am just a button.<span class="hljs-tag">&lt;/<span class="hljs-title">button</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">button</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">"submit"</span>&gt;</span>I am a submit button!<span class="hljs-tag">&lt;/<span class="hljs-title">button</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">button</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">"reset"</span>&gt;</span>I am a reset button!<span class="hljs-tag">&lt;/<span class="hljs-title">button</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">button</span> <span class="hljs-attribute">type</span>=<span class="hljs-value">"button"</span>&gt;</span>I am a button with an image! <span class="hljs-tag">&lt;<span class="hljs-title">br</span>&gt;</span> <span class="hljs-tag">&lt;<span class="hljs-title">img</span> <span class="hljs-attribute">src</span>=<span class="hljs-value">"rocketship.png"</span> <span class="hljs-attribute">alt</span>=<span class="hljs-value">"udacity-rocket"</span>&gt;</span><span class="hljs-tag">&lt;/<span class="hljs-title">button</span>&gt;</span>
    </code></pre><p><button>I am just a button.</button><br></p>
    <p><button type="submit">I am a submit button!</button><br></p>
    <p><button type="reset">I am a reset button!</button><br></p>
    <p><button type="button">I am a button with an image! <br> <img src="https://d125fmws0bore1.cloudfront.net/assets/svgs/icon-rocket-3d59dfa75cb89b0356997dcb453c534f7c5837fb21a612652cdd15d264a84d9c.svg" alt="udacity-rocket"></button><br></p>
    <p>Often, you will use a submit button to submit and process the information in the form. For now, focus on making your forms look great and you'll make those submit buttons functional in a later course. 😊 </p>
    <p>Great! Now that you have all the pieces of an HTML form, try making a form in the next quiz.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>

21. HTML Structure Part 2
22. HTML Documents in Depth

    - We went through doctypes, head, body
    - tried just typing `<h1>This is a title</h1>` without the doctype into the [W3C HTML Validator](https://validator.w3.org/#validate_by_input) and got an error
    > Thanks for completing that!
    > Nice work! The validator didn’t know what type of document it was, so it assumed it was HTML 4.01. There are also errors and warnings about missing doctypes and unknown character encodings.
    
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>title fo sho</title>
    </head>
    <body>
        <h1>This is a title</h1>
    </body>
    </html>
    ```

    Lesson notes

    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><h3 id="html-doctypes">HTML Doctypes</h3>
    <p>An HTML document will usually start with a type declaration (which is not a tag, so it should not have a closing tag). The declaration helps the browser determine what type of HTML document it’s trying to parse and display.</p>
    <p>If you’ve ever looked at an <a target="_blank" href="http://www.3riversstadium.com/index2.html">older website</a> using dev tools, you might have noticed a doctype that looks like this:</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"&gt;</span>

    (Triggers Standards mode but specifies an older form of validation.)
    </code></pre><p>Or maybe you didn’t see a doctype at all?</p>
    <pre><code><span class="hljs-tag">&lt;<span class="hljs-title">html</span>&gt;</span>
        … 
    <span class="hljs-tag">&lt;/<span class="hljs-title">html</span>&gt;</span>

    (Triggers “Quirks” mode. This is bad.)
    </code></pre><p>But newer websites (and your websites!) will have a declaration that looks like this:</p>
    <pre><code><span class="hljs-doctype">&lt;!DOCTYPE html&gt;</span>

    (Triggers Standards mode with all updated features.) 😊
    </code></pre><p>Browsers look for this doctype declaration to determine which <strong>rendering mode</strong> to use to render the site. Generally, newer sites follow standard HTML specifications. The current standard HTML specification is called HTML5 (which is what you're learning!). On the other hand, older sites, created before HTML standards really existed, might use a different rendering mode that imitates the behavior of older browsers.</p>
    <p>If you are interested in reading more about doctype declarations and different rendering modes, you can read about them <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Quirks_Mode_and_Standards_Mode">here</a>.</p>
    <p>Once you’ve declared the doctype, the next part of your HTML document is the <code>&lt;html&gt;</code> tag, which tells the browser that everything enclosed inside the <code>&lt;html&gt; ...  &lt;/html&gt;</code> should be parsed as HTML. Then you have the two main sections of your HTML document: <code>&lt;head&gt;</code> and <code>&lt;body&gt;</code></p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/578ea34e_html-tree/html-tree.png" class="index--image--1wh9w" style="width: 465.5px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Basic HTML Tree Structure</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><h3 id="-head-and-body-"><code>&lt;head&gt;</code> and <code>&lt;body&gt;</code></h3>
    <p>The <code>&lt;head&gt;</code> will contain general information and metadata about the page, while the <code>&lt;body&gt;</code> will contain the content that will be displayed on the page. Here’s an example tree structure for a full HTML document:</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/578ea3b9_full-html-tree/full-html-tree.png" class="index--image--1wh9w" style="width: 465.5px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Full HTML Tree Structure</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>All of the HTML syntax that you’ve learned in this lesson will help you create the <strong>content</strong> of the page, which is always contained inside the <code>&lt;body&gt;</code> tags. The <code>&lt;body&gt;</code> is always visible.</p>
    <p>The <code>&lt;head&gt;</code>, on the other hand, is never visible, but the information in it describes the page and links to other files the browser needs to render the website correctly. For instance, the <code>&lt;head&gt;</code> is responsible for:</p>
    <ul>
    <li>the document’s title (the text that shows up in browser tabs): <code>&lt;title&gt;About Me&lt;/title&gt;</code>.</li>
    <li>associated CSS files (for style): <code>&lt;link rel="stylesheet" type="text/css" href="style.css"&gt;</code>.</li>
    <li>associated JavaScript files (multipurpose scripts to change rendering and behavior): <code>&lt;script src="animations.js"&gt;&lt;/script&gt;</code>.</li>
    <li>the charset being used (the text's <a target="_blank" href="https://en.wikipedia.org/wiki/Character_encoding">encoding</a>): <code>&lt;meta charset="utf-8"&gt;</code>.</li>
    <li>keywords, authors, and descriptions (often useful for <a target="_blank" href="https://en.wikipedia.org/wiki/Search_engine_optimization">SEO</a>): <code>&lt;meta name="description" content="This is what my website is all about!"&gt;</code>.</li>
    <li>… and more!</li>
    </ul>
    <p>At this point, just focus on these two tags:</p>
    <ul>
    <li><code>&lt;title&gt;About Me&lt;/title&gt;</code></li>
    <li><code>&lt;meta charset="utf-8"&gt;</code></li>
    </ul>
    <p><code>&lt;meta charset="utf-8"&gt;</code> is pretty standard, and will allow your website to display any <a target="_blank" href="http://unicode-table.com/en/">Unicode character</a>. (<a target="_blank" href="https://en.wikipedia.org/wiki/UTF-8">Read more on how UTF-8 works here</a>.) <code>&lt;title&gt;</code> will define the title of the document and will be displayed in the tab of the browser window when a user visits the page.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/July/578ea580_full-html-template/full-html-template.png" class="index--image--1wh9w" style="width: 465.5px;"></div><div class="index--caption--34paT"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Full HTML Template</p>
    </div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><h1 id="html-validators">HTML Validators</h1>
    <p>This might seem like a lot to remember, but thankfully, there are tools out there to help you. Much like how the Udacity Feedback Extension tells you when you've met all the requirements for a particular project, <a target="_blank" href="https://validator.w3.org">HTML validators</a> analyze your website and verify that you're writing valid HTML.</p>
    <p>I want you to try one out now!</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><div class="quiz-styles--container--2-qpA"><div class="quiz-styles--prompt--ZLAZm"><h3 class="quiz-styles--question-number--3EbH8">Question 1 of 2</h3><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Using the <a target="_blank" href="https://validator.w3.org/#validate_by_input">W3C HTML Validator</a>, what happens when you enter the following HTML into the "validate by input" text box:</p>
    <pre><code><span class="hljs-tag">&lt;<span class="hljs-title">h1</span>&gt;</span>This is a title<span class="hljs-tag">&lt;/<span class="hljs-title">h1</span>&gt;</span>
    </code></pre></div></div><ul><li class="_answer--answer-correct--13UjS _answer--answer--1HCPX"><div class="_answer--status--1Esuk"><div class="_answer--answered-label--313DP"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The validator found errors or warnings in the HTML</p>
    </div></div></div></li><li class="_answer--answer--1HCPX"><div class="_answer--status--1Esuk"><div class="_answer--selector--lhYoz"><span class="ureact-checkbox--wrapper--cpLpX"><input type="checkbox" readonly="" class="ureact-checkbox--checkbox--1Rfc2" id="ureact-checkbox-qac9bw07" style="margin-right: 0.5em;" value="on"><label for="ureact-checkbox-qac9bw07" class="ureact-checkbox--label--3Lngk"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The validator crashed because the HTML was in the incorrect format</p>
    </div></label></span></div></div></li><li class="_answer--answer--1HCPX"><div class="_answer--status--1Esuk"><div class="_answer--selector--lhYoz"><span class="ureact-checkbox--wrapper--cpLpX"><input type="checkbox" readonly="" class="ureact-checkbox--checkbox--1Rfc2" id="ureact-checkbox-lxk982fp" style="margin-right: 0.5em;" value="on"><label for="ureact-checkbox-lxk982fp" class="ureact-checkbox--label--3Lngk"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The validator assumed the document was HTML5</p>
    </div></label></span></div></div></li><li class="_answer--answer-correct--13UjS _answer--answer--1HCPX"><div class="_answer--status--1Esuk"><div class="_answer--answered-label--313DP"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>The validator assumed the document was something other than HTML5</p>
    </div></div></div></li></ul></div><div class="checkbox-quiz-atom--buttons--cp1vx _quiz-atom--buttons--3vJgG"><button type="button" class="index--primary--P14pO index--_btn--9nYKH  index--standard--3U4zZ" style="cursor: pointer;">Submit</button></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><noscript></noscript><div class="quiz-styles--container--2-qpA"><div class="quiz-styles--prompt--ZLAZm"><h3 class="quiz-styles--question-number--3EbH8">Question 2 of 2</h3><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Now, modify the HTML you entered previously so it follows the HTML template. Make sure to set doctype for HTML5!</p>
    <p>What is the message displayed once the validator successfully validates your code?</p>
    </div></div><ul><li class="_answer--answer--1HCPX"><div class="_answer--status--1Esuk"><div class="_answer--selector--lhYoz" style="margin-right: 0.5em;"><input type="radio" readonly="" class="ureact-radio--radio--FEdev" id="ureact-radio-xdpeykp6" style="margin-right: 0.5em;" value="on"><label for="ureact-radio-xdpeykp6" class="ureact-radio--label--2deTg"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>No errors found while checking this document as HTML5!</p>
    </div></label></div></div></li><li class="_answer--answer--1HCPX"><div class="_answer--status--1Esuk"><div class="_answer--selector--lhYoz" style="margin-right: 0.5em;"><input type="radio" readonly="" class="ureact-radio--radio--FEdev" id="ureact-radio-zanvrtzq" style="margin-right: 0.5em;" value="on"><label for="ureact-radio-zanvrtzq" class="ureact-radio--label--2deTg"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Document checking completed.</p>
    </div></label></div></div></li><li class="_answer--answer--1HCPX"><div class="_answer--status--1Esuk"><div class="_answer--selector--lhYoz" style="margin-right: 0.5em;"><input type="radio" readonly="" class="ureact-radio--radio--FEdev" id="ureact-radio-zdc05hjg" style="margin-right: 0.5em;" value="on"><label for="ureact-radio-zdc05hjg" class="ureact-radio--label--2deTg"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>No errors or warnings to show.</p>
    </div></label></div></div></li><li class="_answer--answer--1HCPX"><div class="_answer--status--1Esuk"><div class="_answer--selector--lhYoz" style="margin-right: 0.5em;"><input type="radio" readonly="" class="ureact-radio--radio--FEdev" id="ureact-radio-jzg62gcm" style="margin-right: 0.5em;" value="on"><label for="ureact-radio-jzg62gcm" class="ureact-radio--label--2deTg"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>Document checking completed. No errors or warnings to show.</p>
    </div></label></div></div></li></ul></div><div class="radio-quiz-atom--buttons--Y7OWz _quiz-atom--buttons--3vJgG"><button type="button" class="index--primary--P14pO index--_btn--9nYKH  index--standard--3U4zZ" disabled="" style="cursor: default;">Submit</button></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div></div>


23. Mockup to Website

    - Going from designers/UX who provide images to the actual website.


    <div class="_main--content-container--ILkoI"><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><h2 id="mockup-to-website">Mockup to Website</h2>
    <p>It's common for web developers to work with designers who focus on creating user interfaces and user experiences. Designers use software like Adobe Photoshop to mock up - draw - websites. The mockups that they create are usually just images of websites with some annotations and descriptions. </p>
    <p>As a web developer, one of the tasks you might be asked to do is take a mockup created by a visual designer and translate it into a live website. I use the word "translate" because the process of going from mockup to website is similar to the process of translating between natural languages. Just as you can create the same meaning using different words and phrases with a natural language, you can create the same website design using different HTML elements.</p>
    <p>I want you to practice the process of going from a mockup to a website now! Here is a website mockup (note: I zoomed in for the screen shot):</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="image-atom--image-atom--1XDdu"><div class="index--image-atom-content--YoZVu"><div class="index--image-and-annotations-container--1o6QP"><img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/June/593763fd_mockup/mockup.png" class="index--image--1wh9w" style="width: 465.5px;"></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="ureact-markdown--markdown--3IhZa ureact-markdown "><p>You can find a copy of this image in <code>web-dev-blog.zip</code> in the instructor notes. You'll also find a file to start editing (<code>index.html</code>) and a copy of the mockup.</p>
    <p>There are many ways to turn this mockup into website. As such, you won't be getting feedback on your site using the Chrome extension. Rather, I want you to compare your website to the mockup. You'll know you've finished this exercise when your site looks the same :)</p>
    <h3 id="how-to-complete-this-quiz">How to Complete this Quiz</h3>
    <ol>
    <li>Download and unzip <a target="_blank" href="https://www.udacity.com/api/nodes/7231514902/supplemental_media/web-dev-blogzip/download?_ga=1.140458419.1290139238.1470161293">web-dev-blog.zip</a>.</li>
    <li>Open the mockup and decide how you want to create the article.</li>
    <li>Edit <code>index.html</code> until your website looks identical to the mockup.</li>
    <li>Practice indenting children elements. I'll show you how I indented my HTML in the solution.</li>
    </ol>
    <p>Just to be clear, there is no feedback from the Chrome extension. It's up to you to decide when your website looks identical to the mockup.</p>
    </div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div><noscript></noscript><div class="task-list-atom--container--WBrU5"><div class="task-list-atom--tasks-container--3MvCe"><span class="task-list-atom--icon-container--3-v6v">Task List</span><div class="task-list-atom--tasks-checkbox-container--LMF6d"><div><span class="index--wrapper--Z_Wv3"><input type="checkbox" id="ureact-checkbox-qj28i4y4" class="index--checkbox--3qGuh" value="on"><label for="ureact-checkbox-qj28i4y4" class="index--label--3MXRg"><div class="index--markdown--2I2Ir ureact-markdown "><p>Edit the HTML so your website looks <em>exactly</em> like the mock up. Click here when you're done.</p>
    </div></label></span></div></div></div></div></div><span></span></div><div class="index--instructor-notes-container--24U8Y shared--outer-container--3eppq"><div class="index--instructor-notes--39nNE layout--content--3Smmq"><div><noscript></noscript></div></div></div></div><div class="_main--resources-container--2Mxsv layout--content--3Smmq"><div><h4>Supporting Materials</h4><div class="resources--links--Dmbld"><div><a href="https://www.udacity.com/api/nodes/7231514902/supplemental_media/web-dev-blogzip/download" target="_blank" class="resources--resource-link--37SIs"><span class="ureact-glyph--icon-download-sm--1Ddlb ureact-glyph--icon--3AXgN" title=""><i></i></span><!-- react-text: 6731 --> <!-- /react-text --><!-- react-text: 6732 -->web-dev-blog.zip<!-- /react-text --></a></div></div></div></div></div>

24. HTML Syntax Outro