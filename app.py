import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import openpyxl
from time import sleep
import os

def driver():
    url = 'https://www.mercadolivre.com.br/apple-iphone-13-256-gb-productred-distribuidor-autorizado/p/MLB1018500853#polycard_client=search-nordic&wid=MLB2627784031&sid=search&searchVariation=MLB1018500853&position=2&search_layout=stack&type=product&tracking_id=05bc62d4-013c-4321-bdb9-7500611e05da'
    
    # Verificar se o arquivo já existe ou criar um novo
    if os.path.exists("Precos.xlsx"):
        wb = openpyxl.load_workbook("Precos.xlsx")
        sheet = wb.active
    else:
        wb = openpyxl.Workbook()
        sheet = wb.active
        # Adicionar cabeçalhos se a planilha for nova
        sheet.append(["Nome", "Valor", "Data", "Link"])

    while True:
        try:
            app = uc.Chrome()
            app.get(url)

            # Aguardar o elemento de preço estar disponível
            elemento = WebDriverWait(app, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'andes-money-amount__fraction'))
            )

            if elemento:
                try:
                    # Extrair preço, nome e horário
                    preco = app.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[2]').text
                    nome = app.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/h1').text
                    horario = datetime.datetime.now()

                    # Adicionar os dados na próxima linha disponível
                    dados = [nome, preco, horario, url]
                    sheet.append(dados)

                    # Salvar o arquivo Excel
                    wb.save("Precos.xlsx")

                except Exception as e:
                    print(f'Ocorreu um erro ao obter os dados: {e}')

            else:
                print('Não localizou o elemento preço')

        except Exception as e:
            print(f'Ocorreu um erro ao carregar a página: {e}')
        finally:
            if 'app' in locals():
                app.quit()

        print('Monitoramento realizado, aguardando 30 minutos para realizar uma nova verificação...')
        sleep(1800)  # Espera 30 minutos

driver()
