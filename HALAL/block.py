import hashlib
import json
import uuid
from datetime import datetime, timedelta  #untuk data expired dengan jangka 2th kedepan

class Block:
    def __init__(self, index: int, data: dict, previous_hash: str):
        self.index = index
        self.id = str(uuid.uuid4())
        self.timestamp = datetime.utcnow().isoformat()
        if self.index == 0:
            self.expired = None
        else:
            self.expired = (datetime.utcnow() + timedelta(days=730)).isoformat()

        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_data = {
            "index": self.index,
            "id": self.id,
            "timestamp": self.timestamp,
            "expired": self.expired,
            "data": self.data,
            "previous_hash": self.previous_hash
        }

        encoded = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()