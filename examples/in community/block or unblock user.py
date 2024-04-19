import AminoService


client = AminoService.Client()
client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
subclient = AminoService.SubClient(aminoId="AMINO ID", profile=client.profile)

# Block
subclient.block('USER ID')

# Unblock
subclient.unblock('USER ID')
