from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

MODEL_VERSION = "tiny-linear-v1"
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "8090"))


def predict(x: float) -> float:
    return 2.0 * x + 1.0


class Handler(BaseHTTPRequestHandler):
    def _send(self, status: int, body: dict) -> None:
        raw = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send(200, {"status": "ok", "model_version": MODEL_VERSION})
        else:
            self._send(404, {"error": "not_found"})

    def do_POST(self) -> None:
        if self.path != "/predict":
            self._send(404, {"error": "not_found"})
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            body = json.loads(self.rfile.read(size))
            value = float(body["x"])
        except (ValueError, KeyError, TypeError, json.JSONDecodeError):
            self._send(400, {"error": "invalid_input"})
            return
        self._send(200, {"prediction": predict(value), "model_version": MODEL_VERSION})

    def log_message(self, format: str, *args: object) -> None:
        return


if __name__ == "__main__":
    print(f"ML service listening on http://{HOST}:{PORT}")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
