from bitcoin import *
from PySide6.QtWidgets import (QTabWidget, 
                               QApplication, 
                               QWidget, 
                               QLabel, 
                               QPushButton, 
                               QVBoxLayout, 
                               QHBoxLayout, 
                               QGroupBox, 
                               QSpinBox, 
                               QLineEdit, 
                               QRadioButton, 
                               QComboBox)
import sys

def GenerateBitcoinAddress():
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
  pub2 = privtopub(random_key())
  pub3 = privtopub(random_key())
  multi = mk_multisig_script (pub1, pub2, pub3, 2, 3)
  maddr = scriptaddr (multi)
  return maddr

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

# Define class to create a single push button
class DynamicButton(QWidget):

    def __init__(self):
        # Call parent constructor
        super().__init__()

        # Create a button
        self.btn = QPushButton("Generate Bitcoin Address", self)
        # Set tooltip text for the button
        self.btn.setToolTip('This is a simple button')
        # Set the geometry of the button
        self.btn.setGeometry(0, 0, 200, 40)

        # Call function when the button is clicked
        self.btn.clicked.connect(self.onClicked)

        # Display the window
        self.show()

    # Define function to handle the click event of the button
    def onClicked(self):
        # Set text for the label
        GenerateBitcoinAddress()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Creation of GUI widgets, not yet on the screen
    bitcoin_button = DynamicButton()
    
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
    vlayout.addWidget(bitcoin_button)
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

    # Group Boxes
    top_groupbox = QGroupBox('Actions')
    top_groupbox.setLayout(vlayout)
    bottom_groupbox = QGroupBox('Balance')
    bottom_groupbox.setLayout(hlayout)

    button_and_label = ButtonAndLabel()

    main_tab_area = QTabWidget()
    main_tab_area.addTab(top_groupbox, "Actions")
    main_tab_area.addTab(bottom_groupbox, "Balance")

    layout = QVBoxLayout()
    layout.addWidget(main_tab_area)

    window = QWidget()
    window.setLayout(layout)
    window.show()
    window.resize(800, 600)

    sys.exit(app.exec_())
