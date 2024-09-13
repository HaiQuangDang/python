import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my window")
        self.setGeometry(200, 200, 500, 400)
        self.setWindowIcon(QIcon("guts.jpeg"))

        label = QLabel("hello", self)
        label.setFont(QFont("Arial", 16))
        label.setGeometry(0, 10, 500, 50)
        label.setStyleSheet("color: blue;" "background-color: orange;")
        label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        pixmap = QPixmap("starry-night.jpg")
        label_img = QLabel(self)
        label_img.setGeometry(0, 70, 300, 150)
        label_img.setPixmap(pixmap)
        label_img.setScaledContents(True)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()