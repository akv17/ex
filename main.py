import re

def op():
    f = open('1.txt', 'r').read()
    return f

def tsk1(x):
    print('Task 1\n')
    info = re.findall('[А-Я]\.\s?[А-Я]\w+', x)
    for el in info:
        print(el)
    
def tsk2(y):
    print('\nTask 2\n')
    info = re.findall('([А-Я]\.\s?[А-Я]\w+)|([А-Я]\.\s[А-Я]\.\s?[А-Я]\w+)|([А-Я]\w+ +[А-Я]\w+)', y)   
    for el in info:
        for match in el:
            if match != '':
                print(match)

def main():
    val = tsk1(op())
    val2 = tsk2(op()) 
    return val, val2

main()    
    
    
