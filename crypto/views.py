from django.shortcuts import render

import requests
import json

def crypto(request):

	# Grab Crypto Price Data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,EOS,LTC,BCH,USDT,BNB,XLM,TRX&tsyms=USD")
	price = json.loads(price_request.content)	

	# Grab Crypto News
	news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	news = json.loads(news_request.content)

	return render(request, 'crypto/crypto.html', {'news': news, 'price': price}) 

def prices(request):

	if request.method == 'POST':
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)	
		return render(request, 'crypto/prices.html', {'quote':quote, 'crypto':crypto})
	else:
		notfound = "Enter a crypto currency symbol into the Navbar Lookup Crypto field above... "
		return render(request, 'crypto/prices.html', {'notfound': notfound})
