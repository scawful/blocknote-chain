from PySide6.QtWidgets import QTabWidget, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
import sys
from PySide6.QtWidgets import (QApplication,
                               QWidget,
                               QTabWidget,
                               QVBoxLayout,
                               QHBoxLayout,
                               QGroupBox,
                               QPushButton,
                               QLabel,
                               QSpinBox,
                               QLineEdit,
                               QRadioButton,
                               QComboBox)


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

    # Creation of GUI widgets, not yet on the screen
    button = QPushButton('Submit Order')
    label = QLabel('Currency')
    spinbox = QSpinBox()
    lineedit = QLineEdit()
    radio_button1 = QRadioButton('Generate Address')
    radio_button2 = QRadioButton('Generate Public Key')
    radio_button3 = QRadioButton('Generate Private Key')
    combo_box = QComboBox()
    combo_box.addItems(["Bitcoin", "Ethereum", "Dogecoin", "Blocknote"])

    # VBox is a widget which holds other widgets, and can be assigned to the window to display those widgets
    vlayout = QVBoxLayout()
    vlayout.addWidget(button)
    vlayout.addWidget(radio_button1)
    vlayout.addWidget(radio_button2)
    vlayout.addWidget(radio_button3)
    vlayout.addWidget(spinbox)

    # Horizontal box of widgets 
    hlayout = QHBoxLayout()
    hlayout.addWidget(lineedit)
    hlayout.addWidget(label)
    hlayout.addWidget(combo_box)
    top_groupbox = QGroupBox('Actions')
    top_groupbox.setLayout(vlayout)
    bottom_groupbox = QGroupBox('Balance')
    bottom_groupbox.setLayout(hlayout)

    button_and_label = ButtonAndLabel()

    main_tab_area = QTabWidget()
    main_tab_area.addTab(button_and_label, "Tab 1")
    main_tab_area.addTab(combo_box, "Tab 2")

    layout = QVBoxLayout()
    layout.addWidget(main_tab_area)
    layout.addWidget(top_groupbox)
    layout.addWidget(bottom_groupbox)

    window = QWidget()
    window.setLayout(layout)
    window.show()
    window.resize (1000, 900)

    sys.exit(app.exec_())
