import requests
import json
from datetime import datetime
from .exceptions import (Unauthorized, Empty)

class vxresponse:
    def __init__(self, response: requests.Response):
        self.response = response
        self.parsed = json.loads(self.response)
        self.size = int(self.parsed["size"])
        self.first_seen = datetime.fromisoformat(self.parsed["first_seen"].replace("Z", "+00:00"))
        self.download_link = self.parsed["download_link"]

class vxapi:
    def __init__(self, api_key: str) -> None:
        if isinstance(api_key, str):
            self.api_key = api_key
        else:
            raise ValueError("API key must be string.")

    def get_sample(self, sha256: str) -> vxresponse:
        if isinstance(sha256, str):
            headers = {"Authorization": self.api_key}
            res = requests.get(f"https://virus.exchange/api/samples/{sha256}", headers=headers).text
            if res == "Unauthorized":
                raise Unauthorized("The API key is invalid. Unauthorized.")
            elif res == "{\"errors\":{\"detail\":\"Not Found\"}}":
                raise Empty("Nothing found.")
            return vxresponse(res)
        else:
            raise ValueError("Hash must be string.")