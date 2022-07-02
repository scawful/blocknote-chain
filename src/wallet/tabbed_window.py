from PySide6.QtWidgets import QTabWidget, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
import sys

class ButtonAndLabel(QWidget):

    def __init__(self):
        super(ButtonAndLabel, self).__init__()

        self.button = QPushButton("button")
        self.button.clicked.connect(self.buttonClicked)

        self.label = QLabel("label: before clicked")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def buttonClicked(self):
        self.label.setText("label: after clicked")

class TabbedWindow(QTabWidget):
    def __init__(self, parent=None):
        super(TabbedWindow, self).__init__(parent)
        widget1 = QWidget()
        self.widget2 = ButtonAndLabel()
        widget3 = QWidget()
        self.addTab(widget1, "Tab 1")
        self.addTab(self.widget2, "Tab 2")
        self.addTab(widget3, "Tab 3")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabbedWindow = TabbedWindow()
    tabbedWindow.show()
    sys.exit(app.exec_())
