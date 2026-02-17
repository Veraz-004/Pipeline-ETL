import logging
from pathlib import Path
from extract import Extract
from transform import Transform
from load import Load
from analysis import lucro_max, receita_total, dia_quantidade, dia_receita

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
def rodar_pipeline():
    silver, gold, arquivos = Extract(log)
    arqvs, arqvs_gold = Transform(arquivos)
    Load(arqvs, arqvs_gold, silver, gold, log)
    return arqvs, gold

def rodar_analysis(arqvs):
    if arqvs != []:
        lucro_max(gold, log)
        receita_total(gold, log)
        dia_quantidade(gold, log)
        dia_receita(gold, log)


if __name__ == "__main__":
    arqvs, gold=rodar_pipeline()
    rodar_analysis(arqvs)