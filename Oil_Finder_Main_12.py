# Import System librries
import sys
import os
from pathlib import Path
# Import all user Forms and Windows
from UI_Windows_Objects.Oil_Finder_Layout_12 import Ui_OF_MainWindow
from UI_Windows_Objects.AI_Tools_Main import Ui_AI_Main
from UI_Windows_Objects.DataScience_Tools_Main_7 import Ui_DataScience_Main
from UI_Windows_Objects.DataScience_SpecialSlice_Dialog import Ui_DSc_SelectSlice_Dialog
# from UI_Windows_Objects.ImportWizard_Main import Ui_ImportWindow
from UI_Windows_Objects.ImportWizard_Dialog import Ui_ImportDialog
from UI_Windows_Objects.Interpretation_Main import Ui_Interpretation_Main
from UI_Windows_Objects.SpecDecompTool_Main import Ui_SpecDecomTool_Main
from UI_Windows_Objects.ImportTraceVSP_DialogWindow import Ui_Trace_VSP_Import_Dialog

# Import Plotting libraries
from Plotting_Classes.mplwidget import MplWidget
from Plotting_Classes.Plot_2D_Seismic import Plot2DSeismic
from Plotting_Classes.Plot_3D_Seismic import Plot3DSeismic 
from Plotting_Classes.Plot_2D_DataScience_Graphs_2 import Plot2D_DataScienceGraph
from Plotting_Classes.Plot_2D_DataScience_Pies_2 import Plot2D_DataSciencePies
from Plotting_Classes.Plot_SingleTraceVSP_Seismic import Plot_SingleTrace_VSP

# Import Windows Functionality Windows

# from Windows_Functionality_Classes.Import_Wizard_MainWindow_Class import ImportWizard_Main_Window
# from Windows_Functionality_Classes.Import_Wizard_MainWindow_2_Class import ImportWizard_Main_Window
from Windows_Functionality_Classes.Import_Wizard_Dialog_Class import ImportWizard_Dialog
from Windows_Functionality_Classes.Import_SeisWizard_MainWindow_Class import ImportSeisWizard_Main_Window
from Windows_Functionality_Classes.Interpretation_MainWindow_Class import Interpretation_Main_Window
from Windows_Functionality_Classes.SpecDecomp_MainWindow_Class import SpecDecomp_Main_Window
from Windows_Functionality_Classes.Artif_Intell_MainWindow_Class import AI_Main_Window
from Windows_Functionality_Classes.DataScience_SelectSlice_Dialog_Class import DSc_SpecialSlice_Dialog
# from Windows_Functionality_Classes.DataScience_MainWindow_Class import DataScience_Main_Window


# Import libraries
from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtCore as qtc 
import numpy as np
import xarray as xr  
import pandas as pd   
import segyio
import csv
 
# Make sure that we are using QT5
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

