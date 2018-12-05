import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyqtLib')
        self.setFixedSize(1000, 800)

        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        layout = QHBoxLayout(self)

        self.graph_show = pg.PlotWidget()
        layout.addWidget(self.graph_show)
        self.graph_show.setRange(yRange = (0, 5), xRange = (0, 10), disableAutoRange=True)
        self.graph_show.invertY()
        for i in range(1, 10):
            self.graph_show.addLine(x=i, pen='k')

        ay = self.graph_show.getAxis('left')
        ticks = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
        ay.setTicks([[(v, str(v)) for v in ticks]])

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())




