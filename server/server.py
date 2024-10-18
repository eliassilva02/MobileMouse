import asyncio
import json
from websockets.asyncio.server import serve
from touch import TouchPad

HOST: str = '0.0.0.0'
PORT: int = 2345

async def websocket_handler(websocket):
    async for message in websocket: 
        touch_pad = TouchPad(json.loads(message.encode()))
        
        if 'click' in touch_pad.data:
            # await touch_pad.click()
            continue
        
        await touch_pad.move()

async def main():
    async with serve(websocket_handler, HOST, PORT):
        await asyncio.get_event_loop().create_future()

asyncio.run(main())