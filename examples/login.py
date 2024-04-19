import AminoService

client = AminoService.Client()
client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
print(client.profile.nickname)

