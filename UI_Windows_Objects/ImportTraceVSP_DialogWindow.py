# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImportTraceVSP_DialogWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Trace_VSP_Import_Dialog(object):
    def setupUi(self, Trace_VSP_Import_Dialog):
        Trace_VSP_Import_Dialog.setObjectName("Trace_VSP_Import_Dialog")
        Trace_VSP_Import_Dialog.resize(599, 758)
        self.Import_TraceVSPWizard_buttonBox = QtWidgets.QDialogButtonBox(Trace_VSP_Import_Dialog)
        self.Import_TraceVSPWizard_buttonBox.setGeometry(QtCore.QRect(220, 720, 341, 32))
        self.Import_TraceVSPWizard_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.Import_TraceVSPWizard_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Import_TraceVSPWizard_buttonBox.setObjectName("Import_TraceVSPWizard_buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Trace_VSP_Import_Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 551, 621))
        self.groupBox.setObjectName("groupBox")
        self.Trace_SegyHeader_textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.Trace_SegyHeader_textBrowser.setGeometry(QtCore.QRect(10, 280, 531, 331))
        self.Trace_SegyHeader_textBrowser.setObjectName("Trace_SegyHeader_textBrowser")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 59, 17))
        self.label.setObjectName("label")
        self.Input_Offset_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Input_Offset_lineEdit.setGeometry(QtCore.QRect(90, 38, 61, 23))
        self.Input_Offset_lineEdit.setObjectName("Input_Offset_lineEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 117, 51, 17))
        self.label_3.setObjectName("label_3")
        self.Input_XCoord_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Input_XCoord_lineEdit.setGeometry(QtCore.QRect(90, 114, 61, 23))
        self.Input_XCoord_lineEdit.setObjectName("Input_XCoord_lineEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 157, 59, 17))
        self.label_4.setObjectName("label_4")
        self.Input_YCoord_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Input_YCoord_lineEdit.setGeometry(QtCore.QRect(90, 154, 61, 23))
        self.Input_YCoord_lineEdit.setObjectName("Input_YCoord_lineEdit")
        self.VSP_TraceRange_label = QtWidgets.QLabel(self.groupBox)
        self.VSP_TraceRange_label.setGeometry(QtCore.QRect(270, 40, 261, 20))
        self.VSP_TraceRange_label.setText("")
        self.VSP_TraceRange_label.setObjectName("VSP_TraceRange_label")
        self.VSP_OffsetRange_label = QtWidgets.QLabel(self.groupBox)
        self.VSP_OffsetRange_label.setGeometry(QtCore.QRect(270, 81, 261, 20))
        self.VSP_OffsetRange_label.setText("")
        self.VSP_OffsetRange_label.setObjectName("VSP_OffsetRange_label")
        self.Multiplier_Offset_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Multiplier_Offset_lineEdit.setGeometry(QtCore.QRect(174, 38, 61, 23))
        self.Multiplier_Offset_lineEdit.setObjectName("Multiplier_Offset_lineEdit")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(170, 10, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.Multiplier_XCoord_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Multiplier_XCoord_lineEdit.setGeometry(QtCore.QRect(172, 114, 61, 23))
        self.Multiplier_XCoord_lineEdit.setObjectName("Multiplier_XCoord_lineEdit")
        self.Multiplier_YCoord_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Multiplier_YCoord_lineEdit.setGeometry(QtCore.QRect(172, 154, 61, 23))
        self.Multiplier_YCoord_lineEdit.setObjectName("Multiplier_YCoord_lineEdit")
        self.Input_Trace1stSamples_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Input_Trace1stSamples_lineEdit.setGeometry(QtCore.QRect(90, 193, 61, 23))
        self.Input_Trace1stSamples_lineEdit.setObjectName("Input_Trace1stSamples_lineEdit")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(8, 194, 81, 17))
        self.label_11.setObjectName("label_11")
        self.IO_Trace1stSampleText_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.IO_Trace1stSampleText_lineEdit.setGeometry(QtCore.QRect(90, 227, 61, 23))
        self.IO_Trace1stSampleText_lineEdit.setObjectName("IO_Trace1stSampleText_lineEdit")
        self.Multiplier_Trace1stSampleText_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Multiplier_Trace1stSampleText_lineEdit.setGeometry(QtCore.QRect(172, 227, 61, 23))
        self.Multiplier_Trace1stSampleText_lineEdit.setObjectName("Multiplier_Trace1stSampleText_lineEdit")
        self.SampleRate_label = QtWidgets.QLabel(self.groupBox)
        self.SampleRate_label.setGeometry(QtCore.QRect(270, 160, 261, 17))
        self.SampleRate_label.setText("")
        self.SampleRate_label.setObjectName("SampleRate_label")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 218, 59, 41))
        self.label_12.setObjectName("label_12")
        self.VSP_TimeRange_label = QtWidgets.QLabel(self.groupBox)
        self.VSP_TimeRange_label.setGeometry(QtCore.QRect(269, 120, 261, 20))
        self.VSP_TimeRange_label.setText("")
        self.VSP_TimeRange_label.setObjectName("VSP_TimeRange_label")
        self.ReadTrace_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.ReadTrace_pushButton.setGeometry(QtCore.QRect(400, 234, 111, 30))
        self.ReadTrace_pushButton.setObjectName("ReadTrace_pushButton")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(360, 10, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 59, 17))
        self.label_2.setObjectName("label_2")
        self.Input_TVD_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Input_TVD_lineEdit.setGeometry(QtCore.QRect(90, 75, 61, 23))
        self.Input_TVD_lineEdit.setObjectName("Input_TVD_lineEdit")
        self.Multiplier_Trace_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Multiplier_Trace_lineEdit.setGeometry(QtCore.QRect(174, 75, 61, 23))
        self.Multiplier_Trace_lineEdit.setObjectName("Multiplier_Trace_lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(Trace_VSP_Import_Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 20, 551, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.SingleTrace_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.SingleTrace_radioButton.setGeometry(QtCore.QRect(10, 30, 104, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.SingleTrace_radioButton.setFont(font)
        self.SingleTrace_radioButton.setChecked(True)
        self.SingleTrace_radioButton.setObjectName("SingleTrace_radioButton")
        self.VSP_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.VSP_radioButton.setGeometry(QtCore.QRect(120, 30, 104, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.VSP_radioButton.setFont(font)
        self.VSP_radioButton.setObjectName("VSP_radioButton")
        self.Trace_FileName_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.Trace_FileName_lineEdit.setGeometry(QtCore.QRect(360, 30, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Trace_FileName_lineEdit.setFont(font)
        self.Trace_FileName_lineEdit.setText("")
        self.Trace_FileName_lineEdit.setObjectName("Trace_FileName_lineEdit")
        self.SelectFile_Trace_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.SelectFile_Trace_pushButton.setGeometry(QtCore.QRect(293, 26, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SelectFile_Trace_pushButton.setFont(font)
        self.SelectFile_Trace_pushButton.setObjectName("SelectFile_Trace_pushButton")

        self.retranslateUi(Trace_VSP_Import_Dialog)
        self.Import_TraceVSPWizard_buttonBox.accepted.connect(Trace_VSP_Import_Dialog.accept)
        self.Import_TraceVSPWizard_buttonBox.rejected.connect(Trace_VSP_Import_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Trace_VSP_Import_Dialog)

    def retranslateUi(self, Trace_VSP_Import_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Trace_VSP_Import_Dialog.setWindowTitle(_translate("Trace_VSP_Import_Dialog", "Import Trace/VSP Wizard"))
        self.groupBox.setTitle(_translate("Trace_VSP_Import_Dialog", "Trace Bytes:"))
        self.label.setText(_translate("Trace_VSP_Import_Dialog", "Offset:"))
        self.Input_Offset_lineEdit.setText(_translate("Trace_VSP_Import_Dialog", "9"))
        self.label_3.setText(_translate("Trace_VSP_Import_Dialog", "X coord:"))
        self.Input_XCoord_lineEdit.setText(_translate("Trace_VSP_Import_Dialog", "73"))
        self.label_4.setText(_translate("Trace_VSP_Import_Dialog", "Y coord:"))
        self.Input_YCoord_lineEdit.setText(_translate("Trace_VSP_Import_Dialog", "77"))
        self.Multiplier_Offset_lineEdit.setText(_translate("Trace_VSP_Import_Dialog", "1"))
        self.label_9.setText(_translate("Trace_VSP_Import_Dialog", "Multiplier:"))
        self.Multiplier_XCoord_lineEdit.setText(_translate("Trace_VSP_Import_Dialog", "1"))
        self.Multiplier_YCoord_lineEdit.setText(_translate("Trace_VSP_Import_Dialog", "1"))
        self.Input_Trace1stSamples_lineEdit.setText(_translate("Trace_VSP_Import_Dialog", "109"))
        self.label_11.setText(_translate("Trace_VSP_Import_Dialog", "1st Sample:"))
        self.Multiplier_Trace1stSampleText_lineEdit.setText(_translate("Trace_VSP_Import_Dialog", "1"))
        self.label_12.setText(_translate("Trace_VSP_Import_Dialog", "<html><head/><body><p>1st Text:</p></body></html>"))
        self.ReadTrace_pushButton.setText(_translate("Trace_VSP_Import_Dialog", "Read Seismic"))
        self.label_5.setText(_translate("Trace_VSP_Import_Dialog", "Seismic Info:"))
        self.label_2.setText(_translate("Trace_VSP_Import_Dialog", "TVD:"))
        self.Input_TVD_lineEdit.setText(_translate("Trace_VSP_Import_Dialog", "21"))
        self.Multiplier_Trace_lineEdit.setText(_translate("Trace_VSP_Import_Dialog", "1"))
        self.groupBox_2.setTitle(_translate("Trace_VSP_Import_Dialog", "Import Seismic"))
        self.SingleTrace_radioButton.setText(_translate("Trace_VSP_Import_Dialog", "Single Trace"))
        self.VSP_radioButton.setText(_translate("Trace_VSP_Import_Dialog", "VSP"))
        self.SelectFile_Trace_pushButton.setText(_translate("Trace_VSP_Import_Dialog", "File"))
