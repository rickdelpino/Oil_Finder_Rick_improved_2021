# Import System librries
import sys
import os
from pathlib import Path

# Import all user Forms and Windows
# from UI_Windows_Objects.Oil_Finder_Layout_9 import Ui_OF_MainWindow
# from UI_Windows_Objects.AI_Tools_Main import Ui_AI_Main
# from UI_Windows_Objects.DataScience_Tools_Main_3 import Ui_DataScience_Main
# from UI_Windows_Objects.ImportWizard_Main import Ui_ImportWindow
from UI_Windows_Objects.Interpretation_Main import Ui_Interpretation_Main
from UI_Windows_Objects.SpecDecompTool_Main import Ui_SpecDecomTool_Main

# Import Plotting libraries
# from Plotting_Classes.mplwidget import MplWidget
# from Plotting_Classes.Plot_2D_Seismic import Plot2DSeismic 
# from Plotting_Classes.Plot_2D_DataScience_Graphs import Plot2D_DataScienceGraph

# Import Windows Functionality Windows
# from Windows_Functionality_Classes.Import_Wizard_MainWindow_Class import ImportWizard_Main_Window
# from Windows_Functionality_Classes.Interpretation_MainWindow_Class import Interpretation_Main_Window
from Windows_Functionality_Classes.SpecDecomp_MainWindow_Class import SpecDecomp_Main_Window
# from Windows_Functionality_Classes.Artif_Intell_MainWindow_Class import AI_Main_Window
# from Windows_Functionality_Classes.DataScience_MainWindow_Class import DataScience_Main_Window

# Import libraries
from PyQt5 import QtWidgets as qtw 
# from PyQt5 import QtCore as qtc 
# import numpy as np
# import pandas as pd
# import segyio
# import csv
# # Make sure that we are using QT5
# import matplotlib
# matplotlib.use('Qt5Agg')
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# from matplotlib import pyplot as plt



# CLASS to give funtionality to Interpretation Main Window
class Interpretation_Main_Window(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui_InterSeis = Ui_Interpretation_Main()
        self.ui_InterSeis.setupUi(self)
        ############################################################################
        # Buttons clicked funtionality for Interpretation Main Window
        ############################################################################

        # Call to Spectral Decomposition Method with Button
        self.ui_InterSeis.SeisIntSpecDecomToolButton.clicked.connect(self.SpecDecomp_Win_Show) 
        

        ############################################################################
        # End Buttons clicked funtionality for Interpretation Main Window
        ############################################################################
    
    ###############################################################
    # Methods of Interpretation Main Window buttons
    ###############################################################
    
    # Method to show and call Spectral Decomposition Tool Window
    def SpecDecomp_Win_Show(self):
        self.SpecDecom_Window = SpecDecomp_Main_Window(self)
        self.SpecDecom_Window.show()
    

    ###############################################################
    # End Methods of Interpretation Main Window buttons
    ###############################################################

