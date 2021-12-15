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
class Plot2D_DataSciencePies():
    """ - Ui_QWidget = es el QWidget en la Ui al que se le anadira el Matplot.
        - DSc_filename   = es el nombre del archivo Segy a abrir."""
    def __init__(self, Ui_QWidget, df_filt_def_counted, chart_title, attr_names_x, tocount_title, 
        attr_tocount_y, name_of_rows, isexploded, selected_slice):
    
    # Class Plot2D_DataScienceGraph:
    # Ui_QWidget:   Object from Main Window (window), related to the DataScience Tab
    # pandas_dataframe: Sub Dataframe with all data filtered with two columns from the CSV file
    # chart_title:      text with the title of the chart: feature selected from left list
    # attr_names_x:     text list with the attributes selected: from the left list 
    # tocount_title:    text with the feature to count, which contain the attributes from the right lst
    # attr_tocount_y:   text list with the attributes to count selected: from the right list
    # name_of_rows:     text explaining what are each row in the dataframe (frequency)
    # selected_slice:   text with the name of the slice to explode
        # Coneccion del QWidget con la clase promovida MplWidget() en el Qt Designer
        self.plot_DSC_chart = MplWidget(Ui_QWidget)

        self.exploded = []

        # Getting columns names for the pandas.pivot() method:
        self.df_columns_names = list(df_filt_def_counted.columns)

        self.list_to_explode = list(df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
            self.df_columns_names[2]).index)

        # Names of columns AFTER pivoting
        self.list_of_dfcolumns = list(df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
            self.df_columns_names[2]).columns)
        
        print('List of dataframe columns:', self.list_of_dfcolumns)
        
        for i in range(len(self.list_to_explode)):
            if (self.list_to_explode[i] != selected_slice): 
                self.exploded.append(0)
            else:
                self.exploded.append(0.34)

        print(self.exploded)
        
        self.frame_pivoted = df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
            self.df_columns_names[2])

        print('Dataframe to plot: ', self.frame_pivoted)

        # Getting a Colormap to create a consistent color distribution: this colorbar is short!
        # BE CAREFUL! THIS COLORMAP IS SHORT, PUT A METHOD TO CONSTRAIN OR ALERT FOR LONG FEATURES!
        #my_default_colorbar = ['blue', 'orange', 'green', 'red', 'purple', 
        #    'brown', 'pink', 'gray', 'olive', 'cyan']
        
        my_default_colorbar = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 
            'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
        #colorbar_short = plt.cm.get_cmap('tab10', len(self.list_to_explode))
        #colorbar_short = plt.cm.get_cmap('viridis', len(self.list_to_explode))
        # rgb_colormap = []
        # for i in range(colorbar_short.N):
        #     rgb = colorbar_short(i)[:4] # will return rgba, we take only first 3 so we get rgb
        #     #rgb_colormap.append(matplotlib.colors.to_rgba)
        #     rgb_colormap.append(matplotlib.colors.rgb2hex(rgb))
        colormap_edit = []
        for i in range(len(self.list_to_explode)):
            colormap_edit.append(my_default_colorbar[i])

        self.frame_pivoted['Colors'] = colormap_edit
        print('Colormap= ', self.frame_pivoted)
         





        ############################################
        # PLOTTING SECTION:
        ############################################
        
        # Plotea el Titulo del Grafico:
        #self.plot_DSC_chart.canvas.axes.set_title('Analisis of feature:  ' + chart_title)

        if (isexploded == 'No explode'):
            ix = 0
            
            for col in self.list_of_dfcolumns:
                values_pie = []
                #print(self.frame_pivoted[index].dropna())
                self.pie_df = self.frame_pivoted[[col,'Colors' ]].dropna()
                color_pie   = self.pie_df['Colors'].tolist()
                print('COLORSSSSS: ',color_pie)
                label_pie = self.pie_df.index.tolist()
                self.pie_df = self.pie_df[col]
                
                for h in self.pie_df.values.tolist():
                    values_pie.append(float(h))
                
                print('Labels: ',label_pie, 'Values: ',values_pie)
                ix = ix + 1
                ax = self.plot_DSC_chart.canvas.fig.add_subplot(1,len(self.list_of_dfcolumns), ix)
                print(ax)
                patches = ax.pie(x= values_pie, 
                    labels= label_pie,
                    autopct='%1.1f%%',
                    colors = color_pie)

                ax.legend(label_pie,
                    title = chart_title,
                    loc = "upper center",
                    bbox_to_anchor = (0.5, -0.1))

                ax.set_title(self.list_of_dfcolumns[ix-1], 
                    fontweight = 'bold',
                    fontsize = 'x-large',
                    pad=28)
                


            #cmap = matplotlib.cm.get_cmap('Spectral')
                #self.pie_df.plot(ax=self.plot_DSC_chart.canvas.axes,kind='pie', autopct='%1.1f%%', subplots=True, ylabel='')
            #self.frame_pivoted.plot(ax=self.plot_DSC_chart.canvas.axes,kind='pie', autopct='%1.1f%%', subplots=True, ylabel='')

            # Getting the Axes of the subplots:
            my_axes = self.plot_DSC_chart.canvas.fig.get_axes()
            print('My Axes:', my_axes)
            
            # Plotting legends:
            i = 0
            # for ax in my_axes:
            #     ax.legend(title = chart_title,
            #     loc = "upper center",
            #     bbox_to_anchor = (0.5, -0.1))

                
            #     ax.set_title(self.list_of_dfcolumns[i], 
            #     fontweight = 'bold',
            #     fontsize = 'x-large',
            #     pad=28)
            #     i = i + 1

    #loc = 'top', position = (1.5,0.5), y = 2.0,   x = 0.5,   ha = 'center',
            self.plot_DSC_chart.show()

        elif (isexploded == 'Explode'):

            del self.frame_pivoted['Colors']    
            self.frame_pivoted.plot(ax=self.plot_DSC_chart.canvas.axes, 
                kind='pie', 
                autopct='%1.1f%%', 
                subplots=True,
                shadow = True,
                explode = self.exploded)
          
            # self.frame_pivoted.plot(ax=self.plot_DSC_chart.canvas.axes, 
            #     kind='pie', 
            #     autopct='%1.1f%%', 
            #     subplots=True,
            #     shadow = True,
            #     explode = self.exploded)



            # Getting the Axes of the subplots:
            my_axes = self.plot_DSC_chart.canvas.fig.get_axes()
            print('My Axes:', my_axes)
            
            # Plotting legends:
            i = 0
            for ax in my_axes:
                ax.legend(title = chart_title,
                loc = "upper center",
                bbox_to_anchor = (0.5, -0.1))

                
                ax.set_title(self.list_of_dfcolumns[i], 
                fontweight = 'bold',
                fontsize = 'x-large',
                pad=28)
                i = i + 1

 
 
            self.plot_DSC_chart.show()

