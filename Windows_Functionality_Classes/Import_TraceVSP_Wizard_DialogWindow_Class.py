# Import System libraries
import sys
import os
from pathlib import Path

# Import all user Forms and Windows
# from UI_Windows_Objects.Oil_Finder_Layout_9 import Ui_OF_MainWindow
# from UI_Windows_Objects.AI_Tools_Main import Ui_AI_Main
# from UI_Windows_Objects.DataScience_Tools_Main_3 import Ui_DataScience_Main
# from UI_Windows_Objects.ImportWizard_Main import Ui_ImportWindow
# from UI_Windows_Objects.Interpretation_Main import Ui_Interpretation_Main
# from UI_Windows_Objects.SpecDecompTool_Main import Ui_SpecDecomTool_Main
from UI_Windows_Objects.ImportTraceVSP_DialogWindow import Ui_Trace_VSP_Import_Dialog

# Import Plotting libraries
# from Plotting_Classes.mplwidget import MplWidget
# from Plotting_Classes.Plot_2D_Seismic import Plot2DSeismic 
# from Plotting_Classes.Plot_2D_DataScience_Graphs import Plot2D_DataScienceGraph

# # Import Windows Functionality Windows
#from Oil_Finder_Main_9 import OilFinderWindow
# from Oil_Finder_Main_9 import window
# from Windows_Functionality_Classes.Import_Wizard_MainWindow_Class import ImportWizard_Main_Window
# from Windows_Functionality_Classes.Interpretation_MainWindow_Class import Interpretation_Main_Window
# from Windows_Functionality_Classes.SpecDecomp_MainWindow_Class import SpecDecomp_Main_Window
# from Windows_Functionality_Classes.Artif_Intell_MainWindow_Class import AI_Main_Window
# from Windows_Functionality_Classes.DataScience_MainWindow_Class import DataScience_Main_Window

# Import libraries
from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtCore as qtc 
# import numpy as np
# import pandas as pd
import segyio
# import csv
# # Make sure that we are using QT5
# import matplotlib
# matplotlib.use('Qt5Agg')
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# from matplotlib import pyplot as plt


