from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Configure the Selenium web driver
path_driver= 'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path_driver)

# Open the webpage
url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
driver.get(url)

# Wait for the desired content to load
driver.implicitly_wait(10)

# Click on the first element to load the page and collect data
driver.find_element_by_xpath('//*[@id="table_id"]/tbody/tr[1]/td[2]/a/b').click()

# Initialize the lists to store the data
quest_no =[]
estd_value_notes=[]
description = []
closing_date = []
owner_no = []
posting_type = []
city_details = []
county_details = []
project_category_code = []
additional_description = []
solicitor_name = []
design_discipline = []
address = []
phone = []
fax_data = []
email_id = []
contact = []

#Loop through the quests
while True:
    try:
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_prevnext_next"]')))
        next_button.click()
        driver.implicitly_wait(10)
        q_no = driver.find_element_by_xpath('//*[@id="view-bid-posting"]/div[2]/div[2]/div/h4/span/b').text.strip()
        quest_no.append(q_no.split(":")[1])
        evn = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]').text.strip()
        estd_value_notes.append(evn)
        desc = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]').text.strip()
        description.append(desc) 
        close_date = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]').text.strip()
        closing_date.append(close_date)
        own_no = driver.find_element_by_xpath('//*[@id="view-bid-posting"]/div[2]/div[2]/div/b[1]').text.strip()
        owner_no.append(own_no.split(":")[1])
        post_type = driver.find_element_by_xpath('//*[@id="view-bid-posting"]/div[2]/div[2]/div/b[3]').text.strip()
        posting_type.append(post_type.split(":")[1])
        city = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[1]/div/table/tbody/tr[1]/td[2]').text.strip()
        city_details.append(city)
        county = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[1]/div/table/tbody/tr[2]/td[2]').text.strip()
        county_details.append(county)
        proj_cat_code = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[2]/td[2]').text.strip()
        project_category_code.append(proj_cat_code)
        add_desc = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[4]/td[2]').text.strip()
        additional_description.append(add_desc)
        sol_name = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[4]/div/table[2]/tbody/tr[1]/td[2]').text.strip()
        solicitor_name.append(sol_name)
        des_disc = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[4]/div/table[2]/tbody/tr[2]/td[2]').text.strip()
        design_discipline.append(des_disc)
        add = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[4]/div/table[2]/tbody/tr[3]/td[2]').text.strip()
        address.append(add)
        ph = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[4]/div/table[2]/tbody/tr[4]/td[2]').text.strip()
        phone.append(ph)
        fax = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[4]/div/table[2]/tbody/tr[5]/td[2]').text.strip()
        fax_data.append(fax)
        cont = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[4]/div/table[2]/tbody/tr[6]/td[2]').text.strip()
        contact.append(cont)
        email = driver.find_element_by_xpath('//*[@id="current_project"]/div/div[4]/div/table[2]/tbody/tr[7]/td[2]/a').text.strip()
        email_id.append(email)   
        
    except:
        break
    
# Create a dictionary from the collected data
data = {"Quest Number":quest_no,
        "Owner Number": owner_no,
        "Closing Date": closing_date,
        "Postin type": posting_type,
        "City": city_details,
        "County": county_details,
        "Estd. Value Notes": estd_value_notes,
        "Project category code": project_category_code,
        "Description": description,
        "Additional description": additional_description,
        "Solicitor name": solicitor_name,
        "Design discipline": additional_description,
        "Address": address,
        "Phone": phone,
        "Fax ": fax_data,
        "Email": email_id,
        "Contact": contact
        }


# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('Quest data.xlsx', index=False)

# Close the driver
driver.quit()
