from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_contacts(self):
        link = "https://raw.githubusercontent.com/Helen85236/19_1/main/contacts.html"
        response = requests.get(link)
        return response.text

    def do_POST(self):
        c_len = int(self.headers.get('Content-Length'))
        client_data = self.rfile.read(c_len)
        print(client_data.decode())

        self.send_response(200)

    def do_GET(self):
        page_content = self.__get_contacts()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))

if __name__ == "__main__":
    # Web server initilization
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    # Start server
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    # Close server
    webServer.server_close()
    print("Server stopped.")