 python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x=(1,2,3,4)
>>> y=[1,2,3,4]
>>> type(x)
<class 'tuple'>
>>> type(y)
<class 'list'>
>>> y.append(5)
>>> y
[1, 2, 3, 4, 5]
>>> y.remove(3)
>>> y
[1, 2, 4, 5]
>>> x.append(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> x.remove(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'remove'
>>> z=list(x)
>>> z
[1, 2, 3, 4]
>>> z.append(10)
>>> z
[1, 2, 3, 4, 10]
>>> len(x)
4
>>> x+y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "list") to tuple
>>> y=(5,6,7,8)
>>> x+y
(1, 2, 3, 4, 5, 6, 7, 8)
>>> x*5
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> 3 in x
True
>>> 5 in x
False
>>> for n in x:print(n)
... 
1
2
3
4
>>> for n in x:print(n*10)
... 
10
20
30
40
>>> x={1,2,3,4,2,3,4}
>>> type(x)
<class 'set'>
>>> x
{1, 2, 3, 4}
>>> y=["a","b","c","d","b","c","a"]
>>> z.set(y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'set'
>>> z=set(y)
>>> z
{'c', 'a', 'd', 'b'}
>>> s1{1,2,3,4,5}
  File "<stdin>", line 1
    s1{1,2,3,4,5}
      ^
SyntaxError: invalid syntax
>>> s1={1,2,3,4,5}
>>> s1={3,4,5,6,7,8}
>>> s2={3,4,5,6,7,8}
>>> s1={1,2,3,4,5}
>>> s3={"a,"b","c","d","d"}
  File "<stdin>", line 1
    s3={"a,"b","c","d","d"}
                ^
SyntaxError: invalid syntax
>>> s3={"a","b","c","d","d"}
>>> s1.add(6)
>>> s1
{1, 2, 3, 4, 5, 6}
>>> s1.remove(6)
>>> s1
{1, 2, 3, 4, 5}
>>> s1.remove(7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 7
>>> s3.discard("b")
>>> s3
{'c', 'a', 'd'}
>>> s3.discard("z")
>>> s3
{'c', 'a', 'd'}
>>> s1.difference(s2)
{1, 2}
>>> s2.difference(s1)
{8, 6, 7}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> s1.intersection(s2)
{3, 4, 5}
>>> s2.intersection(s3)
set()
>>> x={"a":I}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'I' is not defined
>>> x={"a":I,"b":2,"c":3,"d":4}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'I' is not defined
>>> x={"a":1,"b":2,"c":3,"d":4}
>>> type(x)
<class 'dict'>
>>> code={67:"Effence",41:"Saido",38:"Tessa",58:"Nkimalantoi"}
>>> code
{67: 'Effence', 41: 'Saido', 38: 'Tessa', 58: 'Nkimalantoi'}
>>> code[58]
'Nkimalantoi'
>>> code[50]="Naima"
>>> code
{67: 'Effence', 41: 'Saido', 38: 'Tessa', 58: 'Nkimalantoi', 50: 'Naima'}
>>> code[38]="Marie"
>>> code
{67: 'Effence', 41: 'Saido', 38: 'Marie', 58: 'Nkimalantoi', 50: 'Naima'}
>>> code.pop(41)
'Saido'
>>> code
{67: 'Effence', 38: 'Marie', 58: 'Nkimalantoi', 50: 'Naima'}
>>> 67 in code
True
>>> 41 in code
False
>>> "Marie" in code
False
>>> code.keys()
dict_keys([67, 38, 58, 50])
>>> code.values()
dict_values(['Effence', 'Marie', 'Nkimalantoi', 'Naima'])
>>> "Marie" in code.values()
True
>>> "Saido" in code.values()
False
>>> for key in code.keys():print(key)
... 
67
38
58
50
>>> for value in code.values()
  File "<stdin>", line 1
    for value in code.values()
                             ^
SyntaxError: invalid syntax
>>> for value in code.values():print(value.upper)
... 
<built-in method upper of str object at 0x7f0105e09b30>
<built-in method upper of str object at 0x7f0105e181b0>
<built-in method upper of str object at 0x7f0105e18170>
<built-in method upper of str object at 0x7f0105e18130>
>>> for value in code.values():print(value.upper())
... 
EFFENCE
MARIE
NKIMALANTOI
NAIMA
>>> z=dict()
>>> z
{}
>>> z{"a"}=10
  File "<stdin>", line 1
    z{"a"}=10
     ^
SyntaxError: invalid syntax
>>> z{"a"}=10
  File "<stdin>", line 1
    z{"a"}=10
     ^
SyntaxError: invalid syntax
>>> z=dict()
>>> z
{}
>>> type(z)
<class 'dict'>
>>> 
[1]+  Stopped                 python3

