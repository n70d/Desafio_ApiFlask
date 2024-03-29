# -*- coding: utf-8 -*-
"""flask_api.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11HtXpmo72lUtfAvIo5QeibUAPiVDMRUW
"""

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
tabela = pd.read_excel('Vendas.xlsx')

@app.route("/")
def fat():
    faturamento = tabela['Valor Final'].sum()
    return jsonify({"Faturamento": float(faturamento)})  # Converte o faturamento para float antes de retornar

@app.route("/vendas/produtos")
def vendas_produtos():
    tabela_vendas_produtos = tabela.groupby("Produto")["Valor Final"].sum().reset_index()
    dic_vendas_produtos = tabela_vendas_produtos.set_index("Produto").to_dict()["Valor Final"]
    return jsonify(dic_vendas_produtos)

@app.route("/vendas/produtos/<produto>")
def fat_produto_especifico(produto):
    vendas_produto = tabela.groupby("Produto")["Valor Final"].sum()
    if produto in vendas_produto.index:
        return jsonify({produto: float(vendas_produto.loc[produto])})  # Converte o valor do produto para float antes de retornar
    else:
        return jsonify({produto: "Inexistente"})

if __name__ == "__main__":
    app.run(debug=True)