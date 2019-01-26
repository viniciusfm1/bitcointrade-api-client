# -*- coding: utf-8 -*-
"""
Comunicação com a Exchange de criptomoedas Bitcoin Trade através da sua API
Vinícius Machado <viniciusfm1@outlook.com>

    Referências:
        https://apidocs.bitcointrade.com.br/
"""

import requests
import datetime

class Bitcointrade:
    def __init__(self, par, apitoken):
        self.par = par
        self.url = 'https://api.bitcointrade.com.br/v2/public/{par}/{method}/'
        self.privateUrl = 'https://api.bitcointrade.com.br/v2'
        self.apitoken = apitoken
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ApiToken {apitoken}'.format(apitoken = self.apitoken)
        }

    def ticker(self, method='ticker'):
        
        """Retorna informações com o resumo das últimas 24 horas de negociações."""

        response = requests.get(self.url.format(par = self.par, method = method))
        return response.json()

    def orders(self, method='orders'):
        
        """Retorna lista de ordens ativas atualmente no book de ofertas"""

        response = requests.get(self.url.format(par = self.par, method = method))
        return response.json()

    def trades(self, method = 'trades?start_time={start_time}&end_time={end_time}&page_size={page_size}&current_page=1'):
        
        """Retorna lista de trades baseados nos critérios de pesquisa"""

        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now()

        response = requests.get(self.url.format(par = self.par, method = method, 
        start_time = start_time, end_time = end_time, page_size = 1))
        return response.url

    def balance(self):

        """Lista de carteiras e saldos"""

        response = requests.get(self.privateUrl + '/wallets/balance', headers = self.headers)
        return response.json()
        
    def estimate(self, amount, typeorder):
        
        """Retorna o preço estimado de uma determinada quantidade de moeda"""

        response = requests.get(self.privateUrl + '/market/estimated_price?amount={amount}&pair={par}&type={typeorder}'.format(
            amount = amount, par = self.par, typeorder = typeorder), headers = self.headers)
        return response.json()
