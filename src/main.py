from PyQt6.QtWidgets import QApplication
from gui import PlanejadorMochila
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlanejadorMochila()
    window.show()
    sys.exit(app.exec())