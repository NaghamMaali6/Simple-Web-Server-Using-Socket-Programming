import os  #Import the OS module for file-related operations
from socket import *  #Import all socket functions for network communication

#Server configuration:
serverPort = 9932  #Define the port number the server will listen on(derived from ID: 1212312)
serverSocket = socket(AF_INET, SOCK_STREAM)  #Create a TCP socket using IPv4
serverSocket.bind(('' , serverPort))  #Bind the socket to all interfaces on the specified port
serverSocket.listen(1)  #Start listening for incoming connections, 1 queued connection allowed
print("Server is running on port" , serverPort)  #Inform the user that the server has started

#Function to determine the content type based on the file extension:
def get_content_type(filename):
    if filename.endswith(".html"):
        return "text/html"
    elif filename.endswith(".css"):
        return "text/css"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        return "image/jpeg"
    elif filename.endswith(".mp4"):
        return "video/mp4"
    else:
        return "application/octet-stream"  #Default type for unknown extensions

#Function to map request paths to actual file names:
def get_actual_path(path):
    if path in ["/" , "/index.html" , "/main_en.html" , "/en"]:
        return "main_en.html"  #Default to English version
    elif path in ["/ar" , "/main_ar.html"]:
        return "main_ar.html"  #Arabic version
    else:
        return path.lstrip("/")  #Remove leading slash and return the path

#Function to send a 404 Not Found response:
def respond_404(connectionSocket , ip , port):
    try:
        with open("Error404.html", "r" , encoding="utf-8") as file: 
            content = file.read()   #Try to open a custom 404 page
        
        content = content.replace("<p>Your IP address and port number will be shown here by the server.</p>" , f"<p>Client IP: {ip} | Port: {port}</p>")  #Inject IP and port into the content (replace placeholder)

        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n" + content
        connectionSocket.sendall(response.encode())
    except:
        connectionSocket.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n404 Page Not Found")  #Fallback plain text 404 response if file not found

#Main server loop:
try:
    while True:
        connectionSocket , addr = serverSocket.accept()  #Accept a new client connection
        ip , port = addr  #Extract IP and port from the client address

        try:
            request = connectionSocket.recv(2048).decode()  #Receive and decode the HTTP request
        except Exception as e:
            print("Error receiving request:" , e)  #Log any error
            connectionSocket.close()
            continue  #Skip to next connection

        if not request:  #If the request is empty, close and move on
            connectionSocket.close()
            continue

        print("======================================================")
        print("HTTP Request from IP:" , ip , "Port:" , port)  #Show who sent the request
        print(request.strip())  #Print the raw HTTP request

        try:
            first_line = request.split('\n')[0]  #Extract the first line of the HTTP request
            method , path , _ = first_line.split()  #Split into method, path, and version

            if method != "GET":  #Only allow GET requests
                connectionSocket.sendall(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
                connectionSocket.close()
                continue

            #Handle search query like /search?file=filename:
            if path.startswith("/search?file="):
                from urllib.parse import unquote, urlparse, parse_qs  #Import URL parsing utilities
                parsed_url = urlparse(path)  #Parse the full path
                params = parse_qs(parsed_url.query)  # Extract query parameters
                filename = unquote(params.get("file" , [""])[0])  # Decode the filename parameter

                if os.path.isfile(filename):  #If the file exists
                    content_type = get_content_type(filename)  #Get its content type
                    with open(filename , "rb") as file:
                        content = file.read()  #Read file content
                    header = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\n\r\n"
                    connectionSocket.sendall(header.encode() + content)  #Send HTTP header + content
                    print(f"Served {filename} to {ip}:{port}")  #Log successful serve
                else:
                    #Determine which Google tab to search in (image/video/general):
                    if filename.lower().endswith((".png", ".jpg" , ".jpeg")):
                        search_type = "isch"  #Google Image Search
                    elif filename.lower().endswith(".mp4"):
                        search_type = "vid"  #Google Video Search
                    else:
                        search_type = ""  #General search

                    query = filename  #The search term is the filename
                    if search_type:
                        url = f"https://www.google.com/search?q={query}&tbm={search_type}"
                    else:
                        url = f"https://www.google.com/search?q={query}"

                    response = f"HTTP/1.1 307 Temporary Redirect\r\nLocation: {url}\r\n\r\n"
                    connectionSocket.sendall(response.encode())  #Redirect to Google search
                    print("307 Temporary Redirect")  #Log it
                    print(f"Response: 307 Redirect to {url} for {ip}:{port} on port {serverPort}")  #Print where it redirected
                    print(f"Redirected to Google search for {filename}")

                connectionSocket.close()
                continue  #Skip to next connection

            #Serve a normal file based on path:
            filename = get_actual_path(path)  #Convert path to local filename
            if os.path.isfile(filename):  #If file exists
                content_type = get_content_type(filename)  #Get content type
                with open(filename , "rb") as file:
                    content = file.read()
                header = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\n\r\n"
                connectionSocket.sendall(header.encode() + content)  #Send response
                print(f"Served {filename} to {ip}:{port}")  #Log success
            else:
                respond_404(connectionSocket , ip , port)  #File not found, respond with 404
                print(f"File not found: {filename}")

        except Exception as e:
            print("Error processing request:" , e)  #Log any processing error
            respond_404(connectionSocket , ip , port)  #Send 404 in case of error

        finally:
            connectionSocket.close()  #Always close the client connection

except KeyboardInterrupt:
    print("\nServer stopped by user.")  #Stop message on Ctrl+C
    serverSocket.close()  #Close the main server socket