# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas(FigureCanvas):
    def __init__(self):
        width=14
        height=7.3
        dpi=100
        #self.fig = Figure()
        #self.fig = Figure(tight_layout=True)
        self.fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        #self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        #self.fig.set_tight_layout(True)
        

# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas()                  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        #self.vbl.addStretch(1)         
        #self.vbl = QtWidgets.QGridLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
#        self.canvas.set_tight_layout(True)
#        self.canvas.setFocus()
#        self.vbl.setCentralWidget(self.canvas)
        