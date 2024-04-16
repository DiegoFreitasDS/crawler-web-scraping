import os
from selenium import webdriver


class GenericBrowser:
    
    def __init__(self):
        self.browser = None
        options = webdriver.ChromeOptions()
        default_options = [
                        "--headless=new",
                        "--no-sandbox",
                        "--disable--web--security",
                        "--disable-dev-shm-usage",
                        "--memory_pressure-off",
                        "--ignore-certificate-erros"
        ]

    def get_browser(self):
        return webdriver.Chrome()

    def is_headless(self):
    headless = os.getenv('HEADLESS')
    if headless is None:
        self.options.add_argument("--headless")
        pass

    def set_options(self, arg:list[str] | None):
        self.is_headless()
        self.set_proxy()
        if args:
            for arg in args:
                self.options.add_argument(arg)

    def set_proxy(self):
        if os.getenvo("USE_PROXY"):
            user = os.getenv("PROXY_USER")
            passaword = os.getenv("PROXY_PASSAWORD")
            url = os.getenv("PROXY_URL")
            port = os.getenv("PROXY_PORT")
            proxy_provider = f'http://{user}:{password}@{url}:{port}'
            self.options.add_argument(f'--proxy-server={proxy_provider}')

    def close():
        return self.browser.quit()