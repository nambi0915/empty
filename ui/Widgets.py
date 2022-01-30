from PyQt5.QtWidgets import QMessageBox


class Widgets:
    def __init__(self):
        pass

    def get_message_box(self, text=""):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setMinimumSize(300, 200)
        msg_box.setText(text)
        msg_box.setWindowTitle("Message")
        msg_box.setStandardButtons(QMessageBox.Ok)

        return msg_box
