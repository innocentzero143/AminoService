import AminoService
import asyncio

async def main():
    client = AminoService.Client()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")

    # Send Images
    with open("file.png", "rb") as file:
        await client.send_message(chatId="CHAT ID", file=file)

    # Send Audios
    with open("file.mp3", "rb") as file:
        await client.send_message(chatId="CHAT ID", file=file, fileType="audio")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())