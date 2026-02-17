import pandas as pd
from pathlib import Path

gold=Path("data/gold")
def lucro_max(gold):
    df=pd.read_csv(gold/"gold.csv")
    lucro_max=df['lucro_total'].max() 
    linha=df[df['lucro_total'] == lucro_max]
    produto = linha['produto'].iloc[0]
    print(f"O produto mais vendido é: {produto}")

def receita_total(gold):
    df=pd.read_csv(gold/'gold.csv')
    receita_total=df['receita'].sum()
    print(f'A soma das receitas é: {receita_total}')

def dia_quantidade(gold):
    df=pd.read_csv(gold/"gold.csv")
    vendas_por_dia= df.groupby('data')['quantidade'].sum()
    dia_max=vendas_por_dia.idxmax()
    print(f"O dia que teve mais vendas foi: {dia_max}")

def dia_receita(gold):
    df=pd.read_csv(gold/'gold.csv')
    receita_por_dia=df.groupby('data')['quantidade'].sum()
    dia_max=receita_por_dia.idxmax()
    print(f"O dia com maior receita é: {dia_max}")