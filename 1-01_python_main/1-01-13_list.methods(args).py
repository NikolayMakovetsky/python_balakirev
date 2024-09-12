
print("----------------LIST.METHODS(ARGS)----------------")
print("                      COPY                ")
a = [1, 2, 3]
a.append(5)
print("a = [1, 2, 3]; a.append(5); a = ", a, "             // .append adds 1 item to the list")

b = [23, 43, -54]
c = b.copy()
print("b = [23, 43, -54]; c = b.copy(); c = ", c, "      // .copy make diff object with the same data")

c = b[:]
print("b = [23, 43, -54]; c = b[:]; c = ", c, "         // [:] coping list using full slice")

c = list(b)
print("b = [23, 43, -54]; c = list(b); c = ", c, "         // list() coping list using function list()")

print("                      COUNT                ")
d = [1, 1, -5, 0, 1]
i = d.count(1)
print("d = [1, 1, -5, 0, 1]; i = d.count(1); i = ", i, "          // .count(elem) counts elem-s in list")

d.append(True)
i = d.count(True)
print("d = [1, 1, -5, 0, 1, True]; i = d.count(True); i = ", i, "      //   .count(True)")

d[5] = False
i = d.count(False)
print("d = [1, 1, -5, 0, 1, False]; i = d.count(False); i = ", i, "    //   .count(False)")

print("                      REVERSE                ")
a = [3, 8, 0, 1]
a.reverse()
print("a = [3, 8, 0, 1]; a.reverse(); a = ", a, "         //  .reverse() changes current (actual) list")

print("                      SORT                ")
b = [56, 0, 4, -1, 8]
b.sort()
print("b = [56, 0, 4, -1, 8]; b.sort(); b = ", b, "         // .sort() sorts current list in ascending order")
b.sort(reverse=True)
print("b.sort(reverse=True); b = ", b, "              // .sort(reverse=True) sorts current list in descending order")

c = sorted(b)
print("b = [56, 0, 4, -1, 8]; c = sorted(b); c = ", c, "// sorted() func returns new list in contrast of .sort() method")

print("                      INSERT                ")
a = [5, 0, -1]
a.insert(2, -1000)
print("a = [5, 0, -1]; a.insert(2, -1000); a = ", a, " // .insert(itemNum, item)  includes to the current list a new item to a selected place")

print("                      REMOVE                ")
b = [1, 2, 3, True, "Sex"]
b.remove(True)
print("b = [1, 2, 3, True, \"Sex\"]; b.remove(True); b = ", b, "// removes first found item  // 1 == True; 0 == False")
print("b.remove(\"Town\")  ->  ValueError: list.remove(x): x not in list")

print("                      POP                ")
b = [1, 2, 3, True, "Sex"]
c = b.pop(4)
print("b = [1, 2, 3, True, \"Sex\"]; c = b.pop(4); c = ", c, type(c), " //  delete selected item from current list and returns it")
print(b)
c = b.pop()
print("c = b.pop(); b = ", b, "      //  .pop() deletes and returns last item if you don't use args")

print("                      CLEAR                ")
print('b =', b)
b.clear()
print("b.clear(); b =", b, "          //  makes clear current list")

print("                      INDEX                ")
d = [9, -4, 0, 550, 0].index(0)
print("[9, -4, 0, 550, 0].index(0) =", d, "    // returns index of first found item")
e = [9, -4, 0, 550, 0].index(0, 3)
print("[9, -4, 0, 550, 0].index(0, 3) =", e, "       // .index(value, itemStartNum) starts searching value from itemStartNum")
print("[9, -4, 0, 550, 0].index(\"home\")   ->   ValueError: \'home\' is not in list")
