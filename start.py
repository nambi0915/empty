import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMainWindow
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from ui.MainUI import MainUI
from assets import properties

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainUI()
    app.setActiveWindow(main)
    # main.setWindowState(Qt.WindowMaximized)
    app_icon = QIcon()
    app_icon.addFile(properties.ICON_PATH, QSize(256, 256))
    main.setWindowIcon(app_icon)
    main.show()
    sys.exit(app.exec_())
