import AminoService
import asyncio

async def main():
    client = AminoService.Client()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")

    chats = await client.get_chat_threads()
    for chatName, chatId in zip(chats.title, chats.chatId):
        print(chatName, chatId)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())