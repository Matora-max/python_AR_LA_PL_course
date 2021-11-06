
"""
Spyder Editor

This is a temporary script file.
"""
print('hello world')
print("_"*50)
print("让编程变得更加有趣吧")
print("Everyone should learn how to code a computer")
print("3+3")

print("加:",3+3)
print("减:",3-1)
print("幂:",3**3)
print("乘：",3*3)
print("除：",3/3)
print("整除：",3//2)
print("整除：",7//4)
print("余数：",3%2)
print("余数：",5%3)

x=5
func=2*x+1
print(func)

x=5.0
monadic_equation=2*x+1
print("monadic_equation=",monadic_equation)
print("monadic_equation=%2f"%monadic_equation)
print("monadic_equation={:2f}".format(monadic_equation))

if 20==20:
    print("heiheihei")
else:
    print("no no no")
if 30==40:
    print("刘丽华是帅哥")
else:
    print("刘丽华是傻逼")
    
city_name="Xi'an"
coordinate_longitude=108.942292
coordinate_latitude=34.261013
print("The longitude of Xi'an coordinate is{lon:.2f},and the latitude os{lat}.".format(lon=coordinate_longitude,lat=coordinate_latitude))

x,y,b=2,5,7
func_2=2*x+3*y+b
print("x={}，y={},b={},func_2={}".format(x,y,b,func_2))

x,y,*z=0,1,2,3,4,5,6
func_2=2*x+3*y+b
print("func_2={}".format(x,y,*z,func_2))

lst_s=list(map(chr,range(100,100)))
print(lst_s)
print("_"*50)
print("[3:6]->{}".format(lst_s[3:6]))
print("[-3:-1]->{}".format(lst_s[-3:-1]))
print("[-3:]->{}".format(lst_s[-3:]))
print("[:3]->{}".format(lst_s[:3]))

help(map)

print("5//4")
print("取整:",4//2)
print("取整：",5//2)

if 3!=4:
    print("God save the queen")
else:
    print("London bridge is falling down")
if 3<=4:
    print("yes yes yes")
else:
    print("no no no")
if 5==5:
    print("happy")
else:
    print("sad")
    
lst_n=list(range(5,20,3))
print(lst_n)
print("The list length={}".format(len(lst_n)))
print("Maximum value={}".format(max(lst_n)))
print("Minimum value={}".format(min(lst_n)))

lst_s=list(map(chr,range(100,110)))
print(lst_s)
print("_"*50)
print("[3:6]->{}".format(lst_s[3:6]))
print("[-3:-1]->{}".format(lst_s[-3:-1]))
print("[-3:]->{}".format(lst_s[-3:]))
print("[:3]->{}".format(lst_s[:3]))
print(lst_s)
print("_"*50)
print("[0:10:2]->{}".format(lst_s[0:10:2]))
print("[::3]->{}".format(lst_s[::3]))
print("[9:3:-2]->{}".format(lst_s[9:3:-2]))
print("[20:3:-1]->{}".format(lst_s[20:3:-1]))
print("[7::-3]->{}".format(lst_s[7::-3]))
print("[:3:-2]->{}".format(lst_s[:3:-2]))
print(lst_s)
print("_"*50)
lst_s[5]=99
print("lst_s[5]=99->{}".format(lst_s))

lst_none=lst_s+[None]*6
print("lst_s+[None]*6->{}".format(lst_none))
lst_none[13]=2015
print("lst_none[13]=2015->{}".format(lst_none))
lst_none[1:1]=[0,0,0,12]
print("lst_none[1:1]=[0,0,0,12]->{}".format(lst_none))
del lst_none[-2:]
print("del lst_none[-2:]->{}".format(lst_none))
lst_none[-6:-3]=list(range(100,104,2))
print("lst_none[-6:-3]=list(rang(100:104:2))->{}".format(lst_none[-6:-3]))

lst_s_2=list(map(chr,range(100,105)))
print(lst_s_2)
print("_"*50)
lst_s_2.append(99)
print("lst_s_2.append(99)->{}".format(lst_s_2))
lst_s_2.append(list(range(50,80,5)))
print("lst_s_2.append(list(range(50,80,5)))->{}".format(lst_s_2))

lst_spechars=['*',')','*']
lst_s_2.extend(lst_spechars)
print("lst_s_2.extend(lst_spechars)->{}".format(lst_s_2))
print("lst_s_2.count('*')={}".format(lst_s_2.count('*')))
print("lst_s_2.index('e')={}".format(lst_s_2.index('e')))

lst_s_2.remove('*')
print("lst_s_2.remove('*')_retention->{}".format(lst_s_2))

lst_s_2.insert(2,[1000,1200,1500])
print("lst_s_2.insert(2,[1000,1200,1500])->{}".format(lst_s_2))
print("lst_s_2.pop(7)_popup->{}".format(lst_s_2.pop(7)))
print("lst_s_2.pop(7)_retention->{}".format(lst_s_2))

lst_n_2=[2,42,6,95,4,3]
lst_n_2.sort()
print("list_n_2.sort()->{}".format(lst_n_2))

tuple_1=2,3,5
print("tuple_1=2,3,5,->{}".format(tuple_1))
print("3*(20*3,)->{}".format(3*(20*3)))
print("tuple((5,8,9))->{}".format(tuple((5,8,9))))
print("tuple([5,8,9])->{}".format(tuple([5,8,9])))

import random
items=[(0,[i for i in range(5)]),(1,[random.sample(list(range(100,200,1)),3)]),(2,'python')]
print("items->{}".format(items))

dic=dict(items)
print("dic[1]->{}".format(dic[1]))
print("len(dic)->{}".format(len(dic)))

dic[3]=(random.random(),random.uniform(200,300))
print("dic[3]=(random.random(,random.uniform(200,300))->{}".format(dic))
del dic[1]
print("del dic[1]->{}".format(dic))
print("3 in dic->{}".format(3 in dic))
print("5 in dic->{}".format(5 in dic))
print("dic.keys()->{}".format(dic.keys()))
print("dic.items()->{}".format(dic.items()))
print("_"*50)
print("list(dic.keys()->{}".format(list(dic.keys())))

lst_A=list(range(6,20,3))
lst_B=list(range(100,150,15))
print("lst_A={},lst_B={}".format(lst_A,lst_B))
dic_2={0:lst_A,1:lst_B}
print("dic_2={}".format(dic_2))
print("_"*50)
dic_assignment=dic_2
print("dic_assignment={}".format(dic_assignment))
dic_2.clear()
print("dic_2.clear()->{}".format(dic_2))
print("dic_assignment={}".format(dic_assignment))
dic_2[5]=list(range(1,9,2))
print("dic_2[5]=list(range(1,9,2))->{}".format(dic_2))
dic_copy=dic_2.copy()
print("dic_copy=dic_2.copy()->{}".format(dic_copy))
dic_2[8]=[5,7]
print("dic_2[8]=[5,7]->{}".format(dic_2))
print("dic_copy={}".format(dic_copy))
dic_copy[5].remove(5)
print("dic_copy[5].remove(5)->{}".format(dic_copy))
dic_copy.setdefault(6,[77,99]) 
print("dic_copy.setdefault(6,[77,99])->{}".format(dic_copy))
dic_2.pop(5) 
print("dic_2.pop(5)->{}".format(dic_2))
dic_update={8:[5,7,6,3,2],9:[3,2,33,55,66]}
print("dic_update={}".format(dic_update))
dic_2.update(dic_update) 
print("dic_2.update(dic_update->{}".format(dic_2))
print("dic_2.get(9)->{}".format(dic_2.get(9)))
dic_2.popitem() 
print("dic_2.popitem()->{}".format(dic_2))

dic_3={}.fromkeys([0,1,2,3,4,'A']) 
print("dic_3={}"+".fromkeys([0,1,2,3,4,'A'])->{}".format(dic_3)) 

from string import Template
s_template_1=Template("$x,glorious,$x!")
s_1=s_template_1.substitute(x="Python")
print("s_1=s_template_1.substitute(x=\"Python\")->{}".format(s_1))
s_template_2=Template("${x}thon is amazing!")
s_2=s_template_2.substitute(x="py")
print("s_2=s_template_2.substitute(x=\"py\")->{}".format(s_2))
s_template_3=Template("$x and $y are both amazing!")
substitute_dict=dict([('x','Python'),('y','Grasshopper')])
print("substitute_dict={}".format(substitute_dict))
s_3=s_template_3.substitute(substitute_dict)
print("s_3=s_template_3.substitute(substitute_dict)->{}".format(s_3))


lst_A=list(range(6,20,3))
lst_B=list(range(100,150,15))
print("lst_A={},lst_B={}".format(lst_A,lst_B))
dic_2={0:lst_A,1:lst_B}
print("_"*50)
dic_assignment=dic_2
print("dic_assignment={}".format(dic_assignment))
dic_2.clear()
print("dic_2.clear()->{}".format(dic_2))
dic_copy=dic_2.copy()
print("dic_copy=dic_2.copy()->{}".format(dic_2.copy))
dic_2[8]=[5,7]
print("dic_2[8]=[5,7]->{}".format(dic_2))
print("dic_copy=dic{}".format(dic_copy))
dic_2[5]=list(range(1,9,2))
print("dic_2[5]=list(range(1,9,2))->{}".format(dic_2))
dic_copy.setdefault(6,[77,99])
print("dic_copy.setdefault(6,[77,99])->{}".format(dic_copy))
dic_3={}.fromkeys([0,1,2,3,4,'A'])
print("dic_3={}"+".fromkeys([0,1,2,3,4,'A'])->{}".format(dic_3))

lst_s_3=list("Hello Python!")
print("lst_s_3=list(\"Hello Python!\")->{}".format(lst_s_3))
print("\"Hello\"+\"Python!\"->{}".format("Hello"+"Python!"))
print("\"+\".join(str(123456))->{}".format("+".join(str(123456))))
print("\"Hello Python!\")->{}".format(len("Hello Python!")))

coordinates="120,132007,30,300500,9,7"
print("coordinates.split(\",\")->{}".format(coordinates.split(",")))
print("eval(coordinates)->{}".format(eval(coordinates)))
print("\"Hello Python!\".lower()->{}".format("Hello Python!".lower()))
print("\"Hello Python!\".upper()->{}".format("Hello Python!".upper()))

hello_lst=list("Hello Python!")
hello_lst.sort()
print("hello.lst.sort()->{}".format(hello_lst))
print("\"Hello Python!\".find(\"Py\"->{}".format("Hello Python!".find("Py")))

lst_s_3=list("Hello Python!")
print("lst_s_3=list(\"Hello Python!\"->{}".format("Hello"+"Python"))
print("\"+\".join(str(123456))->{}".format("+".join(str(123456))))
format_str="Hello,%s and %s!"
values=("Python","Grasshopper")
new_str=format_str % values
print("new_str=format_str % values->{}".format(new_str))
format_str_2="Pi with three decimals:%.3f,and enter a value with percent sign:%2f %%"
from math import pi
new_str_2=format_str_2 % (pi,3.1415926)
print("new_str_2=format_str_2 % (pi,3.1415926)->{}".format(new_str_2))
format_str_3="%10f,%10.2f,%.2f,%.5s,%.*s,%d,%x,%f"
new_str_3=format_str_3%(pi,pi,pi,"Hello Python!",5,"Hello Python!",52,52,pi)
print("{}".format(new_str_3))
from string import Template
s_template_1=Template("Sx.glorious,Sx!")
s_1=s_template_1.substitute(x="Python")
print("s_1=s_template_1.substitute(x=\"Python\"->{}".format(s_1))
s_template_2=Template("S(x)thon is nice!")
s_2=s_template_2.substitute(x="py")
print("s_2=s_template_2.substitute(x=\"py\")->{}".format(s_2))
s_template_3=Template("Sx and Sy are both good.")
substitute_dict=dict([('x','Python'),('y','Grasshopper')])
print("substitute_dict={}".format(substitute_dict))
s_3=s_template_3.substitute(substitute_dict)
print("s_3=s_template_3.substitute(substitute_dict)->{}".format(s_3))

import re
pattern_1='Python'
text="Hello Python!"
print("re.findall(pattern_1,text)->{}".format(re.findall(pattern_1,text)))

pattern_2='python'
print("re.findall(pattern_2,text)->{}".format(re.findall(pattern_2,text)))
print("re.findall('.ython','Hello Python!')->{}".format(re.findall('.ython','Hello Python!')))
print("re.findall('.ython','Hello gython!')->{}".format(re.findall('.ython','Hello gython!')))
print("re.findall('.ython','Hello gPython！')->{}".format(re.findall('.ython','Hello gPython!')))
print("re.findall('.ython','Hello ython!')->{}".format(re.findall('.ython','Hello ython!')))
print("re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')->{}".format(re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn')))
print("re.findall(r'w{2}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{2}\.cadesign\.cn','www.cadesign.cn')))
print("re.findall(r'w{1,3}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{1,3}\.cadesign\.cn','www.cadesign.cn')))
print("re.findall('[Py]*thon!','Hello Python!')->{}".format(re.findall('[Py]*thon!','Hello Python!')))
print("re.findall('[Py]*thon!','Hello Python!')->{}".format(re.findall('[Py]*thon!','Hello Python!')))
print("re.findall('[Py]*thon!','Hello ython!')->{}".format(re.findall('[Py]*thon!','Hello ython!')))
print("re.findall('[Py]*thon!','Hello ython！')->{}".format(re.findall('[Py]*thon!','Hello thon!')))
print("re.findall(('\d','number=9')->{}".format(re.findall('\d','number=9')))
print("re.findall('\D',number=9')->{}".format(re.findall('\D','number=9')))
print("re.findall('[^0-9]','number=11')->{}".format(re.findall('[^0-9]','number=11')))
print("re.findall('[a-z]','python')->{}".format(re.findall('[a-z]','python-3.0')))
print("re.search('[a-z]+','python')->{}".format(re.search('[a-z]+','python')))

if re.search('[a-z]+','python'):
    print("re.search('[a-z]+','python')->found it!")
if re.match('p','python'):
    print("re.match('p','python')->found it!")

x=10
if x==0:
    print('What a coinsidence!')
elif x<0:
    print('It is no friendly to Matoramax.')
elif 0<x<10:
    print('Victory!')
else:
    print('My gift is not that easy to find')

x=y=[3,6,9]
z=[3,6,9]
print("x==y->{}".format(x==y))
print("x is y->{}".format(x is y))
print("x==z->{}".format(x==z))
print("x is z->{}".format(x is z))
print("x is not z->{}".format(x is not z))
print("id_x:{}；id_y:{}；id_z:{}".format(id(x),id(y),id(z)))
del x[2]
print("x={},y={}，z={} after del x[2]".format(x,y,z))

x=[3,6,9]
print("3 in x->{}".format(3 in x))
print("0 in x->{}".format(0 in x))
print("3 not in x->{}".format(3 not in x))
print("0 not in x->{}".format(0 not in x))

y=[1,4,7,9]
print("1 in y->{}".format(1 in y))
print("5 in y->{}".format(5 in y))
print("5 not in y->{}".format(5 not in y))

a,b,c=0,10,15
if c>a and c<b:
    print('a<c<b')
else: print('a<c<b kidding!')

e,f,g=4,9,7
if e<f and e<g:
    print("I'm the winner.")
else:print("loser--")

def simple_func(x,y):
    z=pow(x,2)+y
    return z
print("simple_func(3,7)->{}".format(simple_func(3,7)))
print("simple_func(7,3)->{}".format(simple_func(7,3)))
print("simple_func(y=7,x=3)->{}".format(simple_func(y=7,x=3)))

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))

lst_1=list(range(29,37,2))
print("lst_1={}".format(lst_1))
print("_"*50)
print("for i in lst_1:")
for i in lst_1:
    print(i)
print("for i in range(len(lst_1)):")
for i in range(len(lst_1)):
    print("idx={},val={}".format(i,lst_1[i]))
print("+"*50)
dic_4=dict(a=2,b=3,c=6,d=0)
print("dic_4={}".format(dic_4))
print("_"*50)
print("for k in dic_4:")
for k in dic_4:
    print(k)
print("for k,v in dic_4.items():")
for k,v in dic_4.items():
    print("key={},val={}".format(k,v))
    
x=1
while x<=100:
    print("x={}".format(x))
    x+=10
    
x=1
while x<=100:
    print("x={}".format(x))
    x+=10
    if x>=50:break
    
import sys
print("sys.maxsize={}".format(sys.maxsize))
for i in range(sys.maxsize):
    print("i={}".format(i))
    i+=10
    if i>=30:break
    
    lst_d=list(range(3,20,2))
print("lst_d={}".format(lst_d))
print("_"*50)
lst_iter=iter(lst_d)
print("next(lst_iter)->{}".format(next(lst_iter)))
print("next(lst_iter)->{}".format(next(lst_iter)))
for i in lst_iter:
    print(i)
        
def factorial(n):
    if n==1:
        return 1
    else:
        print(n)
        print("_"*50)
        print(n*factorial(n-1))
        print("+"*50)

x,y,*z=0,1,2,3,4,5,6
func_2=2*x+3*y+b
print("func_2={}".format(x,y,*z,func_2))   

x,y,*z=0,1
func_2=2*x+3*y+b
print("func_2={}".format(x,y,*z,func_2))

a=[1,2]
b=[3,4]
c=[5,6]
d=[7,8]
z=zip(a,b,c,d)
x=zip(*z)

print(type(x))
print(list(x))





    
    
