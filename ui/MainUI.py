from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class MainUI(QWidget):

    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setMinimumSize(800, 600)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle('Welcome')
