from bitcointrade import Bitcointrade

versao ='v2'
moeda ='LTC'
par = 'BRL' + moeda
exchange = Bitcointrade(versao,par)

ticker = exchange.ticker()

if ticker['message'] == None:
    ticker = ticker['data']


print('última negociação :',ticker['last'])
print('volume 24h        :',ticker['volume'])
print('compra            :',ticker['buy'])
print('venda             :',ticker['sell'])

