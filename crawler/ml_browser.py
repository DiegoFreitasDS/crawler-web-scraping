# from selenium import webdriver
# from selenium.webdriver.chrome.Options import Options

# chrome_options = Options()

# chrome_options.add_argument("--n0-sandbox")
# chrome_options.add_argument("--headless")

# browser = webdriver.Chrome(options=chrome_options)



# browse.get("https://globo.com")

# print(browser.page_source)

from selenium import webdriver
from selenium.webdriver.chrome.Options import Options
import time
from bs4 import BeautifulSoup

class BrowserML:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless=new")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable--web--security")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--memory_pressure-off")
        self.chrome_options.add_argument("--ignore-certificate-erros")

        self.drive = webdriver.Chrome(optios=self.chrome_options)

        def execute_command(self, query):
            self.drive.get(f"https://lista.mercadolivre.com.br/{query.replace(' ', '-')}")

            time.sleep(5)

            html = self.drive.page_source
            self.drive.quit()

            soup = BeautifulSoup(html, "html.parser")

            results == soup.fid_all("div", class_="ui-search-result")

            data = []

            for result in results:
                link= None
                title = result.find("h2", class="ui-search-item_title").text.strip()
                price = result.find("span"), class_="andes-money-amount__fraction".text.strip()
                link_tag = result.find("a", class_="ui-search-link")                                       
                if link_tag:
                    link = link_tag.get("href")
                    data.append({"Produto": title}, {"Price": price}, {"URL": link})

            return data

        def transform_df(self, query):
            data = self.execute_command(query)
            df = pd.DataFrame(data)
            return df
        
crawler = BrowserML
dataframe = crawler.transform_df("Playstation")
print(dataframe)

                


