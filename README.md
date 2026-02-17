# 📊 Pipeline ETL + Análise + Relatório Automático

Este projeto implementa uma pipeline completa de dados em Python, incluindo:

* Extração de múltiplos arquivos CSV
* Limpeza e transformação dos dados
* Geração de métricas analíticas
* Logging da execução
* Criação automática de relatório em arquivo de texto

O objetivo é simular um fluxo real de engenharia de dados e Business Intelligence.

---

## 🧠 Fluxo da Pipeline

### 🥉 Extract

Busca arquivos CSV na pasta `data/bronze/` e garante a existência das pastas:

* `data/bronze`
* `data/silver`
* `data/gold`

Se nenhum arquivo for encontrado, a pipeline registra erro no log.

---

### 🥈 Transform

Limpeza dos dados:

* Conversão de tipos
* Remoção de valores inválidos
* Remoção de duplicatas
* Tratamento de diferentes encodings e separadores

Criação dos dados analíticos:

* receita = preço × quantidade
* custo_total = custo × quantidade
* lucro_total = (preço − custo) × quantidade

---

### 🥇 Load

Salva os resultados:

* `data/silver/silver.csv` → dados limpos
* `data/gold/gold.csv` → dados prontos para análise

---

## 📈 Análises Geradas

A partir dos dados gold:

* Produto mais lucrativo
* Receita total
* Dia com maior quantidade vendida
* Dia com maior receita

---

## 📄 Relatório Automático

Após a análise, o sistema gera:

```
reports/relatórios.txt
```

Contendo:

* Produto mais vendido
* Receita total
* Dia com mais vendas
* Dia com maior montante

---

## 🧾 Logging

A execução da pipeline é registrada em:

```
logs/pipeline.log
```

Incluindo:

* etapas executadas
* arquivos processados
* avisos e erros

---

## 📂 Estrutura do Projeto

```
ETL_base/
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── reports/
├── logs/
│
├── extract.py
├── transform.py
├── load.py
├── analysis.py
├── relatório.py
├── main.py
└── requirements.txt
```

---

## ▶️ Como Executar

### 1️⃣ Instalar dependências

```
pip install -r requirements.txt
```

### 2️⃣ Adicionar arquivos CSV

Coloque os arquivos em:

```
data/bronze/
```

### 3️⃣ Executar a pipeline

```
python main.py
```

---

## 🎯 Objetivo

Projeto desenvolvido para prática de:

* Engenharia de Dados
* Automação com Python
* ETL
* Análise de dados
* Logging de sistemas

---

## 👨‍💻 Autor

Projeto desenvolvido para estudos e portfólio.
