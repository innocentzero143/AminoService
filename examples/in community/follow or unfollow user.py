import AminoService


client = AminoService.Client()
client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
subclient = AminoService.SubClient(aminoId="AMINO ID", profile=client.profile)

    # Follow
subclient.follow("USER ID")

    # Unfollow
subclient.unfollow("USER ID")

