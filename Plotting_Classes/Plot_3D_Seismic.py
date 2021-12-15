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
# from Plotting_Classes.mplwidget import MplWidget

from Plotting_Classes.mplwidget3DSeis import MplWidget3DSeismic
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
class Plot3DSeismic():
    """ - Ui_QWidget = es el QWidget en la Ui al que se le anadira el Matplot.
        - filename   = es el nombre del archivo Segy a abrir."""
    def __init__(self, Ui_QWidget, seismic_to_plot, filename, inline_number, xline_number, tslice_number,
        nrows, ncols, index): # Aqui se anadio 'filename' en lugar de def __init__(self, parent=None, width=5, height=4, dpi=100):
        width=8
        height=7
        dpi=100
     
        # Coneccion del QWidget con la clase promovida MplWidget() en el Qt Designer
        # self.plot3Dseismic = MplWidget3DSeismic(Ui_QWidget, nrows, ncols, 1)
        self.plot3Dseismic = MplWidget3DSeismic(Ui_QWidget, 1, 1, 1)
        #self.plot3Dseismic1 = MplWidget3DSeismic(Ui_QWidget, 1, 2, 2)

        # Dandole nombre al objeto plotseismic
        self.plot3Dseismic.setObjectName("plot3Dseismic")
        #self.plot3Dseismic1.setObjectName("plot3Dseismic1")       
        
        
        # seismic_to_plot = seismic_to_plot.trace.raw[:]
        #seismic_to_plot = seismic_to_plot.T
        inline_to_plot = seismic_to_plot.iline[inline_number]
        xline_to_plot = seismic_to_plot.xline[xline_number]
        tslice_to_plot = seismic_to_plot.depth_slice[tslice_number]
        
        inline_to_plot = inline_to_plot.T
        xline_to_plot = xline_to_plot.T
        #seismic_to_plot = seismic_to_plot.T
        print(inline_to_plot)

        clip = abs(np.percentile(inline_to_plot, 0.999))   
        
        # Seccion de Ploteo de la sismica usando la clase Figure de Matplotlb
        # self.plot3Dseismic.canvas.axes.cla()
        # self.plot3Dseismic.canvas.axes.clear()
        self.plot3Dseismic.canvas3Ds.axes3Ds.set_title( Path('{0}'.format(filename)).stem )
        #self.plot3Dseismic1.canvas3Ds.axes3Ds.set_title('TimeSlice')
        self.plot3Dseismic.canvas3Ds.axes3Ds.set_ylabel('XLine no.')
        self.plot3Dseismic.canvas3Ds.axes3Ds.set_xlabel('Inline no.')
        # self.plot3Dseismic1.canvas3Ds.axes3Ds.set_ylabel('Samples')
        # self.plot3Dseismic1.canvas3Ds.axes3Ds.set_xlabel('Trace no.')
        # # f = self.plot3Dseismic.canvas.axes.imshow(seismic_to_plot, interpolation='bilinear', aspect='auto',vmin=-clip,vmax=clip,cmap='seismic')
        
        f1 = self.plot3Dseismic.canvas3Ds.axes3Ds.imshow(tslice_to_plot, interpolation='bilinear', aspect='auto',vmin=-clip,vmax=clip,cmap='seismic')
        #f2 = self.plot3Dseismic1.canvas3Ds.axes3Ds.imshow(inline_to_plot, interpolation='bilinear', aspect='auto',vmin=-clip,vmax=clip,cmap='seismic')
        self.plot3Dseismic.canvas3Ds.fig3Ds.colorbar(f1, orientation='vertical')
        self.plot3Dseismic.canvas3Ds.fig3Ds.tight_layout()
        # self.plot3Dseismic1.canvas3Ds.fig3Ds.tight_layout()
        
        self.plot3Dseismic.show()
        #sself.plot3Dseismic1.show()
        # # self.plot3Dseismic1.show()
# seismic_r      
#     self.plotseismic.canvas.draw()
