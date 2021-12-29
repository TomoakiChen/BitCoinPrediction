from GoldAPI.Client import  GoldAPIClient

client = GoldAPIClient("goldapi-14sk9jtkxqaji16-io")
datas = client.getJsonStatus()
print(datas)
