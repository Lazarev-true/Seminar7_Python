import view
import model

def start():
    view.showinfo('Добро пожаловать в телефонный справочник!')
    
    view.showinfo(f'Операции с телефонной книгой: \n{model.com}')

    while True:
        com_base = view.getNumb('Выберите команду --> ')
        if not com_base in model.commands.keys():
            view.showinfo('Некорректный ввод')
            continue
        else:
            model.commands[com_base]()
            break