#************************************************************************************************************************************
# MAIN WINDOW CLASS *****************************************************************************************************************
#************************************************************************************************************************************
class OilFinderWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_OF_MainWindow()
        self.ui.setupUi(self)
       
       ###############################################################
        # Main Window button actions
       ###############################################################  
       
       
        # Call Import Data Button Signal
        self.ui.Import_Button.clicked.connect(self.ImportWizard_Window_show)

        # Call AI Tools Button Signal
        self.ui.AI_Button.clicked.connect(self.AI_Window_show)

        # Call DataScience Tools Button Signal
        self.ui.DataScience_Button.clicked.connect(self.DataScience_Window_show)

        # Call Interpretation Tools Button Signal
        self.ui.Interpretation_Button.clicked.connect(self.Interpretation_Window_show)
                
       
        ###############################################################
        # End Main Window button actions
        ###############################################################

    ###############################################################
    # Methods to show Windows from Main Window buttons
    ###############################################################

    # Method Import Wizard Window
    @qtc.pyqtSlot()
    def ImportWizard_Window_show(self):
        self.ImportWizard_Dialog = ImportWizard_Dialog(self)
        self.ImportWizard_Dialog.show()

        # Get the seismic filename:  
             
        if  (self.ImportWizard_Dialog.exec_() == qtw.QDialog.Accepted):
            print('Cuarto Nivel: ',self.ImportWizard_Dialog.seismic_filename_1)
            print('Type of seismic 4th Level: ', self.ImportWizard_Dialog.type_of_seismic)

            if (self.ImportWizard_Dialog.type_of_seismic == 'No Geometry'):
                Plot2DSeismic(window.ui.Tab_2D_graphics, self.ImportWizard_Dialog.seismic_filename_1)

            elif (self.ImportWizard_Dialog.type_of_seismic == '3D Seis'):
                with segyio.open(self.ImportWizard_Dialog.seismic_filename_1, 'r', 
                    iline=self.ImportWizard_Dialog.inline_byte, xline=self.ImportWizard_Dialog.xline_byte) as segy3Dfile:
                    data = segyio.tools.cube(segy3Dfile)
                    ntraces = segy3Dfile.tracecount
                    sr = segyio.tools.dt(segy3Dfile)/1e3
                    nsamples = segy3Dfile.samples.size
                    twt = segy3Dfile.samples
                    size_mb= data.nbytes/1024**2
                    inlines = segy3Dfile.ilines
                    crosslines = segy3Dfile.xlines
                    print('Inline byte:',self.ImportWizard_Dialog.inline_byte)
                    print('Xline byte:', self.ImportWizard_Dialog.xline_byte)


                    inline_number = 156
                    xline_number = 200
                    tslice_number = 1000
                    self.seismic_to_plot = segy3Dfile
                    # self.seismic_to_plot = segy3Dfile.iline[156]
                    nrows = 1
                    ncols = 1
                    index = [1,2]
                    print('index 0: ',index[0])
                    print('index 1: ',index[1])
                    #Plot3DSeismic(window.ui.Tab_3D_Seismic, self.seismic_to_plot, self.ImportWizard_Dialog.seismic_filename_1)
                    # Plot3DSeismic(window.ui.Tab_3Dseis_graphicsView, self.seismic_to_plot, 
                    #     self.ImportWizard_Dialog.seismic_filename_1, inline_number, xline_number, tslice_number)
                    Plot3DSeismic(window.ui.Tab_3Dseis_graphicsView, self.seismic_to_plot, 
                        self.ImportWizard_Dialog.seismic_filename_1, inline_number, xline_number, 
                            tslice_number, nrows, ncols, index)
                    # Plot3DSeismic(window.ui.Tab_3Dseis_graphicsView, self.seismic_to_plot, 
                    #     self.ImportWizard_Dialog.seismic_filename_1, inline_number, xline_number, 
                    # tslice_number, nrows, ncols, 2)

                # seismic_cube = xr.DataArray(data,[('IL',inlines),('XL',crosslines),('TWT',twt)])
                # seismic_cube.sel(IL=156).plot.imshow(x='XL',y='TWT',robust=True,yincrease=False)
                 # # seismic_cube.sel(IL=1376).plot.imshow(x='XL',y='TWT',robust=True,yincrease=False)
                #     # near = xr.DataArray(data,[('IL',inlines),('XL',crosslines),('TWT',twt)])  
            #############################
            # Plotting Single Trace VSP
            #############################
            elif (self.ImportWizard_Dialog.type_of_trace == 'Single Trace'):
                print(self.ImportWizard_Dialog.data_traceVSP_1) 
                print('Fue Ploteada traza VSP', self.ImportWizard_Dialog.trace_filename)
                Plot_SingleTrace_VSP(window.ui.Tab_Traces_VSP_graphics, self.ImportWizard_Dialog.data_traceVSP_1, 
                    Path(self.ImportWizard_Dialog.trace_filename[0]).stem, self.ImportWizard_Dialog.sample_rate)
        

    # Method AI Window Button
    def AI_Window_show(self):
        self.AI_Window = AI_Main_Window(self)
        self.AI_Window.show()
    
    # Method DataScience Window Button
    def DataScience_Window_show(self):
        self.DataScience_Window = DataScience_Main_Window(self)
        self.DataScience_Window.show()
    
    # Method Interpretation Window Button
    def Interpretation_Window_show(self):
        self.Interpretation_Window = Interpretation_Main_Window(self)
        self.Interpretation_Window.show()

    
    ######################################################
    # End Methods to show Windows from Main Window buttons
    ######################################################
