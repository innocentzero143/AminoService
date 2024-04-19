import AminoService


client = AminoService.Client()
client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
subclient = AminoService.SubClient(aminoId="AMINO ID", profile=client.profile)

    # Send Images
with open("file.png", "rb") as file:
    subclient.send_message(chatId="CHAT ID", file=file, fileType="image")
# Send Audios
with open("file.mp3", "rb") as file:
    subclient.send_message(chatId="CHAT ID", file=file, fileType="audio")

