import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from assets import properties
from ui.MainUI import MainUI

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        main = MainUI()
        app.setActiveWindow(main)
        main.setWindowState(Qt.WindowMaximized)
        app_icon = QIcon()
        app_icon.addFile(properties.ICON_PATH, QSize(256, 256))
        main.setWindowIcon(app_icon)
        main.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
