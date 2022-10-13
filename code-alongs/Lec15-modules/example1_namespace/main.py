import os, sys

x = 5
os.system("cls||clear")

print(f"{'='*30}main.py{'='*30}")

# code imported from another module is executed when imported
import module1

# note __name__ is module1 when ran form outside of module1.py
# when module1.py is run -> __name__= "__main__"

# when importing a module - a reference will be created to sys.modules
print("globals namespace")
print(globals()["module1"])

# when importing a module - it will be stored in sys.modules
print("sys.modules")
print(sys.modules["module1"])   # chooses a key from the dictionary, 'module1'

print(f"\n{'='*30}end main{'='*30}")