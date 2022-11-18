file = open('directory', 'r', encoding = 'utf-8')
lst = file.read().split('\n')

number = {}

for i in lst:
    key = i.split(' ')[0]
    value = ' '.join(i.split()[1:])
    number[key] = value

file.close()

def import_number(a):
    file = open('directory', 'a', encoding = 'utf-8')
    file.write(f'\n{a}')
    file.close()

def import_file():
    open('directory','a').write(f"\n{open('file','r').read()}")
    file.close()

def export_file(a):
    file = open('export', 'a', encoding = 'utf-8')
    file.write(f'{a}\n')
    file.close()