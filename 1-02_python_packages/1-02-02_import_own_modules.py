mymodule = __import__("3-02-02_mymodule")  # we use this construction becase digits can't be in module name
# import mymodule # if mymodule in project directory
# import folder.mymodule # if mymodule in nested folder of project directory
import pprint
import sys  # after this line python interpreter creates module BYTECODE and runs it for 1 time
import importlib

importlib.reload(sys) # modul rerun for 1 time

pprint.pprint(sys.path) # path collection where python trying to find modules it needs
sys.path.append(r"D:\_2_")  # [...'D:\\_2_'] # we add new path to path collection
pprint.pprint(sys.path)
pprint.pprint(dir(mymodule))    # mymodule attributes, here you can see:
                                # [...
                                # 'get_sum_of_pi',
                                # 'math']

res = mymodule.get_sum_of_pi(3)
print(f"{res = }")
print(f"{mymodule.math.pi = }")     # module math added to mymodule
                                    # so, we can use it through mymodule
                                    # but in this case name conflict can happen
                                    # be careful
