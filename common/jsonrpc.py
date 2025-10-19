import requests  # type: ignore
import time
import logging

from typing import Any, Optional, List

class JSONRPC:
    def __init__(self, url: str = "http://localhost:8545", retries: int = 3, delay: float = 0.5) -> None:
        self.url, self.retries, self.delay = url, retries, delay

    def call(self, method: str, params: Optional[List[Any]] = None) -> Any:
        """Minimal JSON-RPC client with retry + logging."""
        params = params or []
        for i in range(self.retries):
            try:
                r = requests.post(
                    self.url,
                    json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params},
                    timeout=5,
                )
                r.raise_for_status()
                result = r.json().get("result")
                logging.info(f"RPC {method} → {result}")
                return result
            except Exception as e:
                logging.warning(f"RPC {method} attempt {i+1} failed: {e}")
                if i == self.retries - 1:
                    raise
                time.sleep(self.delay)