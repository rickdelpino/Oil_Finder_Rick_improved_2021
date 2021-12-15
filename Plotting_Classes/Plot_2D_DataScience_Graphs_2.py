# Import System librries
import sys
import os
from pathlib import Path

# Import all user Forms and Windows
# from UI_Windows_Objects.Oil_Finder_Layout_9 import Ui_OF_MainWindow
# from UI_Windows_Objects.AI_Tools_Main import Ui_AI_Main
# from UI_Windows_Objects.DataScience_Tools_Main_3 import Ui_DataScience_Main
# from UI_Windows_Objects.ImportWizard_Main import Ui_ImportWindow
#from UI_Windows_Objects.Interpretation_Main import Ui_Interpretation_Main
#from UI_Windows_Objects.SpecDecompTool_Main import Ui_SpecDecomTool_Main

# Import Plotting libraries
from Plotting_Classes.mplwidget import MplWidget
# from Plotting_Classes.Plot_2D_Seismic import Plot2DSeismic 
# from Plotting_Classes.Plot_2D_DataScience_Graphs import Plot2D_DataScienceGraph

# Import Windows Functionality Windows
# from Windows_Functionality_Classes.Import_Wizard_MainWindow_Class import ImportWizard_Main_Window
# from Windows_Functionality_Classes.Interpretation_MainWindow_Class import Interpretation_Main_Window
# from Windows_Functionality_Classes.SpecDecomp_MainWindow_Class import SpecDecomp_Main_Window
# from Windows_Functionality_Classes.DataScience_SelectSlice_Dialog_Class import DSc_SpecialSlice_Dialog_window
# from Windows_Functionality_Classes.Artif_Intell_MainWindow_Class import AI_Main_Window
# from Windows_Functionality_Classes.DataScience_MainWindow_Class import DataScience_Main_Window

# Import libraries
from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtCore as qtc 
import numpy as np
import pandas as pd
# import segyio
# import csv
# Make sure that we are using QT5
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt



