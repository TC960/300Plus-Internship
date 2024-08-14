from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re 
driver = webdriver.Chrome()
website = "https://platform.openai.com/playground/chat?models=gpt-4o-mini"

driver.get(website)

instructions = driver.find_element(By.XPATH, """//*[@id="root"]/main/div/div/div/
             div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div[2]
             /div/div/div/div/div//*[@id="root"]/main/div/div/div/div/div/div/
             div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/
             div/div""")

instructions.send_keys("""I am providing you with some answers to questions asked 
             during an interview. Give me a score out of 100; the lower the score, 
             the more original the answer, and vice versa. The only required 
             output is of the form: "Score: [score that you will assign]" """)

userData = driver.find_element(By.XPATH,""" //*[@id="root"]/main/div/div/div/
             div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]
             /div/div/div/div/div""")


with open("FinalOutput.txt","r") as file:
    data = file.read()

userData.send_keys(data)
userData.send_keys(Keys.chord(Keys.COMMAND, Keys.ENTER))


driver.implicitly_wait(15) 

page_source = driver.page_source
pattern = r'Score:\s*(\d+)'

match = re.search(pattern, page_source)
if match:
    score = match.group(1)
    print(f'Score: {score}')
else:
    print("Score not found")

 