WEB SERVER

Whats a child process
-> this is a process created by another process.
the creator process is called the parent process.
The child process can start or stop at will without affecting the parent process.
-> to view all running proccesses along with child processes in atree we use this command: ps axf

HOW THE WEB WORKS
Clients and Servers

-> This are comps connected to the internet
-> clients are basically users connetced to the internet and accessing the web using software like chrome, firefox, microsoft
-> Servers are computers that store webpages, sites or apps.
-> Along with this we have:
       . Internet - this allows one to send and receive data on the web.
       . TCP/IP - transmission controlprotocal and internet protocal are communication protocal that define how data should travel across the internet.
       . DNS - domain name system is like an address book for website.when you type a web address in the browser, the browser looks at the dns to find the website's ip address before it can retrieve the website.
       . HTTP - Hypertext transfer protocal is an application protocal that defines a language for the client and servers to speak to each other.
       . Component file - a website is made up of different files, code files [HTML, CSS, JavaScript] and Assets collective name for all the other things that make up a webpage eg: images, videos, word docs and pdfs


NGINX
-> is a webserver that can also be used as a revers proxy, load balancer, mail proxy and HTTP cache

-> when using the ngix webserver, server blocks can be used to encapsulate configuration details and host more than one domain on a single server

DOMAIN, SUBDOMAIN AND PATHS
Internet Domain -> this is the representation in form of letters of an ip address.
eg: https://www.landingi.com/call-to-action-definition/
in this example - https - is the protocal
                . www - is the subdomain
                . landiningi.com - is the domain
                . call-to-action-definition - is the path

HTTP
Methos and Description: they should all be writen in capital letters
1. GET - The GET method is used to retrieve information from the given server using a given URI. Requests using GET should only retrieve data and should have no other effect on the data.
2. HEAD - Same as GET, but transfers the status line and header section only
3. POST - A POST request is used to send data to the server, for example, customer information, file upload, etc. using HTML forms.
4. PUT - Replaces all current representations of the target resource with the uploaded content
5. DELETE - Removes all current representations of the target resource given by a URI
6. CONNECT - Establishes a tunnel to the server identified by a given URI
.
7. OPTIONS - Describes the communication options for the target resource
8. TRACE - Performs a message loop-back along the path to the target resource

REDIRECTS
-> this is the process of forwarding one URL to a different URL
-> sending both users and search engines to a diferent URL from the one they originally requested
-> there are three types of redirects:
1. 301 moved permanently
       - this is a permanent redirect that passes full link equity to the redirected page.
       - its the best method for implementing redirects on a website
2. 302 Found
       - moved teporarily
       - 307 works the same as 302
3. Meta refresh
       - this is a type of redirect executed on the page level rather than the server level.
       - they are slower and not recommended SEO technique
       - looks like this: <http-equiv="refresh" content="0; url=https://example.com/">

-> to redirect an enitre domain to a new site:
       Redirect 301 / http://www.example.com/
-> to redirect a single page
       Redirect 301 /oldpage/ http://www.example.com/newpage/
-> Using apache mod_rewrite
       RewriteEngine on
       RewriteBase /
       rewritecond %{http_host} ^domain.com [nc]
       rewriterule ^(.*)$ http://www.domain.com/$1 [r=301,nc]
-> php redirect
       <?php
       header("Location: https://www.example.com/", true, 301);
       exit();
       ?>
-> javaScript
       - is not recommended
       - <script type="text/javascript">    function redirect1(){        window.location = "http://www.example.com/new-url/"  }   setTimeout('redirect1()', 5000);   </script>


Not Founf HTTP
-> the HTTP 404, 404 not found, 404 error, page nor found or file not found error message is a http standard responce to indicate that the browser was able to communicate with a given server but the server could not find what was requested.
-> the error message couls also be used when a server does not wish to sidclose wheather it has the request info.

