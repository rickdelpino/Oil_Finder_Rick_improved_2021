# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AI_Tools_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AI_Main(object):
    def setupUi(self, AI_Main):
        AI_Main.setObjectName("AI_Main")
        AI_Main.resize(678, 826)
        self.centralwidget = QtWidgets.QWidget(AI_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.AI_SeisInterpreter_Tab = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.AI_SeisInterpreter_Tab.setFont(font)
        self.AI_SeisInterpreter_Tab.setObjectName("AI_SeisInterpreter_Tab")
        self.AI_Restoration_Tab = QtWidgets.QWidget()
        self.AI_Restoration_Tab.setObjectName("AI_Restoration_Tab")
        self.AI_SeisInterpreter_Tab.addTab(self.AI_Restoration_Tab, "")
        self.AI_Wells_Tab = QtWidgets.QWidget()
        self.AI_Wells_Tab.setObjectName("AI_Wells_Tab")
        self.AI_SeisInterpreter_Tab.addTab(self.AI_Wells_Tab, "")
        self.HZ_Well_Nav_tab = QtWidgets.QWidget()
        self.HZ_Well_Nav_tab.setObjectName("HZ_Well_Nav_tab")
        self.AI_SeisInterpreter_Tab.addTab(self.HZ_Well_Nav_tab, "")
        self.AI_SeisDesign_Tab = QtWidgets.QWidget()
        self.AI_SeisDesign_Tab.setObjectName("AI_SeisDesign_Tab")
        self.AI_SeisInterpreter_Tab.addTab(self.AI_SeisDesign_Tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.AI_SeisInterpreter_Tab.addTab(self.tab, "")
        self.gridLayout.addWidget(self.AI_SeisInterpreter_Tab, 0, 0, 1, 1)
        AI_Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AI_Main)
        self.statusbar.setObjectName("statusbar")
        AI_Main.setStatusBar(self.statusbar)

        self.retranslateUi(AI_Main)
        self.AI_SeisInterpreter_Tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AI_Main)

    def retranslateUi(self, AI_Main):
        _translate = QtCore.QCoreApplication.translate
        AI_Main.setWindowTitle(_translate("AI_Main", "AI Window"))
        self.AI_SeisInterpreter_Tab.setTabText(self.AI_SeisInterpreter_Tab.indexOf(self.AI_Restoration_Tab), _translate("AI_Main", "Restoration Analysis"))
        self.AI_SeisInterpreter_Tab.setTabText(self.AI_SeisInterpreter_Tab.indexOf(self.AI_Wells_Tab), _translate("AI_Main", "Wells Success Analysis"))
        self.AI_SeisInterpreter_Tab.setTabText(self.AI_SeisInterpreter_Tab.indexOf(self.HZ_Well_Nav_tab), _translate("AI_Main", "HZ Wells AutoNavigator"))
        self.AI_SeisInterpreter_Tab.setTabText(self.AI_SeisInterpreter_Tab.indexOf(self.AI_SeisDesign_Tab), _translate("AI_Main", "SeisDesign Optimization"))
        self.AI_SeisInterpreter_Tab.setTabText(self.AI_SeisInterpreter_Tab.indexOf(self.tab), _translate("AI_Main", "Seismic Interpreter"))