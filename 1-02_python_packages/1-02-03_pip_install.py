print("\n--------------ADDITIONAL PACKAGES IN PYTHON   look pypi.org--------------")
print("NumPy - work with multidimentional arrays")
print("Matplotlib - work with graphics")
print("Pygame - 2D graphics")
print("Flask\nDjango...\n")

# list of Python modules installed on my computer
help('modules') # IN TERMINAL: >>> help() >>> modules
                # IN TERMINAL: >>> pip list

print("\n---------------HOW TO INSTALL PACKAGE USING TERMINAL?---------------------")
print("pip install pygame ")
print("pip install flask == 1.1.2")


print("\n---------------HOW TO INSTALL PACKAGE USING PYCHARM?---------------------")
print("NB! ALL MODULES INSTALLED BINDING TO SOME FIX PYTHON VERSION...FOR EXAMPLE 3.8 OR 3.10")
print("File -> Settings -> Python Interpreter -> choose package from list")

print("\n----------HOW TO INSTALL LIST OF PACKAGES USING EXTERNAL TEXT FILE?------------")
print("pip install -r file.txt")  # you can write it by the hands or create it automatically

print("\n----------HOW TO CREATE FILE WITH LIST OF PACKAGES AUTOMATICALLY?------------")
print("pip freeze > requirements.txt")  # in project directory python will create this file
print("pip install -r requirements.txt")