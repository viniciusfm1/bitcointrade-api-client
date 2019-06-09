from bitcointrade import Bitcointrade

exchange = Bitcointrade('brlltc','apitoken')

book_orders = exchange.book_orders()

print(book_orders)




