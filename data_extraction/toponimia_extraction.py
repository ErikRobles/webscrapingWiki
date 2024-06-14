import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def extract_state_links(driver):
    state_links = []
    rows = driver.find_elements(By.XPATH, '//table[1]//tr')  # Ensure correct table selection
    for row in rows[2:]:  # Skip header rows
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) > 0:
            try:
                link = cells[3].find_element(By.TAG_NAME, 'a')  # Adjusted to the correct cell containing the state link
                state_name = link.text.strip()
                state_url = link.get_attribute('href')  # URL remains encoded

                # Remove any <sup> elements from the state name
                sup_elements = link.find_elements(By.XPATH, ".//sup")
                for sup in sup_elements:
                    driver.execute_script("arguments[0].remove();", sup)

                state_name = link.text.strip()  # Re-fetch the state name after removing <sup> elements

                # Ensure only valid state names are processed
                if state_name and state_url and state_name not in ["nota", "", None]:
                    state_links.append((state_name, state_url))
                    print(f"Extracted link: State: {state_name}, URL: {state_url}")
            except Exception as e:
                print(f"Error extracting link from row: {e}")
    print(f"Extracted {len(state_links)} state links.")
    return state_links

def extract_toponimia(driver, state_links):
    toponimia_data = []

    for state_name, state_url in state_links:
        print(f"Extracting 'Toponimia' for {state_name}...")
        driver.get(state_url)
        time.sleep(5)

        xpaths = [
            "//span[@id='Toponimia']/following::p[1]",
            "//span[contains(@id, 'Toponimia')]/following::p[1]",
            "//span[contains(text(), 'Toponimia')]/following::p[1]",
            "//span[contains(text(), 'Toponimia y gentilicio')]/following::p[1]",
            "//h2[span[@id='Toponimia']]/following-sibling::p[1]",
            "//h2[span[contains(@id, 'Toponimia')]]/following-sibling::p[1]",
            "//h2[span[contains(text(), 'Toponimia')]]/following-sibling::p[1]",
            "//h2[span[contains(text(), 'Toponimia y gentilicio')]]/following-sibling::p[1]",
            "//h3[span[@id='Toponimia']]/following-sibling::p[1]",
            "//h3[span[contains(@id, 'Toponimia')]]/following-sibling::p[1]",
            "//h3[span[contains(text(), 'Toponimia')]]/following-sibling::p[1]",
            "//h3[span[contains(text(), 'Toponimia y gentilicio')]]/following-sibling::p[1]",
            "//h4[span[@id='Toponimia']]/following-sibling::p[1]",
            "//h4[span[contains(@id, 'Toponimia')]]/following-sibling::p[1]",
            "//h4[span[contains(text(), 'Toponimia')]]/following-sibling::p[1]",
            "//h4[span[contains(text(), 'Toponimia y gentilicio')]]/following-sibling::p[1]",
            "//p[contains(., 'Toponimia')]"
        ]

        toponimia_text = None
        for xpath in xpaths:
            try:
                toponimia_section = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                toponimia_text = toponimia_section.text.strip()
                if toponimia_text:
                    break
            except:
                continue

        if toponimia_text and 'municipios' not in toponimia_text:
            toponimia_data.append([state_name, toponimia_text])
            print(f"Extracted 'Toponimia' for {state_name}.")
        else:
            print(f"'Toponimia' section not found or incorrect for {state_name}.")
            toponimia_data.append([state_name, ""])

    return toponimia_data

def save_toponimia(state_links, toponimia_data):
    df_state_links = pd.DataFrame(state_links, columns=["Entidad", "Link"])
    df_toponimia = pd.DataFrame(toponimia_data, columns=["Entidad", "Toponimia"])
    df_toponimia = df_toponimia.drop_duplicates(subset=["Entidad"])

    with pd.ExcelWriter('mexico_toponimia.xlsx') as writer:
        df_state_links.to_excel(writer, sheet_name='State Links', index=False)
        df_toponimia.to_excel(writer, sheet_name='Toponimia', index=False)

    print("Toponimia extraction and file creation successful")
