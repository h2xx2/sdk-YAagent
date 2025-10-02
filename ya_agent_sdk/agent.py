import time
import uuid
import requests


class YAAgent:
    def __init__(self, agent: str, key: str, base_url: str = "https://3bpvxit706.execute-api.us-west-2.amazonaws.com/dev"):
        self.agent = agent
        self.key = key
        self.base_url = base_url.rstrip("/")
        self.session_id = f"py-{agent}-{uuid.uuid4().hex[:8]}-{int(time.time())}"

    def sendMessage(self, message: str) -> str:
        if not message.strip():
            raise ValueError("Message cannot be empty")

        url = f"{self.base_url}/public-send"
        payload = {
            "agentId": self.agent,
            "sessionId": self.session_id,
            "message": message,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.key,
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=30)

        if resp.status_code != 200:
            raise RuntimeError(f"API Error {resp.status_code}: {resp.text}")

        try:
            data = resp.json()
        except Exception:
            raise RuntimeError(f"Invalid JSON response: {resp.text}")

        return data.get("response", "Нет ответа от сервера")

    def getSessionId(self) -> str:
        """Возвращает sessionId текущего чата"""
        return self.session_id
