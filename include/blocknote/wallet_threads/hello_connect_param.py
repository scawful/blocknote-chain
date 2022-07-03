import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
from PySide6 import QtCore

app = QApplication (sys.argv)

hello_line_edit = QLineEdit ()
world_label = QLabel ("")

layout = QVBoxLayout ()
layout.addWidget (hello_line_edit)
layout.addWidget (world_label)

def set_world_label (text):
    world_label.setText (text.upper())
    hello_line_edit.textChanged.connect (set_world_label)

window = QWidget ()
window.setLayout (layout)
window.resize (200, 200)
window.show ()

sys.exit (app.exec_())

