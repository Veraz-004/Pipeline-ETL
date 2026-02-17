import pandas as pd
from pathlib import Path
import logging
log=logging.getLogger(__name__)

gold=Path("data/gold")
def lucro_max(gold, log):
    try:
        df=pd.read_csv(gold/"gold.csv")
    except:
        log.error("Nenhum dado localizado em data/gold/gold.csv")
        log.warning("Não foi possível continuar a operação: etl/analysis.py")
    lucro_max=df['lucro_total'].max() 
    linha=df[df['lucro_total'] == lucro_max]
    produto = linha['produto'].iloc[0]
    return produto

def receita_total(gold, log):
    try:
        df=pd.read_csv(gold/'gold.csv')
    except:
        log.error("Nenhum dado localizado em data/gold/gold.csv")
        log.warning("Não foi possível continuar a operação: etl/analysis.py")
    receita_total_var=df['receita'].sum()
    return receita_total_var


def dia_quantidade(gold, log):
    try:
        df=pd.read_csv(gold/"gold.csv")
    except:
        log.error("Nenhum dado localizado em data/gold/gold.csv")
        log.warning("Não foi possível continuar a operação: etl/analysis.py")
    vendas_por_dia= df.groupby('data')['quantidade'].sum()
    dia_max_quantidade=vendas_por_dia.idxmax()
    return dia_max_quantidade

def dia_receita(gold, log):
    try:
        df=pd.read_csv(gold/'gold.csv')
    except:
        log.error("Nenhum dado localizado em data/gold/gold.csv")
        log.warning("Não foi possível continuar a operação: etl/analysis.py")
    receita_por_dia=df.groupby('data')['receita'].sum()
    dia_max_receita=receita_por_dia.idxmax()
    return dia_max_receita