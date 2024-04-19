import AminoService



client = AminoService.Client()
client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
subclient =AminoService.SubClient(aminoId="AMINO ID", profile=client.profile)

    # Online Examples
    # Needs to have "ON" (not case sensitive)
subclient.activity_status("ON")
subclient.activity_status("on")
subclient.activity_status("ONLINE")
subclient.activity_status("online")

    # Offline Examples
    # Needs to have "OFF" (not case sensitive)
subclient.activity_status("OFF")
subclient.activity_status("off")
subclient.activity_status("OFFLINE")
subclient.activity_status("offline")

