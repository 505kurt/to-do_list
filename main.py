from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import list_management

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-do List")
        self.setGeometry(100, 100, 400, 300)  # (x, y, w, h)

        layout = QVBoxLayout()
        header_layout = QHBoxLayout()

        header = QLabel("To-do list funcionando :D", self)
        header.setFont(QFont('Arial', 12, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(header)
        header_layout.setAlignment(Qt.AlignCenter)

        layout.addLayout(header_layout)

        #sample text; testing alignment
        text = QLabel("Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sit amet accumsan lectus, in aliquet velit. Ut massa ante, consectetur id ullamcorper eu, venenatis eget felis. Nunc tristique nulla mi, tristique porttitor purus auctor non. Curabitur imperdiet ligula eros, a mattis ipsum dictum eu. Quisque lobortis placerat elit ac facilisis. Nulla in felis sed nisi tristique condimentum. Nulla suscipit sem et viverra rhoncus. Donec efficitur arcu nec malesuada fringilla. Etiam gravida vitae mauris eu tincidunt. Nulla quis sodales neque. Curabitur sed porttitor neque. Duis sodales convallis mattis.")
        text.setAlignment(Qt.AlignJustify)
        text.setWordWrap(True)
        layout.addWidget(text)

        self.setLayout(layout)

        self.setFixedSize(400, 300)

        self.show()

app = QApplication([])
main_window = Window()

app.exec()