# Copyright (C) 2026 Lixiod Technologies

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

# CONFIGURATION
PORT = int(os.getenv("PORT", 8080))
HOST = os.getenv("HOST", "0.0.0.0")
WEB_DIR = os.getenv("WEB_DIR", "public")

class DynamicRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # ROOT DIR OF THE SERVER
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        requested_path = self.translate_path(self.path)
        if not os.path.exists(requested_path) and not requested_path.endswith('/'):
            custom_404 = os.path.join(WEB_DIR, "404.html")
            if os.path.exists(custom_404):
                self.path = "/404.html"
        return super().do_GET()

def run():
    if not os.path.exists(WEB_DIR):
        os.makedirs(WEB_DIR)
        with open(os.path.join(WEB_DIR, "index.html"), "w", encoding="utf-8") as f:
            f.write("<!DOCTYPE html><html><body><h1>Serveur Opérationnel !</h1></body></html>")

    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, DynamicRequestHandler)
    print(f"Server started at http://{HOST}:{PORT} (Dossier: '{WEB_DIR}')")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStoping server.")
        httpd.server_close()
        sys.exit(0)

if __name__ == "__main__":
    run()
