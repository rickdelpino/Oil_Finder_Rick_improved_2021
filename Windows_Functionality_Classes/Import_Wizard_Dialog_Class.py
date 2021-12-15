# Import System libraries
import sys
import os
from pathlib import Path

# Import all user Forms and Windows
# from UI_Windows_Objects.Oil_Finder_Layout_9 import Ui_OF_MainWindow
# from UI_Windows_Objects.AI_Tools_Main import Ui_AI_Main
# from UI_Windows_Objects.DataScience_Tools_Main_3 import Ui_DataScience_Main
# from UI_Windows_Objects.ImportWizard_Main import Ui_ImportWindow
from UI_Windows_Objects.ImportWizard_Dialog import Ui_ImportDialog 
# from UI_Windows_Objects.Interpretation_Main import Ui_Interpretation_Main
# from UI_Windows_Objects.SpecDecompTool_Main import Ui_SpecDecomTool_Main
from UI_Windows_Objects.ImportSeisWizard_DialogWindow import Ui_Seismic_Import_Dialog

# Import Plotting libraries
# from Plotting_Classes.mplwidget import MplWidget
# from Plotting_Classes.Plot_2D_Seismic import Plot2DSeismic 
# from Plotting_Classes.Plot_2D_DataScience_Graphs import Plot2D_DataScienceGraph

# # Import Windows Functionality Windows
#from Oil_Finder_Main_9 import OilFinderWindow
# from Oil_Finder_Main_9 import window
from Windows_Functionality_Classes.Import_SeisWizard_MainWindow_Class import ImportSeisWizard_Main_Window
from Windows_Functionality_Classes.Import_TraceVSP_Wizard_DialogWindow_Class import ImportTraceVSP_Wizard_Dialog

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
class ImportWizard_Dialog(qtw.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui_ImportWiz = Ui_ImportDialog()
        self.ui_ImportWiz.setupUi(self)

        self.seismic_filename_1 = []
        self.trace_filename = []
        self.type_of_seismic = []
        self.seis_3D_data = None
        self.seis_3D_twt = None
        self.seis_3D_inlines = None
        self.seis_3D_crosslines = None
        self.data_traceVSP_1 = None
        

        # Apretar Boton de Importar Sismica:
        # Antiguo Call Import Data Button Signal
        self.ui_ImportWiz.ImportSeisButton.clicked.connect(self.ImportSeisWizard_Main_Window_show)
        
        self.ui_ImportWiz.ImportTraceVSP_Button.clicked.connect(self.ImportTraceVSPWizard_Dialog_show)


        self.ui_ImportWiz.ImportWiz_buttonBox.accepted.connect(self.push_Ok_ImportWiz)
        self.ui_ImportWiz.ImportWiz_buttonBox.rejected.connect(self.rejected)

    # Method Import Seis Wizard Window SHOW:
    @qtc.pyqtSlot()
    def ImportSeisWizard_Main_Window_show(self):
        self.ImportSeisWizard_Window = ImportSeisWizard_Main_Window(self)
        self.ImportSeisWizard_Window.show()

        # Get the name of slice and show it:        
        if  (self.ImportSeisWizard_Window.exec_() == qtw.QDialog.Accepted):
            self.seismic_filename_1 = self.ImportSeisWizard_Window.seis_filename[0]
            self.type_of_seismic   = self.ImportSeisWizard_Window.is_2D_or_3D
            self.inline_byte = self.ImportSeisWizard_Window.iline
            self.xline_byte = self.ImportSeisWizard_Window.xline
            # self.seis_3D_data_1 = self.seis_3D_data
            # self.seis_3D_twt_1 = self.seis_3D_twt
            # self.seis_3D_inlines_1 = self.seis_3D_inlines
            # self.seis_3D_crosslines_1 = self.seis_3D_crosslines
            print('2do Level:', self.seismic_filename_1)
            print('Type of seismic 2do level:', self.type_of_seismic)

    @qtc.pyqtSlot()
    # Method Import Trace/VSP Wizard Window Button
    def ImportTraceVSPWizard_Dialog_show(self):
        self.TraceVSP_Window = ImportTraceVSP_Wizard_Dialog(self)
        self.TraceVSP_Window.show()
        # self.AI_Window = AI_Main_Window(self)
        # self.AI_Window.show()
        if  (self.TraceVSP_Window.exec_() == qtw.QDialog.Accepted):
            self.data_traceVSP_1 = self.TraceVSP_Window.data_trace_VSP
            self.trace_filename = self.TraceVSP_Window.traceVSP_filename
            self.sample_rate = self.TraceVSP_Window.sr
            self.type_of_trace = self.TraceVSP_Window.is_Trace_or_VSP
            print('se ploteo self.data_trace_VSP 2do nivel')




    def push_Ok_ImportWiz(self):
        
        print('Tercer Nivel:', self.seismic_filename_1)
        self.accept()

    # if  __name__ == "__main__":
#     app = qtw.QApplication([])
#     dialog = ImportWizard_Main_Window()
#     dialog.show()

#     app.exec_()            



    # Method Import Seismic Button Data   
   