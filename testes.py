from bitcointrade import Bitcointrade

#careful, don't expose your api key
exchange = Bitcointrade('BRLLTC','token')


ticker = exchange.ticker()
orders = exchange.orders()
trades = exchange.trades('2019-01-01T00:00:00-03:00','2019-01-02T23:59:59-03:00',1)

balance = exchange.balance()

print('preço estimado: ')
print(exchange.estimated_price(2,'buy'))
print('resumo: ')
print(exchange.summary())




