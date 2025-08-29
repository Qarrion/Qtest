# python -m c

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("안녕하세요 서버!")
        response = await websocket.recv()
        print(f"서버로부터 응답: {response}")

asyncio.run(hello())