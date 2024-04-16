from abc import ABC


class AbstractCrawler(ABC):
    
    def  __init__(self):
        self.redis=RedisClient.get()
        self.mongo = MongoConnection()
        self.browser = GenericBrowser().get_browser()

    @abstractmethod
    def crawl(self):
        pass

    @abstractmethod
    def execute_main(self):
        pass

    @abstractmethod
    def execute_before(self):
        pass

    @abstractmethod
    def execute_after(self)
        pass

    @abstractmethod
    def get_steps(self, site):
        try:
            return self.redis.get(site)
        except:
            raise("Redis não funciona")

    @abstractmethod
    def save_data(self, data):
        try:
            self.mongo.save_dataframe(data)
        except:
            raise("Mongo Não Funciona")