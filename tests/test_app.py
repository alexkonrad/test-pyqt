import pytest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
import app.main as am

@pytest.fixture
def hello_world_app(qtbot):
    """Fixture to create the application window."""
    window = am.HelloWorldApp()
    qtbot.addWidget(window)
    window.show()
    return window

def test_hello_world_label(hello_world_app, qtbot):
    """Test to verify the window displays 'Hello World'."""
    
    # Check if the central widget is a QLabel
    label = hello_world_app.centralWidget()
    assert isinstance(label, QLabel)
    
    # Check if the text is 'Hello World'
    assert label.text() == "Hello World"
    
    # Optional: Check if the text is centered
    assert label.alignment() == Qt.AlignCenter
