# HTTP in the real world

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

[HTTP & Web Servers](https://www.udacity.com/course/http-web-servers--ud303)

Lesson 3. HTTP in the Real World: Deploying to Heroku

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Lesson](#lesson)
  - [Deploying to a hosting service](#deploying-to-a-hosting-service)
  - [Static content and more](#static-content-and-more)
  - [Caching](#caching)
  - [Cookies](#cookies)
  - [HTTPS for security](#https-for-security)
  - [Beyond GET and POST](#beyond-get-and-post)
  - [New developments in HTTP](#new-developments-in-http)
  - [Keep learning](#keep-learning)
- [Feedback](#feedback)

## Lesson

### Deploying to a hosting service

#### Can I just host my web service at home

> Maybe! Plenty of people do, but not everyone can. It's a common hobbyist activity, but not something that people would usually do for a job.
>
> There's nothing fundamentally special about the computers that run web servers. They're just computers running an operating system such as Linux, Mac OS, or Windows (usually Linux). Their connection to the Internet is a little different from a typical home or mobile Internet connection, though. A server usually needs to have a stable (static) IP address so that clients can find it and connect to it. Most home and mobile systems don't assign your computer a static IP address.
>
> Also, most home Internet routers don't allow incoming connections by default. You would need to reconfigure your router to allow it. This is totally possible, but way beyond the scope of this course (and I don't know what kind of router you have).
>
> Lastly, if you run a web service at home, your computer has to be always on.
>
> So, for the next exercise in this course, you'll be deploying one of your existing web services to Heroku, a commercial service that will host it on the web where it will be publicly accessible.
>
>

#### Steps to deployment

>
> Here's an overview of the steps you'll need to complete. We'll be going over each one in more detail.
>
> 1. Check your server code into a new local Git repository.
> 2. Sign up for a free Heroku account.
> 3. Download the Heroku command-line interface (CLI).
> 4. Authenticate the Heroku CLI with your account: `heroku login`
> 5. Create configuration files *Procfile*, *requirements.txt*, and *runtime.txt- and check them into your Git repository.
> 6. Modify your server to listen on a configurable port.
> 7. Create your Heroku app: `heroku create your-app-name`
> 8. Push your code to Heroku with Git: `git push heroku master`

##### 1. Check your server code into a new local Git repository

I created *udacity-fsnd/files/02_tools/fsnd02_12-http-python*, copied in my version and Udacity's version of the bookmark server code, along with the README.md, and checked it in with Git.

##### Heroku Python tutorial

- I signed up for Heroku
- I went to the [Heroku Python getting started guide](https://devcenter.heroku.com/articles/getting-started-with-python#introduction). The Python web app instructions are different than the CLI instructions used in this lesson, but I thought they could be helpful for future work with Flask and Django, so I branched from the lesson here and walked through the Python instructions.
- `pip install pipenv`
- Installed [Postgres](http://postgresapp.com/), initialized a new server by clicking "initalize," and configured `$PATH` to use command line tools

  ```bash
  sudo mkdir -p /etc/paths.d &&
  echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
  ```

- Installed CLI. May have installed this three times.
  - Toolbelt: Did this during the Heroku Python installation above. The download wouldn't start. I opened the Mac OS X link in a new tab, which actually took me to a [JSON](https://cli-assets.heroku.com/branches/stable/heroku-osx.pkg) listing the [link to the toolbelt package](https://cli-assets.heroku.com/branches/stable/heroku-osx.pkg). I pasted that link into a new window and downloaded that, and ran the installation.
  - I then found that I could install with direct download (of a different CLI file apparently), or through Homebrew. I installed the direct download.
  - I then ran `brew install heroku/brew/heroku`, which asked me to overwrite the previous installation. I did. See *udacity-fsnd_02_13-http-heroku-terminal.md- for full iTerm 2 Terminal logs.
- Deployed app as detailed in the [Heroku Python getting started guide](https://devcenter.heroku.com/articles/getting-started-with-python#introduction). Apps run in Linux containers called [dynos](https://devcenter.heroku.com/articles/dynos).
- Tried scaling with `$ heroku ps:scale web=0` (not running) vs. `$ heroku ps:scale web=1`. *Why do you need more dynos? To handle more traffic?*
- [Declare app dependencies](https://devcenter.heroku.com/articles/getting-started-with-python#declare-app-dependencies):
  - This is where we got started with Python-specific stuff.
  - > Heroku recognizes an app as a Python app by the existence of a Pipfile or requirements.txt file in the root directory.
- Run the app locally:
  - > The app is almost ready to start locally. Django uses local assets, so first, you’ll need to run collectstatic: `$ python manage.py collectstatic`
  - `heroku local`
  - Navigate to [http://localhost:5000/](http://localhost:5000/).
- Define config vars: I started getting errors with `heroku local`. I committed and pushed, and it worked online, so it must be an issue with something related that is installed locally. `gunicorn` and `django` were not found.
- Provision a database: created database tables with the standard Django `manage.py migrate` to create the tables.
  - > The code to access the database is straightforward, and makes use of a simple Django model called Greetings that you can find in hello/models.py.
- Done! Next, I can work through [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python), and maybe deploy my movie trailer python web server.

##### Heroku Python tutorial from Udacity

- Create configuration files *Procfile*, *requirements.txt*, and *runtime.txt- and check them into your Git repository.
  - *requirements.txt*: `requests>=2.12`
  - *runtime.txt*: `python-3.6.3`
  - *Procfile*: `web: python BookmarkServer-udacity.py`
  - `$ git commit -m "Add Heroku configuration files"`
- Modify your server to listen on a configurable port.
  - Modified the Python file to make the port configurable

    ```python
    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 8000))  # Use PORT if it's there.
        server_address = ('', port)
        httpd = http.server.HTTPServer(server_address, Shortener)
        httpd.serve_forever()
    ```

  - `$ git commit -m "Use PORT from environment"`
- Navigated to [http://localhost:8000/](http://localhost:8000/) to check servers
- Create your Heroku app

  ```bash
  $ heroku create bookmarkserver-br3ndonland
  Creating ⬢ bookmarkserver-br3ndonland... done
  https://bookmarkserver-br3ndonland.herokuapp.com/ | https://git.heroku.com/bookmarkserver-br3ndonland.git
  ```

  ```bash
  $ heroku create bookmarkserver-udacity
  Creating ⬢ bookmarkserver-udacity... done
  https://bookmarkserver-udacity.herokuapp.com/ | https://git.heroku.com/bookmarkserver-udacity.git
  ```

- Push your code to Heroku with Git: `git push heroku master`

Tried it with both versions of the Bookmark Server: mine and Udacity's. Created separate directories for each.

- Test websites:
  - [Google Scholar](https://scholar.google.com/citations?user=ZJ2yZa8AAAAJ&hl=en) did not work.
    - br3ndonland got a Heroku Application Error: "An error occurred in the application and your page could not be served. If you are the application owner, check your logs for details."
    - Udacity got "Couldn't fetch URI '[https://scholar.google.com/citations?user=ZJ2yZa8AAAAJ&hl=en](https://scholar.google.com/citations?user=ZJ2yZa8AAAAJ&hl=en)'. Sorry!"
  - [DuckDuckGo](https://duckduckgo.com/) worked in both!
  - [Bear](http://www.bear-writer.com/) worked in both!

Here's how it looks on Heroku:

![bookmarkserver-br3ndonland](img/fsnd02_13-http-heroku-bookmarkserver-br3ndonland01.png "bookmarkserver-br3ndonland")

#### Heroku URLs

- [https://bookmarkserver-br3ndonland.herokuapp.com/](https://bookmarkserver-br3ndonland.herokuapp.com/)
- [https://bookmarkserver-udacity.herokuapp.com/](https://bookmarkserver-udacity.herokuapp.com/)
- [https://guarded-ridge-60265.herokuapp.com/](https://guarded-ridge-60265.herokuapp.com/)

#### Handling more requests

The instructor explains the issue in this section:

> That's right! The basic, built-in http.server.HTTPServer class can only handle a single request at once. The bookmark server tries to fetch every URI that we give it, while it's in the middle of handling the form submission.

It's like an old-school telephone that can only have one call at once. Because it can only handle one request at a time, it can't "pick up" the second request until it's done with the first … but in order to answer the first request, it needs the response from the second.

We needed to build in concurrency support by adding a mixin to the HTTPServer class.

Two additions to bookmark server Python files:

Top of file:

```python
import threading
from socketserver import ThreadingMixIn

class ThreadHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    "This is an HTTPServer that supports thread-based concurrency."
```

Bottom of file:

```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server_address = ('', port)
    httpd = ThreadHTTPServer(server_address, Shortener)
    httpd.serve_forever()
```

```bash
$ git commit -m "Add HTTPServer mixin that supports thread-based concurrency"
$ git push heroku master
```

Worked on my first try!

![bookmarkserver-br3ndonland](img/fsnd02_13-http-heroku-bookmarkserver-br3ndonland02.png "bookmarkserver-br3ndonland")

Still got the error with Google Scholar though.

### Static content and more

> The Web was originally designed to serve documents, not to deliver applications. Even today, a large amount of the data presented on any web site is static content — images, HTML files, videos, downloadable files, and other media stored on disk.

That's a great point. While the internet has scaled remarkably since Vint Cerf and Stephen Crocker first established TCP/IP, it is true that it is largely for static content. We need a new distributed internet, like a p2p bit torrent network for the entire internet (like the one Richard tries to build in Silicon Valley), focused on functional web apps over static web content. The closest thing I've seen to this is the new WebAssembly project, designed to allow use of other languages than JavaScript.

#### What's an Apache or Nginx

Nginx is pronounced "engine x".

#### Routing and load balancing

- *Request routing*, or *reverse proxying*, is when a specialized server allocates web requests to the appropriate backend servers.
- Splitting web requests among multiple servers is called *load balancing.*

#### Concurrent users

- I can definitely understand the challenges here. At any time, there could be thousands of concurrent requests to the servers.
- Requests to the server that have not been resolved are called *in-flight requests*.

> *Question 1 of 2*
> In September 2016, the English Wikipedia received about 250 million page views per day. That's an average of about 2,900 page views every second. Let's imagine that an average page view involves three HTTP queries (the page HTML itself and two images), and that each HTTP query takes 0.1 seconds (or 100 milliseconds) to serve. About how many requests are in flight at any instant?

Let's solve this in Python! The question wasn't really specific enough (what's an instant?), but I was assuming an "instant" was a second. This just makes it simple arithmetic:

```python
$ python
>>> num_requests = 2900 - 3 - 0.1
>>> print(num_requests)
870.0
```

### Caching

- Caching is temporary storage of frequently-accessed information.
- They linked out to [Google Web Fundamentals: HTTP caching](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching)

> *Question 2 of 2*
> Imagine that you have a service that is handling 6,000 requests per second. One-third of its of requests are for the site's CSS file, which doesn't change very often. So browsers shouldn't need to fetch it every time they load the site. If you tell the browser to cache the CSS, 1% of visitors will need to fetch it. After this change, about how many requests will the service be getting?

This was just easy mental math. CSS requests are reduced to `6000 / 3 - 0.01` = 20. The website is still getting the other 4000 requests, plus the 20 for the CSS, so 4020.

> 2,000 requests per second are the CSS file, so the other 4,000 requests are other things. Those 4,000 will be unaffected by this change.
>
> The 2,000 CSS requests will be reduced by 99%, to 20 requests.
>
> This means that after the caching improvement, the service will be getting 4,020 requests per second.

### Cookies

- Cookies ask the browser to retain information.
- Cookies allow users to store website preferences.
- Cookies allow the server to retain information, and implement sessions and logins.

#### How cookies happen

- The server sets the cookie at the first browser request.
- The browser then sends back the cookie with each subsequent request in the HTTP headers.

#### Seeing cookies in your browser

- The cookie's name and content are a key: value store.
- Domain and path set the webpages on which the cookie can be set.

> Browsers don't make it easy to find cookies that have been set, because removing or altering cookies can affect the expected behavior of web services you use. However, it is possible to inspect cookies from sites you use in every major browser. Do some research on your own to find out how to view the cookies that your browser is storing.
>
> > The first two, the cookie's name and content, are also called its key and value. They're analogous to a dictionary key and value in Python — or a variable's name and value for that matter. They will both be sent back to the server. There are some syntactic rules for which characters are allowed in a cookie name; for instance, they can't have spaces in them. The value of the cookie is where the "real data" of the cookie goes — for instance, a unique token representing a logged-in user's session.
>
> The next two fields, Domain and Path, describe the scope of the cookie — that is to say, which queries will include it. By default, the domain of a cookie is the hostname from the URI of the response that set the cookie. But a server can also set a cookie on a broader domain, within limits. For instance, a response from www.udacity.com can set a cookie for udacity.com, but not for com.
>
> The fields that Chrome describes as "Send for" and "Accessible to script" are internally called Secure and HttpOnly, and they are boolean flags (true or false values). The internal names are a little bit misleading. If the Secure flag is set, then the cookie will only be sent over HTTPS (encrypted) connections, not plain HTTP. If the HttpOnly flag is set, then the cookie will not be accessible to JavaScript code running on the page.
>
> Finally, the last two fields deal with the lifetime of the cookie — how long it should last. The creation time is just the time of the response that set the cookie. The expiration time is when the server wants the browser to stop saving the cookie. There are two different ways a server can set this: it can set an Expires field with a specific date and time, or a Max-Age field with a number of seconds. If no expiration field is set, then a cookie is expired when the browser closes.

#### Using cookies in Python

> To set a cookie from a Python HTTP server, all you need to do is set the Set-Cookie header on an HTTP response. Similarly, to read a cookie in an incoming request, you read the Cookie header. However, the format of these headers is a little bit tricky; I don't recommend formatting them by hand. Python's http.cookies module provides handy utilities for doing so.
>
> To create a cookie on a Python server, use the SimpleCookie class. This class is based on a dictionary, but has some special behavior once you create a key within it:
>
> ```python
> from http.cookies import SimpleCookie, CookieError
>
> out_cookie = SimpleCookie()
> out_cookie["bearname"] = "Smokey Bear"
> out_cookie["bearname"]["max-age"] = 600
> out_cookie["bearname"]["httponly"] = True
> ```
>
> Then you can send the cookie as a header from your request handler:
>
> ```python
> self.send_header("Set-Cookie", out_cookie["bearname"].OutputString())
> ```
>
> To read incoming cookies, create a SimpleCookie from the Cookie header:
>
> ```python
> in_cookie = SimpleCookie(self.headers["Cookie"])
> in_data = in_cookie["bearname"].value
> ```
>
> Be aware that a request might not have a cookie on it, in which case accessing the Cookie header will raise a KeyError exception; or the cookie might not be valid, in which case the SimpleCookie constructor will raise http.cookies.CookieError.
>
> > Important safety tip: Even though browsers make it difficult for users to modify cookies, it's possible for a user to modify a cookie value. Higher-level web toolkits, such as Flask (in Python) or Rails (in Ruby) will cryptographically sign your cookies so that they won't be accepted if they are modified. Quite often, high-security web applications use a cookie just to store a session ID, which is a key to a server-side database containing user information.
> >
> > Another important safety tip: If you're displaying the cookie data as HTML, you need to be careful to escape any HTML special characters that might be in it. An easy way to do this in Python is to use the html.escape function, from the built-in html module!
>

#### Exercise: A server that remembers you

##### Set the fields of the cookie

- My initial attempts were unsuccessful. I was repeatedly getting the following:

  ```bash
  $ python test.py
  Testing connecting to the server.
  Connection attempt succeeded.
  Testing GET request.
  GET request without cookie succeeded!
  Testing POST request, looking for redirect & cookie.
  Couldn't communicate with the server. (('Connection aborted.', RemoteDisconnected('Remote end closed connection without response',)))
  If it's running, take a look at its output.
  ```

- The `Traceback` was difficult to interpret, but the two lines I could recognize were

  ```text
    File "cookieserver.py", line 49, in do_POST
    c['domain'] = 'localhost'
  http.cookies.CookieError: Attempt to set a reserved key 'domain'
  ```

- I didn't set the cookie properly. I had

  ```python
        # 1. Set the fields of the cookie.
        #    Give the cookie a value from the 'yourname' variable,
        #    a domain (localhost), and a max-age.
        c['value'] = yourname
        c['domain'] = 'localhost'
        c['max_age'] = 60
  ```

- and the solution had

  ```python
        c['yourname'] = yourname
        c['yourname']['domain'] = 'localhost'
        c['yourname']['max-age'] = 60
  ```

##### Extract and decode the cookie

- Got this one right!

  ```python
                # 2. Extract and decode the cookie.
                #    Get the cookie from the headers and extract its value
                #    into a variable called 'name'.
                in_cookie = SimpleCookie(self.headers['cookie'])
                name = in_cookie['yourname'].value
  ```

- After I modified the cookie setting syntax in 1, the code passed *test.py.*
- When I ran cookieserver.py and navigated to [http://localhost:8000/](http://localhost:8000/) I was able to enter my name, and the name was stored and shown.

  ![Cookie site](img/fsnd02_13-http-heroku-cookies01.png "Cookie site")
  ![Cookie storage](img/fsnd02_13-http-heroku-cookies02.png "Cookie storage")

#### DNS domains and cookie security

> Back in Lesson 1, you used the host or nslookup command to look up the IP addresses of a few different web services, such as Wikipedia and your own localhost. But domain names play a few other roles in HTTP besides just being easier to remember than IP addresses. A DNS domain links a particular hostname to a computer's IP address. But it also indicates that the owner of that domain intends for that computer to be treated as part of that domain.
>
> Imagine what a bad guy could do if they could convince your browser that their server evilbox was part of (say) Facebook, and get you to request a Facebook URL from evilbox instead of from Facebook's real servers. Your browser would send your facebook.com cookies to evilbox along with that request. But these cookies are what prove your identity to Facebook … so then the bad guy could use those cookies to access your Facebook account and send spam messages to all your friends.
>
> In the immortal words of Dr. Egon Spengler: *It would be bad.*
>
> This is just one reason that DNS is essential to web security. If a bad guy can take control of your site's DNS domain, they can send all your web traffic to their evil server … and if the bad guy can fool users' browsers into sending that traffic their way, they can steal the users' cookies and reuse them to break into those users' accounts on your site.

### HTTPS for security

#### What HTTPS does for you

- **Privacy**
- **Authenticity**
- **Integrity**

> When a browser and a server speak HTTPS, they're just speaking HTTP, but over an encrypted connection. The encryption follows a standard protocol called [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security), or TLS for short. TLS provides some important guarantees for web security:
>
> - It keeps the connection **private** by encrypting everything sent over it. Only the server and browser should be able to read what's being sent.
> - It lets the browser **authenticate** the server. For instance, when a user accesses [https://www.udacity.com/](https://www.udacity.com/), they can be sure that the response they're seeing is really from Udacity's servers and not from an impostor.
> - It helps protect the **integrity** of the data sent over that connection — checking that it has not been (accidentally or deliberately) modified or replaced.
>
> Note: TLS is also very often referred to by the older name SSL (Secure Sockets Layer). Technically, SSL is an older version of the encryption protocol. This course will talk about TLS because that's the current standard.

#### Inspecting TLS on your service

> If you deployed a web service on Heroku earlier in this lesson, then HTTPS should already be set up. The URI that Heroku assigned to your app was something like [https://yourappname.herokuapp.com/](https://yourappname.herokuapp.com/).
>
> From there, you can use your browser to see more information about the HTTPS setup for this site. However, the specifics of where to find this information will depend on your browser. You can experiment to find it, or you can check the documentation: Chrome, Firefox, Safari.
>
> > Note: In some browser documentation you'll see references to SSL certificates. These are the same as TLS certificates. Remember, SSL is just the older version of the encryption standard.

#### Keys and certificates

> The server-side configuration for TLS includes two important pieces of data: a private key and a public certificate. The private key is secret; it's held on the server and never leaves there. The certificate is sent to every browser that connects to that server via TLS. These two pieces of data are mathematically related to each other in a way that makes the encryption of TLS possible.
>
> The server's certificate is issued by an organization called a certificate authority (CA). The certificate authority's job is to make sure that the server really is who it says it is — for instance, that a certificate issued in the name of Heroku is actually being used by the Heroku organization and not by someone else.
>
> The role of a certificate authority is kind of like getting a document notarized. A notary public checks your ID and witnesses you sign a document, and puts their stamp on it to indicate that they did so.

#### How does TLS assure privacy

> The data in the TLS certificate and the server's private key are mathematically related to each other through a system called public-key cryptography. The details of how this works are way beyond the scope of this course. The important part is that the two endpoints (the browser and server) can securely agree on a shared secret which allows them to scramble the data sent between them so that only the other endpoint — and not any eavesdropper — can unscramble it.

#### How does TLS assure authentication

> A server certificate indicates that an encryption key belongs to a particular organization responsible for that service. It's the job of a certificate authority to make sure that they don't issue a cert for (say) udacity.com to someone other than the company who actually runs that domain.
>
> But the cert also contains metadata that says what DNS domain the certificate is good for. The cert in the picture above is only good for sites in the .herokuapp.com domain. When the browser connects to a particular server, if the TLS domain metadata doesn't match the DNS domain, the browser will reject the certificate and put up a big scary warning to tell the user that something fishy is going on.

#### How does TLS assure integrity

Every request and response sent over a TLS connection is sent with a [message authentication code](https://en.wikipedia.org/wiki/Message_authentication_code) (MAC) that the other end of the connection can verify to make sure that the message hasn't been altered or damaged in transit.

Question 3 of 4

> Suppose that an attacker were able to trick your browser into sending your udacity.com requests to the attacker's server instead of Udacity's real servers. What could the attacker do with that evil ability?

- Yes: Steal your udacity.com cookies, use them to log into the real site as you, and post terrible spam to the discussion forums.
- Yes: Make this course appear with terrible images in it instead of nice friendly ones.
- No: access other sites like Gmail or Facebook
- No: cause your computer to explode

> If your browser believes the attacker's server is udacity.com, it will send your udacity.com authentication cookies to the attacker's server. They can then put those cookies in their own web client and masquerade as you when talking to the real site. Also, if your browser is fetching content from the attacker's server, the attacker can put whatever they want in that content. They could even forward most of the content from the real server.
>
> However, compromising Udacity's site would not allow an attacker to break into your Gmail or Facebook accounts, and fortunately it wouldn't let the attacker blow up your computer either.
>
> HTTPS only protects your data in transit. It doesn't protect it from an attacker who has taken over your computer, or the computer that's running your service.

### Beyond GET and POST

Web APIs use several other methods.

#### PUT for creating resources

- Client sends URI and content to create to server
- Server responds with `201 Created` status code if successful
- A GET request to the URI shows the created content
- PUT must be done in application code (JavaScript).
- Most file uploads are actually done with POST requests, which only require HTTP. See [Mozilla](https://developer.mozilla.org/en-US/docs/Using_files_from_web_applications).

#### DELETE for deleting

- DELETE requests usually require authentication.
- After a successful DELETE requests, further requests to the URI will yield 404 Not Found.

#### PATCH for making changes

- PATCH is relatively new
- PATCH is like a Git commit-it updates a resource
- PATCH requests are not necessarily standardized, but there are some standard protocols, like [JSON Patch](http://jsonpatch.com/) and [JSON Merge Patch](https://tools.ietf.org/html/rfc7386).

#### HEAD, OPTIONS, TRACE for debugging

- HEAD is like a GET request for headers.
- OPTIONS explain available features of the server.
- TRACE echoes what the server received from the client, but may be disabled for security reasons.

#### Great responsibility

- Generally HTTP requests are used for their expected behavior, but not always.
- [In 2006](http://thedailywtf.com/articles/The_Spider_of_Doom), a government employee copied and pasted content into a webpage, including a link to edit the page (so editing and deleting were possible with GET requests). Google's webcrawling spider followed the link, bypassing cookies and JavaScript, and deleted the contents of the website.

#### The standard tells all

For much more about HTTP methods, consult the [HTTP standards documents](https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html).

### New developments in HTTP

#### HTTP/0.9

- 1991
- GET requests
- Responses in HTML

#### HTTP/1.0

- 1996
- Headers
- POST requests
- Status codes
- Content-type

#### HTTP/1.1

- Cache controls
- Range requests (resuming downloads)
- Transfer encodings (compression)
- Persistent connection
- Chunked messages
- Host header (multiple sites per IP address)

#### HTTP/2

- Multiplexing
- Better compression
- Server push
- Newest version of HTTP
- Based on protocol work done at Google, named SPDY (speedy)
- Python libraries not ready yet.

##### HTTP/2 demos

- We did the [Gophertiles demo](https://http2.golang.org/gophertiles) from the Go language.
- Others
  - [http://www.http2demo.io/](http://www.http2demo.io/)
  - [https://http2.akamai.com/demo](https://http2.akamai.com/demo)

#### Exercise: multiple connections

- We ran *Parallelometer.py* and navigated to [http://localhost:8000/](http://localhost:8000/).
- Most browsers can open up to six connections to the same server.

#### Multiplexing

> But if you're requesting hundreds of different tiny files from the server — as in this demo or the Gophertiles demo — it's kind of limiting to only be able to fetch six at a time. This is particularly true when the latency (delay) between the server and browser gets high. The browser can't start fetching the seventh image until it's fully loaded the first six. The greater the latency, the worse this affects the user experience.
>
> HTTP/2 changes this around by multiplexing requests and responses over a single connection. The browser can send several requests all at once, and the server can send responses as quickly as it can get to them. There's no limit on how many can be in flight at once.
>
> And that's why the Gophertiles demo loads much more quickly over HTTP/2 than over HTTP/1.

#### Server Push

- Under HTTP/2, servers are now able to pre-emptively send multiple associated assets, such as sending *style.css- along with a request for *index.html*.

#### Encryption

- HTTPS encryption is not officially required in HTTP/2, but most browsers do it anyway.

#### Many more features

[https://http2.github.io/faq/](https://http2.github.io/faq/)

### Keep learning

#### Resources

- [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- HTTP/1.1 standards, starting at [RFC 7230](https://tools.ietf.org/html/rfc7230).
- [HTTP/2 standards documents](https://http2.github.io/faq/)
- [Let's Encrypt](https://letsencrypt.org/) helps learn about HTTPS.
- [HTTP Spy](https://chrome.google.com/webstore/detail/http-spy/agnoocojkneiphkobpcfoaenhpjnmifb?hl=en) is a Chrome extension that shows headers and request information.

## Feedback

I didn't feel like the instructor clearly led us into the code for each exercise. I would compare it with Kunal's instruction in the foundational Python work in Part 1 of the Full Stack Web Developer Nanodegree program. It was also challenging, but Kunal did an excellent job of carefully leading us through the exercises, so at the end, I naturally arrived at the solutions to the problem sets on my own.

[(Back to TOC)](#table-of-contents)