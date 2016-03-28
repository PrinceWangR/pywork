
# def myabs(x):
	# if not isinstance(x, (int, float)):
		# raise TypeError('bad operand type')
	# if x >= 0:
		# return x
	# else:
		# return -x
		
#空函数
# def nop():
	# pass#作为占位符；执行空语句
	
#当函数返回多个值时，返回的是一个tuple
# import math
# def move(x, y, step, angle = 0):
	# nx = x + step * math.cos(angle)　
	# ny = y + step * math.sin(angle)
	# return nx, ny

#返回一元二次方程的两个根
#ax^2 + bx + c = 0
# import math
# def quadratic(a, b, c):
	## if not isinstance(a,(int, float), b, (int, float), c, (int, float)):
	    ## raise TypeError('bad operand type')
	# if a == 0:
		# return -c/b
	# elif b*b - 4*a*c < 0:
		# return None
	# elif b*b - 4*a*c == 0:
		# return -b/(2*a)
	# else:
		# x1 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
		# x2 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
		# return (x1, x2)
# a = float(input('input a'))
# b = float(input('input b'))
# c = float(input('input c'))
# print(quadratic(a,b,c))

#位置参数，计算x^n 
# def power(x,n):
	# s = 1
	# while n > 0:
		# n = n - 1
		# s = s*x
	# return s 
##调用函数时 先more函数文件.py, 然后在解释器中导入函数

#设置默认参数，计算x^n 
# def power(x,n = 2):
	# s = 1
	# while n > 0:
		# n = n - 1
		# s = s*x
	# return s 

##设置多个默认参数，变化大的参数放在前面，变化小的参数放在后面
# def enroll(name, gender, age = 6, city = 'Beijing'):
	# print('name:', name)
	# print('gender:', gender)
	# print('age:', age)
	# print('city:', city)

##默认参数必须指向不便对象，而空的List是可变的
# def add_end(L = None):
	# if L == None:
		# L = []
	# L.append('END')
	# return L 
	
##会报错的类型
# def add_end(L = []):
	# L.append('END')
	# return L 
## >>> add_end()
## ['END']
## >>> add_end()
## ['END', 'END']

##可变参数
# def calc(*numbers):#加*之后，就不用非要传入一个list 或者 tuple；
	# sum = 0
	# for n in numbers:
		# sum = sum + n*n 
	# return sum
# print('calc(*[1,3,5]):',calc(*[1,3,5]))
# print('calc(*(2,4,6)):',calc(*(2,4,6)))

##关键字参数
# def person(name, age, **ot)：
	# print('name:', name, 'age:', age, 'other:', ot)
	
##命名关键字参数
# def person(name, age, **ot):
	# if 'city' in ot:#检查是否有city参数
		# pass
	# if 'job' in ot:
		# pass
	# print('name:', name, 'age:', age, 'other:', ot)

#如果要限制关键字参数的名字，就可以用命名关键字参数，
# def person(name,age,*,city,job):
	# print('name:',name,'age:',age,'city:',city,'job:',job)
#给命名关键字参数city设置默认值
# def person(name,age,*,city = 'Chengdu',job):
	# print('name:',name,'age:',age,'city:',city,'job:',job)
	
##还可以进行参数组合
# def f1(a,b,c = 0,*args,**ot):
	# print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'ot = ', ot)
	
##递归函数
# def fact(n):#factorial -阶乘
	# if n == 1:
		# return 1
	# else:
		# return n*fact(n-1)
#改进 改成尾递归方式
# def fact(n):
	# return fact_iter(n,1)#函数里调用函数
# def fact_iter(num,product):
	# if num == 1:
		# return product
	# else:
		# return fact_iter(num-1, num*product)#直到num-1为1

# 利用递归函数移动汉诺塔:
# def move(n, a, b, c):
    # if n == 1:#当只剩下一个盘子的时候
        # print('move', a, '-->', c)
        # return
    # move(n-1, a, c, b)
    # print('move', a, '-->', c)
    # move(n-1, b, a, c)

# move(4, 'A', 'B', 'C')

# def hanoi(n,x,y,z):
    # if n==1:
        # print(x,'-->',z)
    # else:
        # hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        # hanoi(1,x,y,z)#将最底下的最后一个盘子从x移动到z上
        # hanoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上
# n=int(input('请输入汉诺塔的层数：'))
# hanoi(n ,'x','y','z')