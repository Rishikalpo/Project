import socket
import os
import json

HOST = '127.0.0.1'
PORT = 8080

def handle_request(request):
    lines = request.split('\r\n')
    request_line = lines[0]
    method, path, _ = request_line.split()

    if method != 'GET':
        return http_response(405, 'Method Not Allowed', 'Method Not Allowed')

    if path == '/':
        return serve_html('static/index.html')
    elif path == '/book':
        return serve_json('books.json')
    else:
        return http_response(404, 'Not Found', '<h1>404 Not Found</h1>')

def http_response(status_code, status_text, body, content_type='text/html'):
    body_bytes = body.encode('utf-8')
    headers = (
        f"HTTP/1.1 {status_code} {status_text}\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    return headers.encode('utf-8') + body_bytes

def serve_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            body = f.read()
        return http_response(200, 'OK', body, 'text/html')
    except FileNotFoundError:
        return http_response(404, 'Not Found', '<h1>404 File Not Found</h1>')

def serve_json(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        body = json.dumps(data, indent=2)
        return http_response(200, 'OK', body, 'application/json')
    except FileNotFoundError:
        return http_response(404, 'Not Found', '{"error": "File not found"}', 'application/json')

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server running at http://{HOST}:{PORT}")

        while True:
            client_socket, addr = s.accept()
            with client_socket:
                request = client_socket.recv(1024).decode('utf-8')
                if request:
                    response = handle_request(request)
                    client_socket.sendall(response)

if __name__ == '__main__':
    start_server()
