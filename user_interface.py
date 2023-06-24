import data_provider
import csv_creator

mode = 0


def menu():
    global mode
    try:
        mode = int(input('\nЗаметки:\n'
                         '1 - Добавить заметку\n'
                         '2 - Просмотреть заметку\n'
                         '3 - Редактировать заметку\n'
                         '4 - Удалить заметку\n'
                         '5 - Просмотреть все заметки\n'
                         '6 - Найти заметки по дате\n'
                         '7 - Экспорт в файл\n'
                         '8 - Импорт из файла\n'
                         '0 - Выход\n'))
        if mode not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            mode = 0
            print('Input incorrect\n')
        return mode
    except ValueError:
        mode = 0
        print('Input incorrect\n')
        return mode


def get_mode():
    return mode


def notes_run():
    while menu():
        match get_mode():
            case 1:
                # добавить заметку
                if data_provider.add_note():
                    print('Данные добавлены')
                else:
                    print('Запись с таким Идентификатором уже существует')
            case 2:
                # просмотреть заметку
                print(data_provider.get_note_by_id(
                    input('Введите идентификатор заметки: ')))
            case 3:
               # редактировать заметку
                if data_provider.edit_note_by_id(
                        input('Введите идентификатор заметки: ')):
                    print('Заметка изменена')
                else:
                    print('Заметка не найдена')
            case 4:
               # удалить заметку
                if data_provider.delete_note_by_id(
                        input('Введите идентификатор заметки: ')):
                    print('Заметка удалена')
            case 5:
                # просмотреть все заметки
                print_notes(data_provider.get_notes())
            case 6:
                # Найти заметки по дате
                print_notes(data_provider.find_by_date(
                    input('Введите дату в формате дд.мм.гггг :')))
            case 7:
                # сохранение в csv
                csv_creator.export_notes(
                    'notes.csv', data_provider.get_notes())
                print('Данные сохранены в файл notes.csv')
            case 8:
                # загрузить данные из csv
                data_provider.set_notes(csv_creator.import_notes('notes.csv'))
                print('Данные загружены из файла notes.csv')


def print_notes(notes: list):
    for note in notes:
        print(note)
