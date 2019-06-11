#from PyQt5.QtWidgets import  QWidget, QPushButton, QLineEdit, QTextEdit, QMessageBox
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(881, 667)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 881, 651))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.searchLineEdit = QtGui.QLineEdit(self.tab)
        self.searchLineEdit.setGeometry(QtCore.QRect(20, 40, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchLineEdit.setFont(font)
        self.searchLineEdit.setText(_fromUtf8(""))
        self.searchLineEdit.setObjectName(_fromUtf8("searchLineEdit"))
        self.dbRadioButton = QtGui.QRadioButton(self.tab)
        self.dbRadioButton.setGeometry(QtCore.QRect(170, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dbRadioButton.setFont(font)
        self.dbRadioButton.setChecked(True)
        self.dbRadioButton.setObjectName(_fromUtf8("dbRadioButton"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.nameLineEdit = QtGui.QLineEdit(self.tab)
        self.nameLineEdit.setGeometry(QtCore.QRect(20, 110, 811, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setReadOnly(True)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.webRadioButton = QtGui.QRadioButton(self.tab)
        self.webRadioButton.setGeometry(QtCore.QRect(330, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.webRadioButton.setFont(font)
        self.webRadioButton.setObjectName(_fromUtf8("webRadioButton"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.originalTextEdit = QtGui.QTextEdit(self.tab)
        self.originalTextEdit.setEnabled(True)
        self.originalTextEdit.setGeometry(QtCore.QRect(20, 180, 811, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.originalTextEdit.setFont(font)
        self.originalTextEdit.setReadOnly(True)
        self.originalTextEdit.setObjectName(_fromUtf8("originalTextEdit"))
        self.prevCommandLinkButton = QtGui.QCommandLinkButton(self.tab)
        self.prevCommandLinkButton.setGeometry(QtCore.QRect(20, 580, 101, 41))
        self.prevCommandLinkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.prevCommandLinkButton.setObjectName(_fromUtf8("prevCommandLinkButton"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 540, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.stemmedTextEdit = QtGui.QTextEdit(self.tab)
        self.stemmedTextEdit.setEnabled(True)
        self.stemmedTextEdit.setGeometry(QtCore.QRect(20, 390, 811, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stemmedTextEdit.setFont(font)
        self.stemmedTextEdit.setReadOnly(True)
        self.stemmedTextEdit.setObjectName(_fromUtf8("stemmedTextEdit"))
        self.adStatusComboBox = QtGui.QComboBox(self.tab)
        self.adStatusComboBox.setGeometry(QtCore.QRect(190, 540, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.adStatusComboBox.setFont(font)
        self.adStatusComboBox.setObjectName(_fromUtf8("adStatusComboBox"))
        self.adStatusComboBox.addItem(_fromUtf8(""))
        self.adStatusComboBox.addItem(_fromUtf8(""))
        self.adStatusComboBox.addItem(_fromUtf8(""))
        self.nextCommandLinkButton = QtGui.QCommandLinkButton(self.tab)
        self.nextCommandLinkButton.setGeometry(QtCore.QRect(700, 580, 131, 41))
        self.nextCommandLinkButton.setObjectName(_fromUtf8("nextCommandLinkButton"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 360, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.unclassifiedOnlyCheckBox = QtGui.QCheckBox(self.tab)
        self.unclassifiedOnlyCheckBox.setGeometry(QtCore.QRect(630, 40, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unclassifiedOnlyCheckBox.setFont(font)
        self.unclassifiedOnlyCheckBox.setObjectName(_fromUtf8("unclassifiedOnlyCheckBox"))
        self.goPushButton = QtGui.QPushButton(self.tab)
        self.goPushButton.setGeometry(QtCore.QRect(490, 40, 71, 31))
        self.goPushButton.setObjectName(_fromUtf8("goPushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 540, 131, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.appCounterLabel = QtGui.QLabel(self.tab)
        self.appCounterLabel.setGeometry(QtCore.QRect(160, 590, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.appCounterLabel.setFont(font)
        self.appCounterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appCounterLabel.setObjectName(_fromUtf8("appCounterLabel"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 470, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.originalTextEdit_2 = QtGui.QTextEdit(self.tab_2)
        self.originalTextEdit_2.setEnabled(True)
        self.originalTextEdit_2.setGeometry(QtCore.QRect(20, 110, 811, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.originalTextEdit_2.setFont(font)
        self.originalTextEdit_2.setReadOnly(True)
        self.originalTextEdit_2.setObjectName(_fromUtf8("originalTextEdit_2"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.stemmedTextEdit_2 = QtGui.QTextEdit(self.tab_2)
        self.stemmedTextEdit_2.setEnabled(True)
        self.stemmedTextEdit_2.setGeometry(QtCore.QRect(20, 320, 811, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stemmedTextEdit_2.setFont(font)
        self.stemmedTextEdit_2.setReadOnly(True)
        self.stemmedTextEdit_2.setObjectName(_fromUtf8("stemmedTextEdit_2"))
        self.nameLineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.nameLineEdit_2.setGeometry(QtCore.QRect(20, 40, 811, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLineEdit_2.setFont(font)
        self.nameLineEdit_2.setReadOnly(True)
        self.nameLineEdit_2.setObjectName(_fromUtf8("nameLineEdit_2"))
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 290, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "App Analyzer", None))
        self.dbRadioButton.setText(_translate("MainWindow", "Search in Database", None))
        self.label_5.setText(_translate("MainWindow", "Name:", None))
        self.webRadioButton.setText(_translate("MainWindow", "Search on Google Play", None))
        self.label_3.setText(_translate("MainWindow", "Description:", None))
        self.label.setText(_translate("MainWindow", "Search for apps:", None))
        self.prevCommandLinkButton.setText(_translate("MainWindow", "Prev App", None))
        self.label_2.setText(_translate("MainWindow", "Advertizement status:", None))
        self.adStatusComboBox.setItemText(0, _translate("MainWindow", "Unknown", None))
        self.adStatusComboBox.setItemText(1, _translate("MainWindow", "Advertiser-friendly", None))
        self.adStatusComboBox.setItemText(2, _translate("MainWindow", "Not suitable for ads", None))
        self.nextCommandLinkButton.setText(_translate("MainWindow", "Next App", None))
        self.label_4.setText(_translate("MainWindow", "Stemmed description:", None))
        self.unclassifiedOnlyCheckBox.setText(_translate("MainWindow", "Show unclassified apps only", None))
        self.goPushButton.setText(_translate("MainWindow", "Go", None))
        self.pushButton_2.setText(_translate("MainWindow", "Update Status", None))
        self.appCounterLabel.setText(_translate("MainWindow", "App {} of {}", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Manual Classification", None))
        self.label_6.setText(_translate("MainWindow", "Advertizement status:", None))
        self.label_7.setText(_translate("MainWindow", "Name:", None))
        self.label_8.setText(_translate("MainWindow", "Description:", None))
        self.label_9.setText(_translate("MainWindow", "Stemmed description:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Automatic Prediction", None))

class EventHandling_MainWindow:
    adStatuses = {
        0: None,
        1: True,
        2: False
    }

    def __init__(self, mainWindow):  
        self.mainWindow = mainWindow
        self.mainWindow.goPushButton.clicked.connect(self.onGoClick)
        self.mainWindow.nextCommandLinkButton.clicked.connect(self.next)
        self.mainWindow.prevCommandLinkButton.clicked.connect(self.prev)

    def onGoClick(self):
        self.mainWindow.nameLineEdit.setText('')
        self.mainWindow.originalTextEdit.setPlainText('')
        self.mainWindow.stemmedTextEdit.setPlainText('')

        searchStr = self.mainWindow.searchLineEdit.text()

        if (self.mainWindow.dbRadioButton.isChecked()):
            self.searcher = self.dbSearcher
        else:
            self.searcher = self.webSearcher

        if (self.searcher.search(searchStr, self.mainWindow.unclassifiedOnlyCheckBox.isChecked()) > 0):
            self.currentApp = self.searcher.apps[0]
            self.updateAppInfo(self.currentApp)

        self.mainWindow.appCounterLabel.setText("App {} of {}".format(self.searcher.currentAppIndex + 1, self.searcher.appsTotal))
       
    def updateAppInfo(self, app):                
        if app.stemmedDescription is None:
            app.stemmedDescription = ' '.join(self.stem(app.description))

        comboboxIndex = [key for key, value in self.adStatuses.items() if value == app.isAdvertizerFriendly][0]
        self.mainWindow.adStatusComboBox = comboboxIndex

        self.mainWindow.nameLineEdit.setText(app.name)
        self.mainWindow.originalTextEdit.setPlainText(self.currentApp.description)
        self.mainWindow.stemmedTextEdit.setPlainText(self.currentApp.stemmedDescription)

    def next(self):
        if self.searcher.appsTotal > 0:
            self.currentApp = self.searcher.next()
            self.updateAppInfo(self.currentApp)
            self.mainWindow.appCounterLabel.setText("App {} of {}".format(self.searcher.currentAppIndex + 1, self.searcher.appsTotal))
        
    def prev(self):
        if self.searcher.appsTotal > 0:
            self.currentApp = self.searcher.prev()
            self.updateAppInfo(self.currentApp)
            self.mainWindow.appCounterLabel.setText("App {} of {}".format(self.searcher.currentAppIndex + 1, self.searcher.appsTotal))


    def onAnalyzeClick(self):
        processingResult = self.ProcessInput(self.descriptionInput.toPlainText())
        self.tokenizedResultOutput.setPlainText('|'.join(processingResult))
       
    def stem(self, textToAnalyze):
        pass