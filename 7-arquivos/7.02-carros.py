import csv

dados_tabela = [
    ["BAIRRO","CIDADE","ESTADO","CEP"],
    ["Jardim Belval","Barueri","SP","06420320"],
    ["Parque Santana I","Santana de Parnaíba","SP","06325800"],
    ["Suburbano","Itapevi","SP","06542300"],
    ["Centro","Jandira","SP","05230000"]
]

with open("7.02-cidades.csv","w",encoding="utf-8",newline="") as arquivo_csv:
    escrevendo = csv.writer(arquivo_csv)
    escrevendo.writerows(dados_tabela)
    