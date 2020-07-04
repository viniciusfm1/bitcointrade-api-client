from bitcointrade import Bitcointrade

exchange = Bitcointrade('brlltc','apitoken')

ticker = exchange.ticker()

print(ticker)




