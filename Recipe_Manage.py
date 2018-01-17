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

    def sendToFile(self, Recipe):

        # Import objects from file and creates list
        try:
            pickle_in = open("RecipeSaves.pickle", "rb")
            Recipe_List = pickle.load(pickle_in)
            Recipe_List.insert(0, Recipe)
            pickle_in.close()
            print("went through try")
        except:
            Recipe_List = []
            Recipe_List.insert(0, Recipe)
            print("went through except")

        # rewrites to file
        pickle_out = open("RecipeSaves.pickle", "wb")
        pickle.dump(Recipe_List, pickle_out)
        pickle_out.close()

    def addingSelectedRecipe(recipe):
        try:
            global selectedRecipe
            selectedRecipe.append(recipe)
            print('added to selected recipes')
        except:
            global selectedRecipe
            selectedRecipe = []
            selectedRecipe.append(recipe)
            print('selected recipes created')
        return selectedRecipe

    def addingSelectedAmount(servings):
        try:
            global selectedAmount
            selectedAmount.append(servings)
            print('added to selected amount')
        except:
            global selectedAmount
            selectedAmount = []
            selectedAmount.append(servings)
            print('selected amount created')
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
            # simplifying lists by combining common items
            for l in range(0, len(totalUnits), 1):
                for k in range(l+1, len(totalUnits), 1):
                    if totalTypes[l] == totalTypes[k]:
                        if totalUnits[l] == totalUnits[k]:
                            quantNew = totalQuantity[l] + totalQuantity[k]
                            unitNew = ''.join(totalUnits[l])
                            typeNew = ''.join(totalTypes[l])
                            del totalTypes[l]
                            del totalTypes[k]
                            del totalUnits[l]
                            del totalUnits[k]
                            del totalTypes[l]
                            del totalTypes[k]
                            totalTypes.append(typeNew)
                            totalUnits.append(unitNew)
                            totalQuantity.append(quantNew)
            # combining lists into a string
            for n in range(0, len(totalTypes), 1):
                print(totalTypes[n])
                print(str(totalQuantity[n]) + ' ' + totalUnits[n] + ' of ' + totalTypes[n] + '/n')

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

