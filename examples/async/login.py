import amino
import asyncio

async def main():
    client = amino.AsyncClient()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")

    print(client.profile.nickname)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())