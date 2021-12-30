from MatalPrice.MetalsAPI.Client import MatalsAPIClient, GoldPriceClient

client = MatalsAPIClient("b7aujpu9wa73t64sx0p4gwiragdv1pziw6029efu8n52xgm87hbcqq632o9l")
# symbol_data = client.getDesigCurrencySymbolDataByCode("XAU")
# print("symbol.label= " + symbol_data.getLabel())

# datas = client.getJsonSymbolsData()

# json_time_sereis_datas = client.getJsonTimeSeriesData(base="XAU", symbols=["USD"]) # 照順序是可以如同java代入param的
# print(json_time_sereis_datas)

# datas = client.getDesigCurrencySymbolDataByLabel("Gold")
# for data in datas:
#     print("data.label= " + data.getLabel())

gold_price_client = GoldPriceClient("b7aujpu9wa73t64sx0p4gwiragdv1pziw6029efu8n52xgm87hbcqq632o9l")
prices = gold_price_client.getJsonPrices(start_date="2021-12-21")
print(prices)
