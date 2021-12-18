import asyncio
import websockets
import json
from handler import MessageHandler
from custom_handler import CustomMessageHandler, MongoDB


# -------------------------------------------------------------------------------------
# WebSocketClient
# -------------------------------------------------------------------------------------
class WebSocketClient:
    def __init__(self, url, payload, identifier, handler: MessageHandler):
        self.url = url
        self.payload = payload
        self.identifier = identifier
        self.handler = handler

    async def connect(self):
        print(f"[{self.identifier}] Connect to {self.url}")

        websocket = await websockets.connect(self.url, ssl=True)
        await websocket.send(json.dumps(self.payload))

        while True:
            if not websocket.open:
                try:
                    # print(f'[{self.id}] 1. Websocket is NOT connected. Reconnecting...')
                    websocket = await websockets.connect(self.url, ssl=True)
                    await websocket.send(json.dumps(self.payload))
                except:
                    # print(f'[{self.id}] 2. Unable to reconnect, trying again.')
                    pass
            try:
                async for message in websocket:
                    if message is not None:
                        self.handler.run(message)
            except:
                # print(f'[{self.id}] 3.Error receiving message from websocket.')
                pass


# -------------------------------------------------------------------------------------
# Main Controller
# -------------------------------------------------------------------------------------
if __name__ == "__main__":

    with open('config.json', 'r') as f:
        config = json.load(f)
        
    print('==== Start =====')
    
    mongo_db = MongoDB(config["DB"]["URL"], config["DB"]["DATABASE"])
    
    ws_clients = []
    for ws in config["WS"]:
        ws_url = ws["URL"]
        ws_payload = ws["PAYLOAD"]
        ws_id = ws["ID"]

        handler = CustomMessageHandler(mongo_db, ws_id)
        client = WebSocketClient(ws_url, ws_payload, ws_id, handler)
        ws_clients.append(client.connect())
    
    async def connect(tasks):
        await asyncio.wait(tasks)

    asyncio.run(connect(ws_clients))
    
