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
    def __init__(self, versao,par):
        self.versao = versao
        self.par = par
        self.url = 'https://api.bitcointrade.com.br/{versao}/public/{par}/{method}/'
    
    def ticker(self, method='ticker'):
        
        """Retorna informações com o resumo das últimas 24 horas de negociações."""

        response = requests.get(self.url.format(versao = self.versao, par = self.par, method = method))
        return response.json()

    def orders(self, method='orders'):
        
        """Retorna lista de ordens ativas atualmente no book de ofertas"""

        response = requests.get(self.url.format(versao = self.versao, par = self.par, method = method))
        return response.json()

    def trades(self, method = 'trades?start_time={start_time}&end_time={end_time}&page_size={page_size}&current_page=1'):
        
        """Retorna lista de trades baseados nos critérios de pesquisa"""

        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now()
        page_size = 1

        response = requests.get(self.url.format(versao = self.versao, par = self.par, method = method, 
        start_time = start_time, end_time = end_time, page_size = page_size))
        return response.url

    def balance(self):
        pass
