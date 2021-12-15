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
# from Windows_Functionality_Classes.Artif_Intell_MainWindow_Class import AI_Main_Window
# from Windows_Functionality_Classes.DataScience_MainWindow_Class import DataScience_Main_Window

# Import libraries
from PyQt5 import QtWidgets as qtw 
# from PyQt5 import QtCore as qtc 
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
    def __init__(self, Ui_QWidget, pandas_dataframe, chart_title, attr_names_x, tocount_title, 
        attr_tocount_y, name_of_rows, chart_type):
    
    # Class Plot2D_DataScienceGraph:
    # Ui_QWidget:   Object from Main Window (window), related to the DataScience Tab
    # pandas_dataframe: Sub Dataframe with all data filtered with two columns from the CSV file
    # chart_title:      text with the title of the chart: feature selected from left list
    # attr_names_x:     text list with the attributes selected: from the left list 
    # tocount_title:    text with the feature to count, which contain the attributes from the right lst
    # attr_tocount_y:   text list with the attributes to count selected: from the right list
    # name_of_rows:     text explaining what are each row in the dataframe (frequency)
    # chart_type:

    #def __init__(self, Ui_QWidget, pandas_dataframe, chart_type): # Aqui se anadio 'filename' en lugar de def __init__(self, parent=None, width=5, height=4, dpi=100):
        width=8                                                   # Tambien se anadio dataframe de Pandas
        height=7
        dpi=100
     
        # Coneccion del QWidget con la clase promovida MplWidget() en el Qt Designer
        self.plot_DSC_chart = MplWidget(Ui_QWidget)
        #self.plot_DSC_chart_2 = MplWidget(Ui_QWidget)

        # Dandole nombre al objeto plot_DSC_chart
        self.plot_DSC_chart.setObjectName("plot_DSC_chart") 

           
        
        # Manejo del Dataframe de Pandas
#        self.df_features_names = pandas_dataframe.columns.tolist()
#        print('Lista de Features: ', self.df_features_names)
#        print('Numero de Features:', len(self.df_features_names))

