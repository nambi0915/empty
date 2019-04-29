from PyQt5.QtWidgets import (QWidget, QSizePolicy, QVBoxLayout, QPushButton, QSplitter, QHBoxLayout, QFrame, QLabel,
                             QTableWidget, QAbstractItemView, QAbstractScrollArea, QHeaderView, QFileDialog, QListView,
                             QTreeView, QTableWidgetItem)
from PyQt5.QtCore import Qt, QDir
from assets import styles
from ui.Widgets import Widgets
from backie.Empty import Empty


class MainUI(QWidget):

    def __init__(self, parent=None):
        try:
            super(MainUI, self).__init__(parent)
            # self.setMinimumSize(800, 600)
            self.selected_folders = []
            self.empty = Empty()
            self.widgets = Widgets()
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
        right_top_frame = self._initialize_left_top_frame()
        right_bottom_frame = self._initialize_left_bottom_frame()
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
        left_top_frame = self._initialize_right_top_frame()
        left_bottom_frame = self._initialize_right_bottom_frame()
        splitter.addWidget(left_top_frame)
        splitter.addWidget(left_bottom_frame)
        layout.addWidget(splitter)
        frame.setLayout(layout)
        return frame

    def _initialize_left_top_frame(self):
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

    def _initialize_left_bottom_frame(self):
        frame = self.new_qframe()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        self.delete_all_button = QPushButton('Delete All')
        self.delete_selected_button = QPushButton('Delete Selected')
        self.delete_selected_button.setEnabled(False)
        self.delete_all_button.setEnabled(False)
        self.delete_all_button.setStyleSheet(styles.DIALOG_BUTTON)
        self.delete_selected_button.setStyleSheet(styles.DIALOG_BUTTON)

        layout.addWidget(self.delete_selected_button)
        layout.addWidget(self.delete_all_button)

        frame.setLayout(layout)
        return frame

    def _initialize_right_top_frame(self):
        frame = self.new_qframe()
        frame.setMaximumHeight(50)
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        header = QLabel('Empty Folders')
        header.setStyleSheet(styles.LABEL_HEADER)
        layout.addWidget(header)
        frame.setLayout(layout)
        return frame

    def _initialize_right_bottom_frame(self):
        frame = self.new_qframe()
        layout = QHBoxLayout()
        self._initialize_folder_table_view()

        layout.addWidget(self.folder_list_view)
        frame.setLayout(layout)
        return frame

    def _initialize_folder_table_view(self):
        self.folder_list_view = self._get_table_widget()
        self.folder_list_view.setColumnCount(4)
        self.folder_list_view.setHorizontalHeaderLabels(['Folder Name', 'Path', 'Created time', 'Deleted time'])
        self.folder_list_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.folder_list_view.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.folder_list_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def _get_table_widget(self):
        table_widget = QTableWidget()
        table_widget.setStyleSheet(styles.TABLE_WIDGET_STYLE)
        table_widget.verticalHeader().setVisible(False)
        table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        table_widget.verticalScrollBar().setStyleSheet(styles.SCROLL_AREA)
        table_widget.horizontalHeader().setHighlightSections(False)
        table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table_widget.horizontalHeader().setStretchLastSection(True)

        return table_widget

    def delete_all_button_clicked(self):
        pass

    def delete_selected_button_clicked(self):
        pass

    def select_button_clicked(self):
        try:
            print('Folder')
            self._get_file_dialog()
            if self.selected_folders:
                print(self.selected_folders)
                self.folder_table_contents = self.empty.get_empty_folders_list(self.selected_folders)
                print(self.folder_table_contents)
            if self.folder_table_contents:
                self.delete_selected_button.setEnabled(True)
                self.delete_all_button.setEnabled(True)
                self.generate_folder_list_view()
            else:
                message_box = self.widgets.get_message_box("No Empty folders")
                message_box.exec()


        except Exception as e:
            print(e)

    def generate_folder_list_view(self):
        self.folder_list_view.setRowCount(len(self.folder_table_contents))
        index = 0
        for folder in self.folder_table_contents:
            self.folder_list_view.setItem(index, 0, QTableWidgetItem(folder[0]))
            self.folder_list_view.setItem(index, 1, QTableWidgetItem(folder[1]))
            self.folder_list_view.setItem(index, 2, QTableWidgetItem(folder[2]))
            self.folder_list_view.setItem(index, 3, QTableWidgetItem(folder[3]))
            index += 1
        self.folder_list_view.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.folder_list_view.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.folder_list_view.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.folder_list_view.horizontalHeader().setSectionResizeMode(3, QHeaderView.Interactive)

    def _get_file_dialog(self):
        self.file_dialog = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        options |= QFileDialog.DontUseNativeDialog
        self.file_dialog.setFileMode(QFileDialog.DirectoryOnly)
        self.file_dialog.setOptions(options)
        self.file_dialog.setWindowTitle("Select Folder")
        self.file_dialog.setDirectory(QDir.home())
        self.file_dialog.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.file_dialog.findChildren(QListView)[0].setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.file_dialog.findChildren(QTreeView)[0].setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.file_dialog.setFixedSize(800, 600)
        if self.file_dialog.exec():
            self.selected_folders = self.file_dialog.selectedFiles()
