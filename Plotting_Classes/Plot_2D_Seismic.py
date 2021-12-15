# Import System librries
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

# Import Plotting libraries
from Plotting_Classes.mplwidget import MplWidget
# from Plotting_Classes.Plot_2D_Seismic import Plot2DSeismic 
# from Plotting_Classes.Plot_2D_DataScience_Graphs import Plot2D_DataScienceGraph

# # Import Windows Functionality Windows
# from Windows_Functionality_Classes.Import_Wizard_MainWindow_Class import ImportWizard_Main_Window
# from Windows_Functionality_Classes.Interpretation_MainWindow_Class import Interpretation_Main_Window
# from Windows_Functionality_Classes.SpecDecomp_MainWindow_Class import SpecDecomp_Main_Window
# from Windows_Functionality_Classes.Artif_Intell_MainWindow_Class import AI_Main_Window
# from Windows_Functionality_Classes.DataScience_MainWindow_Class import DataScience_Main_Window

# Import libraries
from PyQt5 import QtWidgets as qtw 
# from PyQt5 import QtCore as qtc 
import numpy as np
# import pandas as pd
import segyio
# import csv
# Make sure that we are using QT5
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# from matplotlib import pyplot as plt




# PLOTTING CLASS: Seismic - from a segy file using Matplolib, SEGYIO and Qwidgets
class Plot2DSeismic():
    """ - Ui_QWidget = es el QWidget en la Ui al que se le anadira el Matplot.
        - filename   = es el nombre del archivo Segy a abrir."""
    def __init__(self, Ui_QWidget, filename): # Aqui se anadio 'filename' en lugar de def __init__(self, parent=None, width=5, height=4, dpi=100):
        width=8
        height=7
        dpi=100
     
        # Coneccion del QWidget con la clase promovida MplWidget() en el Qt Designer
        self.plotseismic = MplWidget(Ui_QWidget)

        # Dandole nombre al objeto plotseismic
        self.plotseismic.setObjectName("plotseismic")       
        
        # Seccion de lectura de la sismica (usando SEGYIO):
        print('Opening seismic file:    ',filename)
        with segyio.open(filename, 'r', ignore_geometry=True) as segyfile:
            ntraces = segyfile.tracecount
            sr = segyio.tools.dt(segyfile)/1e3
            nsamples = segyfile.samples.size
            twt = segyfile.samples
            seismicdata = segyfile.trace.raw[:]
            size_mb= seismicdata.nbytes/1024**2
            header = segyio.tools.wrap(segyfile.text[0])

            print('number of traces: ', ntraces)
            print('number of samples: ', nsamples)
            print('sample rate (ms):  ', sr)
            print('trace length (ms): ', sr * nsamples)
            print('size (Mb):         ', size_mb)

            #seismicdata = seismicdata
            seismicdata = seismicdata.T
            clip = abs(np.percentile(seismicdata, 0.999))   
            
            # Seccion de Ploteo de la sismica usando la clase Figure de Matplotlb
            self.plotseismic.canvas.axes.cla()
            self.plotseismic.canvas.axes.clear()
            self.plotseismic.canvas.axes.set_title(
                Path('{0}'.format(filename)).stem)
            self.plotseismic.canvas.axes.set_ylabel('Samples')
            self.plotseismic.canvas.axes.set_xlabel('Trace no.')
            self.plotseismic.canvas.axes.imshow(seismicdata,interpolation='bilinear', aspect='auto',vmin=-clip,vmax=clip,cmap='Greys')
            #self.plotseismic.canvas.fig.tight_layout()
            self.plotseismic.show()
            
 #           self.plotseismic.canvas.draw()
