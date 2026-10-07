from http.server import BaseHTTPRequestHandler, HTTPServer
import os

APP_ENV = os.getenv("APP_ENV", "dev")
APP_NAME = os.getenv("APP_NAME", "simple-docker-app")
OWNER = os.getenv("OWNER", "Azeez Opeoluwa")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        message = (
            f"Hello from {APP_NAME}\n"
            f"Environment: {APP_ENV}\n"
            f"Owner: {OWNER}\n"
        )

        self.wfile.write(message.encode("utf-8"))


server = HTTPServer(("0.0.0.0", 8080), Handler)
print("Server running on port 8080")
server.serve_forever()