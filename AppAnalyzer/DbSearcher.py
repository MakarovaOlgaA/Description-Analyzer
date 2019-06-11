from ApplicationModel import Application

class DbSearcher(object):
    def __init__(self, repository):  
        self.repo = repository
        self.appsTotal = 0
        self.currentAppIndex = -1
  
    def search(self, searchStr, unclassifiedOnly):
        self.unclassifiedOnly = unclassifiedOnly
        self.apps = self.repo.search(searchStr, unclassifiedOnly)
        self.appsTotal = len(self.apps)

        if self.appsTotal > 0:
           self.currentAppIndex = 0
        else:
           self.currentAppIndex = -1

        return self.appsTotal

    def next(self):
        if self.currentAppIndex < self.appsTotal - 1:
            self.currentAppIndex = self.currentAppIndex + 1
        return self.apps[self.currentAppIndex]

    def prev(self):
        if self.currentAppIndex > 0:
            self.currentAppIndex = self.currentAppIndex - 1
        return self.apps[self.currentAppIndex]
