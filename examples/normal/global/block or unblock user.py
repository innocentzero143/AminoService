import AminoService

client = AminoService.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')

# Follow
client.block('USER ID')

# Unfollow
client.unblock('USER ID')