import serial
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QPushButton
from PyQt5.QtSerialPort import QSerialPort

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
        self.ser = serial.Serial('/dev/rfcomm0', 115200)

    def initUI(self):
        self.resize(300, 200)

        self.pushbutton_to_hand_fist = QPushButton('Fist')
        self.pushbutton_to_hand_rest = QPushButton('Rest')
        self.pushbutton_to_arm_start = QPushButton('Start')
        self.pushbutton_to_arm_stop = QPushButton('Stop')

        layout_main = QGridLayout(self)

        layout_main.addWidget(self.pushbutton_to_hand_fist, 1, 2, 1, 1)
        layout_main.addWidget(self.pushbutton_to_arm_start, 2, 1, 1, 1)
        layout_main.addWidget(self.pushbutton_to_arm_stop, 2, 3, 1, 1)
        layout_main.addWidget(self.pushbutton_to_hand_rest, 3, 2, 1, 1)

        self.pushbutton_to_hand_fist.clicked.connect(self.action_hand_fist)
        self.pushbutton_to_hand_rest.clicked.connect(self.action_hand_rest)

    def action_hand_fist(self):
        self.ser.write(b'A')

    def action_hand_rest(self):
        self.ser.write(b'B')



if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
