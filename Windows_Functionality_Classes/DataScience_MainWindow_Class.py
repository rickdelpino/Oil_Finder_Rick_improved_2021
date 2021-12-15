# Import System libraries
import sys
import os
from pathlib import Path
# Import all user Forms and Windows
# from UI_Windows_Objects.Oil_Finder_Layout_9 import Ui_OF_MainWindow
# from UI_Windows_Objects.AI_Tools_Main import Ui_AI_Main
from UI_Windows_Objects.DataScience_Tools_Main_3 import Ui_DataScience_Main
# from UI_Windows_Objects.ImportWizard_Main import Ui_ImportWindow
# from UI_Windows_Objects.Interpretation_Main import Ui_Interpretation_Main
# from UI_Windows_Objects.SpecDecompTool_Main import Ui_SpecDecomTool_Main

# # Import Plotting libraries
# from Plotting_Classes.mplwidget import MplWidget
# from Plotting_Classes.Plot_2D_Seismic import Plot2DSeismic 
# from Plotting_Classes.Plot_2D_DataScience_Graphs import Plot2D_DataScienceGraph
# # Import Windows Functionality Windows
# #from Windows_Functionality_Classes.Import_Wizard_MainWindow_Class import ImportWizard_Main_Window
# from Windows_Functionality_Classes.Interpretation_MainWindow_Class import Interpretation_Main_Window
# from Windows_Functionality_Classes.SpecDecomp_MainWindow_Class import SpecDecomp_Main_Window
# from Windows_Functionality_Classes.Artif_Intell_MainWindow_Class import AI_Main_Window
# from Windows_Functionality_Classes.DataScience_MainWindow_Class import DataScience_Main_Window

# # Import libraries
from PyQt5 import QtWidgets as qtw 
# from PyQt5 import QtCore as qtc 
import numpy as np
# import pandas as pd
# import segyio
# import csv
 
# # Make sure that we are using QT5
# import matplotlib
# matplotlib.use('Qt5Agg')
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# from matplotlib import pyplot as plt


