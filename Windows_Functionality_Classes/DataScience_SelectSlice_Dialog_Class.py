# Import System librries
import sys
import os
from pathlib import Path

# Import all user Forms and Windows
# from UI_Windows_Objects.Oil_Finder_Layout_11 import Ui_OF_MainWindow
# from UI_Windows_Objects.AI_Tools_Main import Ui_AI_Main
#from UI_Windows_Objects.DataScience_Tools_Main_7 import Ui_DataScience_Main
# from UI_Windows_Objects.DataScience_SpecialSlice_Main import Ui_DSc_SelectSlice_MainWindow
from UI_Windows_Objects.DataScience_SpecialSlice_Dialog import Ui_DSc_SelectSlice_Dialog
# from UI_Windows_Objects.ImportWizard_Main import Ui_ImportWindow
# from UI_Windows_Objects.Interpretation_Main import Ui_Interpretation_Main
# from UI_Windows_Objects.SpecDecompTool_Main import Ui_SpecDecomTool_Main

# Import Plotting libraries
# from Plotting_Classes.mplwidget import MplWidget
# from Plotting_Classes.Plot_2D_Seismic import Plot2DSeismic 
from Plotting_Classes.Plot_2D_DataScience_Graphs_2 import Plot2D_DataScienceGraph

# Import Windows Functionality Windows
# from Windows_Functionality_Classes.Import_Wizard_MainWindow_Class import ImportWizard_Main_Window
# from Windows_Functionality_Classes.Interpretation_MainWindow_Class import Interpretation_Main_Window
# from Windows_Functionality_Classes.SpecDecomp_MainWindow_Class import SpecDecomp_Main_Window
# from Windows_Functionality_Classes.Artif_Intell_MainWindow_Class import AI_Main_Window
# from Windows_Functionality_Classes.DataScience_SelectSlice_Dialog_Class import DSc_SpecialSlice_Dialog
# from Oil_Finder_Main_11 import DataScience_Main_Window

# Import libraries
from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtCore as qtc 
# import numpy as np
# import pandas as pd
# import segyio
# import csv
# Make sure that we are using QT5
#import matplotlib
#matplotlib.use('Qt5Agg')
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# from matplotlib import pyplot as plt



# AQUI TRANSFORME TODA LA CLASE QUE SUPUESTAMENTE ERA INTOCABLE...LES QUITE EL self, *args, **kwargs AL 
# __INIT__ Y AL __SUPER__, LE QUITE EL SELF DE DONDE LLAMAN ESTA CLASE, Y YA LE PASE LA VARIABLE!!!

class DSc_SpecialSlice_Dialog(qtw.QDialog):
    
    #selected_item_text = 'No selection'
    signal_selected_item = qtc.pyqtSignal(str)
    
    # IMPORTANTE!: SEGUIR ESTE ESQUEMA EN LAS DECLRACIONES CON *ARGS Y **KWARGS:
    # SEGUNDA Y TERCERA OPCION AL FINAL:
    def __init__(self, df_filt_def_counted, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui_SelectSlice = Ui_DSc_SelectSlice_Dialog()
        self.ui_SelectSlice.setupUi(self)
        
        
        # Llena los nombres del conteo en la lista inferior:
        self.ui_SelectSlice.DSc_SelectSlice_listWidget.clear()

        # Get Labels from Dataframe filtered:
        self.df_columns_names = list(df_filt_def_counted)
        self.df_pivot_toExplodeList = df_filt_def_counted.pivot(self.df_columns_names[0], 
            self.df_columns_names[1], self.df_columns_names[2])

        self.df_rows_names = list(self.df_pivot_toExplodeList.index)            
        
        self.fillingup_list(self.df_rows_names)
        
        self.ui_SelectSlice.DSc_SelectSlice_listWidget.clicked.connect(self.getting_selected_item)
        
        
        self.ui_SelectSlice.DSc_SelectSlice_buttonBox.accepted.connect(self.push_OK_Button)
        self.ui_SelectSlice.DSc_SelectSlice_buttonBox.rejected.connect(self.reject)

        
    def fillingup_list(self, df_rows_names):     
        for i in df_rows_names:
            self.ui_SelectSlice.DSc_SelectSlice_listWidget.addItem(i)
        
                
    def getting_selected_item(self):
        self.selected_item = self.ui_SelectSlice.DSc_SelectSlice_listWidget.currentItem()
        
        self.ui_SelectSlice.Selected_Slice_label.setText(self.selected_item.text())

    def push_OK_Button(self):
        self.selected_item_text = self.selected_item.text()
        self.accept()
        
            
  
# SEGUNDA OPCION PARA INICIALIZAR:
# class Select_variable_window(QtWidgets.QDialog):
    # def __init__(self, items, parent=None):
    #     super().__init__(parent)

        

# FORMA ORIGINAL DE LA CLASE...GUARDAR:
# class DSc_SpecialSlice_MainWindow(qtw.QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(self, *args, **kwargs)

#         self.ui_SelectSlice = Ui_DSc_SelectSlice_MainWindow()
#         self.ui_SelectSlice.setupUi(self)