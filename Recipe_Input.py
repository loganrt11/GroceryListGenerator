from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Recipe_Manage import Recipe_Manage
import sys
import os


class Recipe_Input(QWidget):

    def __init__(self):
        super().__init__()

        # adding components
        self.nameLabel = QLabel("Name of Recipe:")
        self.name = QLineEdit()
        self.categoryLabel = QLabel("Category:")
        self.category = QComboBox()
        self.category.addItems(["Dinner", "Breakfast", "Dessert", "Appetizers"] )
        self.quantityLabel = QLabel("Quantity")
        self.unitsLabel = QLabel("Units")
        self.typeLabel = QLabel("Type")
        self.DescriptionLabel = QLabel("Enter the recipe Instructions:")
        self.DescriptionEdit = QTextEdit()
        self.example = QLabel("example:")
        self.quantityEx = QLabel("12")
        self.unitsEx = QLabel("Cups")
        self.typeEx = QLabel("Milk")
        self.picChecker = QLineEdit()
        self.picChecker.setReadOnly(True)
        self.amountInd = QLabel("How many people does this feed?")
        self.pictureChooser = QPushButton("Choose a Picture")
        self.pictureChooser.clicked.connect(self.selectFile)
        self.amountSel = QLineEdit()
        self.amountSel.setFixedWidth(40)
        self.amountSel.setAlignment(Qt.AlignCenter)
        self.submit = QPushButton("Submit")
        self.submit.clicked.connect(self.RecipeSubmit)
        self.error = QTextEdit()
        self.error.setReadOnly(True)
        self.error.setUpdatesEnabled(True)
        self.error.setTextColor(QColor(255, 0, 0))
        self.error.setFrameStyle(0)
        self.error.setStyleSheet("background-color: rgb(240 , 240, 240);")
        self.quantity1 = QLineEdit()
        self.units1 = QLineEdit()
        self.type1 = QLineEdit()
        self.quantity2 = QLineEdit()
        self.units2 = QLineEdit()
        self.type2 = QLineEdit()
        self.quantity3 = QLineEdit()
        self.units3 = QLineEdit()
        self.type3 = QLineEdit()
        self.quantity4 = QLineEdit()
        self.units4 = QLineEdit()
        self.type4 = QLineEdit()
        self.quantity5 = QLineEdit()
        self.units5 = QLineEdit()
        self.type5 = QLineEdit()
        self.quantity6 = QLineEdit()
        self.units6 = QLineEdit()
        self.type6 = QLineEdit()
        self.quantity7 = QLineEdit()
        self.units7 = QLineEdit()
        self.type7 = QLineEdit()
        self.quantity8 = QLineEdit()
        self.units8 = QLineEdit()
        self.type8 = QLineEdit()
        self.quantity9 = QLineEdit()
        self.units9 = QLineEdit()
        self.type9 = QLineEdit()
        self.quantity10 = QLineEdit()
        self.units10 = QLineEdit()
        self.type10 = QLineEdit()

    # user interface for adding new recipe
    def addRecipeUI(self):

        # Setting up GridLayout
        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 2)
        grid.setColumnStretch(2, 2)
        grid.setColumnStretch(3, 2)
        grid.setColumnStretch(4, 1)
        grid.setColumnStretch(5, 4)
        grid.setColumnStretch(6, 4)

        # adding widgets to grid
        grid.addWidget(self.nameLabel, 0, 1)
        grid.addWidget(self.name, 0, 2, 1, 2)
        grid.addWidget(self.quantityLabel, 1, 1)
        grid.addWidget(self.unitsLabel, 1, 2)
        grid.addWidget(self.typeLabel, 1, 3)
        grid.addWidget(self.categoryLabel, 0, 5)
        grid.addWidget(self.category, 1, 5)
        grid.addWidget(self.DescriptionLabel, 2, 5, 1, 2)
        grid.addWidget(self.example, 2, 0)
        grid.addWidget(self.quantityEx, 2, 1)
        grid.addWidget(self.unitsEx, 2, 2)
        grid.addWidget(self.typeEx, 2, 3)
        grid.addWidget(self.DescriptionEdit, 3, 5, 6, 2)
        grid.addWidget(self.quantity1, 3, 1)
        grid.addWidget(self.units1, 3, 2)
        grid.addWidget(self.type1, 3, 3)
        grid.addWidget(self.quantity2, 4, 1)
        grid.addWidget(self.units2, 4, 2)
        grid.addWidget(self.type2, 4, 3)
        grid.addWidget(self.quantity3, 5, 1)
        grid.addWidget(self.units3, 5, 2)
        grid.addWidget(self.type3, 5, 3)
        grid.addWidget(self.quantity4, 6, 1)
        grid.addWidget(self.units4, 6, 2)
        grid.addWidget(self.type4, 6, 3)
        grid.addWidget(self.quantity5, 7, 1)
        grid.addWidget(self.units5, 7, 2)
        grid.addWidget(self.type5, 7, 3)
        grid.addWidget(self.quantity6, 8, 1)
        grid.addWidget(self.units6, 8, 2)
        grid.addWidget(self.type6, 8, 3)
        grid.addWidget(self.quantity7, 9, 1)
        grid.addWidget(self.units7, 9, 2)
        grid.addWidget(self.type7, 9, 3)
        grid.addWidget(self.quantity8, 10, 1)
        grid.addWidget(self.units8, 10, 2)
        grid.addWidget(self.type8, 10, 3)
        grid.addWidget(self.quantity9, 11, 1)
        grid.addWidget(self.units9, 11, 2)
        grid.addWidget(self.type9, 11, 3)
        grid.addWidget(self.quantity10, 12, 1)
        grid.addWidget(self.units10, 12, 2)
        grid.addWidget(self.type10, 12, 3)
        grid.addWidget(self.pictureChooser, 9, 5)
        grid.addWidget(self.picChecker, 9, 6)
        grid.addWidget(self.amountInd, 10, 5)
        grid.addWidget(self.amountSel, 10, 6)
        grid.addWidget(self.submit, 14, 6)
        grid.addWidget(self.error, 11, 5, 3, 2)

        self.setLayout(grid)
        self.setWindowTitle("Add a Recipe")
        self.show()


    def RecipeSubmit(self):

        self.error.clear()

        # error testing
        if not self.DescriptionEdit.toPlainText():
            self.error.setText("The recipe instructions are blank")

        if not self.amountSel.text():
            self.error.append("The amount of people this recipe supports is blank")

        if not self.name.text():
            self.error.append("The name of the recipe has been left blank")

        if not self.picChecker.text():
            self.fname = '/home/loganrt11/PycharmProjects/Grocery/noImage.jpg'

        # combining input into lists and variables
        Quantities = [self.quantity1.text(), self.quantity2.text(), self.quantity3.text(), self.quantity4.text(), self.quantity5.text(), self.quantity6.text(), self.quantity7.text(), self.quantity8.text(), self.quantity9.text(), self.quantity10.text()]
        Units = [self.units1.text(), self.units2.text(), self.units3.text(), self.units4.text(), self.units5.text(), self.units6.text(), self.units7.text(), self.units8.text(), self.units9.text(), self.units10.text()]
        Types = [self.type1.text(), self.type2.text(), self.type3.text(), self.type4.text(), self.type5.text(), self.type6.text(), self.type7.text(), self.type8.text(), self.type9.text(), self.type10.text()]
        NumPeople = self.amountSel.text()
        Description = self.DescriptionEdit.toPlainText()
        name = self.name.text()
        category = str(self.category.currentText())

        # error testing for ingredients input
        for i in range(0, 10, 1):
            if Quantities[i] or Units[i] or Types[i]:
                if not Quantities[i] or not Units[i] or not Types[i]:
                    self.error.append("Ingredients input line " + str(i+1) + " is not acceptable")
            if not Quantities[i].isdigit() and Quantities[i]:
                self.error.append("Quantity input " + str(i+1) + " is not a whole number")
        if not NumPeople.isdigit():
            self.error.append("The number of people is not a whole number")

        # Trimming lists of empty spots
        Quantities = list(filter(None, Quantities))
        Units = list(filter(None, Units))
        Types = list(filter(None, Types))

        # converting needed variables to integer
        if not self.error.toPlainText():
            NumPeople = int(NumPeople)
            Quantities = [int(i) for i in Quantities]

        # creating objects
            Recipe = Recipe_Manage(Quantities, Units, Types, NumPeople, Description, name, category, self.fname)
            Recipe.sendToFile(Recipe)


    def selectFile(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', '/pycharmprojects/Grocery', '*.jpg')[0]
        self.picChecker.setText(self.fname)