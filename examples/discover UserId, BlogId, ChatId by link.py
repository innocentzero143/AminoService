import AminoService


client = AminoService.Client()
client.login(email="YOUR EMAIL", password="YOUR PASSWORD")

objectId =client.get_from_code("https://aminoapps.com/p/EXAMPLE").objectId
print(objectId)

