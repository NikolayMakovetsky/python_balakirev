print("------------------NESTED LISTS-------------------")
colorLine = ['R', 'G', 'B']
image = [colorLine[:], colorLine[:], colorLine[:]]
print("colorLine = ['R', 'G', 'B']\nimage = [colorLine[:], colorLine[:], colorLine[:]]\nimage =", image)
print("image[0][1] =", image[0][1], "                                         // we took the item of nested list")
image[1] = [0, 0, 0]
print("image[1] = [0, 0, 0]\nimage =", image, " // we creates new item image[1] and makes link to it, old item deleted")
image[1][:] = [1] * 3
print("image[1][:] = [1] * 3\nimage =", image, " // we changes values in item image[1] using full slice")

print("\n------------------MULTIDIMENSIONAL LISTS-------------------")
print("             // with different nesting levels in example\n")
a = [[[True, False], [[1, 2], [3]]], ['time'], [['R', 'G', 'B'], ['Color']]]
for x in a:
    print(x)
