from ApplicationModel import Application

class WebSearcher(object):
    def __init__(self, descriptionFetcher, repository):  
        self.fetcher = descriptionFetcher
        self.repo = repository
        self.appsTotal = 0
        self.currentAppIndex = -1
  
    def search(self, searchStr, unclassifiedOnly):
        self.unclassifiedOnly = unclassifiedOnly
        self.appsTotal = self.fetcher.search(searchStr)
        self.apps = [None] * self.appsTotal

        if self.appsTotal > 0:
           self.currentAppIndex = 0
           self.apps[0] = self.loadApp(0)
        else:
           self.currentAppIndex = -1

        return self.appsTotal

    def loadApp(self, index):
         foundApp = self.fetcher.getDescription(index)
         app = self.repo.getApplicationByName(foundApp.name)

         if app is None:
              app = Application(None, foundApp.name, foundApp.description, None, None)

         return app

    def next(self):
        if self.currentAppIndex < self.appsTotal - 1:
            self.currentAppIndex = self.currentAppIndex + 1
            if self.apps[self.currentAppIndex] is None:
                self.apps[self.currentAppIndex] = self.loadApp(self.currentAppIndex)
         
        return self.apps[self.currentAppIndex]

    def prev(self):
        if self.currentAppIndex > 0:
            self.currentAppIndex = self.currentAppIndex - 1
        return self.apps[self.currentAppIndex]