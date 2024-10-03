import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import openpyxl
from time import sleep

def driver():
    app = uc.Chrome()
    url = 'https://www.mercadolivre.com.br/apple-iphone-13-256-gb-productred-distribuidor-autorizado/p/MLB1018500853#polycard_client=search-nordic&wid=MLB2627784031&sid=search&searchVariation=MLB1018500853&position=2&search_layout=stack&type=product&tracking_id=05bc62d4-013c-4321-bdb9-7500611e05da'
    
    while True:
    
        app.get(url)

        # aguardar algum elemento para obter os dados

        try:
            elemento = WebDriverWait(app, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'andes-money-amount__fraction'))
            )

            if elemento:
                # obter o preço do produto
                try:
                    preco = app.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[2]').text
                    nome = app.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/h1').text
                    horario = datetime.datetime.now()

                    wb = openpyxl.Workbook()
                    sheet = wb.active
                    sheet.append(["Nome", "Valor", "Data", "Link"])

                    dados = [nome,preco,horario, url]

                    sheet.append(dados)

                    wb.save("Precos.xlsx")
                    # salvar o conteudo dentro de uma planilha excel
                    # campos planilha: nome, data atual, valor, link

                except Exception as e:
                    print(f'Ocorreu um erro: {e}')
            else:
                print('Não localizou o elemento preço')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
        finally:
            print('Processo finalizado, com sucesso...')
            app.quit()
        print('Monitoramento realizado, aguardando 30 minutos para realizar uma nova verificação...')
        sleep(1800)

driver()