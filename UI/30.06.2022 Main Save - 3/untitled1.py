from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from time import time

class CreateTable(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        fill_button_1 = QtWidgets.QPushButton('fill table - set row count')
        fill_button_1.clicked.connect(self.buildQueueInUI_1)

        fill_button_2 = QtWidgets.QPushButton('fill table - insert rows')
        fill_button_2.clicked.connect(self.buildQueueInUI_2)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(fill_button_1)
        hlayout.addWidget(fill_button_2)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(2)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(hlayout)
        layout.addWidget(self.table)

    def buildQueueInUI_1(self):
        nrows = 500
        self.table.setRowCount(0)
        t0 = time()
        last_row = self.table.rowCount()
        self.table.setRowCount(nrows+self.table.rowCount())
        for i in range(500):
            row = last_row+i
            button = QtWidgets.QPushButton('Click', self)
            button.clicked.connect(lambda _, x=row+1: print('button', x))
            self.table.setCellWidget(row, 0, button)
            self.table.setItem(row, 1, QTableWidgetItem(f'item {row}'))
        print(f'set row count: {time()-t0:.4f} seconds')

    def buildQueueInUI_2(self):
        nrows = 500
        self.table.setRowCount(0)
        t0 = time()
        for i in range(nrows):
            row = self.table.rowCount()
            self.table.insertRow(row)
            button = QtWidgets.QPushButton('Click', self)
            button.clicked.connect(lambda _, x=row+1: print('button', x))
            self.table.setCellWidget(row, 0, button)
            self.table.setItem(row, 1, QTableWidgetItem(f'item {row}'))
        print(f'insert rows: {time() - t0:.4f} seconds')

if __name__ == "__main__":
    app = QApplication([])
    win = CreateTable()
    win.show()
    app.exec_()