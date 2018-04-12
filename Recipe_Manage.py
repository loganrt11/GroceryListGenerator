import pickle
import errno
import os

class Recipe_Manage():

    def __init__(self, Quantity, Units, Types, NumPeople, Description, name, category, fname):
        #super.__init__()

        # setting up object properties
        self.Quantity = Quantity
        self.Units = Units
        self.Types = Types
        self.NumPeople = NumPeople
        self.Description = Description
        self.name = name
        self.category = category
        self.fname = fname
        self.position = 0

    def setPosition(self, position):
        self.position = position

    def sendToFile(self, Recipe):

        # Import objects from file and creates list
        try:
            pickle_in = open("RecipeSaves.pickle", "rb")
            Recipe_List = pickle.load(pickle_in)
            self.position = len(Recipe_List)
            Recipe_List.append(Recipe)
            pickle_in.close()
        except:
            Recipe_List = []
            Recipe_List.insert(0, Recipe)

        # rewrites to file
        pickle_out = open("RecipeSaves.pickle", "wb")
        pickle.dump(Recipe_List, pickle_out)
        pickle_out.close()

    def addingSelectedRecipe(recipe):
        try:
            global selectedRecipe
            selectedRecipe.append(recipe)
        except:
            global selectedRecipe
            selectedRecipe = []
            selectedRecipe.append(recipe)
        return selectedRecipe

    def addingSelectedAmount(servings):
        try:
            global selectedAmount
            selectedAmount.append(servings)
        except:
            global selectedAmount
            selectedAmount = []
            selectedAmount.append(servings)
        return selectedAmount

    def groceryStringGenerator(self):
        global selectedRecipe
        global selectedAmount
        if len(selectedRecipe) > 0:
            totalUnits = []
            totalQuantity = []
            totalTypes = []
            # gathering together all the recipe data into lists
            for i in range(0, len(selectedRecipe), 1):
                totalUnits.append(selectedRecipe[i].getUnits())
                for j in range(0, len(selectedRecipe[i].getQuantity()), 1):
                    tempQuantity = selectedRecipe[i].getQuantity()
                    totalQuantity.append(tempQuantity[j] * (int(selectedAmount[i])/selectedRecipe[i].getNumPeople()))
                totalTypes.append(selectedRecipe[i].getTypes())
            # converting list of lists into list of strings
            for i in range(0, len(totalTypes), 1):
                totalTypes[i] = totalTypes[i][0]
                totalUnits[i] = totalUnits[i][0]
            # simplifying lists by combining common items
            print(totalQuantity)
            print(totalUnits)
            print(totalTypes)
            l = -1
            k = 0
            while True:
                l = l + 1
                k = l + 1
                length = len(totalTypes)
                if l >= length-1:
                    break 
                while k != length:
                    if totalTypes[l] == totalTypes[k]:
                        if totalUnits[l] == totalUnits[k]:
                            quantNew = totalQuantity[l] + totalQuantity[k]
                            unitNew = ''.join(totalUnits[l])
                            typeNew = ''.join(totalTypes[l])
                            del totalQuantity[l]
                            del totalQuantity[k-1]
                            del totalUnits[l]
                            del totalUnits[k-1]
                            del totalTypes[l]
                            del totalTypes[k-1]
                            totalTypes.append(typeNew)
                            totalUnits.append(unitNew)
                            totalQuantity.append(quantNew)
                            l = -1
                            k = 0
                            break
                    k = k + 1

            # combining lists into a string
            for n in range(0, len(totalTypes), 1):
                print(str(totalQuantity[n]) + ' ' + totalUnits[n] + ' of ' + totalTypes[n])

    # Return Functions-----------------------------------------------------------------
    def getDescription(self):
        return self.Description

    def getPicture(self):
        return self.fname

    def getQuantity(self):
        return self.Quantity

    def getUnits(self):
        return self.Units

    def getTypes(self):
        return self.Types

    def getNumPeople(self):
        return self.NumPeople

    def getCategory(self):
        return self.category

    def getName(self):
        return self.name

    def getFname(self):
        return self.fname

    def getPosition(self):
        return self.position

    def getSelectedRecipe():
        global selectedRecipe
        return(selectedRecipe)

    def getSelectedAmount():
        global selectedAmount
        return(selectedAmount)
