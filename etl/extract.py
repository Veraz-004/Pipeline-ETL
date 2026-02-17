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
    
    arquivos=sorted(bronze.glob("*.csv"))
    if not arquivos:
        log.error("Nenhum arquivo .csv encontrado na pasta: data/bronze")
    return silver, gold, arquivos

