# Simple-Web-Server-Using-Socket-Programming
In this project, I built a simple web server using Python and socket programming. The server listens on port 9932, which is based on my student ID (1212312 → Port: 9932). This web server handles HTTP requests from a web browser and sends back the correct web pages or files.

The server is designed to support different types of requests and respond properly, either by returning the requested page or by sending a redirect or an error message when needed. It also prints helpful information in the terminal, such as the client's IP address, the request details, and the response status.

To make the project complete and functional, I created six files:
1.	Web_Server.py: The Python script that runs the server.
2.	main_en.html: The main English web page.
3.	main_ar.html: The Arabic version of the main page.
4.	mySite_1212312_en.html: A local English page with a form to request images or videos.
5.	mySite_1212312_ar.html: The Arabic version of the local page.
6.	Error404.html: A simple HTML error page shown when a file is not found.

The web pages include team member details, a networking topic from the textbook, and useful links. CSS is used to make the pages look clean and attractive. The local page also allows users to enter a file name to request an image or video related to networking, and redirects to Google if the file is not found.

This project helped me understand how a basic web server works and how web pages are sent and displayed in a browser.

The first file in this code is Web_Server.py, This Python code creates a basic web server that listens on a specific port (9932 in this case, which was derived from the ID number 1212312). The server is built using the socket library, which allows communication between devices over a network. The code begins by importing the necessary modules — os for handling file operations and socket for setting up the network communication.
Next, the server is set up to use IPv4 (AF_INET) and TCP connections (SOCK_STREAM). It binds to all available network interfaces on the given port and starts listening for incoming connections, allowing only one connection at a time in the waiting queue. A message is printed to let the user know that the server is now running.
Then there's a function called get_content_type() that checks the type of a file based on its extension. For example, if a file ends with ".html", it returns "text/html" so the browser knows how to handle the file. If the extension isn't recognized, it just sends a general type for binary data.
Another function called get_actual_path() helps translate the requested URL path into a real filename. If someone visits "/", "/index.html", "/main_en.html", or "/en", it will serve "main_en.html" by default. If they visit "/ar" or "/main_ar.html", it will serve the Arabic version of the page. For anything else, it removes the starting slash and returns the rest as a file name.
The respond_404() function is used when the server can’t find the file the client asked for. It tries to open a special HTML file called "Error404.html", and it replaces a placeholder message with the IP address and port number of the person who made the request. If the file doesn’t exist, the server just sends a basic 404 error message.
The main part of the code is an infinite loop that keeps the server running and ready to accept new connections. Every time a client connects, the server gets their IP address and port number. It then waits for a request and tries to read it. If the request is empty or there’s a problem, it closes the connection and moves on.
Once a request is received, the server prints a clear divider and shows the IP, port, and full request content for logging purposes. It then tries to extract the request method (like GET), the requested path (like "/main_en.html"), and ignores the rest.
The server only handles GET requests. If someone tries another method like POST, it responds with a 405 error and closes the connection.
If the request is for a search using the pattern /search?file=filename, the server extracts the file name from the query. It checks if this file exists in the server directory. If it does, the server opens the file, finds out its content type, and sends both the file and its type back to the client. If the file doesn’t exist, the server redirects the user to a related Google search. For example, if someone searched for an image, it redirects to Google Images. If it's a video, it redirects to Google Videos. Otherwise, it redirects to the normal Google search. This redirection uses a 307 response code.
If the request is not a search, the server treats it like a request for a normal file. It uses the earlier function to find the actual path and checks if the file exists. If it does, the file is opened, its content is read, and it is sent back to the client with the correct content type. If not, it sends the 404 error page.
If any error happens during processing, the server logs the error and sends a 404 page to the client. Finally, no matter what happened, the server always closes the connection with that client and waits for a new one.
At the very end, if the user stops the server manually by pressing Ctrl+C, it prints a message saying the server was stopped and closes the main server socket to clean up everything.

