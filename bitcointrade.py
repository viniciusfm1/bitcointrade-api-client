# -*- coding: utf-8 -*-
"""
Comunicação com a Exchange de criptomoedas Bitcoin Trade através da sua API
Vinícius Machado <viniciusfm1@outlook.com>

    Referências:
        https://bitcointrade.com.br/
        https://apidocs.bitcointrade.com.br/
"""

import requests

class Bitcointrade:
    def __init__(self, market, apitoken):
        self.market = market
        self.privateUrl = 'https://api.bitcointrade.com.br/v2'
        self.publicUrl = 'https://api.bitcointrade.com.br/v2/public/{market}/{command}/'
        self.apitoken = apitoken
        self.headers = {
            'Authorization': 'ApiToken {apitoken}'.format(apitoken = self.apitoken)
        }

    def post(self, data):
        pass

    def get(self, command):
        response = requests.get(self.publicUrl.format(market = self.market, command = command))
        response.close()
        return response.json()

    def ticker(self):
        """Retorna informações com o resumo das últimas 24 horas de negociações."""
        command = 'ticker'
        return self.get(command)

    def orders(self):
        """Retorna lista de ordens ativas atualmente no book de ofertas."""
        command = 'orders'
        return self.get(command)

    def trades(self, start_time, end_time, page_size):
        """Retorna lista de trades baseados nos critérios de pesquisa."""
        command = 'trades?start_time={start_time}&end_time={end_time}&page_size={page_size}&current_page=1'.format(
            start_time = start_time, end_time = end_time, page_size = page_size
        )
        return self.get(command)

    def balance(self):
        """Lista de carteiras e saldos."""

        response = requests.get(self.privateUrl + '/wallets/balance', headers = self.headers)
        return response.json()

    def book_orders(self):
        """Retorna informações das ordens de compra e venda e executadas do livro de ofertas de uma determinada moeda."""

        response = requests.get(self.privateUrl + '/market?pair={pair}'.format(pair = self.market),headers = self.headers)
        return response.json() 

    def summary(self):
        """Retorna o resumo de uma moeda nas últimas 24 horas."""

        response = requests.get(self.privateUrl + '/market/summary?pair={pair}'.format(self.market), headers = self.headers)
        return response.json()

    def estimate(self, amount, typeorder):
        """Retorna o preço estimado de uma determinada quantidade de moeda."""

        response = requests.get(self.privateUrl + '/market/estimated_price?amount={amount}&pair={pair}&type={typeorder}'.format(
            amount = amount, pair = self.market, typeorder = typeorder), headers = self.headers)
        return response.json()

    def create_order(self, command, amount, price):
        """Cria uma ordem de compra ou venda."""

        data = {'pair': self.market, 'type': command, 'subtype': 'limited', 'amount': amount, 'unit_price': price, 'request_price': amount * price }
        response = requests.post(self.privateUrl + '/market/create_order', data = data, headers = self.headers)
        return response.json()

    def user_orders(self, status, start_date, end_date, pair, type_order):
        """Retorna informações das ordens de compra e venda do usuário."""
        
        response = requests.get(self.privateUrl + '/market/user_orders/list?status={status}&start_date={start_date}&end_date={end_date}&pair={pair}&type={type}&page_size=50'.format(status = status, start_date = start_date, end_date = end_date, pair = self.market, type = type_order), headers = self.headers)
        return response.json()

    def cancel_order(self, orderId):
        """Cancela uma ordem de compra ou venda."""
        
        data = {'id': orderId}
        response = requests.delete(self.privateUrl + '/market/user_orders', data = data, headers = self.headers)
        return response.json()

