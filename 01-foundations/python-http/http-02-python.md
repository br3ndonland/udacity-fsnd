# The Web from Python

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

br3ndonland

[HTTP & Web Servers](https://www.udacity.com/course/http-web-servers--ud303)

Lesson 2. The Web from Python

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Lesson](#lesson)
  - [Python's `http.server`](#pythons-httpserver)
  - [HTML and forms](#html-and-forms)
  - [GET and POST](#get-and-post)
  - [A server for POST](#a-server-for-post)
  - [Exercise: Messageboard, part one](#exercise-messageboard-part-one)
  - [Exercise: Messageboard, part two](#exercise-messageboard-part-two)
  - [POST-Redirect-GET](#post-redirect-get)
  - [Making Requests](#making-requests)
  - [Using a JSON API](#using-a-json-api)
  - [The Bookmark Server](#the-bookmark-server)

## Lesson

### Python's `http.server`

#### Intro

We got started at the end of the previous lesson by cloning a repo:

```bash
$ cd /Users/br3ndonland/Dropbox/Computing/udacity-fsnd/files/02_tools
br3ndonland (master *) 02_tools
$ git clone https://github.com/udacity/course-ud303
Cloning into 'course-ud303'...
remote: Counting objects: 401, done.
remote: Total 401 (delta 0), reused 0 (delta 0), pack-reused 401
Receiving objects: 100% (401/401), 56.75 KiB | 1.09 MiB/s, done.
Resolving deltas: 100% (151/151), done.
br3ndonland (master *) 02_tools
$ cd course-ud303
br3ndonland (master) course-ud303
$ git remote remove origin
br3ndonland (master) course-ud303
$ ls
CODEOWNERS Lesson-1 Lesson-2 Lesson-3 README.md
```

> In the last lesson, you used the built-in demo web server from the Python `http.server` module. But the demo server is just that — a demonstration of the module's abilities. Just serving static files out of a directory is hardly the only thing you can do with HTTP. In this lesson, you'll build a few different web services using `http.server`, and learn more about HTTP at the same time. You'll also use another module, `requests`, to write code that acts as an HTTP client.
>
> These modules are written in object-oriented Python. You should already be familiar with creating class instances, defining subclasses, and defining methods on classes. If you need a refresher on the Python syntax for these object-oriented actions, you might want to browse the [Python tutorial on classes](https://docs.python.org/3/tutorial/classes.html) or take another look at [the sections on classes in our Programming Foundations with Python course](https://classroom.udacity.com/courses/ud036).
>
> In the exercises in this lesson, you'll be writing code that runs on your own computer. You'll need the [starter code](https://github.com/udacity/course-ud303) that you downloaded at the end of the last lesson, which should be in a directory called course-ud303. And you'll need your favorite text editor to work on these exercises.

#### Servers and handlers

> Web servers using `http.server` are made of two parts: the `HTTPServer` class, and a request handler class. The first part, the `HTTPServer` class, is built in to the module and is the same for every web service. It knows how to listen on a port and accept HTTP requests from clients. Whenever it receives a request, it hands that request off to the second part — a request handler — which is different for every web service.
>
> Here's what your Python code will need to do in order to run a web service:
>
> - Import `http.server`, or at least the pieces of it that you need.
> - Create a subclass of `http.server.BaseHTTPRequestHandler`. This is your **handler class**.
> - Define a method on the handler class for each **HTTP verb** you want to handle. (The only HTTP verb you've seen yet in this course is `GET`, but that will be changing soon.)
>   - The method for `GET` requests has to be called `do_GET`.
>   - Inside the method, call built-in methods of the handler class to read the HTTP request and write the response.
> - Create an instance of `http.server.HTTPServer`, giving it your handler class and server information — particularly, the port number.
> - Call the `HTTPServer` instance's `run_forever` method.
>
> Once you call the HTTPServer instance's `run_forever` method, the server does that — it runs forever, until stopped. Just as in the last lesson, if you have a Python server running and you want to stop it, type Ctrl-C into the terminal where it's running. (You may need to type it two or three times.)

#### Exercise: The hello server

```bash
$ cd /Users/br3ndonland/Dropbox/Computing/udacity-fsnd/files/02_tools/course-ud303/Lesson-2/0_HelloServer
$ python helloserver.py
```

Navigate to [http://localhost:8000/](http://localhost:8000/) in a web browser.

##### A tour of the hello server

> Open up HelloServer.py in your text editor. Let's take a look at each part of this code, line by line.
> ```python
> from http.server import HTTPServer, BaseHTTPRequestHandler
> ```
> The http.server module has a lot of parts in it. For now, this program only needs these two. I'm using the from syntax of import so that I don't have to type http.server over and over in my code.
> ```python
> class HelloHandler(BaseHTTPRequestHandler):
>     def do_GET(self):
> ```
> This is the handler class. It inherits from the BaseHTTPRequestHandler parent class, which is defined in http.server. I've defined one method, do_GET, which handles HTTP GET requests. When the web server receives a GET request, it will call this method to respond to it.
>
> As you saw in the previous lesson, there are three things the server needs to send in an HTTP response: a status code, some headers, and the response body. The handler parent class has methods for doing each of these things. Inside do_GET, I just call them in order.
> ```python
>         # First, send a 200 OK response.
>         self.send_response(200)
> ```
> The first thing the server needs to do is send a 200 OK status code; and the send_response method does this. I don't have to tell it that 200 means OK; the parent class already knows that.
> ```python
>         # Then send headers.
>         self.send_header('Content-type', 'text/plain; charset=utf-8')
>         self.end_headers()
> ```
> The next thing the server needs to do is send HTTP headers. The parent class supplies the send_header and end_headers methods for doing this. For now, I'm just having the server send a single header line — the Content-type header telling the client that the response body will be in UTF-8 plain text.
> ```python
>         # Now, write the response body.
>         self.wfile.write("Hello, HTTP!\n".encode())
> ```
> The last part of the do_GET method writes the response body.
>
> The parent class gives us a variable called self.wfile, which is used to send the response. The name wfile stands for writeable file. Python, like many other programming languages, makes an analogy between network connections and open files: they're things you can read and write data to. Some file objects are read-only; some are write-only; and some are read/write.
>
> self.wfile represents the connection from the server to the client; and it is write-only; hence the name. Any binary data written to it with its write method gets sent to the client as part of the response. Here, I'm writing a friendly hello message.
>
> What's going on with .encode() though? We'll get to that in a moment. Let's look at the rest of the code first.
> ```python
> if __name__ == '__main__':
>     server_address = ('', 8000)  # Serve on all addresses, port 8000.
>     httpd = HTTPServer(server_address, HelloHandler)
>     httpd.serve_forever()
> ```
> This code will run when we run this module as a Python program, rather than importing it. The HTTPServer constructor needs to know what address and port to listen on; it takes these as a tuple that I'm calling server_address. I also give it the HelloHandler class, which it will use to handle each incoming client request.
>
> At the very end of the file, I call serve_forever on the HTTPServer, telling it to start handling HTTP requests. And that starts the web server running.

##### End of the tour

> That's all that's involved in writing a basic HTTP server in Python. But the hello server isn't very interesting. It doesn't even do as much as the demo server. No matter what query you send it, all it has to say is hello. (Try it: [http://localhost:8000/goodbye](http://localhost:8000/goodbye))
>
> In the rest of this lesson, we'll build servers that do much more than say hello.

#### What about `encode()`

> If you want to send a string over the HTTP connection, you have to `encode` the string into a `bytes` object. The `encode` method on strings translates the string into a bytes object, which is suitable for sending over the network. There is, similarly, a decode method for turning bytes objects into strings.

See the [Python Unicode HOWTO](https://docs.python.org/3.6/howto/unicode.html) for more.

#### The echo server

Creating a server that reads request information and echoes it back.

From *course-ud303/Lesson-2/1_EchoServer/README.md*:

> In this exercise, you'll take the code from the *hello server- and change
> it into the *echo server*.  This new server will also listen on port 8000,
> but it will respond to GET requests by repeating back ("echoing") the text
> of the request path.
>
> See `EchoServer.py` for starter code.
>
> To test your code, you'll need two terminals open.  In one of them, run the
> server (with `python EchoServer.py`).  You can then access it from your
> browser, for instance at [http://localhost:8000/GoodMorningHTTP](http://localhost:8000/GoodMorningHTTP).  In the
> other terminal, run the test script provided (`python test.py`).  The test
> script will send a request to the server and tell you whether it worked.

We had to modify the HelloHandler module to return the path instead of just "Hello, HTTP!\n". Creation of the echo server required a one-line change at the end of do_GET:

```python
self.wfile.write(self.path[1:].encode())
```

> What I'm doing here is taking the path (for instance "/bears"), using a string slice to remove the first character (which is always a slash), and then encoding the resulting string into bytes, then writing that to the HTTP response body.

I was close on my first try. I just needed to add `self`. Note that I was actually able to make my code more concise by removing the `[1:]`. I didn't need to slice the string.

```python
self.wfile.write(self.path.encode())
```

Run the server in the terminal with

```bash
cd /Users/br3ndonland/Dropbox/Computing/udacity-fsnd/files/02_tools/course-ud303/Lesson-2/1_EchoServer
python EchoServer.py
```

If you attempt to run two servers on the same port,
> The new server exits. Under normal conditions, only one program on your computer can listen on a particular port at the same time. If you want to have both servers running, you have to change the port number from 8000 to something else.

#### Queries and quoting

##### Unpacking query parameters

Queries are entered after a ? in the URI.

The URI [https://www.google.com/search?q=gray+squirrel&tbm=isch](https://www.google.com/search?q=gray+squirrel&tbm=isch) will be sent to the server as an HTTP request:

```text
GET /search?q=gray+squirrel&tbm=isch HTTP/1.1
Host: www.google.com
```

The `urllib.parse` Python library can do exactly that, parse URLs.

I followed along with the demo from the course notes:

```python
>>> from urllib.parse import urlparse, parse_qs
>>> address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
>>> parts = urlparse(address)
>>> print(parts)
ParseResult(scheme='https', netloc='www.google.com', path='/search', params='', query='q=gray+squirrel&tbm=isch', fragment='')
>>> print(parts.query)
q=gray+squirrel&tbm=isch
>>> query = parse_qs(parts.query)
>>> query
{'q': ['gray squirrel'], 'tbm': ['isch']}
```

*What does `parse_qs('texture=fuzzy&animal=gray+squirrel')` return?*

The dictionary `{'texture': ['fuzzy'], 'animal': ['gray squirrel']}`

##### URL quoting

- Spaces can't be sent in HTTP requests, so they are translated into an appropriate format. This is called URL quoting, URL encoding, or URL escaping.
- [Docs for `urllib.parse.quote`](https://docs.python.org/3/library/urllib.parse.html#url-quoting)

### HTML and forms

- Run *Lesson-2/1_EchoServer/EchoServer.py* in the terminal
- Open *Lesson-2/2_HTMLForms/LoginPage.html* in a web browser
- Submit user name and password
- Query string is echoed in the output.
- Of course, we now have more advanced ways of inputting passwords.

### GET and POST

- GET puts all form fields into the URI that is sent to the server. Good for search strings, not for more complex actions.
- POST is better when altering or creating a resource.

#### Idempotence

> Vocabulary word of the day: idempotent. An action is idempotent if doing it twice (or more) produces the same result as doing it once. "Show me the search results for 'polar bear'" is an idempotent action, because doing it a second time just shows you the same results. "Add a polar bear to my shopping cart" is not, because if you do it twice, you end up with two polar bears.
>
> POST requests are not idempotent. If you've ever seen a warning from your browser asking you if you really mean to resubmit a form, what it's really asking is if you want to do a non-idempotent action a second time.
>
> (Important note if you're ever asked about this in a job interview: idempotent is pronounced like "eye-dem-poe-tent", or rhyming with "Hide 'em, Joe Tent" — not like "id impotent".)
>
> Adding zero to a number is idempotent, since you can add zero as many times as you want and the original number is unchanged. Adding five to a number is not idempotent, because if you do it twice you'll have added ten. Setting a variable to the value 5 is idempotent: doing it twice is the same as doing it once. Looking up an entry in a dictionary doesn't alter anything, so it's idempotent.

#### Serve a POST request

- As before, run `ncat -l 9999` in a terminal window.
- Then, open *PostForm.html*, enter some text in each box, and click "Do a thing!"
- Return to the terminal and look at the output. The output contains the information that was submitted in the boxes.
- The search string is not added to the URI with POST.
- Note that HTTP headers are case-insensitive.

```bash
$ ncat -l 9999
POST / HTTP/1.1
Host: localhost:9999
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 29
Cookie: username-localhost-8888="2|1:0|10:1512181984|23:username-localhost-8888|44:YWViZjc3MWNjODFlNGNjYzkxZGQzNzQ1MmFiNTM3NjA=|30e4a35d5fcdaa19aaee5e0ce26295b4339722f486a4d5654f3adcb4cc7c8263"; _xsrf=2|b64b3afa|8c30f7b40d004ed1ad52b6edefd9c7aa|1512181984
DNT: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1

magic=DNA&secret=double+helix
```

### A server for POST

We built a message board server with [Requests](http://docs.python-requests.org/en/master/).

When I first used Requests for the profanity checker mini-project (FSND Part 01, Lesson 08), I didn't understand it very well because I didn't understand HTTP. It's good to revisit Requests now.

I already had Requests installed via Anaconda.

> Yes! We'll be using a GET request to display the messageboard's existing contents, and POST to update the contents by creating new messages. Creating new messages is not idempotent — we don't want duplicates.

#### POST handlers read the request body

The *EchoServer.py* had a `do_GET` "handler" class in it. We will use `do_POST` now. `self.rfile.read` reads the request body. `self.wfile`, which we have already seen, writes the response. The length of the request body is sent with the `Content-Length` header.

#### Headers are strings (or missing)

`self.headers` is an object like a Python dictionary.

This Python code will go in the `do_POST` handler class. `length` stores the length of the request body, and `data` reads it.

```python
length = int(self.headers.get('Content-length', 0))
data = self.rfile.read(length).decode()
```

`urllib.parse.parse_qs` can then be used to extract the POST parameters.

### Exercise: Messageboard, part one

#### Setup

The starter code for this exercise is in *Lesson-2/3_MessageboardPartOne*. It's an echo server for post requests.

*Build the code:*

1. *Find the length of the request data.- This was easy. I just used the code for the `length` variable above.
2. *Read the correct amount of request data.- Used the `data` variable.
3. *Extract the "message" field from the request data.- We went through the use of the `urllib.parse.parse_qs` module in the [Queries and quoting](#queries-and-quoting) section, so I reviewed that material. The `self.wfile.write(message.encode())` line references a variable `message`, so I started by creating a variable `message` and calling `parse_qs`.

*Run the code:*

Same as for the echo server:

1. Start the Python HTTP server:

    ```bash
    cd ../3_MessageboardPartOne
    python MessageboardPartOne.py
    ```

2. In a second terminal window, run the test file to check the code:

    ```bash
    cd ../3_MessageboardPartOne
    python test.py
    ```

3. Open *Messageboard.html* in a web browser.

#### Troubleshooting

- I first had `message = parse_qs(data)`. The server terminal window kept giving me `AttributeError: 'MessageHandler' object has no attribute 'parse_qs'`. I realized I had to restart the server every time I changed *MessageboardPartOne.py*. After a Cntrl+C restart, I got:

  ```bash
  $ python test.py
  Testing connecting to the server.
  Connection attempt succeeded.
  Testing POST request.
  The server sent a 200 OK response, but the content differed.
  I expected 'Hi there!' but it sent ''.
  ```

- I then got a different error: `AttributeError: 'dict' object has no attribute 'encode'`.
- I checked the solution at this point. I was almost there! I just needed to add `["message"][0]`: `message = parse_qs(data)["message"][0]`.
  - There is a line in *test.py- that helped me understand this:
    ```python
    def test_POST():
    '''The server should accept a POST and return the "message" field.'''
        print("Testing POST request.")
        mesg = random.choice(["Hi there!", "Hello!", "Greetings!"])
        uri = "http://localhost:8000/"
        try:
            r = requests.post(uri, data = {'message': mesg})
    ```

  - *TODO: WHY?- I still don't totally understand how he got there.
- I then opened *Messageboard.html* in a web browser, entered some text, clicked post, and it showed up on the webpage.

### Exercise: Messageboard, part two

- Handle POST requests and serve the webpage from a single Python file.
- This reminded me of project 1 (The Python Web Server), so I reviewed the code from that, and added the HTML from *Messageboard.html- as a variable in single quotes.
- The Udacity code needed docstrings for the class and function definitions, and an extra line break after the class definition.

*Run the code:*

1. Start the Python HTTP server:
    ```bash
    cd ../4_MessageboardPartTwo
    python MessageboardPartTwo.py
    ```
2. In a second terminal window, run the test file to check the code:
    ```bash
    cd ../3_MessageboardPartTwo
    python test.py
    ```
3. Navigate to [http://localhost:8000/](http://localhost:8000/) in a web browser.

On my first try, the browser just showed the HTML code itself. I simply needed to change the request from 'text/plain' to 'text/html'. Success!

> This particular server doesn't look at the URI path at all. Any GET request will get the form. Any POST request will save a message.

### POST-Redirect-GET

![Post-Redirect-Get](img/fsnd02_12-http-python-screenshot01.png)

- Client POSTs to server
- Server replies with a 303 redirect
- Client GETs the updated resource

Same steps to run the code as Messageboard part 2:

1. Start the Python HTTP server:

    ```bash
    cd ../4_MessageboardPartTwo
    python MessageboardPartTwo.py
    ```

2. In a second terminal window, run the test file to check the code:

    ```bash
    cd ../3_MessageboardPartTwo
    python test.py
    ```

3. Navigate to [http://localhost:8000/](http://localhost:8000/) in a web browser.

Again, I almost got it on my first try. The thing I didn't get was putting together the form and response. I tried to combine the variables with

```python
response = messageboard_form + memory
```

which returned the following error (visible in the terminal window in which I started the server)

```text
handle_one_request
    method()
  File "MessageboardPartThree.py", line 65, in do_GET
    response = messageboard_form + memory
TypeError: must be str, not list
```

The solution code had

```python
mesg = form.format("\n".join(memory))`
```

I need to review how to append variables.

### Making Requests

- Finally moving to the Requests module!
- The instructor first had us look at the [Requests quickstart docs](http://docs.python-requests.org/en/master/user/quickstart/). Already had the site open!
- *How would you send a GET request to the messageboard server?*
  - `requests.get("http://localhost:8000/")`
  - The `requests` function for performing GET requests is `requests.get`, and it takes the URI as an argument.
- Requests return a `response` object:

  ```bash
  $ python
  Python 3.6.3 |Anaconda, Inc.| (default, Oct  6 2017, 12:04:38)
  [GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import requests
  >>> a = requests.get('http://www.udacity.com')
  >>> a
  <Response [200]>
  >>> type(a)
  <class 'requests.models.Response'>
  ```

> *Use the documentation for the requests module to answer this question! If you have a response object called r, how can you get the response body — for instance, the HTML that the server sent?*
>
> Both, but they're different. `r.content` is a bytes object representing the literal binary data that the server sent. `r.text` is the same data but interpreted as a str object, a Unicode string.
>
> *Using the requests module, try making GET requests to nonexistent sites or pages, e.g. `http://bad.example.com` or `http://google.com/NotExisty`.*

```bash
python
>>> uri = "http://google.com/NotExisty"
>>> r = requests.get(uri)
>>> print(r.status_code)
```

```bash
>>> no_uri = 'http://bad.example.com/'
>>> r_no_uri = requests.get(no_uri)
```

> If the requests.get call can reach an HTTP server at all, it will give you a Response object. If the request failed, the Response object has a status_code data member — either 200, or 404, or some other code.
>
> But if it wasn't able to get to an HTTP server, for instance because the site doesn't exist, then requests.get will raise an exception.
>
> However: Some Internet service providers will try to redirect browsers to an advertising site if you try to access a site that doesn't exist. This is called [DNS hijacking](https://en.wikipedia.org/wiki/DNS_hijacking), and it's nonstandard behavior, but some do it anyway. If your ISP hijacks DNS, you won't get exceptions when you try to access nonexistent sites. Standards-compliant DNS services such as [Google Public DNS](https://developers.google.com/speed/public-dns/) don't hijack.

### Using a JSON API

#### JSON Intro

- JSON is based on JavaScript syntax, and often used for APIs.
- Access Star Wars API:

  ```bash
  >>> a = requests.get('http://swapi.co/api/people/1/')
  >>> a.json()['name']
  'Luke Skywalker'
  ```

- We used the website [http://uinames.com/api](http://uinames.com/api) to generate fake user information. It takes two query parameters: `ext`, providing extended info, and `region`, specifying desired country.

#### Exercise: Use JSON with UINames.com

- On my first try, I tried putting the JSON field names directly within the brackets like

  ```python
  return "My name is {'name'} {'surname'} and the PIN on my card is {'pin'}.".format()
  ```

- On the second try, I moved the JSON field names into `format()`:

  ```python
  return "My name is {} {} and the PIN on my card is {}.".format(
      'name', 'surname', 'pin')
  ```

- This actually passed when I ran `python test.py` in the terminal, but it wasn't correct, because it was just outputting those literal titles. I needed to extract the data from `r.json()`. This can be done in two ways:

  ```python
  # no added variable
  r.json()['name'], r.json()['surname'], r.json()['credit_card']['pin']
  # add r.json as variable
  j = r.json()
  j['name'], j['surname'], j['credit_card']['pin']
  ```

### The Bookmark Server

![Bookmark server diagram](img/fsnd02_12-http-python-screenshot02.png)

We made a URL-shortening web server, like TinyURL or Google's goo.gl.

The server does three things, depending on the request received:

1. GET request to the `/` path: display a form with two fields for long and short URLs, and submit POST request to server when user submits form
2. POST:
    1. Look for form fields in request body
    2. Check URI with `requests.get`
        1. Return 200 if successful
        2. Return 404 if unsuccessful
        3. Return 400 if either form field is missing
3. GET request to a short URI: look up long URI and serve redirect.

Steps:

1. Start the Python HTTP server:
    ```bash
    cd ../4_MessageboardPartTwo
    python MessageboardPartTwo.py
    ```
2. In a second terminal window, run the test file to check the code:
    ```bash
    cd ../3_MessageboardPartTwo
    python test.py
    ```
3. Navigate to [http://localhost:8000/](http://localhost:8000/) in a web browser.

I struggled with this a bit, but I basically got it without checking the solution. There were just a few differences:

CheckURI function:

I had

```python
def CheckURI(uri, timeout=5):
    '''Check whether this URI is reachable, i.e. does it return a 200 OK?

    This function returns True if a GET request to uri returns a 200 OK, and
    False if that GET request returns any other response, or doesn't return
    (i.e. times out).
    '''
    r = requests.get(uri)

    if r.status_code == 200:
        return True
    else:
        return False
```

The solution had

```python
def CheckURI(uri, timeout=5):
    '''Check whether this URI is reachable, i.e. does it return a 200 OK?

    This function returns True if a GET request to uri returns a 200 OK, and
    False if that GET request returns any other response, or doesn't return
    (i.e. times out).
    '''
    try:
        r = requests.get(uri, timeout=timeout)
        # If the GET request returns, was it a 200 OK?
        return r.status_code == 200
    except requests.RequestException:
        # If the GET request raised an exception, it's not OK.
        return False
```

I added each to different cells of a Jupyter Notebook and ran them. They both worked.

do_GET function:

I had `memory[name]` in quotes as a string, but it needed to be unquoted.

I ran my server, navigated to [http://localhost:8000/](http://localhost:8000/) and the server sort of worked! My code wouldn't pass *test.py- and although the website worked, I was getting some command-line errors:

```text
127.0.0.1 - - [14/Dec/2017 17:29:12] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [14/Dec/2017 17:29:12] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [14/Dec/2017 17:29:12] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [14/Dec/2017 17:30:25] "POST / HTTP/1.1" 303 -
127.0.0.1 - - [14/Dec/2017 17:30:25] "GET / HTTP/1.1" 200 -
^CTraceback (most recent call last):
  File "bookmarkserver-br3ndonland.py", line 112, in <module>
    httpd.serve_forever()
  File "/Users/br3ndonland/anaconda/lib/python3.6/socketserver.py", line 236, in serve_forever
    ready = selector.select(poll_interval)
  File "/Users/br3ndonland/anaconda/lib/python3.6/selectors.py", line 376, in select
    fd_event_list = self._poll.poll(timeout)
```

[(Back to TOC)](#table-of-contents)