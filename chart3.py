#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#age = 3;
#if age >= 18:
#	print('Your age is' , age)
#	print('adult')
#else:
#	print('Your age is' , age)
#	print('teenager')

#input返回的是字符串
#born = input("birth:") 
#born = int(born)
#if born < 2000:
#	print("00前")
#else:
#	print("00后")

#体重属性判断“体重/身高的平方””
#如：我身高1.71，体重60kg
# height = 1.71
# weight = 60
# p = weight/(height*height)
# if p <= 18.5:
	# print("过轻")
# elif p <= 25:
	# print("正常")
# elif p <= 28:
	# print("过重")
# elif p <= 32:
	# print("肥胖")
# else:
	# print("严重过胖")

#特殊的循环 
# classmates = ["Prince", "Mic", "Jack"]
# for name in classmates:
	# print(name)

# k = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for x in k :
	# sum = sum + x 
# print('The sum of 1 to 10 is:' , sum)

#range()函数生成整数序列
# sum = 0 
# for x in list(range(101)):
	# sum = sum + x 
# print('The sum of 1 to 100 is:', sum)

#while循环
# n = 99
# sum = 0 
# while n > 0 :
	# sum = sum + n 
	# n = n - 2
# print('The sum of odd number below 99 is ：' , sum)

#循环按格式输出
# L = ['B', 'Pe','Ada']
# for name in L :
	# print('Hello,%s!' % name)

#dict
# d = {'Mic':95,'pet':75,'Jack':85}
# print(d)
# print('Mic\'s score is:',d['Mic'])
# Add elements
# d['Prince'] = 86#默认放在首位
# print(d)
# 'Prince' in d #判断key-'Prince'是否在d中
# Delete key
# d.pop('pet')#删掉'pet'
# print(d)

#set
# s = set([1,2,3])
# print(s )
# s1 = set(['a','b','b'])
# print(s1)
# Add key
# s1.add(1)
# print('s1 添加key 1之后:',s1)
# Delete key
# s1.remove('b')
# print('s1 删除key b之后:',s1)
# s & s1#交集
# print('s and s1的交集是',s & s1)
# s | s1#并集
# print('s and s1的并集是',s | s1)
#试着将list放入set中 会报错
#s = set([1,'a',[1,'abs']])

#关于可变与不可变对象：str不可变；list可变
#str
# s2 = 'abc'#s2指向'abc'
# print('s2 is',s2)
# s2.replace('a','A')
# print('s2 is still',s2)
# s3 = s2.replace('a','A')
# print('s3 is',s3)
# list
# l =['a','c','b']
# print('The original l is',l)
# l.sort()
# print('The new l is',l)