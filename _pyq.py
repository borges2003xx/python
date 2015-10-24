import random, sys
from PyQt4.QtCore import Qt, QVariant
from PyQt4.QtGui import *

class NumberSortModel(QSortFilterProxyModel):

    def lessThan(self, left, right):
    
        lvalue = left.data().toDouble()[0]
        rvalue = right.data().toDouble()[0]
        return lvalue < rvalue


if __name__ == "__main__":

    app = QApplication(sys.argv)
    model = QStandardItemModel(5, 5)
    random.seed()
    for i in range(5):
        for j in range(5):
            item = QStandardItem()
            item.setData(QVariant(str(random.randint(-500, 500)/10.0)), Qt.DisplayRole)
            model.setItem(i, j, item)
    
    proxy = NumberSortModel()
    proxy.setSourceModel(model)
    
    view = QTableView()
    view.setModel(proxy)
    view.setSortingEnabled(True)
    view.show()
    sys.exit(app.exec_())
