from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('joker')
my_win.show()
winner = QLabel('Click to find the winner:')
button = QPushButton('Generate')
a=QLabel('?')
v_line = QVBoxLayout()
v_line.addWidget(winner, alignment = Qt.AlignCenter
)
v_line.addWidget(a, alignment = Qt.AlignCenter
)
v_line.addWidget(button, alignment = Qt.AlignCenter
)
my_win.setLayout(v_line)
def show_winner():
    y = randint(1,100)
    a.setText(str(y) )
    winner.setText('Winner:')





button.clicked.connect(show_winner)






app.exec_()