# PLOTTING CLASS: Charts  -  into Data Science Charts using Matplolib with Qwidgets
class Plot2D_DataScienceGraph():
    """ - Ui_QWidget = es el QWidget en la Ui al que se le anadira el Matplot.
        - DSc_filename   = es el nombre del archivo Segy a abrir."""
    def __init__(self, Ui_QWidget, df_filt_def_counted, chart_title, attr_names_x, tocount_title, 
        attr_tocount_y, name_of_rows, chart_type, boxchecker):
    
    # Class Plot2D_DataScienceGraph:
    # Ui_QWidget:   Object from Main Window (window), related to the DataScience Tab
    # pandas_dataframe: Sub Dataframe with all data filtered with two columns from the CSV file
    # chart_title:      text with the title of the chart: feature selected from left list
    # attr_names_x:     text list with the attributes selected: from the left list 
    # tocount_title:    text with the feature to count, which contain the attributes from the right lst
    # attr_tocount_y:   text list with the attributes to count selected: from the right list
    # name_of_rows:     text explaining what are each row in the dataframe (frequency)
    # chart_type:       text with the type of graphs selected
    # boxchecker:       text indicating if the checkboxes are checked

        # Coneccion del QWidget con la clase promovida MplWidget() en el Qt Designer
        self.plot_DSC_chart = MplWidget(Ui_QWidget)
        
        # Getting columns names for the pandas.pivot() method:
        self.df_columns_names = list(df_filt_def_counted.columns)
               
        
        ############################################
        # PLOTTING SECTION:
        ############################################
        
        # Plotea el Titulo del Grafico:
        self.plot_DSC_chart.canvas.axes.set_title('Analisis of feature:  ' + chart_title)
                
        if chart_type == 'barh':
            # Ploteo del titulo de la frecuencia:
            self.plot_DSC_chart.canvas.axes.set_xlabel('Number of ' + name_of_rows)
            # Ploteo nombre de las barras:
            self.plot_DSC_chart.canvas.axes.set_ylabel('Names of Categories')


            # Get Labels for plotting horizontal:
            attr_tocount_pivot = list(df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
                self.df_columns_names[2]).columns)
            

                
            
            # Plotting horizontal bars:            
            df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
                self.df_columns_names[2]).plot(ax=self.plot_DSC_chart.canvas.axes,kind='barh')

            bar_labels = []
            for j in range(len(attr_tocount_pivot)):
                for i in range(len(attr_names_x)):
                    bar_labels.append(attr_tocount_pivot[j])    

            
            
            if (boxchecker == 'LabelsOnTop'):
                i=0
                for rect in self.plot_DSC_chart.canvas.axes.patches:
                    xloc = 5
                    yloc = rect.get_y() + rect.get_height() / 2
                    width = int(rect.get_width())
                    
                    self.plot_DSC_chart.canvas.axes.annotate('{}'.format(bar_labels[i]),
                        xy=(width, yloc),
                        xytext=(xloc, 0),  # 3 points vertical offset
                        textcoords="offset points",
                        horizontalalignment='left', verticalalignment='center',
                        color='black', clip_on=True)
                    i = i + 1
            if (boxchecker == 'ValuesOnTop'):
                for rect in self.plot_DSC_chart.canvas.axes.patches:
                    xloc = 5
                    yloc = rect.get_y() + rect.get_height() / 2
                    width = int(rect.get_width())
                    
                    self.plot_DSC_chart.canvas.axes.annotate('{}'.format(width),
                        xy=(width, yloc),
                        xytext=(xloc, 0),  # 3 points vertical offset
                        textcoords="offset points",
                        horizontalalignment='left', verticalalignment='center',
                        color='black', clip_on=True)
            

            if (boxchecker == 'ValuesAndLabelsOnTop'):
                i = 0
                for rect in self.plot_DSC_chart.canvas.axes.patches:
                    xloc = 5
                    yloc = rect.get_y() + rect.get_height() / 2
                    width = int(rect.get_width())
                    
                    self.plot_DSC_chart.canvas.axes.annotate('{}'.format(bar_labels[i] + ':  '+ str(width)),
                        xy=(width, yloc),
                        xytext=(xloc, 0),  # 3 points vertical offset
                        textcoords="offset points",
                        horizontalalignment='left', verticalalignment='center',
                        color='black', clip_on=True)
                    i = i + 1
            
            if (boxchecker == 'NothingOnTop'):
                i = 0
                for rect in self.plot_DSC_chart.canvas.axes.patches:
                    xloc = 5
                    yloc = rect.get_y() + rect.get_height() / 2
                    width = int(rect.get_width())
                    
                    ann = self.plot_DSC_chart.canvas.axes.annotate([],
                        xy=(width, yloc),
                        xytext=(xloc, 0),  # 3 points vertical offset
                        textcoords="offset points",
                        horizontalalignment='left', verticalalignment='center',
                        color='black', clip_on=True)
                    ann.remove()
                    i = i + 1
                

            # End Labels Plotting Horizontal.
            
            self.plot_DSC_chart.show()


        if chart_type == 'barv':
            # Ploteo del titulo de la frecuencia:
            self.plot_DSC_chart.canvas.axes.set_ylabel('Number of ' + name_of_rows)
            # Ploteo nombre de las barras:
            self.plot_DSC_chart.canvas.axes.set_xlabel('Names of Categories')

            
            df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
                self.df_columns_names[2]).plot(ax=self.plot_DSC_chart.canvas.axes, kind='bar', rot=0)
            
            # Labels plotting horizontal:
            attr_tocount_pivot = list(df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
                self.df_columns_names[2]).columns)
            

            bar_labels = []
            for j in range(len(attr_tocount_pivot)):
                for i in range(len(attr_names_x)):
                    bar_labels.append(attr_tocount_pivot[j])
            
        

            
            if (boxchecker == 'ValuesOnTop'):
                for rect in self.plot_DSC_chart.canvas.axes.patches:
                    height = rect.get_height()
                    self.plot_DSC_chart.canvas.axes.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
                
                            
            if (boxchecker == 'LabelsOnTop'):
                i = 0
                for rect in self.plot_DSC_chart.canvas.axes.patches:
                    height = rect.get_height()
                    self.plot_DSC_chart.canvas.axes.annotate('{}'.format(bar_labels[i]),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
                    i = i + 1
            
            if (boxchecker == 'ValuesAndLabelsOnTop'):
                i = 0
                for rect in self.plot_DSC_chart.canvas.axes.patches:
                    height = rect.get_height()
                    self.plot_DSC_chart.canvas.axes.annotate('{}'.format(bar_labels[i] + ':  ' + str(height)),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
                    i = i + 1

            if (boxchecker == 'NothingOnTop'):
                i = 0
                for rect in self.plot_DSC_chart.canvas.axes.patches:
                    height = rect.get_height()
                    ann = self.plot_DSC_chart.canvas.axes.annotate([],
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
                    ann.remove()
                    i = i + 1


            self.plot_DSC_chart.show()


        elif chart_type == 'pie':
            # self.plot_DSC_chart.canvas.axes.pie(prueba_list, labels=prueba_index, autopct='%1.1f%%')
            # self.plot_DSC_chart.show()
            
            # x = np.arange(len(attr_names_x))
            # width = 0.35
            # for i in range(len(attr_tocount_y)):
            #     dx = x - width/len(attr_tocount_y)
            #     self.plot_DSC_chart.canvas.axes.bar(dx,)
            #     self.plot_DSC_chart.show()

            # df = pd.DataFrame([['g1','c1',10],['g1','c2',12],['g1','c3',13],['g2','c1',8],
            #        ['g2','c2',10],['g2','c3',12]],columns=['group','column','val'])

            #df.pivot("column", "group", "val").plot(ax=self.plot_DSC_chart.canvas.axes,kind='bar')
            df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
                self.df_columns_names[2]).plot(ax=self.plot_DSC_chart.canvas.axes,kind='pie', autopct='%1.1f%%', subplots=True)


            self.plot_DSC_chart.show()

    # def ExplodeSlice_sender(self):
    #      # Sending this pivot to Exploding Slice list:        
    #     self.df_pivot_toExplodeList = self.df_filt_def_counted
        
#         return self.df_pivot_toExplodeList.pivot(self.df_columns_names[0], self.df_columns_names[1],self.df_columns_names[2])
# # class YouAreGay():
#     gay = True
#     def __init__(self):
#         moregay = True
