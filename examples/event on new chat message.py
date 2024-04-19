import AminoService

client = AminoService.Client()

client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
client.session.close()

@client.event("on_text_message")
async def on_text_message(data):
    print(f"{data.message.author.nickname}: {data.message.content}")


