import requests
from datetime import datetime
from .exceptions import (Unauthorized, Nothing)

class vxresponse:
    def __init__(self, response: requests.Response):
        self.response = response.json()
        self.md5 = self.response["md5"]
        self.sha256 = self.response["sha256"]
        self.sha512 = self.response["sha512"]
        self.type = self.response["type"] if not self.response["type"] == "unknown" else None
        self.size = int(self.response["size"])
        self.first_seen = datetime.fromisoformat(self.response["first_seen"].replace("Z", "+00:00"))
        self.download_link = self.response["download_link"]

class vxapi:
    def __init__(self, api_key: str) -> None:
        if isinstance(api_key, str) and len(api_key) > 0:
            self.api_key = api_key
        else:
            raise ValueError("API key must be string.")

    def get_sample(self, sha256: str) -> vxresponse:
        if isinstance(sha256, str) and len(sha256) > 0:
            req = requests.get(f"https://virus.exchange/api/samples/{sha256}", headers={"Authorization": self.api_key})

            if req.status_code == 200:
                return vxresponse(req)
            elif req.status_code == 401:
                raise Unauthorized("The API key is invalid. Unauthorized.")
            elif req.status_code == 404:
                raise Nothing("Nothing found.")
            else:
                raise Exception(req.text)
        else:
            raise ValueError("Hash must be string.")