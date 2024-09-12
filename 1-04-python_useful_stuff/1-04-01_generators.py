print("-----------classic generators-------------")

a = [x for x in range(1, 5)] # list
print(a, type(a))

d = [1, 2, '1', '2', -4, 3, 4]
a = {int(x) for x in d} # set
print(a, type(a))

m = {"неудовл.": 2, "удовл.": 3, "хорошо": '4', "отлично": '5'}
a = {key.upper(): int(value) for key, value in m.items()} # dict
print(a, type(a))

print("-----------'clear' generator-------------")
gen = (x ** 2 for x in range(4))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # StopIteration

print("-----------ex with functions--------")
# Некоторые функции, такие как: list, set, sum, max, min и др
# позволяют работать непосредственно с итераторами.
# То есть, в качестве аргумента им можно передавать генератор, например:

print(list(x ** 2 for x in range(6)))
print(set(x ** 2 for x in range(6)))
print(sum((x ** 2 for x in range(6))))
print(max((x ** 2 for x in range(6))))


print("----you can use generator only one time!!")
# еще раз обратите внимание,
# использовать эти и другие подобные им функции для одного и того же генератора
# можно только один раз

a = (x ** 2 for x in range(6))
print(sum(a))
print(sum(a)) # Видим 0, т.к. использовать генератор можно только единожды

print("---------работа с большими числами----------")
# зачем вообще нужны эти выражения-генераторы?
# Дело в том, что эти объекты по сравнению, например,
# с обычными списками не хранят в памяти все значения сразу,
# а генерируют их по мере необходимости

lst = (x for x in range(1000000000))
 
for i in lst:
    print(i, end=" ")
    if i > 15:
        break