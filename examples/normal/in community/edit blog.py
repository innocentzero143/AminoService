import AminoService

client = AminoService.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')
subclient = AminoService.SubClient(comId='COMMUNITY ID', profile=client.profile)

subclient.edit_blog('BLOG ID', 'TITLE', 'CONTENT')