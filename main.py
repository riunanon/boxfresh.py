import asyncio
import aiohttp
async def send(slug, content):
  h = {'Content-Type': 'application/x-www-form-urlencoded'}
  d = {'slug': slug, 'content': content}
  async with aiohttp.ClientSession() as session:
    async with session.post('https://boxfresh.jp/apppage.php',headers=h,data=d) as r:
      if r.status == 200:
        print('success')
      else:
        print('Error')
async def ready(slug,content):
  while True:
    await send(slug,content)
loop = asyncio.get_event_loop()
slug=input('urlかidを入力してください:').replace('https://box-fresh.jp/index.php?id=','').split('&')[0]
content=input('質問を入力してください:')
for i in range(10):#非同期ループをいくつ作成するか
  asyncio.ensure_future(ready(slug,content))
loop.run_forever()
