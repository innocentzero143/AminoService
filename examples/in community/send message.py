import AminoService


client =AminoService.Client()
client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
subclient =AminoService.SubClient(aminoId="AMINO ID", profile=client.profile)
subclient.send_message(chatId="CHAT ID", message="MESSAGE")


