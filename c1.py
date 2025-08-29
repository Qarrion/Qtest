# client.py
import asyncio
import websockets

async def receive_data():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("✅ 서버 연결 완료")
        while True:
            data = await websocket.recv()
            print(f"📥 받은 데이터: {data}")

if __name__ == "__main__":
    asyncio.run(receive_data())