![image](https://github.com/user-attachments/assets/1d76767c-3ef1-4e71-986e-7eb0a5126abb)

When we search for localhost:9932/ or localhost:9932/en or localhost:9932/main_en.html: 

![image](https://github.com/user-attachments/assets/79ff092e-0f62-4415-a82c-18141e58d81c)

![image](https://github.com/user-attachments/assets/af8e4766-75ae-4379-94e5-ebf1885df7f7)

![image](https://github.com/user-attachments/assets/65920489-2679-4bd9-9454-91d72b2c4cfe)

The file main_en.html is the main English homepage for a web-based project, most likely part of a university assignment related to computer networks (ENCS3320). It demonstrates modern front-end web development using HTML5 and CSS3, while focusing on content presentation, visual design, and responsive layout. Here's a breakdown of its key components:
The file main_en.html is the main English homepage for a web-based project, most likely part of a university assignment related to computer networks (ENCS3320). It demonstrates modern front-end web development using HTML5 and CSS3, while focusing on content presentation, visual design, and responsive layout. Here's a breakdown of its key components:
<meta charset="UTF-8">: Ensures proper character encoding (UTF-8).
<title>: Sets the title shown on the browser tab ("ENCS3320-Webserver").
<style>: Contains internal CSS that defines the entire layout, color scheme, fonts, and visual effects.
Full-screen Background Video: The <video> element plays a looping muted video (mainV.mp4) as the background using position: fixed and object-fit: cover.
Color Scheme: Blue and white tones (baby blue, sky blue, cornflower blue) dominate the interface, giving a calm and tech-like feel.
Typography: Uses Arial, sans-serif for readability and professionalism.
Shadow and Borders: Soft box shadows and rounded borders make content boxes visually appealing.
Presented inside a <section class="team-section"> using Flexbox layout for responsiveness.
Each member has a .member-box showing:
A circular image (<img>)
Name (<h3>)
ID and short personal profile (education, skills, hobbies, and projects).
Highlighted inside <section class="topic-section">.

Explains the topic Network Security including:
Its importance (data protection, integrity).
Related visual (Security.jpg).
Types of threats (still being completed in the file).
Uses lists (<ul>) and subheadings (<h3>) to organize information clearly.

Uses .links class for a centered list of navigation links to other resources or pages (not fully shown in the file).
Enhances user interaction with hover color change (:hover effect).
This HTML file represents a well-structured and visually engaging webpage. It combines HTML, CSS, and media to create a professional look. The page serves as an informative and introductory interface for a computer networking project with details about the team and the main topic.
The output in the terminal:
![image](https://github.com/user-attachments/assets/da3eaf1e-ff8d-48ea-8f41-9d79b5304244)

![image](https://github.com/user-attachments/assets/9cdba62a-2a5e-42ad-b775-e1e504177b67)

![image](https://github.com/user-attachments/assets/397bfb6e-13e8-4320-8a41-3a9c7015581c)

![image](https://github.com/user-attachments/assets/7be9d1e0-64eb-4b3f-a452-404f2125d762)

![image](https://github.com/user-attachments/assets/37bdd2a6-b2be-4d06-8db7-d23de832cb02)

![image](https://github.com/user-attachments/assets/5f164d44-d495-49e0-98c5-1ff53e5aca44)

This is Chrome requesting the home page (likely main_en.html) from the server.
127.0.0.1 is the loopback IP.
Port 50758 is the temporary client-side port used by Chrome.
Served main_en.html confirms the server successfully sent the HTML file back.
Chrome parsed the HTML, found image tags (<img>) pointing to Images_Videos/Security.jpg, Yosra.png, and Nagham.png, and requested them.
the server responded with each image successfully.
then a partial content request for a video (starting from byte 0), which is normal for video streaming. The server successfully served the video file.
Headers like sec-ch-ua, Sec-Fetch-*, and Accept-* are browser metadata headers, mainly for:
Browser info (sec-ch-ua)
Prefetching/prerendering optimizations (Sec-Purpose)
Security context (Sec-Fetch-*)
What content types it accepts (Accept-*)
And when we search for localhost:9932/ar or localhost:9932/main_ar.htm:
![image](https://github.com/user-attachments/assets/17bbe1f9-f66f-47b1-9bdf-42c8d9fbde42)

![image](https://github.com/user-attachments/assets/4ceb4bc0-5e83-470f-bf1a-8bc70c0144d5)

![image](https://github.com/user-attachments/assets/f79e00e3-5b04-4415-ba60-4bec832d553a)

This is just the Arabic version of main_en.htm.
<html lang="ar" dir="rtl"> is used sets the language to Arabic and set text direction from right to left to suit Arabic language.
In the terminal:
![image](https://github.com/user-attachments/assets/d2f6e321-39a2-4543-877b-81b0ae637ba9)
 
![image](https://github.com/user-attachments/assets/e3f522c1-e8c9-46fe-9e28-06c9843b9d2e)

![image](https://github.com/user-attachments/assets/442e7ba4-c5bf-4caf-aa4e-70d45541bc1f)

![image](https://github.com/user-attachments/assets/962a05f2-a955-4a20-a25b-2513bc5e20e5)

![image](https://github.com/user-attachments/assets/0b731a5c-b6d7-4921-824f-6d5ae7ab5be5)

Just as the English version, a full HTTP conversation between the browser and the local server.
Chrome loads the HTML file and request each image and video file it finds in the HTML.

And when we search for localhost:9932/mySite_1212312_en.html or from it’s link in the main_en.html page:
![image](https://github.com/user-attachments/assets/60a6ebc4-5591-466a-809e-fe94ad7b35a0)

This HTML file is called mySite_1212312_en.html, and it’s designed to show a stylish web page related to network security, where users can search for specific files like images. It starts with <!DOCTYPE html>, which tells the browser this is an HTML5 document. Then it opens with the <html lang="en"> tag, which begins the whole HTML content and specifies that the language is English.
Inside the <head> section, the file uses <meta charset="UTF-8"> to set the character encoding. This ensures the browser displays all characters properly, including special ones. The <title> tag is used to give the page a name, which appears in the browser tab. In this case, it says “Network Security.”
Then, there's a <style> section that holds internal CSS styling. This style controls how the page looks. The body selector sets the background using the background property, which applies an image located at Images_Videos/SiteImg.jpg. The image is centered and fixed, meaning it stays in place even when the user scrolls, and it covers the whole screen using background-size: cover. The body also has no margins or padding, uses the Arial font, and sets the text color to white using the color property.
Next is a class called .overlay which is defined with background-color: rgba(0, 0, 50, 0.6)—this gives the whole page a dark bluish overlay with some transparency. This overlay covers the full screen using absolute positioning and is set to stretch from top to bottom and left to right.
There’s another class called .form-container, which is placed in the middle of the screen. It uses position: relative and top: 50% combined with transform: translateY(-50%) to center it vertically. The text-align: center property is used so the content inside it, including the form, is aligned in the center horizontally.
The <h1> tag is used to display the title “Network Security Resources” on the page. It is styled to have a color of DeepSkyBlue using color: #00BFFF.
The form itself is placed inside a <form> tag. This form uses the action="/search" attribute, meaning when the form is submitted, the data will be sent to a URL path /search. The method="get" means the data will be sent through the URL. Inside the form, there is an <input type="text"> element which lets users type in a file name they want to search for. It has a placeholder text to guide the user and is marked as required to prevent empty submissions.
Next to the text input is another input element, <input type="submit">, which acts as the submit button. When clicked, it sends the form’s data to the server. The submit button has styling for padding, background color, border-radius for rounded edges, and cursor changes on hover. The hover effect is added using input[type="submit"]:hover, where the background color becomes a darker blue (#104E8B) when the mouse pointer is over it.
Finally, the <body> section holds the content that appears on the page. The overlay and form-container are nested within it. The page ends with the closing tags for body and html, wrapping up the document.
This file is a simple HTML document that creates a clean and visually appealing search page for a network security-related site. It uses elements like <html>, <head>, <meta>, <title>, <style>, <body>, <div>, <form>, <input>, and <h1> to organize and style the page, handle user input, and make the user experience clear and interactive.
The terminal output:
![image](https://github.com/user-attachments/assets/815da8f5-6853-49ee-a3a7-dd2aaddaff8d)

The line HTTP Request from IP: 127.0.0.1 Port: 52481 means that the computer (the IP address 127.0.0.1 always refers to "localhost", which is yourself) sent a request to the server using port 52481. This is just a random port number used by the browser for communication.
The line GET /Images_Videos/SiteImg.jpg HTTP/1.1 is the actual request the browser sent. It’s asking the server to send back the image file located at /Images_Videos/SiteImg.jpg using the HTTP/1.1 protocol. "GET" means the browser wants to get or download the file.
Host: localhost:9932 tells the server that this request is intended for a web server running locally on port 9932. That port is where the site is hosted temporarily while we’re testing it.
Connection: keep-alive is saying, “don’t close the connection after this request; I might send more soon,” which helps speed up web browsing.
sec-ch-ua-platform: "Windows" is just saying that the request came from a Windows operating system.
User-Agent: Mozilla/5.0 (...) Chrome/136.0.0.0 Safari/537.36 describes the browser and version that made the request. This helps servers know what type of device or browser is being used.
sec-ch-ua, sec-ch-ua-mobile, Sec-Fetch-* headers give extra information about the browser and how it is interacting with the site. For example, Sec-Fetch-Dest: image tells the server this request is for an image, and Sec-Fetch-Mode: no-cors relates to how cross-origin requests are handled, which is a part of browser security.
Accept: image/avif,...,*/*;q=0.8 shows all the image types the browser can accept. The browser is telling the server: “I can handle images in these formats—send me whichever one you have.”
Referer: http://localhost:9932/mySite_1212312_en.html tells the server that this image request came from the HTML file mySite_1212312_en.html, which was already being viewed.
Accept-Encoding and Accept-Language describe what kind of compressed files the browser can read, and which languages it prefers.
Finally, the line Served Images_Videos/SiteImg.jpg to 127.0.0.1:52481 is the server's confirmation. It’s saying: “I’ve successfully sent the image file to your browser at the same IP and port that requested it.”
So in simple terms, the browser asked the local server to send an image file, and the server found it and sent it back—just like delivering a photo from a folder on the computer to the browser window.
If we enter the name of an existing file (image PNG or JPG or video MP4) in the form:
![image](https://github.com/user-attachments/assets/fd2f5c0a-6a1e-438f-88c4-40ff3e0ff308)
![image](https://github.com/user-attachments/assets/955b72fd-1aca-4c8d-8aee-edf8bcef7c74)

This terminal output shows what happened when you typed in the name of an existing image (Images_Videos/Network Security.jpg) into the form on your webpage and clicked the "View Resource" button. The browser then made a new request to the local server to fetch that image. Let's walk through what each line means, using simple words and focusing on how the browser and server communicate.
The first line HTTP Request from IP: 127.0.0.1 Port: 52683 tells us that the computer (127.0.0.1 means "localhost") sent a request from port 52683. This port number is randomly chosen by the browser to handle the request.
The second line GET /search?file=Images_Videos%2FNetwork+Security.jpg HTTP/1.1 is the actual request. It uses the GET method, which means the browser is asking the server to return something. In this case, it's asking for the file at the path Images_Videos/Network Security.jpg. The strange symbols (%2F and +) are just how special characters like slashes and spaces are written in URLs. %2F stands for a forward slash /, and + is used instead of a space.
Host: localhost:9932 tells the server this request is meant for a website running on the computer, using port 9932.
Connection: keep-alive is asking the server to keep the connection open in case the browser needs to send more requests shortly after.
Then we have some browser-specific headers like sec-ch-ua, sec-ch-ua-mobile, and sec-ch-ua-platform, which describe the browser (Google Chrome version 136), whether it's on mobile (it's not), and the platform (Windows). These are mainly used to optimize or customize content if needed.
Upgrade-Insecure-Requests: 1 tells the server that if it has both secure (HTTPS) and insecure (HTTP) versions of the content, the browser prefers the secure one. But in this case, everything is local and not using HTTPS.
User-Agent: Mozilla/5.0 (...) again identifies your browser and operating system. It helps the server understand what kind of browser is making the request.
Accept: text/html,... tells the server which types of content the browser can handle. In this case, it's saying “I’m expecting an HTML page but I can also handle images and other file types.”
Sec-Fetch-Site: same-origin, Sec-Fetch-Mode: navigate, Sec-Fetch-User: ?1, and Sec-Fetch-Dest: document are all headers about how this request is being used. For example, navigate means this is a navigation request (something like opening a new page), and document means the browser expects a whole web page in return.
Referer: http://localhost:9932/mySite_1212312_en.html shows where the request came from—specifically, the form in the file mySite_1212312_en.html.
Accept-Encoding: gzip, deflate, br, zstd lists the types of file compression the browser can handle. The server might use one of these to make the response smaller and faster to load.
Accept-Language: en-US,en;q=0.9,ar;q=0.8 tells the server which languages the browser prefers. In this case, English is preferred, but Arabic is also acceptable.
Finally, the line Served Images_Videos/Network Security.jpg to 127.0.0.1:52683 confirms that the server found the requested image and successfully sent it back to the browser that asked for it, using the same IP and port that made the request.
So in simple terms, this log shows that you entered the name of a valid image, the browser sent a request to get it, and the server found and returned the image successfully.

![image](https://github.com/user-attachments/assets/ed14614b-e826-4b91-b380-02e3fcfb089a)
![image](https://github.com/user-attachments/assets/69218f58-7565-4ac7-8b04-dccacc11cb2f)
![image](https://github.com/user-attachments/assets/cf885bd9-69c3-4845-9de8-a043555f2f77)

This is the browser requesting the video file by URL:
http://localhost:9932/search?file=Images_Videos/Network Security.mp4.
The server successfully found the video file and served it to the browser.
This second request (with a Range header) asks for the video starting from byte 0.
This is typical of how browsers stream video content—they load it in chunks instead of downloading it all at once.
Sec-Fetch-Dest: video tells us this is a video element trying to play.
then The browser is trying to load the website's favicon (the little icon in the browser tab) but we don't have one.
And when we enter a file name doesn’t exist:
![image](https://github.com/user-attachments/assets/a0827a83-ab00-4447-94ae-629b71ede74a)
![image](https://github.com/user-attachments/assets/e3f8f53a-ab07-4f94-9a7d-24152034b55d)

The browser asked for Images_Videos/Network.png.
The %2F is URL encoding for the slash /, and spaces are likely encoded or removed.
Instead of serving the file, your server responded with: 307 Temporary Redirect, which is an HTTP status code that tells the browser: “Hey, I don’t have this file — go look at this URL instead.”
Your server is coded to automatically redirect to a Google Images search if the requested file is missing.
So in this case:
Images_Videos/Network.png was not found locally, so the server redirected to
https://www.google.com/search?q=Images_Videos/Network.png&tbm=isch
— a Google Image search for that filename.
![image](https://github.com/user-attachments/assets/206dd5cf-36b0-40ae-ba24-628dc7c7ecc6)
![image](https://github.com/user-attachments/assets/5bb4a13d-9863-44ec-9352-e32a477cf741)

This terminal output is very similar to the one for the missing image file — the key difference is that the missing file is a video (.mp4) instead of an image (.png).
The browser tried to access Images_Videos/Networks.mp4, but this file doesn’t exist in your server's directory.
Your server detected that the file is missing.

It issued a 307 Temporary Redirect, sending the browser to:
https://www.google.com/search?q=Images_Videos/Networks.mp4&tbm=vid
and &tbm=vid tells Google to show video search results (instead of images or web pages).
In short, if the file exists → your server serves it.
If the file doesn’t exist → your server redirects to an appropriate Google search page, based on the file type: Images: tbm=isch, Videos: tbm=vid
If we search for localhost:9932/mySite_1212312_ar.html:
![image](https://github.com/user-attachments/assets/1571008a-ed6d-47db-8d54-def1a799130e)
![image](https://github.com/user-attachments/assets/e91cd793-f2fa-4bc2-9694-b702c2a3ca04)

Just like the English version, this terminal output shows that the local web server successfully handled two separate HTTP requests from the browser: one for an HTML page and one for an image inside that page.
The first part of the output begins with: HTTP Request from IP: 127.0.0.1 Port: 61934
This means the browser (on your own computer) sent a request to your server from the local IP address 127.0.0.1 using port 61934. This is how the browser connects to the server.
The line GET /mySite_1212312_ar.html HTTP/1.1 shows that the browser is asking the server for a file named mySite_1212312_ar.html using the GET method. It’s a standard way of requesting to view a webpage.
Host: localhost:9932 tells the server that the browser is connecting to the local host machine on port 9932, which is where the server is running.
The other lines, like User-Agent, Accept, and sec-ch-ua, give details about the browser (in this case, Chrome), the types of content it can handle (like HTML, images, and XML), and some other info to help the server respond properly.
At the end of this section, it says:
Served mySite_1212312_ar.html to 127.0.0.1:61934
This means the server found the file and sent it back successfully to the browser.

The second part of the output starts with: HTTP Request from IP: 127.0.0.1 Port: 61936
This is a new request, just like before, but on a different port. It’s common for browsers to open multiple connections at once.
GET /Images_Videos/SiteImg.jpg HTTP/1.1
Now, the browser is asking the server to fetch an image file named SiteImg.jpg located inside the Images_Videos folder. This happens because the HTML page includes this image, so the browser needs to load it separately.
Referer: http://localhost:9932/mySite_1212312_ar.html
This line shows that the image request was triggered from within the HTML file you just opened.
The server then responds:
Served Images_Videos/SiteImg.jpg to 127.0.0.1:61936
This means the image file was found and successfully sent to the browser.
In short, the browser first asked the server for an Arabic version of the website, the server found it and sent it back. Then, the browser automatically asked for an image used in that webpage, and the server also found and sent that image back too. Everything worked correctly.

If we search for a file doesn’t exist like http://localhost:9932/cs.html:
![image](https://github.com/user-attachments/assets/2ce18481-22e0-4cf3-b5d2-2b8236f3fa26)

Error404.html code creates a simple custom error page that shows up when a file is not found, like when the user tries to open an image or video that doesn’t exist. It starts with <!DOCTYPE html>, which tells the browser that the document is written in HTML5, the latest version of HTML. This helps the browser know how to properly read and display the content.
Then the code opens the <html> tag, which wraps the entire page. Inside it, there’s a <head> section. The <head> is used to store meta information about the web page — things that aren’t shown directly on the page itself. Inside the <head>, there’s a <meta charset="UTF-8"> tag. This tag tells the browser to use UTF-8 character encoding, which supports a wide range of characters and symbols from different languages. That’s important if the page ever includes special characters. There’s also a <title>Error 404</title> tag inside the head. This sets the name that appears on the browser tab when the user views this page. In this case, it says “Error 404”.
After the head, the code moves on to the <body> section, which contains everything that will be visible to the user on the web page. The body starts with an <h1> tag that says “404”. This is a large heading, and in this context, it shows the standard error number for a "Not Found" page. Then there’s an <h2> tag with a style attribute that changes the text color to red. This heading says “The file is not found!”, giving a clear message to the user that the requested file doesn’t exist.
Following that, there’s a <p> tag which is used to display a paragraph of text. This paragraph also uses the style attribute to make the text color blue. The paragraph tells the user that their IP address and port number will be shown in the terminal by the server. This is likely included for debugging or informational purposes to show that the server is logging requests.
Finally, the page ends with the closing </body> and </html> tags, marking the end of the body and the whole HTML document. So overall, this code defines a basic and clear error page using common HTML elements like <html>, <head>, <meta>, <title>, <body>, <h1>, <h2>, and <p>, with simple inline CSS styles to color the text.
![image](https://github.com/user-attachments/assets/331f318a-f89b-4b53-b315-f56327f7f432)

This terminal output shows what happens when the browser tries to open a webpage called cs.html, but that file doesn't exist on the server.
The first line says: HTTP Request from IP: 127.0.0.1 Port: 61131
This means the browser (running on the computer) sent an HTTP request from the local IP address 127.0.0.1 — which is a loopback address that always refers to your own machine. The port number used for this connection is 61131. This port is chosen randomly by the system for the browser to communicate with the local server running on the machine.
Next, the request line says: GET /cs.html HTTP/1.1
This means the browser is asking the server to send back a file called cs.html. GET is the HTTP method used to retrieve data. The path /cs.html tells the server the specific file the browser is looking for.
Then there’s a group of headers, like: Host: localhost:9932
This tells the server that the browser is trying to connect to the local machine (localhost) on port 9932. This is where the local web server is running.
Headers like User-Agent, Accept, Connection, Accept-Encoding, Accept-Language, and sec-ch-ua give extra information about the browser and what kind of content it can handle. These are automatically added by the browser to help the server know how to respond properly.
At the bottom of the output, it says: File not found: cs.html
This is the server's response, meaning the requested file (cs.html) doesn’t exist in the directory where the server is looking. As a result, the browser probably shows a 404 error page, maybe the custom one you created earlier.
In summary, this output tells you that the browser tried to load a file called cs.html, but the server couldn’t find it, so it returned an error message.

If we click Ctrl+C, and then try to search for a page:
![image](https://github.com/user-attachments/assets/9212e958-82ea-4137-b0c6-cd4987d38cd2)
![image](https://github.com/user-attachments/assets/7c4885c2-08cc-4702-83b6-b9263c413769)

This terminal output shows what happened when you manually stopped the server using Ctrl+C, and how that affected the ongoing communication between the browser and the local server.
The output begins with an HTTP request from the browser: HTTP Request from IP: 127.0.0.1 Port: 61936
This shows that the browser was still trying to load the image SiteImg.jpg from the local server. It's the same image request from earlier, and it was coming from the same local IP and port.
The request itself (starting with GET /Images_Videos/SiteImg.jpg HTTP/1.1) is a standard way the browser asks the server to give it that image file. It includes information like the browser type (User-Agent), acceptable file formats (Accept), and where the request originated from (Referer: http://localhost:9932/mySite_1212312_ar.html).
The line: Served Images_Videos/SiteImg.jpg to 127.0.0.1:61936
tells us the server successfully found and sent the image to the browser before it was stopped. That request was completed correctly.
Then you see this line: Server stopped by user.
This confirms that you pressed Ctrl+C, which is a command used in the terminal to stop a running process. In this case, that process is your web server.
Once the server is stopped, it's no longer listening on port 9932, and that means it cannot respond to any more requests from the browser. So when you try to reload the page after this, your browser will try to send a request but won’t get any reply because the server is no longer running. That’s why the page won’t load anymore.
The last line: C:\Users\User\Desktop\Computer Networks\Project\Task2> is just the Windows command prompt showing you're back to the directory where the server script was running, and it's now ready to take new commands.
So in short, everything was working fine, but once you stopped the server with Ctrl+C, the connection between the browser and server was cut off, so the browser can no longer load any HTML pages, images, or other files from it.
