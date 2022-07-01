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
app = QApplication(sys.argv)
button = QPushButton('Submit Order')
label = QLabel('Currency')
spinbox = QSpinBox()
lineedit = QLineEdit()
radio_button1 = QRadioButton('Generate Address')
radio_button2 = QRadioButton('Generate Public Key')
radio_button3 = QRadioButton('Generate Private Key')
combo_box = QComboBox()
combo_box.addItems(["Bitcoin", "Ethereum", "Dogecoin", "Blocknote"])
vlayout = QVBoxLayout()
vlayout.addWidget(button)
vlayout.addWidget(radio_button1)
vlayout.addWidget(radio_button2)
vlayout.addWidget(radio_button3)
vlayout.addWidget(spinbox)
hlayout = QHBoxLayout()
hlayout.addWidget(lineedit)
hlayout.addWidget(label)
hlayout.addWidget(combo_box)
top_groupbox = QGroupBox('Actions')
top_groupbox.setLayout(vlayout)
bottom_groupbox = QGroupBox('Balance')
bottom_groupbox.setLayout(hlayout)
layout = QVBoxLayout()
layout.addWidget(top_groupbox)
layout.addWidget(bottom_groupbox)
window = QWidget()
window.setLayout(layout)
window.show()
window.resize (1000, 900)
sys.exit(app.exec_())
