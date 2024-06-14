# main.py
import sys
from data_extraction.table_extraction import extract_tables, save_tables
from data_extraction.toponimia_extraction import extract_state_links, extract_toponimia, save_toponimia
from data_extraction.extract_us_states import USStatesExtractor
from data_extraction.login_wikipedia import WikipediaLogin
from utils.webdriver_setup import get_webdriver

def main(browser='chrome'):

    driver = get_webdriver(browser)
    # Initialize the WebDriver based on the specified browser
    try:
        # Login to Wikipedia
        wikipedia_login = WikipediaLogin(driver)
        if not wikipedia_login.login():
            print("Failed to log in to Wikipedia.")
            return
        
        # Extract and save table data
        first_table_df, second_table_df, third_table_df = extract_tables(driver)
        save_tables(first_table_df, second_table_df, third_table_df)

        # Extract state links and toponimia data
        state_links = extract_state_links(driver)
        toponimia_data = extract_toponimia(driver, state_links)
        save_toponimia(state_links, toponimia_data)

        # Extract US states data
        us_states_extractor = USStatesExtractor(driver)
        us_states_extractor.navigate_to_us_states_page()
        df_us_states = us_states_extractor.extract_us_states_data()
        if df_us_states is not None:
            df_etimologia = us_states_extractor.extract_etimologia(df_us_states)
            us_states_extractor.save_to_excel(df_us_states, df_etimologia)

        # Logout from Wikipedia
        wikipedia_login.logout()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    # Accept the browser type from command line arguments
    browser = sys.argv[1] if len(sys.argv) > 1 else 'chrome'
    main(browser)
