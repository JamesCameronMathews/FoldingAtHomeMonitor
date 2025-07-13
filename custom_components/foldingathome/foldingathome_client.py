import json
import websockets
from typing import Callable, List


class FoldingAtHomeClient:
    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 7396,
        use_proxy: bool = False,
        proxy_host: str = "node1.foldingathome.org",
        proxy_path: str = "/ws/account",
        account=None,
        token=None
    ):
        if use_proxy:
            if not account or not token:
                raise ValueError("Account and token required for proxy mode")
            self.url = f"wss://{proxy_host}{proxy_path}{account}?token={token}"
        else:
            url = f"ws://{host}:{port}/api/websocket"

        self.url = url
        self.ws = None
        self._listeners: List[Callable[[dict], None]] = []


    def register_listener(self, callback: Callable[[dict], None]):
        self._listeners.append(callback)

    async def connect(self):
        self.ws = await websockets.connect(self.url)

    async def disconnect(self):
        if self.ws:
            await self.ws.close()

    async def send(self, payload):
        await self.ws.send(json.dumps(payload))

    async def receive(self):
        msg = await self.ws.recv()
        return json.loads(msg)

    async def get_info(self):
        await self.send({"type": "request", "payload": {"cmd": "info"}})
        return await self.receive()

    async def get_units(self):
        await self.send({"type": "request", "payload": {"cmd": "units"}})
        return await self.receive()

    async def fold(self):
        await self.send({"type": "broadcast", "payload": {"cmd": "state", "state": "fold"}})

    async def pause(self):
        await self.send({"type": "broadcast", "payload": {"cmd": "state", "state": "pause"}})

    async def _notify(self, msg: dict):
        for cb in self._listeners:
            cb(msg)

    async def listen(self):
        while True:
            msg = await self.receive()
            await self._notify(msg)