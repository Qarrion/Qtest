# python -m s

import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f"받은 메시지: {message}")
        await websocket.send(f"서버 응답: {message}")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("웹소켓 서버 실행 중...")

        try:
            await asyncio.Future()
        except asyncio.CancelledError:
            print("서버 태스크가 취소되었습니다.")
        except KeyboardInterrupt:
            print("KeyboardInterrupt 발생, 안전하게 종료합니다...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("메인 루프에서 KeyboardInterrupt 감지, 종료합니다.")
