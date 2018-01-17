from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from Recipe_Input import Recipe_Input
import pickle
from Recipe_Manage import Recipe_Manage


class UserGUI(QMainWindow):

    # Class Constructor
    def __init__(self):
        super().__init__()
        # poorly placed variable declaration
        self.selectShow = QWidget()
        self.dockWidget = QDockWidget()
        self.selectLabel = QLabel()
        self.addRecipe = QPushButton()

    # Main Window
    def main_ui(self):

        # add new recipe button and create list button
        self.addRecipe = QPushButton("Add Recipe", self)
        self.recipeInput = Recipe_Input()
        self.addRecipe.clicked.connect(self.recipeInput.addRecipeUI)
        createList = QPushButton("Create List")
        createList.clicked.connect(Recipe_Manage.groceryStringGenerator)

        # adding in tool bar
        toolBar = QToolBar()
        toolBar.addWidget(self.addRecipe)
        toolBar.addWidget(createList)

        # adding in dock widget
        selectgrid = QGridLayout()
        self.selectLabel = QLabel("Selected Recipes:")
        self.selectLabel.setAlignment(Qt.AlignTop)
        selectgrid.addWidget(self.selectLabel, 0, 0)
        self.selectShow.setLayout(selectgrid)
        self.dockWidget = QDockWidget()
        self.dockWidget.setWidget(self.selectShow)
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea)

        # calling in list of recipes
        try:
            pickle_in = open("RecipeSaves.pickle", "rb")
            Recipe_List = pickle.load(pickle_in)
            pickle_in.close()
        except:
            Recipe_List = []

        # setting up central widget
        central_widget = QWidget()
        grid = QGridLayout()
        from Recipe_Tab_Template import Recipe_Tab_Template
        for i in range(0, len(Recipe_List), 1):
            grid.addWidget(Recipe_Tab_Template(Recipe_List[i]), i+1, 0 )

        # adding in scrollbar to central widget
        central_widget.setLayout(grid)
        scrollArea = QScrollArea()
        scrollArea.setWidget(central_widget)

        # window settings
        self.addToolBar(toolBar)
        self.setCentralWidget(scrollArea)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)
        self.setWindowTitle("Grocery List Generator")
        self.show()
        self.setUpdatesEnabled(True)

    # refreshing Dock widget to show selected recipes
    def refreshDockWidget(self, selectedRecipe, selectedAmount):
        self.selectLabel.setParent(None)
        self.selectLabel.setText("this has been changed")
        self.selectLabel.update()
        self.selectLabel.repaint()
        self.selectShow.update()
        self.selectShow.repaint()
        self.dockWidget.repaint()
        self.dockWidget.update()
        QApplication.processEvents()


# main execution
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.processEvents()
    ex = UserGUI()
    ex.main_ui()
    app.processEvents()
    sys.exit(app.exec_())