# CLASS para darle funcionalidad a la Import Wizard Form Window
class ImportTraceVSP_Wizard_Dialog(qtw.QDialog):
    signal_traceVSP_name = qtc.pyqtSignal(str)
    #data_trace_VSP =   qtc.pyqtSignal(str)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui_ImportTraceVSPWiz = Ui_Trace_VSP_Import_Dialog()
        self.ui_ImportTraceVSPWiz.setupUi(self)

        self.is_Trace_or_VSP = 'Single Trace'
        #self.data_trace_VSP = None
    #     self.seis_3D_data = None
    #     self.iline = None
    #     self.xline = None
    #     # Apretar Boton de Importar Sismica:
    #     # Antiguo Call Import Data Button Signal
        

        
    #     self.ui_ImportSeisWiz.Seis2D_radioButton.toggled.connect(self.onClicked)
    #     self.ui_ImportSeisWiz.Seis3D_radioButton.toggled.connect(self.onClicked)
        self.ui_ImportTraceVSPWiz.SingleTrace_radioButton.toggled.connect(self.onClicked_trace)
        self.ui_ImportTraceVSPWiz.VSP_radioButton.toggled.connect(self.onClicked_trace)
        self.ui_ImportTraceVSPWiz.SelectFile_Trace_pushButton.clicked.connect(self.Import_TraceVSP_window)
        self.ui_ImportTraceVSPWiz.Import_TraceVSPWizard_buttonBox.accepted.connect(self.push_Ok_ImportTraceVSP)
        self.ui_ImportTraceVSPWiz.Import_TraceVSPWizard_buttonBox.rejected.connect(self.reject)


    #     self.ui_ImportSeisWiz.SelectFile_Seis_pushButton.clicked.connect(self.import_seis_window)

       
       
    #     self.ui_ImportSeisWiz.ImportSeisWizard_buttonBox.accepted.connect(self.push_Ok_ImportSeisWiz)
    #     self.ui_ImportSeisWiz.ImportSeisWizard_buttonBox.rejected.connect(self.reject)

        
    #     # Get the name of slice and show it:        
    #     # if  (self.SpecialSlice_Dialog.exec_() == qtw.QDialog.Accepted):
    #     #     self.selected_slice = self.SpecialSlice_Dialog.selected_item_text
    #     #     print('Slice Selected: ', self.selected_slice)
    #     #     self.ui_DataSc.DSc_SelectSlice_Label.setText(self.selected_slice)
    #     #     self.isexploded = 'Explode'

    def onClicked_trace(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.is_Trace_or_VSP = radioBtn.text()
            print('Radio Button: ', self.is_Trace_or_VSP)

    # Method Import Seismic Button Data   
    def Import_TraceVSP_window(self):
        
        if (self.is_Trace_or_VSP == 'Single Trace'):
            self.traceVSP_filename = qtw.QFileDialog.getOpenFileName(self, 'Open File','D:\\Documents\\SEGY_Importantes', 
            'Segy Files (*.sgy *.segy)')

            if (self.traceVSP_filename != ('', '')):
                with segyio.open(self.traceVSP_filename[0], 'r', ignore_geometry=True) as segyfiletrace:
                    ntraces = segyfiletrace.tracecount
                    self.sr = segyio.tools.dt(segyfiletrace)/1e3
                    nsamples = segyfiletrace.samples.size
                    owt = segyfiletrace.samples
                    self.data_trace_VSP = segyfiletrace.trace.raw[:]
                    self.ui_ImportTraceVSPWiz.VSP_TraceRange_label.setText( 'Number of traces: {:.0f}'.format(ntraces))
                    self.ui_ImportTraceVSPWiz.SampleRate_label.setText('Sample Rate: {:.4f}'.format(self.sr))
                    self.ui_ImportTraceVSPWiz.VSP_TimeRange_label.setText('Trace length (ms): {:.0f}'.format(self.sr * nsamples))

                    header = segyio.tools.wrap(segyfiletrace.text[0])
                    self.ui_ImportTraceVSPWiz.Trace_SegyHeader_textBrowser.setText(header)
                    self.ui_ImportTraceVSPWiz.Trace_FileName_lineEdit.setText(Path('{0}'.format(self.traceVSP_filename[0])).stem)

                    self.ui_ImportTraceVSPWiz.ReadTrace_pushButton.clicked.connect(self.push_Ok_ImportTraceVSP)                   
                    # self.ui_ImportSeisWiz.ReadSeis_pushButton.clicked.connect(self.read_segy_bytes)
                
            else:
                qtw.QMessageBox.critical(self, 'Critical!' , 'You have to select a segy file!', 
                    qtw.QMessageBox.Ok)

    def push_Ok_ImportTraceVSP(self):
            print('1st Level: ',self.traceVSP_filename[0])
            print('Type of Seismic:', self.is_Trace_or_VSP)
            print(self.data_trace_VSP)
            print('se ploteo self.data_trace_VSP 1er nivel')
            self.accept()







# if (self.is_Trace_or_VSP == '2D Seis'):
#             self.seis_filename = qtw.QFileDialog.getOpenFileName(self, 'Open File','D:\\Documents\\SEGY_Importantes', 
#             'Segy Files (*.sgy *.segy)')

#             if (self.seis_filename != ('', '')):
#                 with segyio.open(self.seis_filename[0], 'r', ignore_geometry=True) as segyfile2D:
#                     header = segyio.tools.wrap(segyfile2D.text[0])
#                     self.ui_ImportSeisWiz.SegyHeader_textBrowser.setText(header)
#                     self.ui_ImportSeisWiz.Seismic_FileName_lineEdit.setText(Path('{0}'.format(self.seis_filename[0])).stem)
                    
#                     # self.ui_ImportSeisWiz.ReadSeis_pushButton.clicked.connect(self.read_segy_bytes)
                
#             else:
#                 qtw.QMessageBox.critical(self, 'Critical!' , 'You have to select a segy file!', 
#                     qtw.QMessageBox.Ok)

#         elif (self.is_Trace_or_VSP == '3D Seis'):
#             self.seis_filename = qtw.QFileDialog.getOpenFileName(self, 'Open File','D:\\Documents\\SEGY_Importantes', 
#             'Segy Files (*.sgy *.segy)')
            
#             if (self.seis_filename != ('', '')):
#                 with segyio.open(self.seis_filename[0], 'r', ignore_geometry=True) as segyfile3D:
#                     header = segyio.tools.wrap(segyfile3D.text[0])
#                     self.ui_ImportSeisWiz.SegyHeader_textBrowser.setText(header)
#                     self.ui_ImportSeisWiz.Seismic_FileName_lineEdit.setText(Path('{0}'.format(self.seis_filename[0])).stem)

#                     # segyfile3D.close()  -------- revisar

#                     self.ui_ImportSeisWiz.ReadSeis_pushButton.clicked.connect(self.read_segy_bytes)

    # def read_segy_bytes(self):
    #     self.iline = int(self.ui_ImportSeisWiz.Input_Inline_lineEdit.text())
    #     print('Iline = ',self.iline)
    #     self.xline = int(self.ui_ImportSeisWiz.Input_Xline_lineEdit.text())
    #     print('Xline = ', self.xline)
    #     cdpx = int(self.ui_ImportSeisWiz.Input_XCoord_lineEdit.text())
    #     print('XCoor = ', cdpx)
    #     cdpy = int(self.ui_ImportSeisWiz.Input_YCoord_lineEdit.text())
    #     print('YCoor = ', cdpy)
    #     tstat = int(self.ui_ImportSeisWiz.Input_1stSamples_lineEdit.text())
    #     print('tstat = ', tstat)
        
    #     # with segyio.open(self.seis_filename[0], 'r', iline= iline, xline= xline, cdpx= cdpx,
    #     #     cdpy= cdpy, tstat= tstat) as segyfile1:

    #     with segyio.open(self.seis_filename[0], 'r', iline= self.iline, xline= self.xline) as self.segyfile3D:

    #         self.seis_3D_data = segyio.tools.cube(self.segyfile3D)
    #         self.seis_3D_ntraces = self.segyfile3D.tracecount
    #         self.seis_3D_sr = segyio.tools.dt(self.segyfile3D)/1e3
    #         self.seis3D_nsamples = self.segyfile3D.samples.size
    #         #twt = segyfile1.samples + tstat
    #         self.seis_3D_twt = self.segyfile3D.samples
    #         self.seis_3D_size_mb = self.seis_3D_data.nbytes/1024**2
    #         self.seis_3D_inlines = self.segyfile3D.ilines
    #         self.seis_3D_crosslines = self.segyfile3D.xlines
        
    #     self.ui_ImportSeisWiz.Inline_Range_label.setText('Total Inlines: {:.0f}, min={:.0f}, max={:.0f}'.format(self.seis_3D_inlines.size,
    #         self.seis_3D_inlines.min(),self.seis_3D_inlines.max()))
    #     self.ui_ImportSeisWiz.Xline_Range_label.setText('Total Xlines:  {:.0f}, min={:.0f}, max={:.0f}'.format(self.seis_3D_crosslines.size,
    #         self.seis_3D_crosslines.min(),self.seis_3D_crosslines.max()))
    #     self.ui_ImportSeisWiz.TimeRange_label.setText('TWT(ms): 1st = {0}, last = {1}'.format(self.seis_3D_twt[0],self.seis_3D_twt[-1]))

    #     #self.ui_ImportSeisWiz.IO_1stSampleText_lineEdit.setText(str(tstat))


    # def push_Ok_ImportSeisWiz(self):
    #     print('1st Level: ',self.seis_filename[0])
    #     print('Type of Seismic:', self.is_2D_or_3D)
    #     self.accept()
    # #     if (self.is_2D_or_3D == '2D Seismic'):
    # #         self.seis2D_filename = self.seis_filename[0]
        

    # #     elif (self.is_2D_or_3D == '3D Seismic'):
    # #         self.seis3D_data = self.data
    # #     self.accept()

# self.ui_ImportSeisWiz.Inline_Range_label.setText('Total Inlines: {:.0f}, min={:.0f}, max={:.0f}'.format(self.seis_3D_inlines.size,
#             self.seis_3D_inlines.min(),self.seis_3D_inlines.max()))



    # # @qtc.pyqtSlot()
    # # def DSc_SpecialSlice_Dialog_show(self):
    # #     self.SpecialSlice_Dialog = DSc_SpecialSlice_Dialog(self.df_filt_def_counted)
    # #     self.SpecialSlice_Dialog.show()
        
    # #     # Get the name of slice and show it:        
    # #     if  (self.SpecialSlice_Dialog.exec_() == qtw.QDialog.Accepted):
    # #         self.selected_slice = self.SpecialSlice_Dialog.selected_item_text
    # #         print('Slice Selected: ', self.selected_slice)
    # #         self.ui_DataSc.DSc_SelectSlice_Label.setText(self.selected_slice)
    # #         self.isexploded = 'Explode'