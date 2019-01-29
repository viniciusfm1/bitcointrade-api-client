# -*- coding: utf-8 -*-
"""
Comunicação com a Exchange de criptomoedas Bitcoin Trade através da sua API
Vinícius Machado <viniciusfm1@outlook.com>

    Referências:
        https://apidocs.bitcointrade.com.br/
"""

import requests

class Bitcointrade:
    def __init__(self, market, apitoken):
        self.par = market
        self.market = market
        self.url = 'https://api.bitcointrade.com.br/v2/public/{par}/{method}/'
        self.privateUrl = 'https://api.bitcointrade.com.br/v2'
        self.publicUrl = 'https://api.bitcointrade.com.br/v2/public/{market}/{command}/'
        self.apitoken = apitoken
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiToken {apitoken}'.format(apitoken = self.apitoken)
        }

    def post(self, data):
        pass

    def get(self, command):
        response = requests.get(self.publicUrl.format(market = self.market, command = command))
        return response.json()

    def ticker(self):
        """Retorna informações com o resumo das últimas 24 horas de negociações."""
        command = 'ticker'
        return self.get(command)

    def orders(self):
        """Retorna lista de ordens ativas atualmente no book de ofertas"""
        command = 'orders'
        return self.get(command)

    def trades(self, start_time, end_time, page_size):
        """Retorna lista de trades baseados nos critérios de pesquisa"""
        command = 'trades?start_time={start_time}&end_time={end_time}&page_size={page_size}&current_page=1'.format(
            start_time = start_time, end_time = end_time, page_size = page_size
        )
        return self.get()

    def balance(self):

        """Lista de carteiras e saldos"""

        response = requests.get(self.privateUrl + '/wallets/balance', headers = self.headers)
        return response.json()

    def bookOrders(self):
        """Retorna informações das ordens de compra e venda e executadas 
        do livro de ofertas de uma determinada moeda"""

        response = requests.get(self.privateUrl + '/market?pair={pair}'.format(self.market), headers = self.headers)
        return response.json() 

    def estimate(self, amount, typeorder):
        
        """Retorna o preço estimado de uma determinada quantidade de moeda"""

        response = requests.get(self.privateUrl + '/market/estimated_price?amount={amount}&pair={par}&type={typeorder}'.format(
            amount = amount, par = self.par, typeorder = typeorder), headers = self.headers)
        return response.json()

    def createOrder(self, command, amount, price):
        """Cria uma ordem de compra ou venda"""

        data = {'pair': self.market, 'type': command, 'subtype': 'market', 'amount': amount, 'unit_price': price, 'request_price': amount * price }
        response = requests.post(self.privateUrl + '/market/create_order', data = data, headers = self.headers)
        return response.json()
