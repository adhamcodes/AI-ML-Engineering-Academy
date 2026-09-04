from __future__ import annotations

import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from service import Handler, MODEL_VERSION, predict


class ServiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        host, port = cls.server.server_address
        cls.base_url = f"http://{host}:{port}"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def request(self, path: str, body: bytes | None = None) -> tuple[int, dict]:
        request = Request(
            self.base_url + path,
            data=body,
            headers={"Content-Type": "application/json"} if body is not None else {},
            method="POST" if body is not None else "GET",
        )
        try:
            with urlopen(request, timeout=2) as response:
                return response.status, json.loads(response.read())
        except HTTPError as error:
            return error.code, json.loads(error.read())

    def test_prediction_contract(self) -> None:
        self.assertEqual(predict(3.0), 7.0)
        self.assertTrue(MODEL_VERSION)

    def test_health_exposes_model_version(self) -> None:
        status, body = self.request("/health")
        self.assertEqual(status, 200)
        self.assertEqual(body, {"status": "ok", "model_version": MODEL_VERSION})

    def test_predict_endpoint(self) -> None:
        status, body = self.request("/predict", json.dumps({"x": 3}).encode())
        self.assertEqual(status, 200)
        self.assertEqual(body["prediction"], 7.0)
        self.assertEqual(body["model_version"], MODEL_VERSION)

    def test_invalid_requests_are_explicit(self) -> None:
        self.assertEqual(self.request("/predict", b"{not-json")[0], 400)
        self.assertEqual(self.request("/predict", json.dumps({"wrong": 3}).encode())[0], 400)
        self.assertEqual(self.request("/missing")[0], 404)


if __name__ == "__main__":
    unittest.main()
