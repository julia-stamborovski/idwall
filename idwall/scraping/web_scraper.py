import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from idwall.models import WantedPerson
import requests
from selenium.webdriver.common.by import By
logging.basicConfig(level=logging.INFO)

def scrape_fbi_website():
    fbi_url = 'https://www.fbi.gov/wanted/topten'
    driver.get(fbi_url)
    sleep(5)
    logging.info("Extração de dados do site do FBI iniciada.")

    wanted_persons = driver.find_elements(By.XPATH, '//div[@class="mosaic-grid-cell mosaic-width-full mosaic-position-leftmost col-md-12"]')
    extracted_data = []

    for person in wanted_persons:
        name_wanted = person.find_element(By.XPATH, '//h3[@class="title"]').text
        photo = person.find_element(By.XPATH, '//img').get_attribute('src')

        
        fbi_data = requests.get(f'https://www.fbi.gov/wanted/topten/?name={name_wanted}').json()
        
        description = fbi_data.get('description', '')
        crimes_committed = fbi_data.get('crimes', '')
        crime_type = fbi_data.get('crime_type', '')

        data = {
            'name': name_wanted,
            'photo': photo,
            'physical_description': description,
            'crimes_committed': crimes_committed,
            'crime_type': crime_type
        }

        extracted_data.append(data)
    logging.info("Extração de dados do fbi")
    return extracted_data


def scrape_interpol_website():
    interpol_url = 'https://ws-public.interpol.int/notices/v1/red'
    driver.get(interpol_url)
    sleep(5)
    logging.info("Extração de dados do site da Interpol iniciada.")
  
    wanted_persons = driver.find_elements(By.XPATH, '//div[@class="portal-listing-row ng-star-inserted"]')
    extracted_data = []

    for person in wanted_persons:
        name_wanted = person.find_element_by_xpath('.//h3').text
        photo = person.find_element_by_xpath('.//img').get_attribute('src')

        interpol_data = requests.get(f'https://ws-public.interpol.int/notices/v1/red').json()
        
        nationality = interpol_data.get('nationality', '')
        investigation_status = interpol_data.get('investigation_status', '')

        data = {
            'name': name_wanted,
            'photo': photo,
            'nationality': nationality,
            'investigation_status': investigation_status
        }

        extracted_data.append(data)
    logging.info("Extração de dados do Interpol")
    return extracted_data



chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
logging.info("Iniciando web scraping.")

fbi_data = scrape_fbi_website()
interpol_data = scrape_interpol_website()
logging.info(f"Total de dados extraídos: {len(fbi_data) + len(interpol_data)}")


for data in fbi_data + interpol_data:
    wanted_person = WantedPerson(**data)
    try:
        wanted_person.save()
        logging.info(f"Dados salvos para {wanted_person.name}.")
    except Exception as e:
        logging.error(f"Erro ao salvar dados para {wanted_person.name}: {str(e)}")

logging.info("Finalizando scraping.")

driver.quit()
