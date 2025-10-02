<<<<<<< HEAD
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
=======
import requests
import json
import time
import random
import string

class YAAgent:
    def __init__(self, agent_id: str, key: str):
        self.agent_id = agent_id
        self.key = key
        # уникальный session_id для каждой сессии
        self.session_id = f"session-{int(time.time())}-{''.join(random.choices(string.ascii_letters + string.digits, k=6))}"

    def sendMessage(self, message: str) -> str:
        if not message.strip():
            return ""

        url = "https://bn258wvyl7.execute-api.us-west-2.amazonaws.com/prod/public-send"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.key
        }
        payload = {
            "message": message,
            "agentId": self.agent_id,
            "sessionId": self.session_id
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            data = response.json()
            # Если тело внутри "body" как строка
            if isinstance(data.get("body"), str):
                data = json.loads(data["body"])
            return data.get("response", "No response from agent")
        except requests.RequestException as e:
            return f"Error: {str(e)}"
>>>>>>> 1761eda (test2)
