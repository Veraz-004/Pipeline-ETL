from pathlib import Path

def relatorio(produto, receita_total, dia_max_quantidade, dia_max_receita):
    Path('reports').mkdir(parents=True, exist_ok=True)
    relatorio=f"""
    === RELATÓRIO ===
    
    O produto mais vendido é: {produto}
    A receita gerada por todas as vendas é: {receita_total}
    O dia que teve mais vendas é: {dia_max_quantidade}
    O dia que teve maior montante é: {dia_max_receita}
    """
    with open('reports/relatórios.txt', 'w') as arquivo:
        arquivo.write(relatorio)