import amino
import asyncio

async def main():
    client = amino.AsyncClient()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
    subclient = await amino.AsyncSubClient(aminoId="AMINO ID", profile=client.profile)

    # Follow
    await subclient.follow("USER ID")

    # Unfollow
    await subclient.unfollow("USER ID")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
