import sys
from TextProcessor import TextProcessor
from MainWindow import Ui_MainWindow, EventHandling_MainWindow
from Repository import Repository
from DescriptionFetcher import DescriptionFetcher
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QMainWindow
from WebSearcher import WebSearcher

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    window = Ui_MainWindow()
    w = QMainWindow()
    window.setupUi(w)

    handler = EventHandling_MainWindow(window)

    textProcessor = TextProcessor()
    handler.stem = textProcessor.tokenizeText

    repo = Repository()
    fetcher = DescriptionFetcher()
    handler.webSearcher = WebSearcher(fetcher, repo)
    
    w.show()

    #fetcher.init()
    #fetcher.search('test')
    #fetcher.loadAllDescriptions();

    sys.exit(app.exec_())


