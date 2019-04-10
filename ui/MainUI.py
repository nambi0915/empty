from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QPushButton, QSplitter, QHBoxLayout, QFrame
from assets import styles
from PyQt5.QtCore import Qt


class MainUI(QWidget):

    def __init__(self, parent=None):
        try:
            super(MainUI, self).__init__(parent)
            self.setMinimumSize(800, 600)
            self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            self._initialize_components()
            self.setWindowTitle('Delete Empty')
        except Exception as e:
            print(e)

    def _initialize_components(self):
        layout = QVBoxLayout()
        splitter = QSplitter(Qt.Horizontal)

        left_frame = self._initialize_left_frame()
        right_frame = self._initialize_right_frame()
        splitter.addWidget(left_frame)
        splitter.addWidget(right_frame)
        layout.addWidget(splitter)
        self.setLayout(layout)

    def _initialize_left_frame(self):
        frame = QFrame()
        frame.setStyleSheet(styles.FRAME_PAGE_STYLE)
        frame.setMaximumWidth(200)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        select_folder_button=QPushButton("Select Folder")
        select_folder_button.setStyleSheet(styles.DIALOG_BUTTON)
        select_folder_button.setMaximumWidth(160)

        layout.addWidget(select_folder_button)
        frame.setLayout(layout)
        return frame

    def _initialize_right_frame(self):
        frame = QFrame()
        frame.setStyleSheet(styles.FRAME_PAGE_STYLE)
        layout = QVBoxLayout()
        frame.setLayout(layout)
        return frame
