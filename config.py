from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

## Setting UI 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(809, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-79, -70, 921, 871))
        self.label.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(81, 47, 281, 81))
        self.label_2.setStyleSheet("image:url(:/img/NicePng_supreme-logo-png_141087.png)")
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/NicePng_supreme-logo-png_141087.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 110, 71, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 150, 301, 31))
        self.lineEdit.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 200, 301, 31))
        self.lineEdit_2.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 250, 301, 31))
        self.lineEdit_3.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 300, 141, 31))
        self.lineEdit_4.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 300, 141, 31))
        self.lineEdit_5.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 350, 301, 31))
        self.lineEdit_6.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 400, 301, 31))
        self.lineEdit_7.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(80, 450, 141, 31))
        self.lineEdit_8.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 450, 141, 31))
        self.comboBox.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(430, 48, 301, 31))
        self.comboBox_2.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(430, 93, 301, 31))
        self.lineEdit_9.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(430, 149, 81, 31))
        self.comboBox_3.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(520, 149, 81, 31))
        self.comboBox_4.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(660, 149, 71, 31))
        self.lineEdit_10.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(430, 250, 301, 31))
        self.lineEdit_11.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(430, 300, 141, 31))
        self.comboBox_5.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(590, 300, 141, 31))
        self.comboBox_6.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 350, 301, 31))
        self.pushButton.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(430, 400, 301, 81))
        self.textEdit.setStyleSheet("color:rgb(186, 189, 182);\n"
"background-color:rgb(85, 87, 83)")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(481, 207, 201, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "BOT V1.0"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "full name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "email"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "tel"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "address"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "address 2"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "address 3"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "city"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "postcode"))
        self.comboBox.setItemText(0, _translate("MainWindow", "UK"))
        self.comboBox.setItemText(1, _translate("MainWindow", "UK (N. IRELAND)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "AUSTRIA"))
        self.comboBox.setItemText(3, _translate("MainWindow", "BELARUS"))
        self.comboBox.setItemText(4, _translate("MainWindow", "BELGIUM"))
        self.comboBox.setItemText(5, _translate("MainWindow", "BULGARIA"))
        self.comboBox.setItemText(6, _translate("MainWindow", "CROATIA"))
        self.comboBox.setItemText(7, _translate("MainWindow", "CZECH REPUBLIC"))
        self.comboBox.setItemText(8, _translate("MainWindow", "DENMARK"))
        self.comboBox.setItemText(9, _translate("MainWindow", "ESTONIA"))
        self.comboBox.setItemText(10, _translate("MainWindow", "FINLAND"))
        self.comboBox.setItemText(11, _translate("MainWindow", "FRANCE"))
        self.comboBox.setItemText(12, _translate("MainWindow", "GERMANY"))
        self.comboBox.setItemText(13, _translate("MainWindow", "GREECE"))
        self.comboBox.setItemText(14, _translate("MainWindow", "HUNGARY"))
        self.comboBox.setItemText(15, _translate("MainWindow", "ICELAND"))
        self.comboBox.setItemText(16, _translate("MainWindow", "IRELAND"))
        self.comboBox.setItemText(17, _translate("MainWindow", "ITALY"))
        self.comboBox.setItemText(18, _translate("MainWindow", "LATVIA"))
        self.comboBox.setItemText(19, _translate("MainWindow", "LITHUANIA"))
        self.comboBox.setItemText(20, _translate("MainWindow", "LUXEMBOURG"))
        self.comboBox.setItemText(21, _translate("MainWindow", "MONACO"))
        self.comboBox.setItemText(22, _translate("MainWindow", "NETHERLANDS"))
        self.comboBox.setItemText(23, _translate("MainWindow", "NORWAY"))
        self.comboBox.setItemText(24, _translate("MainWindow", "POLAND"))
        self.comboBox.setItemText(25, _translate("MainWindow", "PORTUGAL"))
        self.comboBox.setItemText(26, _translate("MainWindow", "ROMANIA"))
        self.comboBox.setItemText(27, _translate("MainWindow", "RUSSIA"))
        self.comboBox.setItemText(28, _translate("MainWindow", "SLOVAKIA"))
        self.comboBox.setItemText(29, _translate("MainWindow", "SLOVENIA"))
        self.comboBox.setItemText(30, _translate("MainWindow", "SPAIN"))
        self.comboBox.setItemText(31, _translate("MainWindow", "SWEEDEN"))
        self.comboBox.setItemText(32, _translate("MainWindow", "SWITZERLAND"))
        self.comboBox.setItemText(33, _translate("MainWindow", "TURKEY"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Visa"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "American Express"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Mastercard"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Solo"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "number"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "01"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "02"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "03"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "04"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "05"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "06"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "07"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "08"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "09"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "2020"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2021"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "2022"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "2023"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "2024"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "2025"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "2026"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "2027"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "2028"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "2029"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "2030"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "CVV"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "ITEM NAME"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "jackets"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "t-shirts"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "pants"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "tops/sweaters"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "shirts"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "sweatshirts"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "bags"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "accesories"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Small"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Medium"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Large"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "XLarge"))

        self.pushButton.setText(_translate("MainWindow", "ORDER NOW"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Press &quot;ORDER NOW&quot; to proceed...</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "© Copyright Mihai Ene 2020"))
        self.textEdit.setText("")

        ##Getters for UI contents

        def getName(self):
            return self.lineEdit.text()

        def getEmail(self):
            return self.lineEdit_2.text()

        def getPhoneNumber(self):
            return self.lineEdit_3.text()

        def getAddress(self):
            return self.lineEdit_4.text()

        def getAddress2(self):
            return self.lineEdit_5.text()

        def getAddress3(self):
            return self.lineEdit_6.text()

        def getCity(self):
            return self.lineEdit_7.text()

        def getPostalCode(self):
            return self.lineEdit_8.text()

        def getCountry(self):
            return self.comboBox.currentText()

        def getPayMethod(self):
            return self.comboBox_2.currentText()

        def getCardNumber(self):
            return self.lineEdit_9.text()

        def getExpireMonth(self):
            return self.comboBox_3.currentText()

        def getExpireYear(self):
            return self.comboBox_4.currentText()

        def getCVV(self):
            return self.lineEdit_10.text()

        def getItemName(self):
            return self.lineEdit_11.text()

        def getCategory(self):
            return self.comboBox_5.currentText()

        def getSize(self):
            return self.comboBox_6.currentText()

        ## ORDER FUNCTION ##

        def order(k):
            browser = webdriver.Firefox()
            browser.get('https://www.supremenewyork.com/shop')
            browser.find_element_by_class_name(k["category"]).click()
            try:
                WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/form/fieldset[2]/a')))
            except TimeoutException:
                print("Error")
            text = k["item"].lower()
            while (text in browser.page_source.lower()) == False:
                browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset[1]/a').click()
                time.sleep(0.6)
            try:
                WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/form/fieldset[2]/a')))
            except TimeoutException:
                print("Item is sold out!")
            browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input').click()
            try:
                WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/a[2]')))
            except TimeoutException:
                print("Error")
            browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/a[2]').click()
            browser.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
            browser.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
            browser.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["number"])
            browser.find_element_by_xpath('//*[@id="bo"]').send_keys(k["adress"])
            browser.find_element_by_xpath('//*[@id="oba3"]').send_keys(k["adress2"])
            browser.find_element_by_xpath('//*[@id="order_billing_address_3"]').send_keys(k["adress3"]) 
            browser.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])
            browser.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["postcode"])
            Select(browser.find_element_by_id('order_billing_country')).select_by_visible_text(k["country"])
            Select(browser.find_element_by_id('credit_card_type')).select_by_visible_text(k["paymethod"])
            browser.find_element_by_xpath('//*[@id="cnb"]').send_keys(k["cardnumber"])
            Select(browser.find_element_by_id('credit_card_month')).select_by_visible_text(k["cardmonth"])
            Select(browser.find_element_by_id('credit_card_year')).select_by_visible_text(k["cardyear"])
            browser.find_element_by_xpath('//*[@id="vval"]').send_keys(k["cvv"])
            browser.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p/label/div/ins').click()
            browser.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[3]/div/input').click()
            
            ## BUTTON CLICKED FUNCTION ##


        def clicked():
                keys = {
                "name": getName(self),
                "email": getEmail(self),
                "number": getPhoneNumber(self),
                "adress":getAddress(self),
                "adress2":getAddress2(self),
                "adress3":getAddress3(self),
                "city": getCity(self),
                "postcode":getPostalCode(self),
                "country": getCountry(self),
                "paymethod": getPayMethod(self),
                "cardnumber": getCardNumber(self),
                "cardmonth": getExpireMonth(self),
                "cardyear": getExpireYear(self),
                "cvv": getCVV(self),
                "item": getItemName(self),
                "category": getCategory(self),
                "size": getSize(self)
                }
                order(keys)
        self.pushButton.clicked.connect(clicked)
 ## MAIN ##
import file
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

