# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interpretation_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Interpretation_Main(object):
    def setupUi(self, Interpretation_Main):
        Interpretation_Main.setObjectName("Interpretation_Main")
        Interpretation_Main.resize(604, 755)
        self.centralwidget = QtWidgets.QWidget(Interpretation_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Interpretation_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Interpretation_tabWidget.setFont(font)
        self.Interpretation_tabWidget.setObjectName("Interpretation_tabWidget")
        self.SeisAttributes_Tab = QtWidgets.QWidget()
        self.SeisAttributes_Tab.setObjectName("SeisAttributes_Tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SeisAttributes_Tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.SeisAttributes_Tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 552, 627))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.SeisIntSelectWinDataButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SeisIntSelectWinDataButton.setObjectName("SeisIntSelectWinDataButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.SeisIntSelectWinDataButton)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.SeisIntSpecDecomToolButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SeisIntSpecDecomToolButton.setObjectName("SeisIntSpecDecomToolButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SeisIntSpecDecomToolButton)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.SeisIntCoherencyToolButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SeisIntCoherencyToolButton.setObjectName("SeisIntCoherencyToolButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.SeisIntCoherencyToolButton)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.SeisIntAmpliudeToolButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SeisIntAmpliudeToolButton.setObjectName("SeisIntAmpliudeToolButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.SeisIntAmpliudeToolButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.Interpretation_tabWidget.addTab(self.SeisAttributes_Tab, "")
        self.SeisInterpretation_Tab = QtWidgets.QWidget()
        self.SeisInterpretation_Tab.setObjectName("SeisInterpretation_Tab")
        self.Interpretation_tabWidget.addTab(self.SeisInterpretation_Tab, "")
        self.WellCorrelationTab = QtWidgets.QWidget()
        self.WellCorrelationTab.setObjectName("WellCorrelationTab")
        self.Interpretation_tabWidget.addTab(self.WellCorrelationTab, "")
        self.verticalLayout.addWidget(self.Interpretation_tabWidget)
        Interpretation_Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Interpretation_Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 26))
        self.menubar.setObjectName("menubar")
        Interpretation_Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Interpretation_Main)
        self.statusbar.setObjectName("statusbar")
        Interpretation_Main.setStatusBar(self.statusbar)

        self.retranslateUi(Interpretation_Main)
        self.Interpretation_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Interpretation_Main)

    def retranslateUi(self, Interpretation_Main):
        _translate = QtCore.QCoreApplication.translate
        Interpretation_Main.setWindowTitle(_translate("Interpretation_Main", "Interpretation Wizard"))
        self.label.setText(_translate("Interpretation_Main", "Select Seismic:"))
        self.SeisIntSelectWinDataButton.setText(_translate("Interpretation_Main", "Select"))
        self.label_2.setText(_translate("Interpretation_Main", "Spectral Decomposition:"))
        self.SeisIntSpecDecomToolButton.setText(_translate("Interpretation_Main", "Spectral Decomp Tool"))
        self.label_3.setText(_translate("Interpretation_Main", "Coherency Methods:"))
        self.SeisIntCoherencyToolButton.setText(_translate("Interpretation_Main", "Coherency Tool"))
        self.label_4.setText(_translate("Interpretation_Main", "Amplitude Methods:"))
        self.SeisIntAmpliudeToolButton.setText(_translate("Interpretation_Main", "Amplitude Tool"))
        self.Interpretation_tabWidget.setTabText(self.Interpretation_tabWidget.indexOf(self.SeisAttributes_Tab), _translate("Interpretation_Main", "Seismic Attributes"))
        self.Interpretation_tabWidget.setTabText(self.Interpretation_tabWidget.indexOf(self.SeisInterpretation_Tab), _translate("Interpretation_Main", "Seismic Interpretation"))
        self.Interpretation_tabWidget.setTabText(self.Interpretation_tabWidget.indexOf(self.WellCorrelationTab), _translate("Interpretation_Main", "Wells Correlation"))