# CLASS to give funtionality to DataScience Form Window
class DataScience_Main_Window(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui_DataSc = Ui_DataScience_Main()
        self.ui_DataSc.setupUi(self)
        
        ############################################################################
        # Events and Buttons clicked funtionality
        ############################################################################

        # Apretar Boton de Importar Data Frame:
        DSc_open_status = self.ui_DataSc.DSsOpenASCIIButton2.clicked.connect(self.DSc_ASCII_Opener)
        
        # Llamado a get item despues de click en feature list:
        if DSc_open_status != 0:
            # Llenado de List IZQUIERDA con los features
            self.ui_DataSc.DSc_Feature_list.clicked.connect(self.DSc_get_feaure_item)
            # Llenado de List DERECHA con los features
            self.ui_DataSc.DSc_Feature_ToCount_list.clicked.connect(self.DSc_get_count_feaure_item)


            # Hacer algo con el feature obtenido...guardado en str(self.feature_select_item.text())
#            self.DSc_load_feature_subset()

            # Apretar Boton para plotear barras!!
            self.ui_DataSc.DScBarChartButton.clicked.connect(self.DSc_BarChart_Plotter)

            # Apretar Boton para plotear pies!!
            self.ui_DataSc.DScPieChartButton.clicked.connect(self.DSc_PieChart_Plotter)
        else:
            self.qtw.QMessageBox.Critical(self) 
        ############################################################################
        # End Events and Buttons clicked funtionality
        ############################################################################

    ########################################################
    # Methods inside the DataScience Main Window
    ########################################################
    # Method for opening the Data file
    def DSc_ASCII_Opener(self):
        self.DSc_ASCII_filename = qtw.QFileDialog.getOpenFileName(self, 'Open File','D:\Documents\Programas_Python\Oil_Finder_Rick\Data', 'CSV Files (*.csv *.dat)')
        global df_DSc_data
        if self.DSc_ASCII_filename:
            self.ui_DataSc.DSc_ShowFileSelected_Label.setText(
                Path(self.DSc_ASCII_filename[0]).stem)
            print('Opening Data Science file:    ', self.DSc_ASCII_filename[0])
            # Seccion de lectura del CSV (usando CSV reader):
            self.pandas_dataframe = pd.read_csv(self.DSc_ASCII_filename[0])  # Creating PANDAS Dataframe data
            
            #####################################
            # LLENADO DE LISTAS:
            #####################################
            # Llamada a Metodo de llenado de Lista Derecha de Main Features
            self.DSc_load_Features_List()
            # Llamada a Metodo de llenado de Lista Derecha de Main Features
            self.DSc_load_ToCount_Features_List()
            
            return self.pandas_dataframe
        
        else:
            return 0
            qtw.QMessageBox.Critical(self)

    # Method to populate the Left List with Main features
    def DSc_load_Features_List(self):
      
        # Carga del Dataframe de Pandas a la lista
        self.df_features_names = self.pandas_dataframe.columns.tolist()
        print('Lista de Features: ', self.df_features_names)
        print('Numero de Features:', len(self.df_features_names))

        for i in self.df_features_names:
            self.ui_DataSc.DSc_Feature_list.addItem(i)


    # Method to populate the Right List with to count features
    def DSc_load_ToCount_Features_List(self):
      
        # Carga del Dataframe de Pandas a la lista
        self.df_tocount_feat_names = self.pandas_dataframe.columns.tolist()
        print('Lista de Features2: ', self.df_tocount_feat_names)
        print('Numero de Features2:', len(self.df_tocount_feat_names))

        for k in self.df_tocount_feat_names:
            self.ui_DataSc.DSc_Feature_ToCount_list.addItem(k)


    # Method to get an item from RIGHT feature list:
    def DSc_get_feaure_item(self):
        self.feature_select_item = self.ui_DataSc.DSc_Feature_list.currentItem()
        #self.feature_select_item = self.ui_DataSc.DSc_Feature_list.selectedItems()
        #print('OJO, FEATURE SELECTED', str(self.feature_select_item.text()))
        self.ui_DataSc.DSc_FeatBase_Label.setText(str(self.feature_select_item.text()))

        # Llamado al query de valores iguales de un mismo feature: 
        self.DSc_load_feature_subset(str(self.feature_select_item.text()))
   
    
    # Method to get an item from LEFT feature list
    def DSc_get_count_feaure_item(self):
        self.feat_2count_select_item = self.ui_DataSc.DSc_Feature_ToCount_list.currentItem()
        #self.feature_select_item = self.ui_DataSc.DSc_Feature_list.selectedItems()
        #print('OJO, FEATURE SELECTED', str(self.feature_select_item.text()))
        self.ui_DataSc.DSc_Feat2Count_Label.setText(str(self.feat_2count_select_item.text()))





    # Metodo de valores iguales de un mismo feature:
    def DSc_load_feature_subset(self, feature_select_item):
        self.feature_selected = feature_select_item
        print('OJO, FEATURE SELECTED 2', self.feature_selected)
        self.column_feat_select = self.pandas_dataframe[self.feature_selected]
        print('Columna seleccionada=', self.column_feat_select)
        self.diff_values_in_columns = self.pandas_dataframe[self.feature_selected].value_counts()
        print('Diferentes valores en una columna=',self.diff_values_in_columns)
        #self.filter_feat_selec = (self.pandas_dataframe[self.feature_selected] == '')

        # PENDIENTE: COLOCAR UN IF PARA RESTRINGIR MUCHOS VALORES (MENOS DE 20?):
        self.diff_values_name = self.diff_values_in_columns.index.tolist()
        self.diff_values_freq = self.diff_values_in_columns.values.tolist()
        print('Nombre =',self.diff_values_name, 'Frecuencia =',self.diff_values_freq)

        print('Numero de Sub-Features:', len(self.diff_values_name))

        self.ui_DataSc.DSc_Feature_Subset_list.clear()
        for j in self.diff_values_name:
            self.ui_DataSc.DSc_Feature_Subset_list.addItem(j)



    # Method for ploting the Bar Chart
    def DSc_BarChart_Plotter(self):
        Plot2D_DataScienceGraph(window.ui.Tab_DataSc_graphics, self.pandas_dataframe, 'bar')
    # Method for ploting the Pie Chart
    def DSc_PieChart_Plotter(self):
        Plot2D_DataScienceGraph(window.ui.Tab_DataSc_graphics, self.pandas_dataframe, 'pie')
    
        # Revisar OPEN STATUS O errores de carga
            # Se anadio variable filename para pasarsela al ploteador / SE ESTA PASANDO EL OBJETO WIN, NO LA CLASE!
            #Plot2D_DataScienceGraph(window.ui.Tab_DataSc_graphics, self.DSc_ASCII_filename[0], self.ui_DataSc)
            #if #pressed button was X:
            #self.ui_DataSc.DScBarChartButton.clicked.connect()
            #elseif # pressed button was Y:
            #self.ui_DataSc.DScPieChartButton.clicked.connect(Plot2D_DataScienceGraph(window.ui.Tab_DataSc_graphics, self.DSc_ASCII_filename[0], 'pie'))
        #elif os.path.exists(self.filename)=='':
        #    print('No file selected.')


    ########################################################
    # End Methods inside the DataScience Main Window
    ########################################################   
