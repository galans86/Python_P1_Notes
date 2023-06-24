from os import path
import csv


def export_notes(file: str, notes: list):
    csv_line = ''
    with open(file, 'w') as m_file:
        for rec in notes:
            line = ''.join([k+':'+v+' ' for k, v in rec.items()])
            m_file.write(f'{line};\n')
            csv_line += line
    return csv_line



def import_notes(file: str):
    if path.exists(file):
        notes = []
        n_dict = {}
        with open(file) as m_file:
            csv_line = m_file.read().strip()[:-1]
            n_list = [rec for rec in csv_line.split(sep=';')]
            
            for i in n_list:
               m_l = i.split( )
               n_dict = {}
               for x in m_l: 
                 n_dict.setdefault(x.split(':')[0], x.split(sep=':')[1])            
               if n_dict:
                 notes.append(n_dict)
    return notes    