#        for i in range(len(self.df_features_names))
#            self.plot_DSC_chart.

        #print('Info:', pandas_dataframe.info())
        #print('Shape del Dataframe: ', pandas_dataframe.shape)
        #print(pandas_dataframe.head(5))
        #print(pandas_dataframe.columns)
        
        #print(pandas_dataframe['Economic_Success'].value_counts())
        #print(pandas_dataframe.loc[['Tia_Juana'],'Economic_Success'])
        
        #print(pandas_dataframe.loc[[0,1],'Economic_Success'])
        
        # BORRAR: Retorna dos series de PANDAS (left and right features) con los features seleccionados:
        self.left_feature_serie = pandas_dataframe[chart_title].value_counts()
        self.right_feature_serie = pandas_dataframe[tocount_title].value_counts()
        
                
        self.prueba = self.left_feature_serie.loc[attr_names_x]
        #print('OYE MIRA',self.prueba)
   
        # Ahora...seleccion dentro de la lista filtrada:
                
        #self.sub_dataframe.set_index(chart_title, inplace=True)
        
        # FILTRADO QUITANDO LAS FILAS QUE NO SE SELECCIONARON EN EL PANEL IZQUIERDO...SIN MODIFICAR INDEX:
        df_filtered = pandas_dataframe.loc[pandas_dataframe[chart_title].isin(attr_names_x)]
        #print('DATAFRAME FILTRADO: ', df_filtered)
        
        # FILTRADO QUITANDO LAS FILAS QUE NO SE SELECCIONARON EN EL PANEL DERECHO...SIN MODIFICAR INDEX:
        df_filtered_definitive = df_filtered.loc[df_filtered[tocount_title].isin(attr_tocount_y)]
        print('DATAFRAME FILTRADO DEFINITIVO: ', df_filtered_definitive)
        

        # CONTEO de todos los valores y los guarda en otro Dataframe: NO LOS PUEDO CONTAR TODAVIA
        df_filt_def_counted = df_filtered_definitive.value_counts()
        #print('CONTANDO LOS VALUES:', df_filt_def_counted)
        print('otro cuaneto',df_filtered_definitive[tocount_title].value_counts())
        print("meirsadkljfklajk ",df_filtered_definitive.value_counts())
        print("shape: ",df_filtered_definitive.value_counts().shape)
        print('Index: ', df_filt_def_counted.index)

        # Reset Multi-Index from the counting:
        df_filt_def_counted = df_filt_def_counted.reset_index()
        print('Reset Index: ', df_filt_def_counted)
        print('Shape: ', df_filt_def_counted.shape)
        df_filt_def_counted.rename(columns = {0:'Values'}, inplace = True)
        print('Renamed Index: ', df_filt_def_counted)

        df_columns_names = list(df_filt_def_counted.columns)
        print('Columns names: ', df_columns_names)

        


        # print(type(df_filt_def_counted))
        # print(type(pandas_dataframe))
        #print(df_filt_def_counted.shape)
        
        # for i in range(len(attr_tocount_y)):
        #     if (df_filt_def_counted[index] != attr_tocount_y[i]):
        #         print('YOU ARE GAY!')

        
        # Comenzando filtrado para columna 2 (RIGHT):
        # for i in range(len(attr_tocount_y)):
        #     filter_column_2 = (df_filtered_definitive[tocount_title] == attr_tocount_y[i])
        #     temp = df_filtered_definitive[filter_column_2]
        #     if (temp.empty):
        #         print('Aqui se tiene ', 0 , ' de ', attr_tocount_y[i])
        #     else:
        #         print('Conteo No.',i,': ',temp.value_counts())


        # for i in range(len(attr_tocount_y)):
        #     filter_column_2 = pandas_dataframe[tocount_title]==attr_tocount_y[i]
        #     temp = pandas_dataframe[filter_column_2]
        #     print('Temporal ',i,' :\n',temp)
        
        # filtered_series=self.sub_dataframe.loc[attr_names_x]
        # print('Subdataframe FILTRADO:\n', filtered_series)
        # print('Value Counts:',filtered_series.value_counts())

        #CASI DEFINITIVO:
        # for i in range(len(attr_names_x)):
        #     filtered_series_names = filtered_series.loc[attr_names_x[i]]
        #     for j in range(len(attr_tocount_y)):
        #         filt = filtered_series_names[tocount_title] == attr_tocount_y[j]
        #         #print('Prueba de filtro',filt)
                
        #         print('Filter value counts of', attr_tocount_y[j],'in',attr_names_x[i],'=',sum(filt == True))


        
        # CASI CASI DEFINITIVO:
        # list_of_values = []
        # for i in range(len(attr_tocount_y)):
        #     filt_right = filtered_series[tocount_title] == attr_tocount_y[i]
        #     for j in range(len(attr_names_x)):
        #         valor = sum(filt_right.loc[attr_names_x[j]] == True)
        #         print('De la categoria ', attr_names_x[j], 'en el subconjunto ', attr_tocount_y[i], 'se tiene un valor de = ', valor)
        #         list_of_values.append(valor)

        # print('Aqui esta: ', list_of_values)

        # Plotea el Titulo del Grafico:
        self.plot_DSC_chart.canvas.axes.set_title('Analisis of feature:  ' + chart_title)
        
        #self.plot_DSC_chart.canvas.axes.set_ylabel('Number of wells')
        
        # Conversion de PANDAS series a lista para plotearlo en MATPLOTLIB 
        
        prueba_list =  self.prueba.values.tolist()
        prueba_index = self.prueba.index.tolist()
        print(prueba_index, prueba_list)
        
        if chart_type == 'barh':
            # Ploteo del titulo de la frecuencia:
            self.plot_DSC_chart.canvas.axes.set_xlabel('Number of ' + name_of_rows)
            # Ploteo nombre de las barras:
            self.plot_DSC_chart.canvas.axes.set_ylabel('Names of Categories')

            #self.plot_DSC_chart.canvas.axes.barh(prueba_index, prueba_list)
            
            df_filt_def_counted.pivot(df_columns_names[0],df_columns_names[1],
                df_columns_names[2]).plot(ax=self.plot_DSC_chart.canvas.axes,kind='barh')
            self.plot_DSC_chart.show()
        
        if chart_type == 'barv':
            # Ploteo del titulo de la frecuencia:
            self.plot_DSC_chart.canvas.axes.set_ylabel('Number of ' + name_of_rows)
            # Ploteo nombre de las barras:
            self.plot_DSC_chart.canvas.axes.set_xlabel('Names of Categories')

            #self.plot_DSC_chart.canvas.axes.bar(prueba_index, prueba_list)
            rects = df_filt_def_counted.pivot(df_columns_names[0],df_columns_names[1],
                df_columns_names[2]).plot(ax=self.plot_DSC_chart.canvas.axes, kind='bar', rot=0)
            
            #for p in self.plot_DSC_chart.canvas.axes.patches:
                #self.plot_DSC_chart.canvas.axes.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
                #self.plot_DSC_chart.canvas.axes.annotate(str(p.get_height()),
                #     (p.get_x() * 1.010, p.get_height() * 1.010))
            for rect in rects:
                height = rect.get_height()
                self.plot_DSC_chart.canvas.axes.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
            
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
            df_filt_def_counted.pivot(df_columns_names[0],df_columns_names[1],
                df_columns_names[2]).plot(ax=self.plot_DSC_chart.canvas.axes,kind='bar')


            self.plot_DSC_chart.show()