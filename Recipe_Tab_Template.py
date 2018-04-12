from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Recipe_Manage import Recipe_Manage
from UserGUI import UserGUI
import pickle


class Recipe_Tab_Template(QWidget):


    def __init__(self, recipe):

        super().__init__()
        self.recipe = recipe
        self.Description = recipe.getDescription()
        self.units = recipe.getUnits()
        self.quantity = recipe.getQuantity()
        self.type = recipe.getTypes()
        self.fname = recipe.getFname()
        self.NumPeople = recipe.getNumPeople()
        self.name = recipe.getName()
        self.position = recipe.getPosition()

        # adding components
        self.nameLabel = QLabel(self.name)
        self.nameLabel.setFont(QFont('Sans Serif', 15))
        self.servings = QLabel("Serves " + str(self.NumPeople))
        self.choiceLabel = QLabel("How many people to serve:")
        self.choice = QLineEdit()
        self.choice.setMaximumWidth(40)
        self.choice.setAlignment(Qt.AlignLeft)
        self.delete = QPushButton("Delete")
        self.delete.setStyleSheet("background-color: red")
        self.delete.clicked.connect(self.delRecipe)
        self.addRecipe = QPushButton("Add to List")
        self.addRecipe.clicked.connect(self.addRecipetoList)
        self.picture = QLabel()
        pixmap = QPixmap(self.fname)
        self.picture.setPixmap(pixmap)
        self.picture.setAlignment(Qt.AlignCenter)
        self.descriptionLabel = QLabel("INSTRUCTIONS")
        self.descriptionLabel.setAlignment(Qt.AlignCenter)
        self.description = QTextEdit()
        self.description.setText(self.Description)
        self.description.setReadOnly(True)
        self.description.setFrameStyle(1)
        self.description.setStyleSheet("background-color: rgb(240 , 240, 240);")
        self.ingredientsLabel = QLabel("INGREDIENTS")
        self.ingredientsLabel.setAlignment(Qt.AlignCenter)
        self.ingredients = QTextEdit()
        self.ingredients.setReadOnly(True)
        self.ingredients.setFrameStyle(1)
        self.ingredients.setStyleSheet("background-color: rgb(240 , 240, 240);")
        self.selectBox = QCheckBox()

       # adding ingredients
        ingredientLines = []
        for i in range(0, len(self.units), 1):
            ingredientLines.append(" ")
            ingredientLines[i] = "- " + str(self.quantity[i]) + " " + self.units[i] + " of " + self.type[i]
        for i in range(0, len(ingredientLines), 1):
            self.ingredients.append(ingredientLines[i])

        # set up grid layout
        grid = QGridLayout()
        grid.setColumnStretch(0, 2)
        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(2, 4)
        grid.setColumnStretch(3, 1)

        # adding widgets to layout
        grid.addWidget(self.nameLabel, 0, 0)
        grid.addWidget(self.choiceLabel, 2, 0)
        grid.addWidget(self.choice, 2, 1)
        grid.addWidget(self.servings, 1, 0)
        grid.addWidget(self.selectBox, 1, 3)
        grid.addWidget(self.delete, 2, 3)
        grid.addWidget(self.addRecipe, 3, 3)
        grid.addWidget(self.picture, 0, 2, 4, 1)
        grid.addWidget(self.ingredientsLabel, 4, 0)
        grid.addWidget(self.descriptionLabel, 4, 2)
        grid.addWidget(self.ingredients, 5, 0)
        grid.addWidget(self.description, 5, 1, 1, 3)

        self.setLayout(grid)
        self.show()


    def addRecipetoList(self):
        if not self.choice.text() or not self.choice.text().isdigit():
            choiceNum = self.recipe.getNumPeople()
        else:
            choiceNum = int(self.choice.text())
        global selectedRecipe
        global selectedAmount
        selectedRecipe = Recipe_Manage.addingSelectedRecipe(self.recipe)
        selectedAmount = Recipe_Manage.addingSelectedAmount(choiceNum)
        update = UserGUI()
        self.selectBox.toggle()

    def delRecipe(self):
        # prompts user if they're sure if they want to delete
        reply = QMessageBox.question(self, 'Are You Sure?', 'Are you sure you want to delete this recipe?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print('Recipe was Deleted')
            # Import objects from file and creates list
            pickle_in = open("RecipeSaves.pickle", "rb")
            Recipe_List = pickle.load(pickle_in)
            del Recipe_List[self.position]
            pickle_in.close()
            # rewrites to file
            pickle_out = open("RecipeSaves.pickle", "wb")
            pickle.dump(Recipe_List, pickle_out)
            pickle_out.close()