#*********************************************************************************************************************************
# END MAIN WINDOW CLASS **********************************************************************************************************
#*********************************************************************************************************************************



################################################################
# CLASSES OF MAIN FUNCTIONALITY (DONT SUPOUSE TO BE HERE)
################################################################

# CLASS para darle funcionalidad a la Import Wizard Form Window
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class ImportWizard_Main_Window(qtw.QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.ui_ImportWiz = Ui_ImportWindow()
#         self.ui_ImportWiz.setupUi(self)

#         # Apretar Boton de Importar Sismica:
#         # Antiguo Call Import Data Button Signal
#         self.ui_ImportWiz.ImportSeisButton.clicked.connect(self.import_window)
   
#     # Method Import Seismic Button Data   
#     def import_window(self):
#         self.filename = qtw.QFileDialog.getOpenFileName(self, 'Open File','D:\Documents\SEGY_Importantes', 'Segy Files (*.sgy *.segy)')
        
#         if (self.filename != ('', '')):
#         # Revisar OPEN STATUS O errores de carga
#             # Se anadio variable filename para pasarsela al ploteador / SE ESTA PASANDO EL OBJETO WIN, NO LA CLASE!
#             #caca = main_window_object
#             Plot2DSeismic(window.ui.Tab_2D_graphics, self.filename[0])
#             #Plot2DSeismic(Ui_OF_MainWindow.OF
#             #    Ui_OF_MainWindow.Tab_2D_graphics,self.filename[0])
#             #   window.ui.Tab_2D_graphics, self.filename[0])

#         #elif os.path.exists(self.filename)=='':
#         #    print('No file selected.') 
#         else:
#             qtw.QMessageBox.critical(self, 'Critical!' , 'You have to select a segy file!',
#                 qtw.QMessageBox.Ok)



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# CLASS to give funtionality to DataScience Form Window
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
class DataScience_Main_Window(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui_DataSc = Ui_DataScience_Main()
        self.ui_DataSc.setupUi(self)
        
        # Program ask to declare this variablesfor DataScience_Main_Window attibute existence:
        self.boxchecker = []
        self.selection_status = False
        self.success_inferior_right_list = None
        self.success_inferior_left_list = None
        self.feature_select_item = None
        self.feat_2count_select_item = None
        self.isexploded = 'No explode'
        self.selected_slice = ''

        ############################################################################
        # Events and Buttons clicked funtionality
        ############################################################################

        # Apretar Boton de Importar Data Frame:
        DSc_open_status = self.ui_DataSc.DSsOpenASCIIButton2.clicked.connect(self.DSc_ASCII_Opener)
        
        # Llamado a get item despues de click en feature list:
        if (DSc_open_status != ('', '')):
            # Llenado de List IZQUIERDA con los features
            self.ui_DataSc.DSc_Feature_list.clicked.connect(self.DSc_get_feaure_item)
            # Llenado de List DERECHA con los features
            self.ui_DataSc.DSc_Feature_ToCount_list.clicked.connect(self.DSc_get_count_feaure_item)

            ######
            
            
            # Boton que de una vez carga las variables y filtra el Dataframe SOLO UNA VEZ.
            self.ui_DataSc.DSc_FilterDataFrame_Button.clicked.connect(self.DSc_FilterDataframe_all)
            #####


            # Checkboxes caller:
            
            self.ui_DataSc.DSc_ValuesOnTop_checkBox.toggled.connect(self.DSc_CheckBoxes)                
            self.ui_DataSc.DSc_LabelsOnTop_checkBox.toggled.connect(self.DSc_CheckBoxes)
                           
            # Button to show Dialog for Explode Slice (Special Slice):
            self.ui_DataSc.DSc_SpecialSlice_pushButton.clicked.connect(self.DSc_SpecialSlice_Dialog_show)

            # Button to CLEAR selected exploded pie slice:
            self.ui_DataSc.DSc_ClearSpecialSlice_pushButton.clicked.connect(self.DSc_Clear_ExplodedSlice)

            # Hacer algo con el feature obtenido...guardado en str(self.feature_select_item.text())
#            self.DSc_load_feature_subset()

            # Apretar Boton para plotear barras horizontales!!
            self.ui_DataSc.DScHBarChartButton.clicked.connect(self.DSc_HorzBarChart_Plotter)

            # Apretar Boton para plotear barras verticales!!
            self.ui_DataSc.DScVBarChartButton.clicked.connect(self.DSc_VertBarChart_Plotter)

            # Apretar Boton para plotear pies!!
            self.ui_DataSc.DScPieChartButton.clicked.connect(self.DSc_PieChart_Plotter)
        else:
            qtw.QMessageBox.critical(self,'Critical!' , 'There is a problem with your file!',
                qtw.QMessageBox.Ok)
        ############################################################################
        # End Events and Buttons clicked funtionality
        ############################################################################

    ###############################################################
    # Methods to show Windows from Data Science Main Window
    ###############################################################

    # Method to show Select Slice (Explode) Dialog window, and get slice:
    
    @qtc.pyqtSlot()
    def DSc_SpecialSlice_Dialog_show(self):
        self.SpecialSlice_Dialog = DSc_SpecialSlice_Dialog(self.df_filt_def_counted)
        self.SpecialSlice_Dialog.show()
        
        # Get the name of slice and show it:        
        if  (self.SpecialSlice_Dialog.exec_() == qtw.QDialog.Accepted):
            self.selected_slice = self.SpecialSlice_Dialog.selected_item_text
            print('Slice Selected: ', self.selected_slice)
            self.ui_DataSc.DSc_SelectSlice_Label.setText(self.selected_slice)
            self.isexploded = 'Explode'
    
    def DSc_Clear_ExplodedSlice(self):
        self.isexploded = 'No explode'
        self.selected_slice = ''
        self.ui_DataSc.DSc_SelectSlice_Label.setText(self.selected_slice)

    ###############################################################
    # End of Methods to show Windows from Data Science Main Window
    ###############################################################


    ########################################################
    # Methods inside the DataScience Main Window
    ########################################################
    # Methods for checkboxes:
    def DSc_CheckBoxes(self):
        self.checkLabel=self.ui_DataSc.DSc_LabelsOnTop_checkBox.checkState()
        self.checkValue=self.ui_DataSc.DSc_ValuesOnTop_checkBox.checkState()
        print('Checkeo Previo:', self.checkLabel, self.checkValue)

        if (self.checkLabel == 2):
            self.boxchecker = 'LabelsOnTop'
            print(self.boxchecker)

        if (self.checkValue == 2):
            self.boxchecker = 'ValuesOnTop'
            print(self.boxchecker)

        if ((self.checkValue == 2) and (self.checkLabel == 2)):
            self.boxchecker = 'ValuesAndLabelsOnTop'
            print(self.boxchecker)

        if ((self.checkValue == 0) and (self.checkLabel == 0)):
            self.boxchecker = 'NothingOnTop'
            print(self.boxchecker)
        
        #     print(self.boxchecker)
        # if self.ui_DataSc.DSc_LabelsOnTop_checkBox.isChecked():
        #     self.boxchecker = 'LabelsOnTop'
        #     print(self.boxchecker)
        
        # elif self.ui_DataSc.DSc_ValuesOnTop_checkBox.isChecked():
        #     self.boxchecker = 'ValuesOnTop'
        #     print(self.boxchecker)
        
        # elif (self.ui_DataSc.DSc_ValuesOnTop_checkBox.isChecked() and self.ui_DataSc.DSc_LabelsOnTop_checkBox.isChecked()):
        #     self.boxchecker = 'ValuesAndLabelsOnTop'
        #     print(self.boxchecker)
        
        # else: 
        #     self.boxchecker = 'NothingOnTop'
        #     print(self.boxchecker)
            
    # Method for opening the Data file
    def DSc_ASCII_Opener(self):
        self.DSc_ASCII_filename = qtw.QFileDialog.getOpenFileName(self, 'Open File','D:\Documents\Programas_Python\Oil_Finder_Rick\Data', 'CSV Files (*.csv *.dat)')
        print('RESULTS OF OPEN FILE: ', self.DSc_ASCII_filename,  type(self.DSc_ASCII_filename))
        global df_DSc_data
        if (self.DSc_ASCII_filename != ('', '')):
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
            qtw.QMessageBox.critical(self,'Critical!' , 'You have not selected a file!',
                qtw.QMessageBox.Ok)
            return 0
            

    # LISTAS SUPERIORES:
    # Method to populate the Left List with Main features
    def DSc_load_Features_List(self):
      
        # Conversion del nombre de las columnas del Pandas Dataframe a tipo lista Python
        self.df_features_names = self.pandas_dataframe.columns.tolist()
        
        # Limpia la lista de features primero, y luego llena la lista con el nombre de las columnas
        self.ui_DataSc.DSc_Feature_list.clear()
        for i in self.df_features_names:
            self.ui_DataSc.DSc_Feature_list.addItem(i)


    # Method to populate the Right List with to count features
    def DSc_load_ToCount_Features_List(self):
      
        # Conversion del nombre de las columnas del Pandas Dataframe a tipo lista Python 
        self.df_tocount_feat_names = self.pandas_dataframe.columns.tolist()
        
        # Limpia la lista de features primero, y luego llena la lista con el nombre de las columnas
        self.ui_DataSc.DSc_Feature_ToCount_list.clear()
        for k in self.df_tocount_feat_names:
            self.ui_DataSc.DSc_Feature_ToCount_list.addItem(k)


    # Method to get an item from LEFT feature list:
    def DSc_get_feaure_item(self):
        self.feature_select_item = self.ui_DataSc.DSc_Feature_list.currentItem()
        
        # Llama al contador de atributos en una misma columna y llena la lista inferior: 
        self.DSc_load_feature_subset(str(self.feature_select_item.text()))
   
    
    # Method to get an item from RIGHT feature list
    def DSc_get_count_feaure_item(self):
        self.feat_2count_select_item = self.ui_DataSc.DSc_Feature_ToCount_list.currentItem()
              
        # Llama al contador de atributos en una misma columna y llena la lista inferior: 
        self.DSc_load_feat_tocount_subset(str(self.feat_2count_select_item.text()))


    #LISTA INFERIOR IZQUIERDA:
    # Metodo Contador de atributos iguales en una columna del Dataframe, y llenado de lista inferior LEFT:
    def DSc_load_feature_subset(self, feature_select_item):
        self.feature_selected = feature_select_item
        
        # Se usa el feature seleccionado para crear una Serie Pandas del Dataframe, con el feature:
        self.column_feat_select = self.pandas_dataframe[self.feature_selected]
        
        # Cuenta todos los valores diferentes en la Serie Pandas correspondiente al feature seleccionado:
        self.diff_values_in_columns = self.column_feat_select.value_counts()
        
        #print('Feature seleccionado:',self.feature_selected,'Diferentes valores en el feature=',self.diff_values_in_columns)
        #self.filter_feat_selec = (self.pandas_dataframe[self.feature_selected] == '')

        # PENDIENTE: COLOCAR UN IF PARA RESTRINGIR MUCHOS VALORES (MENOS DE 20?):
        self.diff_values_name = self.diff_values_in_columns.index.tolist()
        self.diff_values_freq = self.diff_values_in_columns.values.tolist()
        #print('Nombre =',self.diff_values_name, 'Frecuencia =',self.diff_values_freq)

        #print('Numero de Sub-Features:', len(self.diff_values_name))

        # Llena los nombres del conteo en la lista inferior:
        self.ui_DataSc.DSc_Feature_Subset_list.clear()
        for j in self.diff_values_name:
            self.ui_DataSc.DSc_Feature_Subset_list.addItem(j)

        # Llena las frecuencias de los nombres del conteo en la lista inferior:
        self.str_diff_values_freq = map(str, self.diff_values_freq) # Convertir lista integer to text
        self.ui_DataSc.DSc_Feat_SubFreq_Left_list.clear()   # Limpia la lista antes de llenarla
        for j in self.str_diff_values_freq:
            self.ui_DataSc.DSc_Feat_SubFreq_Left_list.addItem(j)
        
    # Obtencion de los items seleccionados lista izquierda inferior:
    def DSc_get_items_inferior_list_left(self):
        
        
        # Obtiene los items seleccionados
        items = self.ui_DataSc.DSc_Feature_Subset_list.selectedItems()
        
        if (items != []):
            # Crea una lista vacia para llenar
            self.selected_inf_left = []
            # Llenado de la lista de texto usando un Loop
            for i in range(len(items)):
                self.selected_inf_left.append(items[i].text())
                
            #print('Lista seleccionada de items inferiores izquierda!!:', self.selected_inf_left)
            # Imprime en un Label el feature seleccionado:
            self.success_inferior_left_list = True
        else:

            self.success_inferior_left_list = False
                    
        
    # LISTA INFERIOR DERECHA
    # Metodo Contador de atributos iguales en una columna del Dataframe, y llenado de lista inferior RIGHT:
    def DSc_load_feat_tocount_subset(self, feature_select_item):
        self.feature_selected2 = feature_select_item
        
        # Se usa el feature seleccionado para crear una Serie Pandas del Dataframe, con el feature:
        self.column_feat_select2 = self.pandas_dataframe[self.feature_selected2]
        
        # Cuenta todos los valores diferentes en la Serie Pandas correspondiente al feature seleccionado:
        self.diff_values_in_columns2 = self.column_feat_select2.value_counts()
        
        #print('Feature seleccionado 2:',self.feature_selected2,'Diferentes valores en el feature 2=',self.diff_values_in_columns2)
        # PENDIENTE: COLOCAR UN IF PARA RESTRINGIR MUCHOS VALORES (MENOS DE 20?):

        # Toma el texto del conteo (index) y lo envia a una lista de Python:
        self.diff_values_name2 = self.diff_values_in_columns2.index.tolist()
        # Toma los numeros del conteo (values) y lo envia a una lista de Python (frecuencia):
        self.diff_values_freq2 = self.diff_values_in_columns2.values.tolist()

        #print('Nombre =',self.diff_values_name2, 'Frecuencia =',self.diff_values_freq2)

        #print('Numero de Sub-Features:', len(self.diff_values_name2))

        # Llena los nombres del conteo en la lista inferior:
        self.ui_DataSc.DSc_Feat_toCount_subset_list.clear()
        for h in self.diff_values_name2:
            self.ui_DataSc.DSc_Feat_toCount_subset_list.addItem(h)
        # Llena las frecuencias de los nombres del conteo en la lista inferior:
        self.str_diff_values_freq2 = map(str, self.diff_values_freq2) # Convertir lista integer to text
        self.ui_DataSc.DSc_Feat_SubFreq_Right_list.clear()
        for j in self.str_diff_values_freq2:
            self.ui_DataSc.DSc_Feat_SubFreq_Right_list.addItem(j)

    # Obtencion de los items seleccionados lista derecha inferior:
    def DSc_get_items_inferior_list_right(self):
        
        # Obtiene los items seleccionados
        items = self.ui_DataSc.DSc_Feat_toCount_subset_list.selectedItems()
        # Crea una lista vacia para llenar
        self.selected_inf_right = []
        # Llenado de la lista de texto usando un Loop
        if (items != []):
            for i in range(len(items)):
                self.selected_inf_right.append(items[i].text())
            
            #print('Lista seleccionada de items inferiores derecha!!:', self.selected_inf_right)
            
            self.success_inferior_right_list = True
        else:
            
            self.success_inferior_right_list = False


    
    # # Method for ploting the Bar Chart
    # def DSc_BarChart_Plotter(self):
    #     Plot2D_DataScienceGraph(window.ui.Tab_DataSc_graphics, self.pandas_dataframe, 'bar')
    # # Method for ploting the Pie Chart
    # def DSc_PieChart_Plotter(self):
    #     Plot2D_DataScienceGraph(window.ui.Tab_DataSc_graphics, self.pandas_dataframe, 'pie')

    #def __init__(self, Ui_QWidget, pandas_dataframe, chart_title, attr_names_x, tocount_title, attr_tocount_y, chart_type):
    
    
    def DSc_HorzBarChart_Plotter(self):
        if (self.selection_status==True):
            # Obtener texto del LineEdit (Name of Rows) para enviarlo al ploteador
            self.name_of_rows = self.ui_DataSc.DSc_NameOfRows_lineEdit.text()
            self.chart_title = self.feature_select_item.text()
            self.tocount_title = self.feat_2count_select_item.text()
            # self.sub_dataframe = self.pandas_dataframe[[self.chart_title, tocount_title]]    
            
            Plot2D_DataScienceGraph(window.ui.Tab_DataSc_graphics, self.df_filt_def_counted, self.chart_title,
                self.selected_inf_left, self.tocount_title, self.selected_inf_right, self.name_of_rows, 'barh', 
                self.boxchecker)

            # Plot2D_DataScienceGraph(window.ui.Tab_DataSc_graphics, self.sub_dataframe, self.chart_title,
            #     self.selected_inf_left, tocount_title, self.selected_inf_right, self.name_of_rows, 'barh', 
            #     self.boxchecker)
        else:
            qtw.QMessageBox.critical(self,'Critical Error!' , 'You have to push the Filter Dataframe Button to load de Dataframe!',
                qtw.QMessageBox.Ok)

    def DSc_VertBarChart_Plotter(self):
        if (self.selection_status==True):
            # Obtener texto del LineEdit (Name of Rows) para enviarlo al ploteador
            self.name_of_rows = self.ui_DataSc.DSc_NameOfRows_lineEdit.text()

            self.chart_title = self.feature_select_item.text()
            self.tocount_title = self.feat_2count_select_item.text()
            # self.sub_dataframe = self.pandas_dataframe[[self.chart_title, self.tocount_title]]

            Plot2D_DataScienceGraph(window.ui.Tab_DataSc_graphics, self.df_filt_def_counted, self.chart_title,
                self.selected_inf_left, self.tocount_title, self.selected_inf_right, self.name_of_rows, 'barv', 
                self.boxchecker)

            # Plot2D_DataScienceGraph(window.ui.Tab_DataSc_graphics, self.sub_dataframe, self.chart_title,
            #     self.selected_inf_left, self.tocount_title, self.selected_inf_right, self.name_of_rows, 'barv', 
            #     self.boxchecker)
        else:
            qtw.QMessageBox.critical(self,'Critical Error!' , 'You have to push the Filter Dataframe Button to load de Dataframe!',
                qtw.QMessageBox.Ok)
    
    # Method for ploting the Pie Chart
    def DSc_PieChart_Plotter(self):
        if (self.selection_status==True):
            # Obtener texto del LineEdit (Name of Rows) para enviarlo al ploteador
            self.name_of_rows = self.ui_DataSc.DSc_NameOfRows_lineEdit.text()

            self.chart_title = self.feature_select_item.text()
            self.tocount_title = self.feat_2count_select_item.text()
            
            # NO TIENE QUE ESTAR AQUI...MEJOR EN UN METODO:
            # self.sub_dataframe = self.pandas_dataframe[[self.chart_title, self.tocount_title]]
                
            Plot2D_DataSciencePies(window.ui.Tab_DataSc_graphics, self.df_filt_def_counted, self.chart_title,
                self.selected_inf_left, self.tocount_title, self.selected_inf_right, self.name_of_rows, self.isexploded, 
                self.selected_slice)

        else:
            qtw.QMessageBox.critical(self,'Critical Error!' , 'You have to push the Filter Dataframe Button to load de Dataframe!',
                qtw.QMessageBox.Ok)

    def DSc_FilterDataframe_all(self):
        
        self.DSc_get_items_inferior_list_left()
        self.DSc_get_items_inferior_list_right()
        

        if (self.success_inferior_left_list and self.success_inferior_right_list):
            self.chart_title = self.feature_select_item.text()
            self.tocount_title = self.feat_2count_select_item.text()    
            self.attr_names_x = self.selected_inf_left
            self.attr_tocount_y = self.selected_inf_right
            
            
            # FILTERING PANDAS DATAFRAME FROM LEFT FEATURE AND RIGHT FEATURE:
            self.sub_dataframe = self.pandas_dataframe[[self.chart_title, self.tocount_title]]
            
            # FILTERING DATAFRAME: GETTING ONLY SELECTED ELEMENTS FROM INFEROR LEFT LIST (Index not touched):
            df_filtered = self.sub_dataframe.loc[self.sub_dataframe[self.chart_title].isin(self.attr_names_x)]
            
            # FILTERING DATAFRAME: GETTING ONLY SELECTED ELEMENTS FROM INFEROR RIGHT LIST (Index not touched):
            df_filtered_definitive = df_filtered.loc[df_filtered[self.tocount_title].isin(self.attr_tocount_y)]
            
            # COUNTING DATAFRAME ELEMENTS IN EACH ROW, AND GETTING A SERIES WITH MULTI-INDEX:
            self.df_filt_def_counted = df_filtered_definitive.value_counts()
            
            # Resetting Multi-Index from the counting:
            self.df_filt_def_counted = self.df_filt_def_counted.reset_index()
            
            # Renaming last column (with the counted values) to 'Values' (I dont know why it turns to 0):
            self.df_filt_def_counted.rename(columns = {0:'Values'}, inplace = True)

            # Selection Status previous to plot:
            self.selection_status = True
            
            # Update label of Filtering Dataframe Ready!:
            self.ui_DataSc.DSc_FilterReady_Label.setText('Ready to plot!')
            
            # Getting columns names for the pandas.pivot() method:
            # df_columns_names = list(df_filt_def_counted.columns)
        elif (self.success_inferior_left_list):
            qtw.QMessageBox.warning(self, 'Warning!',
                'You have to select at least one item from the right attributes list!', qtw.QMessageBox.Ok)
        elif (self.success_inferior_right_list):
            qtw.QMessageBox.warning(self, 'Warning!',
                'You have to select at least one item from the left attributes list!', qtw.QMessageBox.Ok)
        else:
            qtw.QMessageBox.warning(self, 'Warning!',
                'You have to select at least one item in each one of the attribute lists!', qtw.QMessageBox.Ok)

    

   
   
    ########################################################
    # End Methods inside the DataScience Main Window
    ########################################################   

#class Plotting_3D_2D_seismic():





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


################################################################
# END CLASSES OF MAIN FUNTIONALITY (DONT SUPOUSE TO BE HERE)
################################################################


# Execute Window
if  __name__ == "__main__":
    app = qtw.QApplication([])
    window = OilFinderWindow()
    window.show()

    app.exec_()
