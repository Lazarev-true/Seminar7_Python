import view
import database as db
    
def number_data():
    while True:
        search1 = view.getNumb('Введите номер --> ')
        if search1 not in db.number:
            view.showinfo('Такого номера нет')
            continue
        else:
            result = db.number[search1]
            break
    view.showinfo(result)

def FCs_data():
    while True:
        search2 = view.getNumb('Введите ФИО --> ')
        if search2 not in db.number.values():
            view.showinfo('Такого ФИО нет')
            continue
        else:
            result = list(db.number.keys())[list(db.number.values()).index(search2)]
            break
    view.showinfo(result)
        

com = '1 - импорт вручную\n\
2 - импорт из файла\n\
3 - импортозамещение\n\
4 - экспорт\n\
5 - поиск контакта'

def import_substitution():
    view.showinfo('Неплохо придумано!!!')

def search_1():
    view.showinfo('1 - по номеру или 2 - по ФИО')
    searchIn = view.getNumb('Искать --> ')
    if searchIn == '1':
        number_data()
    elif searchIn == '2':
        FCs_data()
    else:
        view.showinfo('Такого варианта нет')

def import_base():
    import1 = view.getNumb('Введите номер --> ')
    import1 += ' '
    import1 += view.getNumb('Введите ФИО --> ')
    db.import_number(import1)

def import_from():
    db.import_file()
    view.showinfo('Импорт закончен')


def export():
    while True:
        FCs = view.getNumb('Искать контакт по ФИО --> ')
        if FCs == '*':
            break
        elif FCs not in db.number.values():
            view.showinfo('Такого ФИО нет')
            continue
        else:
            contact = list(db.number.keys())[list(db.number.values()).index(FCs)]
            contact += ' ' + FCs
            db.export_file(contact)
            view.showinfo('Экспорт закончен для завершения введите *')


commands = {'1': import_base, 
            '2': import_from,
            '3': import_substitution, 
            '4': export, 
            '5': search_1}


