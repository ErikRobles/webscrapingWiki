import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import StringIO

def extract_tables(driver):
    driver.get("https://es.wikipedia.org/wiki/Anexo:Entidades_federativas_de_M%C3%A9xico_por_superficie,_poblaci%C3%B3n_y_densidad")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="firstHeading"]')))
    print("Page loaded successfully")

    tables = driver.find_elements(By.TAG_NAME, "table")
    dfs = []
    for index, table in enumerate(tables):
        html_table = table.get_attribute('outerHTML')
        df = pd.read_html(StringIO(html_table))[0]
        dfs.append(df)

    first_table_df = dfs[0]

    # Remove unnecessary rows and columns
    first_table_df = first_table_df.drop([0, 1])  # Drop the first two rows
    first_table_df.columns = [' '.join(col).strip() for col in first_table_df.columns.values]
    first_table_df = first_table_df.iloc[:, [3, 4, 6, 7]]
    first_table_df.columns = [
        'Entidad', 
        'Superficie (km²)', 
        'Población (2020)', 
        'Densidad (hab./km²)'
    ]

    print("First table columns after cleaning:", first_table_df.columns)

    second_table_df = dfs[1]
    print("Second table columns before cleaning:", second_table_df.columns)
    second_table_df = second_table_df.drop(columns=second_table_df.columns[0])  # Drop the first column (Pos)
    second_table_df.columns = ['Entidad', '2020', '2010', '2000', '1990', '1980', '1970', '1960', '1950', '1940', '1930', '1921', '1910']

    third_table_df = dfs[2]
    print("Third table columns before cleaning:", third_table_df.columns)
    third_table_df = third_table_df.drop(columns=third_table_df.columns[0])  # Drop the first column (Pos)
    third_table_df.columns = ['Entidad', '2010', '2015', '2020', '2025', '2030']

    return first_table_df, second_table_df, third_table_df

def save_tables(first_table_df, second_table_df, third_table_df):
    with pd.ExcelWriter('mexico_population_data.xlsx') as writer:
        first_table_df.to_excel(writer, sheet_name='Superficie_Poblacion_Densidad', index=False)
        second_table_df.to_excel(writer, sheet_name='Poblacion_Historica', index=False)
        third_table_df.to_excel(writer, sheet_name='Poblacion_Futura', index=False)

    print("Table data extraction and file creation successful")
