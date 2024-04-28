import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import Qt

class GridTableWidget(QWidget):
    def __init__(self, grid):
        super().__init__()
        self.grid = grid
        self.initUI()

    def initUI(self):
        # Set the window properties
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('2D List Grid World')

        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create a QTableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.grid))
        self.tableWidget.setColumnCount(len(self.grid[0]))

        # Set headers (optional)
        #self.tableWidget.setHorizontalHeaderLabels(['Column ' + str(i) for i in range(len(self.grid[0]))])
        #self.tableWidget.setVerticalHeaderLabels(['Row ' + str(i) for i in range(len(self.grid))])

        # Fill the table
        for i, row in enumerate(self.grid):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)

        layout.addWidget(self.tableWidget)

        # Add save button
        btn_save = QPushButton('Save as JPG', self)
        btn_save.clicked.connect(self.saveAsJPG)
        layout.addWidget(btn_save)

    def saveAsJPG(self):
        # Define the size of the table
        size = self.tableWidget.viewport().size()
        # Create a QImage to render the widget
        image = QImage(size, QImage.Format_RGB32)
        image.fill(Qt.white)
        painter = QPainter(image)
        # Render the table to the QPainter
        self.tableWidget.viewport().render(painter)
        painter.end()
        # Save the image
        image.save('table_output.jpg', 'JPG')

def draw_grid(grid):
    app = QApplication(sys.argv)
    ex = GridTableWidget(grid)
    ex.show()
    sys.exit(app.exec_())

'''
import tkinter as tk

# Given 2D list, draw the grid in GUI.
def draw_grid(grid):
    # Calculate size based on the grid dimensions
    cell_size = 50
    width = len(grid[0]) * cell_size
    height = len(grid) * cell_size

    # Create the main window
    root = tk.Tk()
    root.title("2D List Grid World")
    
    # Set the geometry of the tkinter window
    root.geometry(f"{width+10}x{height+10}")
    
    # Create a Canvas widget
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    # Draw the grid
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(val), font=('Helvetica', '10'))

    # Start the GUI
    root.mainloop()
'''