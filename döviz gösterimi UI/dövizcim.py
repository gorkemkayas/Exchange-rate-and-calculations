from döviz_UI import Doviz
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dovizcim(object):
    def setupUi(self, Dovizcim):
        Dovizcim.setObjectName("Dovizcim")
        Dovizcim.resize(800, 370)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        Dovizcim.setFont(font)
        Dovizcim.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dovizcim.setAutoFillBackground(False)
        Dovizcim.setDocumentMode(False)
        Dovizcim.setDockNestingEnabled(False)
        Dovizcim.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Dovizcim)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(410, 30, 361, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gram_altin_label = QtWidgets.QLabel(self.centralwidget)
        self.gram_altin_label.setGeometry(QtCore.QRect(20, 40, 91, 41))
        self.gram_altin_label.setObjectName("gram_altin_label")
        self.dolar_label = QtWidgets.QLabel(self.centralwidget)
        self.dolar_label.setGeometry(QtCore.QRect(20, 70, 81, 41))
        self.dolar_label.setObjectName("dolar_label")
        self.euro_label = QtWidgets.QLabel(self.centralwidget)
        self.euro_label.setGeometry(QtCore.QRect(20, 100, 81, 41))
        self.euro_label.setObjectName("euro_label")
        self.sterlin_label = QtWidgets.QLabel(self.centralwidget)
        self.sterlin_label.setGeometry(QtCore.QRect(20, 130, 81, 41))
        self.sterlin_label.setObjectName("sterlin_label")
        self.bist_label = QtWidgets.QLabel(self.centralwidget)
        self.bist_label.setGeometry(QtCore.QRect(20, 160, 81, 41))
        self.bist_label.setObjectName("bist_label")
        self.bitcoin_label = QtWidgets.QLabel(self.centralwidget)
        self.bitcoin_label.setGeometry(QtCore.QRect(20, 190, 81, 41))
        self.bitcoin_label.setObjectName("bitcoin_label")
        self.gumus_label = QtWidgets.QLabel(self.centralwidget)
        self.gumus_label.setGeometry(QtCore.QRect(20, 200, 81, 81))
        self.gumus_label.setObjectName("gumus_label")
        self.ust_adet_yazisi = QtWidgets.QLabel(self.centralwidget)
        self.ust_adet_yazisi.setGeometry(QtCore.QRect(120, 10, 111, 31))
        self.ust_adet_yazisi.setObjectName("ust_adet_yazisi")
        self.Ust_tutar_Yazisi = QtWidgets.QLabel(self.centralwidget)
        self.Ust_tutar_Yazisi.setGeometry(QtCore.QRect(240, 10, 121, 31))
        self.Ust_tutar_Yazisi.setObjectName("Ust_tutar_Yazisi")
        self.gram_altin_sayac = QtWidgets.QSpinBox(self.centralwidget)
        self.gram_altin_sayac.setGeometry(QtCore.QRect(140, 50, 71, 21))
        self.gram_altin_sayac.setObjectName("gram_altin_sayac")
        self.dolar_sayac = QtWidgets.QSpinBox(self.centralwidget)
        self.dolar_sayac.setGeometry(QtCore.QRect(140, 80, 71, 21))
        self.dolar_sayac.setObjectName("dolar_sayac")
        self.euro_sayac = QtWidgets.QSpinBox(self.centralwidget)
        self.euro_sayac.setGeometry(QtCore.QRect(140, 110, 71, 21))
        self.euro_sayac.setObjectName("euro_sayac")
        self.sterlin_sayac = QtWidgets.QSpinBox(self.centralwidget)
        self.sterlin_sayac.setGeometry(QtCore.QRect(140, 140, 71, 21))
        self.sterlin_sayac.setObjectName("sterlin_sayac")
        self.bist_sayac = QtWidgets.QSpinBox(self.centralwidget)
        self.bist_sayac.setGeometry(QtCore.QRect(140, 170, 71, 21))
        self.bist_sayac.setObjectName("bist_sayac")
        self.bitcoin_sayac = QtWidgets.QSpinBox(self.centralwidget)
        self.bitcoin_sayac.setGeometry(QtCore.QRect(140, 200, 71, 21))
        self.bitcoin_sayac.setObjectName("bitcoin_sayac")
        self.gumus_sayac = QtWidgets.QSpinBox(self.centralwidget)
        self.gumus_sayac.setGeometry(QtCore.QRect(140, 230, 71, 21))
        self.gumus_sayac.setObjectName("gumus_sayac")
        self.gram_altin_tutar = QtWidgets.QLabel(self.centralwidget)
        self.gram_altin_tutar.setGeometry(QtCore.QRect(234, 45, 141, 21))
        self.gram_altin_tutar.setObjectName("gram_altin_tutar")
        self.dolar_tutar = QtWidgets.QLabel(self.centralwidget)
        self.dolar_tutar.setGeometry(QtCore.QRect(230, 80, 151, 21))
        self.dolar_tutar.setObjectName("dolar_tutar")
        self.euro_tutar = QtWidgets.QLabel(self.centralwidget)
        self.euro_tutar.setGeometry(QtCore.QRect(230, 110, 151, 21))
        self.euro_tutar.setObjectName("euro_tutar")
        self.sterlin_tutar = QtWidgets.QLabel(self.centralwidget)
        self.sterlin_tutar.setGeometry(QtCore.QRect(230, 140, 151, 21))
        self.sterlin_tutar.setObjectName("sterlin_tutar")
        self.bist_tutar = QtWidgets.QLabel(self.centralwidget)
        self.bist_tutar.setGeometry(QtCore.QRect(230, 170, 151, 21))
        self.bist_tutar.setObjectName("bist_tutar")
        self.bitcoin_tutar = QtWidgets.QLabel(self.centralwidget)
        self.bitcoin_tutar.setGeometry(QtCore.QRect(230, 200, 151, 21))
        self.bitcoin_tutar.setObjectName("bitcoin_tutar")
        self.gumus_tutar = QtWidgets.QLabel(self.centralwidget)
        self.gumus_tutar.setGeometry(QtCore.QRect(230, 230, 151, 21))
        self.gumus_tutar.setObjectName("gumus_tutar")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 310, 381, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sifirla_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.sifirla_button.setObjectName("sifirla_button")
        self.horizontalLayout_2.addWidget(self.sifirla_button)
        self.toplam_hesapla_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.toplam_hesapla_button.setObjectName("toplam_hesapla_button")
        self.horizontalLayout_2.addWidget(self.toplam_hesapla_button)
        self.ust_doviz_deger_yazisi = QtWidgets.QLabel(self.centralwidget)
        self.ust_doviz_deger_yazisi.setGeometry(QtCore.QRect(410, -1, 361, 31))
        self.ust_doviz_deger_yazisi.setObjectName("ust_doviz_deger_yazisi")
        self.toplam_yazisi = QtWidgets.QLabel(self.centralwidget)
        self.toplam_yazisi.setGeometry(QtCore.QRect(30, 270, 171, 21))
        self.toplam_yazisi.setObjectName("toplam_yazisi")
        self.toplam_tutar = QtWidgets.QLabel(self.centralwidget)
        self.toplam_tutar.setGeometry(QtCore.QRect(190, 260, 181, 41))
        self.toplam_tutar.setObjectName("toplam_tutar")
        Dovizcim.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Dovizcim)
        self.statusbar.setObjectName("statusbar")
        Dovizcim.setStatusBar(self.statusbar)

        self.retranslateUi(Dovizcim)
        QtCore.QMetaObject.connectSlotsByName(Dovizcim)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_all_infos)
        self.timer.start(1000)


    def show_all_infos(self):
        self.label.setText(Doviz().take_infos())

    def retranslateUi(self, Dovizcim):
        _translate = QtCore.QCoreApplication.translate
        Dovizcim.setWindowTitle(_translate("Dovizcim", "Dövizcim GORKIDEV"))
        self.label.setText(_translate("Dovizcim", "TextLabel"))
        self.gram_altin_label.setText(_translate("Dovizcim", "GRAM ALTIN :"))
        self.dolar_label.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">DOLAR :</p></body></html>"))
        self.euro_label.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">EURO :</p></body></html>"))
        self.sterlin_label.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">STERLİN :</p></body></html>"))
        self.bist_label.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">BIST 100 :</p></body></html>"))
        self.bitcoin_label.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">BITCOIN : ($)</p></body></html>"))
        self.gumus_label.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\"><span style=\" font-size:6pt;\">GRAM GÜMÜŞ :</span></p></body></html>"))
        self.ust_adet_yazisi.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">ADET</p></body></html>"))
        self.Ust_tutar_Yazisi.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">TUTAR</p></body></html>"))

        self.gram_altin_tutar.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">0</p></body></html>"))

        self.toplam_hesapla_button.clicked.connect(self.toplam_clicked)
        self.sifirla_button.clicked.connect(self.sifirla_clicked)

        self.deger_tutar_timer = QtCore.QTimer()
        self.deger_tutar_timer.timeout.connect(self.configure_deger)
        self.deger_tutar_timer.start(1000)



        self.dolar_tutar.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.euro_tutar.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.sterlin_tutar.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.bist_tutar.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.bitcoin_tutar.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.gumus_tutar.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.sifirla_button.setText(_translate("Dovizcim", "Sıfırla"))
        self.toplam_hesapla_button.setText(_translate("Dovizcim", "Toplam tutarı hesapla"))
        self.ust_doviz_deger_yazisi.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">DÖVİZ DEĞERLERİ</span></p></body></html>"))
        self.toplam_yazisi.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">TOPLAM : </span></p></body></html>"))
        self.toplam_tutar.setText(_translate("Dovizcim", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">TextLabel</span></p></body></html>"))

    def configure_deger(self):
        self.gram_altınım = self.gram_altin_tutar.setText(str(self.gram_altin_sayac.value() * Doviz().currency_calculatible_values[0]))
        self.dolarım = self.dolar_tutar.setText(str(self.dolar_sayac.value() * Doviz().currency_calculatible_values[1]))
        self.eurom = self.euro_tutar.setText(str(self.euro_sayac.value() * Doviz().currency_calculatible_values[2]))
        self.sterlinim =self.sterlin_tutar.setText(str(self.sterlin_sayac.value() * Doviz().currency_calculatible_values[3]))
        self.bistim = self.bist_tutar.setText(str(self.bist_sayac.value() * Doviz().currency_calculatible_values[4]))
        self.bitcoinim =self.bitcoin_tutar.setText(str(self.bitcoin_sayac.value() * Doviz().currency_calculatible_values[5] * Doviz().currency_calculatible_values[1]))
        self.gumusum = self.gumus_tutar.setText(str(self.gumus_sayac.value() * Doviz().currency_calculatible_values[6]))

    def toplam_clicked(self):
        self.toplam_tutar.setText(str((self.gram_altin_sayac.value() * Doviz().currency_calculatible_values[0]) + (self.dolar_sayac.value() * Doviz().currency_calculatible_values[1]) + (self.euro_sayac.value() * Doviz().currency_calculatible_values[2]) + (self.sterlin_sayac.value() * Doviz().currency_calculatible_values[3]) + (self.bist_sayac.value() * Doviz().currency_calculatible_values[4]) + (self.bitcoin_sayac.value() * Doviz().currency_calculatible_values[5] * Doviz().currency_calculatible_values[1]) + (self.gumus_sayac.value() * Doviz().currency_calculatible_values[6])))

    def sifirla_clicked(self):
        self.gram_altin_sayac.clear()
        self.dolar_sayac.clear()
        self.euro_sayac.clear()
        self.sterlin_sayac.clear()
        self.bist_sayac.clear()
        self.bitcoin_sayac.clear()
        self.gumus_sayac.clear()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dovizcim = QtWidgets.QMainWindow()
    ui = Ui_Dovizcim()
    ui.setupUi(Dovizcim)
    Dovizcim.show()
    sys.exit(app.exec_())
