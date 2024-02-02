import amino
import asyncio

async def main():
    client = amino.AsyncClient()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
    subclient = await amino.AsyncSubClient(aminoId="AMINO ID", profile=client.profile)

    await subclient.delete_blog("BLOG ID")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())