grades = {}


def menuChoice():
   menu = True
   while menu ==True:
    print("Choose Menu option:")
    choice1 = int(input(" 1. Add a module \n 2. View all grades \n 3. View average \n 4. View highest and lowest \n 5. Exit\t"))

    if choice1 == 1:
      moduleAdd()
    elif choice1 == 2:
      viewAllModules()
    elif choice1 == 3:
     viewAverage()
    elif choice1 == 4:
      highestLowest()
    elif choice1 == 5:
       menu = False
   

def moduleAdd():
  moduleName = input("Please enter a module name:\t ")
  moduleGrade = int(input("Please enter grade for this module:\t "))
  grades[moduleName] = moduleGrade

  
  
  
def viewAllModules():
  for ModuleName, ModuleGrade in grades.items():
    print ("\tModule Name:",ModuleName," Module Grade :",ModuleGrade)
  
def viewAverage():
  total = sum(grades.values())
  total1 = total / len(grades.values())
  print("The average for those modules:",total1)
  
  
def highestLowest():
    highest = max(grades.values())
    lowest = min(grades.values())
    print("The highest grade is:",highest)
    print("The lowest grade is:",lowest)

    
menuChoice()