from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'About us')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        response = 'Parameters: '
        for key, value in query_params.items():
            response += f'\n{key}: {value}'
            response += '\n'

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        parsed_data = parse_qs(post_data.decode())
        response = 'Data received: '
        for key, value in parsed_data.items():
            response += f'\n{key}: {value}'
            response += '\n'

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode())


if __name__ == '__main__':
    httpd = HTTPServer(('', PORT), MyHandler)
    print('Сервер запущен на порту: ', PORT)
    httpd.serve_forever()