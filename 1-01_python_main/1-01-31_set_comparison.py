print("-----------------------------------SET COMPARISON-----------------------------------------")
print("""
           INTERSECTION                                     SUBTRACTION
        set A       set B                                set A       set B
(         (////////////)        )               (///////////(          )         )
          set A & set B                                    set A - set B
          
           UNIFICATION                                 SYMMETRIC DIFFERENCE
        set A       set B                                set A       set B
(//////////(////////////)////////)              (//////////(           )/////////)
          set A | set B                                    set A ^ set B""")

print("\n--------------------------------------OPERATOR &------------------------------------")
print("return new set, basic sets don't have changes")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(f"setA = {setA}")
print(f"setB = {setB}")
print(f"setA & setB = {setA & setB}")
setC = {9, 10, 11}
print(f"setC = {setC}")
print(f"setA & setC = {setA & setC}            //  there is no intersect elements between setA and setB")
setA &= setB
print(f"setA &= setB; setA = {setA}    //  we saved result to the setA  // setA = setA & set B")

print("\n--------------------------------.INTERSECTION()-----------------------------------")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(f"setA = {setA}")
print(f"setB = {setB}")
setRes = setA.intersection(setB)
print(f"setRes = setA.intersection(setB); setRes = {setRes}")

print("\n----------------------------.INTERSECTION_UPDATE()---------------------------------")
print("result of intersection saved to the first set")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(f"setA = {setA}")
print(f"setB = {setB}")
setA.intersection_update(setB)
print(f"setA.intersection_update(setB); setA = {setA}")

print("\n--------------------------------------OPERATOR |------------------------------------")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(f"setA = {setA}")
print(f"setB = {setB}")
print(f"setA | setB = {setA | setB}              // there is no changes in setA and setB, new set created")
setA |= setB
print(f"setA |= setB; setA = {setA}       // setA = setA | setB")

print("\n--------------------------------------.UNION()-------------------------------------")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(f"setA = {setA}")
print(f"setB = {setB}")
setRes = setA.union(setB)
print(f"setRes = setA.union(setB); setRes = {setRes}    // there is no changes in setA and setB, new set created")

print("\n-------------------------------------- OPERATOR -   ----------------------------------")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(f"setA = {setA}")
print(f"setB = {setB}")
print(f"setA - setB = {setA - setB}           //  new set created")
print(f"setB - setA = {setB - setA}           //  new set created")
setA -= setB
print(f"setA -= setB; setA = {setA}    //  result saved to setA")

print("\n-------------------------------------- OPERATOR ^   ----------------------------------")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(f"setA = {setA}")
print(f"setB = {setB}")
print(f"setA ^ setB = {setA ^ setB}    //  new set created")

print("\n--------------------------------------SET COMPARISON----------------------------------")
print("setA == setB if in both the same amount of elements and the same values of elements")
setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5, 6, 7}
print(f"setA = {setA}")
print(f"setB = {setB}")
print(f"setA == setB -> {setA == setB}")  # True
print(f"setA != setB -> {setA != setB}")  # False
print("---------------------")
setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5}
print(f"setA = {setA}")
print(f"setB = {setB}")
print(f"setB < setA  ->  {setB < setA}")  # True
print(f"setB > setA  ->  {setB > setA}")  # False
print("---------------------")
setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5, 999}
print(f"setA = {setA}")
print(f"setB = {setB}")
print(f"setB < setA  ->  {setB < setA}   // because nighter setA, nor setB included to another one")  # False
print(f"setB > setA  ->  {setB > setA}")  # False
print("---------------------")
setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5, 6, 7}
print(f"setA = {setA}")
print(f"setB = {setB}")
print(f"setA < setB  ->  {setA < setB}  // because nighter setA, nor setB included to another one")   # False
print(f"setA >= setB  ->  {setA >= setB}")    # True
