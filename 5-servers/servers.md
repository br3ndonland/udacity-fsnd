# Linux server configuration

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Udacity Full Stack Web Developer Nanodegree program

Brendon Smith

[br3ndonland](https://github.com/br3ndonland)

From free [Configuring Linux Web Servers Udacity course](https://classroom.udacity.com/courses/ud299)

## Lesson notes

### Comments

- From free [Configuring Linux Web Servers Udacity course](https://classroom.udacity.com/courses/ud299).
- The lessons for this section were brief. There was only one course and I watched the videos in in about an hour.

### Distributions

- RedHat: Large enterprise/corporate customers
- Ubuntu: Ease of use on servers, desktops, laptops
- Linux Mint: Desktop users with proprietary media support
- CoreOS: Clustered, containerized deployment of apps
- Debian: The instructor Mike Wales also mentioned that Debian is "rock solid."
- Check out [distrowatch](https://distrowatch.com/).

### Vagrant Commands

> We’re now ready to get started working within our Linux virtual machine. If your download hasn’t completed from the initial setup, go ahead and take a break and come back when that has completed. You won’t be able to make further progress until the virtual machine is up and running as much of the course will take place within this environment.
>
> Before we access our machine, let’s quickly review a few commands that vagrant provides to make managing your virtual machines much simpler. Remember, your vagrant machine lives within this specific folder on your computer so make sure you’re within that same folder your created earlier; otherwise these commands won’t work as expected.
>
> 1. Type `vagrant status`
>    - This command will show you the current status of the virtual machine. It should currently read “default running (virtualbox)” along with some other information.
>2. Type `vagrant suspend`
>    - This command suspends your virtual machine. All of your work is saved and the machine is put into a “sleep mode” of sorts. The machines state is saved and it’s very quick to stop and start your work. You should use this command if you plan to just take a short break from your work but don’t want to leave the virtual machine running.
>3. Type `vagrant up`
>    - This gets your virtual machine up and running again. Notice we didn’t have to re-download the virtual machine image, since it’s already been downloaded.
>4. Type `vagrant ssh`
>    - This command will actually connect to and log you into your virtual machine. Once done you will see a few lines of text showing various performance statistics of the virtual machine along with a new command line prompt that reads vagrant@vagrant-ubuntu-trusty-64:~$
>
>Here are a few other important commands that we’ll discuss but you **do not** need to practice at this time:
>
>1. `vagrant halt`
>    - This command halts your virtual machine. All of your work is saved and the machine is turned off - think of this as “turning the power off”. It’s much slower to stop and start your virtual machine using this command, but it does free up all of your RAM once the machine has been stopped. You should use this command if you plan to take an extended break from your work, like when you are done for the day. The command vagrant up will turn your machine back on and you can continue your work.
>2. `vagrant destroy`
>    - This command destroys your virtual machine. Your work is not saved, the machine is turned off and forgotten about for the most part. Think of this as formatting the hard drive of a computer. You can always use vagrant up to relaunch the machine but you’ll be left with the baseline Linux installation from the beginning of this course. You should not have to use this command at any time during this course unless, at some point in time, you perform a task on the virtual machine that makes it completely inoperable.

### Apache servers

> When Apache receives a request it has a number of ways it can respond. What you’ve seen thus far is the simplest method of operation, Apache just returns a file requested or the `index.html` file if no file is defined within the URL.
>
> But, Apache can do so much more! You’ll now configure Apache to hand-off certain requests to an application handler - mod\_wsgi. The first step in this process is to install mod\_wsgi: `sudo apt-get install libapache2-mod-wsgi`.
>
> You then need to configure Apache to handle requests using the WSGI module. You’ll do this by editing the `/etc/apache2/sites-enabled/000-default.conf` file. This file tells Apache how to respond to requests, where to find the files for a particular site and much more. You can read up on everything this file can do within the [Apache documentation](https://httpd.apache.org/docs/2.2/configuring.html).
>
> For now, add the following line at the end of the `<VirtualHost *:80>` block, right before the closing `</VirtualHost>` line: `WSGIScriptAlias / /var/www/html/myapp.wsgi`
>
> Finally, restart Apache with the `sudo apache2ctl restart` command.
> You might get a warning saying "Could not reliably determine the server's fully qualified domain name". If you do, don't worry about it. Check out [this AskUbuntu thread](https://askubuntu.com/questions/256013/apache-error-could-not-reliably-determine-the-servers-fully-qualified-domain-n) for a discussion of the cause of this message.
>
> [WSGI](http://wsgi.readthedocs.org/en/latest/) is a specification that describes how a web server communicates with web applications. Most if not all Python web frameworks are WSGI compliant, including [Flask](http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/) and [Django](https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/); but to quickly test if you have your Apache configuration correct you’ll write a very basic WSGI application.
>
> You just defined the name of the file you need to write within your Apache configuration by using the `WSGIScriptAlias` directive. Despite having the extension `.wsgi`, these are just Python applications. Create the `/var/www/html/myapp.wsgi` file using the command `sudo nano /var/www/html/myapp.wsgi`. Within this file, write the following application:
>
> ```text
> def application(environ, start_response):
>     status = '200 OK'
>     output = 'Hello Udacity!'
>
>     response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
>     start_response(status, response_headers)
>
>     return [output]
>
> ```
>
> This application will simply print return `Hello Udacity!` along with the required HTTP response headers. After saving this file you can reload `http://localhost:8080` to see your application run in all its glory!