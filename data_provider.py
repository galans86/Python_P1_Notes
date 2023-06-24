from datetime import datetime
notes = []


def today():
    today = datetime.now().date()
    month = today.month if today.month > 9 else f"0{today.month}"
    t_s = f"{today.day}.{month}.{today.year}"
    return t_s


def check_id(id):
    global notes
    if id.isnumeric():
        o_note = [o_n for o_n in notes if o_n['id'] == id]
        return id if o_note == [] else 0
    else:
        return 0


def add_note():
    global notes
    id = check_id(input('Идентификатор: '))
    if id:
        n_note = {'id':    id,
                  'title': input('Заголовок: '),
                  'body':  input('Текст: '),
                  'date':  today(),
                  'time':   datetime.now().strftime('%H/%M')}

        notes.append(n_note)
        return True
    else:
        return False


def get_notes():
    return notes


def set_notes(i_notes: list):
    global notes
    notes = i_notes


def get_note_by_id(id):
    if id.isnumeric():
        for note in notes:
            if note['id'] == id:
                return note


def find_by_date(date_str: str):
    global notes
    filt_notes = [note for note in notes if note['date'] == date_str]
    return filt_notes


def delete_note_by_id(id):
    if id.isnumeric():
        for note in notes:
            if note['id'] == id:
                notes.remove(note)
                return True


def edit_note_by_id(id):
    global notes
    if id.isnumeric():
        o_note = [o_n for o_n in notes if o_n['id'] == id]
        if o_note == []:
            return False
        else:
            n_note = { 'id':    id,
                       'title': input('Заголовок: '),
                       'body':  input('Текст: '),
                       'date':  today(),
                       'time':   datetime.now().strftime('%H/%M')}    
            for note in notes:               
                if note['id'] == id:  
                   note.update(n_note)    
                   return True
