import logging
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from idwall.models import WantedPerson

logging.basicConfig(level=logging.INFO)

def scrape_fbi_website():
    options = FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get('https://www.fbi.gov/wanted/cyber')
    sleep(5)
    logging.info("Extração de dados do site do FBI iniciada.")

    wanted_persons = driver.find_elements(By.CLASS_NAME, 'portal-type-person')
    extracted_data = []

    for person in wanted_persons:
        title_element = person.find_element(By.CSS_SELECTOR, 'h3 > a')
      

        # scroll
        driver.execute_script("arguments[0].scrollIntoView(true);", title_element)
        sleep(1)

        # click
        driver.execute_script("arguments[0].click();", title_element)
        sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'wanted-person-wrapper')))
        #  os dados dos detalhes da pessoa procurada aqui
        wanted_persons_details = driver.find_elements(By.CLASS_NAME, 'wanted-person-wrapper')
        name_wanted_details = wanted_persons_details[0].find_element(By.CLASS_NAME, 'documentFirstHeading').text
        summary = wanted_persons_details[0].find_element(By.CLASS_NAME, 'summary').text
        image = wanted_persons_details[0].find_element(By.TAG_NAME, 'img').get_attribute('src')
        
        
        # back iterando
        driver.execute_script("window.history.go(-1)")
        sleep(2)
       
        data = {
            'name': name_wanted_details,
            'crimes_committed': summary,
            'photo': image,
           
        }
        print ("Nome", data['name'],"\n" "Descrição do crime:", data['crimes_committed'], "\n" "Imagem", data['photo'])
        extracted_data.append(data)

    driver.quit()

    for data in extracted_data:
        print("Nome:", data['name'])
       
        print("------")

    logging.info("Extração de dados do FBI concluída.")
    return extracted_data


""" def scrape_interpol_website():
    driver_path = ChromeDriverManager().install()
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    interpol_url = 'https://ws-public.interpol.int/notices/v1/red'
    driver.get(interpol_url)
    sleep(5)
    logging.info("Extração de dados do site da Interpol iniciada.")

    wanted_persons = driver.find_elements(By.XPATH, '//div[@class="portal-listing-row ng-star-inserted"]')
    extracted_data = []

    for person in wanted_persons:
        name_wanted = person.find_element(By.XPATH, './/h3').text
        photo = person.find_element(By.XPATH, './/img').get_attribute('src')

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

    driver.quit()
    logging.info("Extração de dados da Interpol concluída.")
    return extracted_data """


logging.info("Iniciando web scraping.")

fbi_data = scrape_fbi_website()
#interpol_data = scrape_interpol_website()

logging.info(f"Total de dados extraídos: {len(fbi_data)}")

""" for data in fbi_data :
    wanted_person = WantedPerson(**data)
    try:
        wanted_person.save()
        logging.info(f"Dados salvos para {wanted_person.name}.")
    except Exception as e:
        logging.error(f"Erro ao salvar dados para {wanted_person.name}: {str(e)}") """

logging.info("Finalizando scraping.")