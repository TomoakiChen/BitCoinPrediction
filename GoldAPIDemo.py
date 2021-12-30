from MatalPrice.GoldAPI.Client import GoldAPIClient

client = GoldAPIClient("goldapi-14sk9jtkxqaji16-io")
datas = client.getJsonStatus()
# datas = client.getJsonPrice("20211228")
print(datas)
