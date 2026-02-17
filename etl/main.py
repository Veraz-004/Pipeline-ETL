from extract import Extract
from transform import Transform
from load import Load
from analysis import lucro_max, receita_total, dia_quantidade, dia_receita

#* este arquivo só irá rodar as funções dos outros arquivos
if __name__ == "__main__":
    silver, gold, arquivos = Extract()
    arqvs, arqvs_gold = Transform(arquivos)
    Load(arqvs, arqvs_gold, silver, gold)
    lucro_max(gold)
    receita_total(gold)
    dia_quantidade(gold)
    dia_receita(gold)