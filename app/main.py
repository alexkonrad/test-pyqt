import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

class HelloWorldApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window title
        self.setWindowTitle('Hello World App')
        
        # Create a label and set it as the central widget
        label = QLabel('Hello World', self)
        label.setAlignment(Qt.AlignCenter)  # Center the text
        
        self.setCentralWidget(label)
        
        # Set the window size
        self.setGeometry(100, 100, 400, 200)

if __name__ == '__main__':
    # Create the application object
    app = QApplication(sys.argv)
    
    # Create the main window
    window = HelloWorldApp()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec_())
