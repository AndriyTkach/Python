#1
print("-------1-------")
for i in range(1000, 3100):
    if i % 7 == 0 and i % 5 != 0:
       print(i, end=",")
    i+=1
#-----------------------------------------
#3
print("-------3-------")
def factorialR(n):
    if n == 0:
        return 1
    return factorialR(n-1) * n

print(factorialR(5))
#-----------------------------------------
#4
print("-------4-------")
def factorialW(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial
 
print(factorialW(5))
#-----------------------------------------
#5
print("-------5-------")
dicts = {}
n=9
i=1
for i in range(1,n+1):
    dicts[i] = i**2

for i in dicts:
    print(i,':',dicts[i])
#-----------------------------------------
#7
print("-------7-------")
def ToTuple(s):
    l = len(s)
    t = []
    i=0
    while i<l:
        s_int=''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
           t.append(int(s_int))
    tup = tuple(t)
    return tup

t = ()
String  = "4,5 7,8,24,355 235, 012, 45"
t = ToTuple(String)
print(t)
#-----------------------------------------
#8
print("-------8-------")
def ToList(s):
    l = len(s)
    s_list = []
    i=0
    s_word=''
    while i<l:
        a = s[i]
        if a != ',':
            s_word = s_word + a
        else:
            if s_word != '':
                s_list.append(s_word)
                s_word=''
        if i == l-1 and s_word !='' and a!=',':
            s_list.append(s_word)
            s_word=''
        i+=1       
    return s_list

s = []
String  = "name,money,time,listen,table"
s = ToList(String)
s.sort()
print(s)
#-----------------------------------------
#9
print("-------9-------")

def Upper(s):
    for i in s:
       print(i.title())

s = ["name and surname","money","time","listen","table"]
Upper(s)
#-----------------------------------------
#10
print("-------10-------")

def Unique(text):
    words = text.split()
    uniq_list = []
    for word in words:
        if text.count(word) == 1:
            uniq_list.append(word)
    return uniq_list

String = "name and surname money time listen  table and money"
print(Unique(String))
#-----------------------------------------
#11
print("-------11-------")
def BinMultiply(s):
    l = len(s)
    t = []
    b_s = []
    i=0
    while i<l:
        s_int=''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
           t.append(int(s_int))
    for i in t:
        if i % 5 == 0:
            b_s.append(i)
    return b_s

bin_string = "010100110,1101010,1101011,110110,1011110101,1100"
print(BinMultiply(bin_string))
#-----------------------------------------
#12
print("-------12-------")
def Calculate(n):
    s = ''
    sum = 0
    for i in range(1,5,1):
        while len(s)!=i:
            s+=str(n)
        sum+=int(s)
        s=''
    return sum

i = 1
print(Calculate(i))
#-----------------------------------------
#13
print("-------13-------")
def CheckPassword(s):
    chars = set('abcdefghijklmnopqrstuvwxyz')
    if any((c in chars) for c in s):
        pass
    else:
        return "Должна быть хотя бы одна строчная буква a-z"
    chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if any((c in chars) for c in s):
        pass
    else:
        return "Должна быть хотя бы одна заглавная буква A-Z"
    chars = set('0123456789')
    if any((c in chars) for c in s):
        pass
    else:
        return "Должна быть хотя бы одна цифра 0-9"
    chars = set('$#@')
    if any((c in chars) for c in s):
        pass
    else:
        return "Должна быть хотя бы один следующий символ $#@"
    if len(s)<6:
        return "Минимальная длина 6"
    if len(s)>12:
        return "Максимальная длина 12"
    return "Пароль подходит"

password = "an0N@12"
print(CheckPassword(password))
#-----------------------------------------
#14
print("-------14-------")
def SortTuple(t):
    t = sorted(t,  key=lambda x: (x[0], x[1], x[2]))
    return t

t = [('Stan', 25, 250), ('John', 20, 150), ('Andrew', 22, 200), ('Frank', 30, 500), ('Andrew', 31, 200)]
print(SortTuple(t))
#-----------------------------------------
#15
print("-------15-------")
def Distance(comm, x, y):
    if comm == 1:
        x+=1
    elif comm == 2:
        y+=1
    elif comm == 3:
        x-=1
    elif comm == 4:
        y-=1
    dis = (x**2 + y**2)**0.5
    return dis, x, y

command = 5
x = 0
y = 0
distance = 0.0
while command != 0:
    print("1 - UP   2 - RIGHT   3 - DOWN    4 - LEFT    0 - EXIT")
    command = int(input("Введите команду: "))
    if command == 0:
        break
    else:
        distance, x, y = Distance(command, x, y)
        print("\nРастояние между начальной и конечной точками робота: ",distance)
#-----------------------------------------
#16
print("-------16-------")
def CountWords(text):
    words = text.split()
    sdicts = {}
    dicts = {}
    for x in dicts:
        dicts[i] = i**2
    for word in words:
        dicts[word]=text.count(word)
    sorted_dict = {k: dicts[k] for k in sorted(dicts)}
    for key, value in sorted_dict.items():
        print(key, ':', value)
    
text = "name and surname money time listen table and money"
CountWords(text)
#-----------------------------------------


