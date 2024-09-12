import random
import matplotlib.pyplot as plt  

print("-------- работа с псевдослучайными величинами----------")

print("\n--------равномерноый закон распределения---------")
a = random.random() #  [0.0; 1.0)
print(a)

a = random.uniform(3, 5) # [3.0; 5.0)
print(a)

a = random.randint(-3, 7)   # [-3; 7]
print(a)

a = random.randrange(5) # [0, 5, 1) // 0,1,2,3,4
b = random.randrange(-3, 10, 2) # ([start], stop, [step]) // -3,-1,1,3,5,7,9
print(a)
print(b)

print("-------нормальный (гауссовский) закон распределения---------")
a = random.gauss(0, 3.5) # (mean value, standart deviation)
print(a)

	
# # store the random numbers in a list 
# nums = [] 
# mu = 100
# sigma = 50
	
# for i in range(100): 
# 	temp = random.gauss(mu, sigma) 
# 	nums.append(temp) 
		
# # plotting a graph 
# plt.plot(nums) 
# plt.show()

print("-------случайный выбор элемента---------")
lst = [4, 5, 0, -1, 10, 76, 3]
a = random.choice(lst)
print(a)

print("-------перемешивание---------")
lst = [4, 5, 0, -1, 10, 76, 3]
print(lst)
random.shuffle(lst)
print(lst)

print("-------sample---------")
# возвращает новый список с указанным числом неповторяющихся элементов,
# выбранных случайным образом из списка
lst = [4, 5, 0, -1, 10, 76, 3]
a = random.sample(lst, 3)
print(a)

print("------одинаковые случайные последовательности чисел--------")
a = [random.randint(0, 10) for i in range(20)]
print(a)

print("------сидирование--------")
# Для повторяемости результатов экспериментов на разных компьютерах
# нужно зафиксировать, так называемое, зерно генератора случайных чисел
# с помощью функции seed()
random.seed(123)