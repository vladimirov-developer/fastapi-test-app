import aiohttp
import time
import asyncio


async def main():
    print('111')
    async with aiohttp.ClientSession() as session:
        print('222')
        client_id = int(time.time() * 1000)
        async with session.ws_connect(f'http://127.0.0.1:8000/chat/ws/{client_id}') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    with open("ws_messages.txt", "a") as file:
                        file.write(f"{msg.data}\n")

asyncio.run(main())
