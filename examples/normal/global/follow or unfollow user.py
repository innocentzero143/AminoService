import AminoService

client = AminoService.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')

# Follow
client.follow('USER ID')

# Unfollow
client.unfollow('USER ID')