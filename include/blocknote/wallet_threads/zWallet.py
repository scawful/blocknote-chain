from bitcoin import *
outfile = open('wallet.txt','w')
private_key =random_key()
print (private_key)
public_key = privtopub (private_key)
print (public_key)
address = pubtoaddr (public_key)
print ('my address is :' +address)
outfile.write ('my bitcoin address :' +address+ '\n')
outfile.write ('my public key :' +privtopub (private_key)+ '\n')
outfile.write ('my hexadecimal private key :' +private_key +'/n')
pub1 = privtopub(random_key())

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
                               QLineEdit,
                               QRadioButton,
                               QComboBox)


class ButtonAndLabel(QWidget):

    def __init__(self):
        super(ButtonAndLabel, self).__init__()

        self.button = QPushButton("Generate Random Public Key")
        self.button.clicked.connect(self.buttonClicked)
        self.label = QLabel("Key Not Generated")
        
        combo_box = QComboBox()
        combo_box.addItem('public key')
        print (public_key)
        print ('my address is :' +address)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def buttonClicked(self):
        self.label.setText("Key Generated")
        combo_box = QComboBox()

class TabbedWindow(QTabWidget):
    def __init__(self, parent=None):
        super(TabbedWindow, self).__init__(parent)
        widget1 = QWidget()
        self.widget2 = ButtonAndLabel()
        widget3 = QWidget()
        self.addTab(widget1, "Transact")
        self.addTab(self.widget2, "Balance")
        self.addTab(widget3, "Tab 3")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Creation of GUI widgets, not yet on the screen
    button = QPushButton('Submit Action')
    label = QLabel('Currency')
    layout = QVBoxLayout ()
    hello_line_edit = QLineEdit ()
    layout.addWidget (hello_line_edit)
    lineedit = QLineEdit()
    radio_button1 = QRadioButton('Send')
    radio_button2 = QRadioButton('Receive')
    radio_button3 = QRadioButton('Swap')
    combo_box = QComboBox()
    combo_box.addItems(["Bitcoin", "Ethereum", "Dogecoin", "Blocknote"])

    # VBox is a widget which holds other widgets, and can be assigned to the window to display those widgets
    vlayout = QVBoxLayout()
    vlayout.addWidget(button)
    vlayout.addWidget(radio_button1)
    vlayout.addWidget(radio_button2)
    vlayout.addWidget(radio_button3)


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
    main_tab_area.addTab(button_and_label, "Transact")
    main_tab_area.addTab(combo_box, "Wallet")

    layout = QVBoxLayout()
    layout.addWidget(main_tab_area)
    layout.addWidget(top_groupbox)
    layout.addWidget(bottom_groupbox)

    

    window = QWidget()
    window.setLayout(layout)
    window.show()
    window.resize (1000, 900)

    sys.exit(app.exec_())

