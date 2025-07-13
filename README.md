# 📊 Captador de Temperatura de São Paulo

Este projeto consiste em uma automação com Python que coleta informações de **temperatura** e **umidade** do site [ClimaTempo](https://www.climatempo.com.br/) para a cidade de **São Paulo**, e registra os dados em uma planilha Excel, incluindo **data e hora da coleta**.

---

## 📌 Objetivo

Automatizar o processo de consulta da previsão do tempo, permitindo a coleta periódica e o armazenamento dos dados em planilhas para histórico e visualização futura (ex: gráficos).

---

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Selenium](https://pypi.org/project/selenium/)
- [OpenPyXL](https://pypi.org/project/openpyxl/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (interface gráfica)

---

## ⚙️ Como executar

### Pré-requisitos:

- Python 3.10+
- Chrome instalado
- Instale os pacotes:

```bash
pip install selenium
pip install openpyxl

## Iniciar a aplicação
python main.py

Clique no botão "Buscar previsão"

A aplicação abrirá o site, coletará os dados e gravará no arquivo Excel clima_sao_paulo.xlsx.

O Excel gerado conterá colunas com:

Data/Hora da coleta
Cidade
Temperatura mínima/máxima
Umidade mínima/máxima