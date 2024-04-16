import requests
from bs4 import BeautifulSoup
import pandas as pd

class RequestML:
    def execute_command(self, query):
        url = f"https://lista.mercadolivre.com.br/{query.replace(' ', '-')}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }

        response = response.get()

        if response == 200:
            html = response.text()
            soup = BeautifulSoup(html, "html.parser")

        results == soup.fid_all("div", class_="ui-search-result")

        data = []

        for result in results:
            link = None
            title = result.find("h2", class_="ui-search-item_title").text.strip()
            price = result.find("span", class_="andes-money-amount__fraction").text.strip()
            link_tag = result.find("a", class_="ui-search-link")                                       
            if link_tag:
                link = link_tag.get("href")
                data.append({"Produto": title}, {"Price": price}, {"URL": link})

        return data

    def transform_df(self, query):
            data = self.execute_command(query)
            df = pd.DataFrame(data)
            return df
    
if __name__ == "__main__":
    crawler = RequestML()
    data = crawler.transform_df("iphone")
    print(data.head())
