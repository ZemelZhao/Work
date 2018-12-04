import pyqtgraph as pg

class PlotWidgetLib(pg.PlotWidget):
    def __init__(self, *arg, **kwarg):
        super(PlotWidgetLib, self).__init__(*arg, **kwarg)

    def mouseMoveEvent(self, e):
        pass

    def mousePressEvent(self, e):
        pass

    def mouseReleaseEvent(self, e):
        pass

    def wheelEvent(self, e):
        pass

