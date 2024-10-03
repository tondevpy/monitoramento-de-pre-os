# Monitoramento de Preços - Mercado Livre

Este projeto é um **monitorador de preços** que verifica o preço de um produto no **Mercado Livre** a cada 30 minutos e registra as informações em uma planilha Excel. O monitoramento é feito através da biblioteca **Selenium** e a planilha é gerada com a **openpyxl**.

## Descrição

O objetivo do projeto é automatizar a verificação do preço de um produto em uma página específica do Mercado Livre. O script acessa a página, obtém o preço e outras informações como nome do produto e data/hora da coleta, e registra esses dados em um arquivo Excel. O processo se repete automaticamente a cada 30 minutos.

### Principais Funcionalidades

- Acessar automaticamente uma página do Mercado Livre usando **Selenium**.
- Extrair informações como nome do produto e preço.
- Registrar as informações coletadas em uma planilha Excel com as seguintes colunas:
  - Nome do produto
  - Preço
  - Data e hora da coleta
  - Link do produto
- Executar o processo de verificação de preços a cada 30 minutos de forma automática.

## Requisitos

Antes de rodar o projeto, você precisa instalar algumas bibliotecas. Para isso, utilize o seguinte comando:

```bash
pip install undetected-chromedriver selenium openpyxl