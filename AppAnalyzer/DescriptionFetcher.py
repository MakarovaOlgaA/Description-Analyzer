from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.parse as urlparser
import os

class DescriptionFetcher(object):
    linkPattern = 'https://play.google.com/store/search?q={}&c=apps'
    
    appLinkClass = 'JC71ub'
    desciptionSelector = '[jsname="sngebd"]'
    nameSelector = '[itemprop="name"]'

    driver = None
    apps = []

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('lang=en')
       # self.options.add_argument('--headless')

        self.driverPath = os.path.join(os.getcwd(), 'chromedriver')

    def search(self, searchString):
        if self.driver is None:
            self.driver = webdriver.Chrome(options=self.options, executable_path=self.driverPath)        

        url = self.linkPattern.format(urlparser.quote_plus(searchString))
        self.driver.get(url)

        links = self.driver.find_elements_by_class_name(self.appLinkClass)  
        self.apps = [Application(link.get_attribute("href"), None, None) for link in links]
        return len(self.apps)

    def loadAllDescriptions(self):
        for app in self.apps:
            if app.name is None:
                self.loadDescription(app)

    def getDescription(self, index):
        if self.apps[index].name is None:
             self.loadDescription(self.apps[index])
        return self.apps[index];

    def loadDescription(self, app):
        self.driver.get(app.href)
        app.name = self.driver.find_element_by_css_selector(self.nameSelector).text
        app.description = self.driver.find_element_by_css_selector(self.desciptionSelector).text

class Application:
    def __init__(self, href, name, description):  
        self.href = href
        self.name = name
        self.description = description