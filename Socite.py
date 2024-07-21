import asyncio
import websockets
import json

async def connect_to_server():
    uri = "ws://127.0.0.1:5000/socket.io/?EIO=4&transport=websocket"

    async with websockets.connect(uri) as websocket:
        # Send a message
        message = {"data": "Hello, WebSocket Server!"}
        await websocket.send(json.dumps(message))
        print("Message sent")

        # Receive a response
        response = await websocket.recv()
        print("Response received:", response)

asyncio.get_event_loop().run_until_complete(connect_to_server())
