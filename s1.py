# server.py
import asyncio
import websockets
import random
import datetime
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError

async def stream_data(websocket):
    while True:
        # 예시: 랜덤 값과 타임스탬프 생성
        data = {
            "timestamp": datetime.datetime.now().isoformat(),
            "value": round(random.uniform(100, 200), 2)
        }
        try:
            await websocket.send(str(data))  # 문자열로 전송
            await asyncio.sleep(1)  # 1초마다 전송
        except ConnectionClosedError as e:
            # 비정상 종료 (예: 네트워크 오류 등)
            print(f"⚠️ connection closed abnormally: code={e.code}, reason={e.reason}")
        finally:
            # 혹시 열려 있다면 정리
            if not websocket.closed:
                await websocket.close()
            print("🧹 handler finished.")
            
async def main():
    async with websockets.serve(stream_data, "localhost", 8765):
        print("📡 WebSocket 서버 실행 중 (ws://localhost:8765)")
        
        try:
            await asyncio.Future()  # 서버가 계속 실행되도록 유지
        except asyncio.CancelledError:
            print("서버 태스크가 취소되었습니다.")
        except KeyboardInterrupt:
            print("KeyboardInterrupt 발생, 안전하게 종료합니다...")
            
if __name__ == "__main__":
    asyncio.run(main())
