from bitcointrade import Bitcointrade

exchange = Bitcointrade('BRLLTC','apitoken')

ticker = exchange.ticker()

print(ticker)




