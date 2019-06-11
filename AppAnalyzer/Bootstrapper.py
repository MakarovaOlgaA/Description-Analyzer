import sys
from TextProcessor import TextProcessor
from MainWindow import Ui_MainWindow, EventHandling_MainWindow
from Repository import Repository
from DescriptionFetcher import DescriptionFetcher
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from WebSearcher import WebSearcher
from DbSearcher import DbSearcher

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    window = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    window.setupUi(w)

    handler = EventHandling_MainWindow(window)

    textProcessor = TextProcessor()
    handler.stem = textProcessor.tokenizeText

    repo = Repository()
    fetcher = DescriptionFetcher()
    handler.webSearcher = WebSearcher(fetcher, repo)
    handler.dbSearcher = DbSearcher(repo)
    handler.repo = repo

    w.show()

    #fetcher.init()
    #fetcher.search('test')
    #fetcher.loadAllDescriptions();

    sys.exit(app.exec_())