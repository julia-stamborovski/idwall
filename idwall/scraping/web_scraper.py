import logging
import requests
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from idwall.models import WantedPerson

logging.basicConfig(level=logging.INFO)

logging.info("Iniciando web scraping.")


def scrape_fbi_website():
    driver = uc.Chrome()
    driver.get("https://www.fbi.gov/wanted/cyber")
    sleep(5)
    logging.info("Extração de dados do site do FBI iniciada.")

    wanted_persons = driver.find_elements(By.CLASS_NAME, "portal-type-person")
    extracted_data = []

    for person in wanted_persons:
        title_element = person.find_element(By.CSS_SELECTOR, "h3 > a")

        driver.execute_script("arguments[0].scrollIntoView(true);", title_element)
        sleep(1)

        driver.execute_script("arguments[0].click();", title_element)
        sleep(2)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "wanted-person-wrapper"))
        )
        wanted_persons_details = driver.find_elements(
            By.CLASS_NAME, "wanted-person-wrapper"
        )
        name_wanted_details = (
            wanted_persons_details[0]
            .find_element(By.CLASS_NAME, "documentFirstHeading")
            .text
        )
        summary = wanted_persons_details[0].find_element(By.CLASS_NAME, "summary").text
        image = (
            wanted_persons_details[0]
            .find_element(By.TAG_NAME, "img")
            .get_attribute("src")
        )

        sleep(2)
        driver.execute_script("window.history.go(-1)")
        sleep(2)

        data = {
            "name": name_wanted_details,
            "crimes_committed": summary,
            "photo": image,
        }

        print(
            "Nome",
            data["name"],
            "\n" "Descrição do crime:",
            data["crimes_committed"],
            "\n" "Imagem",
            data["photo"],
        )
        extracted_data.append(data)

        save_in_database = WantedPerson(
            name=data["name"],
            photo=data["photo"],
            crimes_committed=data["crimes_committed"],
        )
        save_in_database.save()

    driver.quit()

    logging.info("Extração de dados do FBI concluída.")
    return extracted_data


extracted_data = scrape_fbi_website()

logging.info(f"Total de dados extraídos: {len(extracted_data)}")

logging.info("Finalizando scraping.")
