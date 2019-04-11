from PyQt5.QtWidgets import (QWidget, QSizePolicy, QVBoxLayout, QPushButton, QSplitter, QHBoxLayout, QFrame, QLabel,
                             QTableWidget, QAbstractItemView, QAbstractScrollArea, QHeaderView)
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

    def new_qframe(self):
        frame = QFrame()
        frame.setStyleSheet(styles.FRAME_PAGE_STYLE)
        return frame

    def _initialize_left_frame(self):
        frame = self.new_qframe()
        frame.setMaximumWidth(200)
        splitter = QSplitter(Qt.Vertical)
        right_top_frame = self._initialize_right_top_frame()
        right_bottom_frame = self._initialize_right_bottom_frame()
        splitter.addWidget(right_top_frame)
        splitter.addWidget(right_bottom_frame)
        layout = QVBoxLayout()

        layout.addWidget(splitter)
        frame.setLayout(layout)
        return frame

    def _initialize_right_frame(self):
        frame = self.new_qframe()
        layout = QVBoxLayout()
        splitter = QSplitter(Qt.Vertical)
        left_top_frame = self._initialize_left_top_frame()
        left_bottom_frame = self._initialize_left_bottom_frame()
        splitter.addWidget(left_top_frame)
        splitter.addWidget(left_bottom_frame)
        layout.addWidget(splitter)
        frame.setLayout(layout)
        return frame

    def _initialize_right_top_frame(self):
        frame = self.new_qframe()
        frame.setMaximumHeight(50)
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        select_folder_button = QPushButton("Select Folder")
        select_folder_button.setStyleSheet(styles.DIALOG_BUTTON)
        select_folder_button.setMaximumWidth(160)
        select_folder_button.clicked.connect(self.select_button_clicked)

        layout.addWidget(select_folder_button)
        frame.setLayout(layout)
        return frame

    def _initialize_right_bottom_frame(self):
        frame = self.new_qframe()
        layout = QHBoxLayout()
        frame.setLayout(layout)
        return frame

    def _initialize_left_top_frame(self):
        frame = self.new_qframe()
        frame.setMaximumHeight(50)
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        header = QLabel('Empty Directories')
        header.setStyleSheet(styles.LABEL_HEADER)
        layout.addWidget(header)
        frame.setLayout(layout)
        return frame

    def _initialize_left_bottom_frame(self):
        frame = self.new_qframe()
        layout = QHBoxLayout()
        self._initialize_folder_table_view()

        layout.addWidget(self.folder_list_view)
        frame.setLayout(layout)
        return frame

    def select_button_clicked(self):
        print('Folder')

    def _initialize_folder_table_view(self):
        self.folder_list_view = self._get_table_widget()
        self.folder_list_view.setColumnCount(4)
        self.folder_list_view.setHorizontalHeaderLabels(['Folder Name', 'Path', 'Created time', 'Deleted time'])
        self.folder_list_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.folder_list_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def _get_table_widget(self):
        table_widget = QTableWidget()
        table_widget.setStyleSheet(styles.TABLE_WIDGET_STYLE)
        table_widget.verticalHeader().setVisible(False)
        table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        table_widget.verticalScrollBar().setStyleSheet(styles.SCROLL_AREA)
        return table_widget
