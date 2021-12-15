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
class Plot_SingleTrace_VSP():
    """ - Ui_QWidget = es el QWidget en la Ui al que se le anadira el Matplot.
        - filename   = es el nombre del archivo Segy a abrir."""
    def __init__(self, Ui_QWidget, tracedata, filename, samplerate): # Aqui se anadio 'filename' en lugar de def __init__(self, parent=None, width=5, height=4, dpi=100):
        width=8
        height=7
        dpi=100
     
        # Coneccion del QWidget con la clase promovida MplWidget() en el Qt Designer
        self.plot_Trace_VSP = MplWidget(Ui_QWidget)

        # Dandole nombre al objeto plotseismic
        self.plot_Trace_VSP.setObjectName("plottraceVSP")       
        
        
        #seismicdata = seismicdata
        #seismicdata = seismicdata.T
        #tracedata = tracedata.T
        clip = abs(np.percentile(tracedata,0.99))
        #clip = abs(np.percentile(seismicdata, 0.999))   
        
        # Seccion de Ploteo de la sismica usando la clase Figure de Matplotlb
        # self.plotseismic.canvas.axes.cla()
        # self.plotseismic.canvas.axes.clear()
        
        # amplitude = tracedata[0]
        # time = []
        # for i in range(len(tracedata[0])):
        #     time.append(i*samplerate)



        print(tracedata.shape)
        self.plot_Trace_VSP.canvas.axes.set_title(
            Path('{0}'.format(filename)).stem)
        self.plot_Trace_VSP.canvas.axes.set_ylabel('Amplitude')
        self.plot_Trace_VSP.canvas.axes.set_xlabel('Time (ms)')
        
        ntraces, nsamples = tracedata.shape
        print('ntraces, nsamples',ntraces, nsamples)
        ntraces = ntraces 
        for i in range(ntraces):
            amplitude = tracedata[i]
            time = []
            for j in range(nsamples):
                time.append(j*samplerate)
            amplitude = amplitude + i*500
            self.plot_Trace_VSP.canvas.axes.plot(time, amplitude)
            #self.plot_Trace_VSP.canvas.axes.invert_yaxis()
            self.plot_Trace_VSP.canvas.axes.set_ylim([-500,5000])
            
            #self.plot_Trace_VSP.canvas.axes.fill_between(time, 0, amplitude, where= amplitude > 0, interpolate= True)

        #self.plot_Trace_VSP.canvas.axes.plot(tracedata[1]  )
        #self.plotseismic.canvas.fig.tight_layout()
        self.plot_Trace_VSP.show()
            
 #           self.plotseismic.canvas.draw()
