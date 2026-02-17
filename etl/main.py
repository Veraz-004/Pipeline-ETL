import logging
from pathlib import Path
from extract import Extract
from transform import Transform
from load import Load
from analysis import lucro_max, receita_total, dia_quantidade, dia_receita
from relatório import relatorio
Path("logs").mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format=" %(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
    
)
log=logging.getLogger(__name__)

#* este arquivo só irá rodar as funções dos outros arquivos
def rodar_pipeline(log):
    silver, gold, arquivos = Extract(log)
    arqvs, arqvs_gold = Transform(arquivos, log)
    Load(arqvs, arqvs_gold, silver, gold, log)
    return arqvs, gold

def rodar_analysis(arqvs, gold):
    if arqvs:
        produto = lucro_max(gold, log)
        receita_total_var = receita_total(gold, log)
        dia_max_quantidade = dia_quantidade(gold, log)
        dia_max_receita = dia_receita(gold, log)
        return produto, receita_total_var, dia_max_quantidade, dia_max_receita


if __name__ == "__main__":
    arqvs, gold=rodar_pipeline(log)
    produto, receita_total_var, dia_max_quantidade, dia_max_receita = rodar_analysis(arqvs, gold)
    relatorio(produto, receita_total_var, dia_max_quantidade, dia_max_receita)