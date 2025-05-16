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

The first file in this code is Web_Server.py, This Python code creates a basic web server that listens on a specific port (9932 in this case, which was derived from the ID number 1212312). The server is built using the socket library, which allows communication between devices over a network. The code begins by importing the necessary modules — os for handling file operations and socket for setting up the network communication.

Next, the server is set up to use IPv4 (AF_INET) and TCP connections (SOCK_STREAM). It binds to all available network interfaces on the given port and starts listening for incoming connections, allowing only one connection at a time in the waiting queue. A message is printed to let the user know that the server is now running.
Then there's a function called get_content_type() that checks the type of a file based on its extension. For example, if a file ends with ".html", it returns "text/html" so the browser knows how to handle the file. If the extension isn't recognized, it just sends a general type for binary data.

The server only handles GET requests. If someone tries another method like POST, it responds with a 405 error and closes the connection.

![image](https://github.com/user-attachments/assets/10750362-0afc-4ced-a2dd-7859fbb0050d)

If the request is for a search using the pattern /search?file=filename, the server extracts the file name from the query. It checks if this file exists in the server directory. If it does, the server opens the file, finds out its content type, and sends both the file and its type back to the client. If the file doesn’t exist, the server redirects the user to a related Google search. For example, if someone searched for an image, it redirects to Google Images. If it's a video, it redirects to Google Videos. Otherwise, it redirects to the normal Google search. This redirection uses a 307 response code.

If the request is not a search, the server treats it like a request for a normal file. It uses the earlier function to find the actual path and checks if the file exists. If it does, the file is opened, its content is read, and it is sent back to the client with the correct content type. If not, it sends the 404 error page.

If any error happens during processing, the server logs the error and sends a 404 page to the client. Finally, no matter what happened, the server always closes the connection with that client and waits for a new one.

At the very end, if the user stops the server manually by pressing Ctrl+C, it prints a message saying the server was stopped and closes the main server socket to clean up everything.


When we search for localhost:9932/ or localhost:9932/en or localhost:9932/main_en.html: 

![image](https://github.com/user-attachments/assets/79ff092e-0f62-4415-a82c-18141e58d81c)
![image](https://github.com/user-attachments/assets/af8e4766-75ae-4379-94e5-ebf1885df7f7)
![image](https://github.com/user-attachments/assets/65920489-2679-4bd9-9454-91d72b2c4cfe)

The file main_en.html is the main English homepage for a web-based project, most likely part of a university assignment related to computer networks (ENCS3320). It demonstrates modern front-end web development using HTML5 and CSS3, while focusing on content presentation, visual design, and responsive layout.

And when we search for localhost:9932/ar or localhost:9932/main_ar.htm:

![image](https://github.com/user-attachments/assets/17bbe1f9-f66f-47b1-9bdf-42c8d9fbde42)
![image](https://github.com/user-attachments/assets/4ceb4bc0-5e83-470f-bf1a-8bc70c0144d5)
![image](https://github.com/user-attachments/assets/f79e00e3-5b04-4415-ba60-4bec832d553a)

This is just the Arabic version of main_en.htm.

(lang="ar" dir="rtl") is used sets the language to Arabic and set text direction from right to left to suit Arabic language.


And when we search for localhost:9932/mySite_1212312_en.html or from it’s link in the main_en.html page:

![image](https://github.com/user-attachments/assets/60a6ebc4-5591-466a-809e-fe94ad7b35a0)

This HTML file is called mySite_1212312_en.html, and it’s designed to show a stylish web page related to network security, where users can search for specific files like images.This file is a simple HTML document that creates a clean and visually appealing search page for a network security-related site. 
If we enter the name of an existing file (image PNG or JPG or video MP4) in the form:

![image](https://github.com/user-attachments/assets/fd2f5c0a-6a1e-438f-88c4-40ff3e0ff308)
![image](https://github.com/user-attachments/assets/4e5ad7d1-c2f4-4d67-9b48-b6340a134618)

And when we enter a file name doesn’t exist:

![image](https://github.com/user-attachments/assets/057bd14f-84d4-426a-90cc-a6b0a2f955e4)
![image](https://github.com/user-attachments/assets/24e23b8b-4f17-424c-91c4-bf167fb785d1)

So, if the file exists → your server serves it.

If the file doesn’t exist → your server redirects to an appropriate Google search page, based on the file type: Images: tbm=isch, Videos: tbm=vid


If we search for localhost:9932/mySite_1212312_ar.html:

![image](https://github.com/user-attachments/assets/1571008a-ed6d-47db-8d54-def1a799130e)
![image](https://github.com/user-attachments/assets/e91cd793-f2fa-4bc2-9694-b702c2a3ca04)


If we search for a file doesn’t exist like http://localhost:9932/cs.html:

![image](https://github.com/user-attachments/assets/2ce18481-22e0-4cf3-b5d2-2b8236f3fa26)

Error404.html code creates a simple custom error page that shows up when a file is not found, like when the user tries to open an image or video that doesn’t exist. 


If we click Ctrl+C, and then try to search for a page:

![image](https://github.com/user-attachments/assets/9212e958-82ea-4137-b0c6-cd4987d38cd2)

Once you stopped the server with Ctrl+C, the connection between the browser and server was cut off, so the browser can no longer load any HTML pages, images, or other files from it.
