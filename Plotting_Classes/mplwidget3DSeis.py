# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas3DSeis(FigureCanvas):
    def __init__(self, nrows, ncols, index):
        width=14
        height=7.3
        dpi=100
        #self.fig = Figure()
        #self.fig = Figure(tight_layout=True)
        self.fig3Ds = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        #self.fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes3Ds = self.fig.add_subplot(111)
        self.axes3Ds = self.fig3Ds.add_subplot(nrows, ncols, index)
        print('nrows, ncols, index:', nrows, ncols, index)
        FigureCanvas.__init__(self, self.fig3Ds)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        #FigureCanvas.updateGeometry(self)
        
        #self.fig.set_tight_layout(True)
        

# Matplotlib widget
class MplWidget3DSeismic(QtWidgets.QWidget):
    def __init__(self, parent, nrows, ncols, nindex):
    #def __init__(self, parent=None):
        #super().__init__(self, parent=None, nrows, ncols, nindex)
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas3Ds = MplCanvas3DSeis(nrows, ncols, nindex)                  # Create canvas object
        self.vbl3Ds = QtWidgets.QVBoxLayout()         # Set box for plotting
        #self.vbl.addStretch(1)         
        #self.vbl = QtWidgets.QGridLayout()
        self.vbl3Ds.addWidget(self.canvas3Ds)
        self.setLayout(self.vbl3Ds)
#        self.canvas.set_tight_layout(True)
#        self.canvas.setFocus()
#        self.vbl.setCentralWidget(self.canvas)
        