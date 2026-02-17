from pathlib import Path
import logging
log=logging.getLogger(__name__)
#* Neste arquivo, vamos criar atálhos para os diretórios e pegar todos os dados
def Extract(log):
    bronze=Path("data/bronze")
    silver=Path("data/silver")
    gold=Path("data/gold")
    bronze.mkdir(parents=True, exist_ok=True)
    silver.mkdir(parents=True, exist_ok=True)
    gold.mkdir(parents=True, exist_ok=True)
    try:
        arquivos=sorted(bronze.glob("*.csv"))
    except:
        log.error("Arquivos .csv não encontrados")
    return silver, gold, arquivos