#explode = self.exploded,#






        # if chart_type == 'barh':
        #     # Ploteo del titulo de la frecuencia:
        #     self.plot_DSC_chart.canvas.axes.set_xlabel('Number of ' + name_of_rows)
        #     # Ploteo nombre de las barras:
        #     self.plot_DSC_chart.canvas.axes.set_ylabel('Names of Categories')


        #     # Get Labels for plotting horizontal:
        #     attr_tocount_pivot = list(df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
        #         self.df_columns_names[2]).columns)
            

                
            
        #     # Plotting horizontal bars:            
        #     df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
        #         self.df_columns_names[2]).plot(ax=self.plot_DSC_chart.canvas.axes,kind='barh')

        #     bar_labels = []
        #     for j in range(len(attr_tocount_pivot)):
        #         for i in range(len(attr_names_x)):
        #             bar_labels.append(attr_tocount_pivot[j])    

            
            
        #     if (boxchecker == 'LabelsOnTop'):
        #         i=0
        #         for rect in self.plot_DSC_chart.canvas.axes.patches:
        #             xloc = 5
        #             yloc = rect.get_y() + rect.get_height() / 2
        #             width = int(rect.get_width())
                    
        #             self.plot_DSC_chart.canvas.axes.annotate('{}'.format(bar_labels[i]),
        #                 xy=(width, yloc),
        #                 xytext=(xloc, 0),  # 3 points vertical offset
        #                 textcoords="offset points",
        #                 horizontalalignment='left', verticalalignment='center',
        #                 color='black', clip_on=True)
        #             i = i + 1
        #     if (boxchecker == 'ValuesOnTop'):
        #         for rect in self.plot_DSC_chart.canvas.axes.patches:
        #             xloc = 5
        #             yloc = rect.get_y() + rect.get_height() / 2
        #             width = int(rect.get_width())
                    
        #             self.plot_DSC_chart.canvas.axes.annotate('{}'.format(width),
        #                 xy=(width, yloc),
        #                 xytext=(xloc, 0),  # 3 points vertical offset
        #                 textcoords="offset points",
        #                 horizontalalignment='left', verticalalignment='center',
        #                 color='black', clip_on=True)
            

        #     if (boxchecker == 'ValuesAndLabelsOnTop'):
        #         i = 0
        #         for rect in self.plot_DSC_chart.canvas.axes.patches:
        #             xloc = 5
        #             yloc = rect.get_y() + rect.get_height() / 2
        #             width = int(rect.get_width())
                    
        #             self.plot_DSC_chart.canvas.axes.annotate('{}'.format(bar_labels[i] + ':  '+ str(width)),
        #                 xy=(width, yloc),
        #                 xytext=(xloc, 0),  # 3 points vertical offset
        #                 textcoords="offset points",
        #                 horizontalalignment='left', verticalalignment='center',
        #                 color='black', clip_on=True)
        #             i = i + 1
            
        #     if (boxchecker == 'NothingOnTop'):
        #         i = 0
        #         for rect in self.plot_DSC_chart.canvas.axes.patches:
        #             xloc = 5
        #             yloc = rect.get_y() + rect.get_height() / 2
        #             width = int(rect.get_width())
                    
        #             ann = self.plot_DSC_chart.canvas.axes.annotate([],
        #                 xy=(width, yloc),
        #                 xytext=(xloc, 0),  # 3 points vertical offset
        #                 textcoords="offset points",
        #                 horizontalalignment='left', verticalalignment='center',
        #                 color='black', clip_on=True)
        #             ann.remove()
        #             i = i + 1
                

        #     # End Labels Plotting Horizontal.
            
        #     self.plot_DSC_chart.show()


        # if chart_type == 'barv':
        #     # Ploteo del titulo de la frecuencia:
        #     self.plot_DSC_chart.canvas.axes.set_ylabel('Number of ' + name_of_rows)
        #     # Ploteo nombre de las barras:
        #     self.plot_DSC_chart.canvas.axes.set_xlabel('Names of Categories')

            
        #     df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
        #         self.df_columns_names[2]).plot(ax=self.plot_DSC_chart.canvas.axes, kind='bar', rot=0)
            
        #     # Labels plotting horizontal:
        #     attr_tocount_pivot = list(df_filt_def_counted.pivot(self.df_columns_names[0],self.df_columns_names[1],
        #         self.df_columns_names[2]).columns)
            

        #     bar_labels = []
        #     for j in range(len(attr_tocount_pivot)):
        #         for i in range(len(attr_names_x)):
        #             bar_labels.append(attr_tocount_pivot[j])
            
        

            
        #     if (boxchecker == 'ValuesOnTop'):
        #         for rect in self.plot_DSC_chart.canvas.axes.patches:
        #             height = rect.get_height()
        #             self.plot_DSC_chart.canvas.axes.annotate('{}'.format(height),
        #                 xy=(rect.get_x() + rect.get_width() / 2, height),
        #                 xytext=(0, 3),  # 3 points vertical offset
        #                 textcoords="offset points",
        #                 ha='center', va='bottom')
                
                            
        #     if (boxchecker == 'LabelsOnTop'):
        #         i = 0
        #         for rect in self.plot_DSC_chart.canvas.axes.patches:
        #             height = rect.get_height()
        #             self.plot_DSC_chart.canvas.axes.annotate('{}'.format(bar_labels[i]),
        #                 xy=(rect.get_x() + rect.get_width() / 2, height),
        #                 xytext=(0, 3),  # 3 points vertical offset
        #                 textcoords="offset points",
        #                 ha='center', va='bottom')
        #             i = i + 1
            
        #     if (boxchecker == 'ValuesAndLabelsOnTop'):
        #         i = 0
        #         for rect in self.plot_DSC_chart.canvas.axes.patches:
        #             height = rect.get_height()
        #             self.plot_DSC_chart.canvas.axes.annotate('{}'.format(bar_labels[i] + ':  ' + str(height)),
        #                 xy=(rect.get_x() + rect.get_width() / 2, height),
        #                 xytext=(0, 3),  # 3 points vertical offset
        #                 textcoords="offset points",
        #                 ha='center', va='bottom')
        #             i = i + 1

        #     if (boxchecker == 'NothingOnTop'):
        #         i = 0
        #         for rect in self.plot_DSC_chart.canvas.axes.patches:
        #             height = rect.get_height()
        #             ann = self.plot_DSC_chart.canvas.axes.annotate([],
        #                 xy=(rect.get_x() + rect.get_width() / 2, height),
        #                 xytext=(0, 3),  # 3 points vertical offset
        #                 textcoords="offset points",
        #                 ha='center', va='bottom')
        #             ann.remove()
        #             i = i + 1


        #     self.plot_DSC_chart.show()


    # def ExplodeSlice_sender(self):
    #      # Sending this pivot to Exploding Slice list:        
    #     self.df_pivot_toExplodeList = self.df_filt_def_counted
        
#         return self.df_pivot_toExplodeList.pivot(self.df_columns_names[0], self.df_columns_names[1],self.df_columns_names[2])
# # class YouAreGay():
#     gay = True
#     def __init__(self):
#         moregay = True