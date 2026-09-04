# Simple HTTP Server

A lightweight, fully configurable static HTTP server written in native Python with zero external dependencies. Designed with clean code practices, security, and repository-readiness in mind—no hardcoded configuration, making it ideal for containerization, local development, and seamless GitHub deployment.

---

## Features

- **Zero External Dependencies**: Built entirely with Python's standard library (`http.server`, `os`, `sys`).
- **100% Configurable**: No hardcoded ports, hostnames, or paths. All parameters are injected via environment variables with sensible defaults.
- **Custom 404 Error Handling**: Automatic fallback to a custom `404.html` page if present in your web directory.
- **Auto-Initialization**: Creates the root web directory and a fallback `index.html` on first launch if none exists.
- **Graceful Shutdown**: Handles `SIGINT` (`Ctrl+C`) cleanly without throwing unhandled stack traces.
- **Production-Ready Layout**: Prepared for Docker, CI/CD pipelines, and cloud hosting platforms (e.g., Render, Railway, Heroku).

---

## Directory Structure

```
.
├── server.py           # Core HTTP server script
├── public/             # Web root directory for static files
│   ├── index.html      # Home page
│   ├── 404.html        # Custom 404 page (optional)
│   ├── css/            # Stylesheets
│   └── js/             # Client-side scripts
├── .env.example        # Template for environment variables
└── README.md           # Project documentation
```

---

## Quick Start

### Prerequisites

- Python **3.8+** installed on your system.

### Running the Server

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Miaoumap24/Simple-HTTP-Server.git
   cd Simple-HTTP-Server
   ```

2. **Start with default settings:**
   ```bash
   python server.py
   ```
   By default, the server listens on `http://0.0.0.0:8080` and serves files from the `./public` directory.

3. **Access in browser:**
   Navigate to http://localhost:8080.

---

## Configuration

The application reads configuration settings from environment variables.

| Environment Variable | Description | Default Value |
| :--- | :--- | :--- |
| `PORT` | Network port the server listens on | `8080` |
| `HOST` | IP address binding (`0.0.0.0` for all interfaces, `127.0.0.1` for local only) | `0.0.0.0` |
| `WEB_DIR` | Relative or absolute path to static assets directory | `public` |

### Custom Environment Examples

**On Linux / macOS:**
```bash
PORT=3000 HOST=127.0.0.1 WEB_DIR=dist python server.py
```

**On Windows (PowerShell):**
```powershell
$env:PORT="3000"; $env:HOST="127.0.0.1"; $env:WEB_DIR="dist"; python server.py
```

**Using a `.env` loader (optional):**
If you use `python-dotenv` or similar tools, create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

---

## Containerization (Docker)

You can containerize this server using a lightweight Python image.

### Example `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy server implementation
COPY server.py .

# Expose default port
EXPOSE 8080

# Run server with environment variable defaults
CMD ["python", "server.py"]
```

### Build and Run Docker Image

```bash
# Build image
docker build -t static-http-server .

# Run container with custom port and directory mount
docker run -d -p 8080:8080 -v $(pwd)/public:/app/public static-http-server
```

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## License

Distributed under the **MIT License**. See `LICENSE` for more information.
