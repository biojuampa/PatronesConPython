#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  phonebook.py - Intensivo desde Cero (ejercicio 2)
#


import pickle
import sys
import os
from time import sleep


WORKDIR = f'{os.environ["HOME"]}/.phonebook'
BOOKS = f'{WORKDIR}/books'


phonebook = {}
phonebook_name = 'phonebook'


def load_phonebook(path):
    print(f'Abriendo la agenda [{os.path.basename(path)}] ...')
    sleep(1)
    if not os.path.exists(f'{path}.bin'):
        print(f'La agenda [{os.path.basename(path)}] no existe!')
        sleep(2)
        main_menu()
    
    if not os.path.getsize(f'{path}.bin'):
        print(f'La agenda [{os.path.basename(path)}] está vacía')
        return {}
    
    try:
        with open(f'{path}.bin', 'rb') as fhand:
            book = pickle.load(fhand)        
        return book
    except:
        print(f'ERROR: Imposible leer la agenda [{os.path.basename(path)}]!')
        sleep(2)
        main_menu()


def create_phonebook(path):
    print(f'Creando la agenda [{path}] ...')
    sleep(1)
    if os.path.exists(f'BOOKS/{path}.bin') and os.path.getsize(f'{path}.bin'):
        print(f'La agenda [{path}] existe y tiene datos. Por seguridad, no se creará\n'
              'una agenda nueva que sobreescriba otra existente conteniendo datos.\n'
              'Primero debe borrarla, bien desde el menú principal, o bien manualmente.\n'
              )
        input('Pulse enter para continuar ...')
        main_menu()
    
    global phonebook
    global phonebook_name
    try:
        fhand = open(f'{path}.bin', 'wb')
        fhand.close()
        phonebook = {}
        phonebook_name = path
    except:
        print(f'ERROR: No se pudo crear la agenda [{path}]!')
        sleep(2)
        main_menu()


def delete_phonebook(path):
    option = input(f'Está seguro que desea borrar permanentemente la agenda [{path}] [y/N]')

    if option == 'y':
        print(f'Borrando la agenda [{path}] ...')
        sleep(1)
        if os.path.exists(f'{path}.bin'):
            os.remove(f'{path}.bin')
            global phonebook_name
            phonebook_name = 'phonebook'
        else:
            print(f'La agenda [{path}] NO existe, compruebe el nombre y la ruta.')
            
        
def save_phonebook(path):
    with open(f'{path}.bin', 'rb') as fhand:
        saved_phonebook = pickle.load(fhand)
    
    if saved_phonebook == phonebook:
        return 
    
    print(f'Guardando la agenda [{path}] ...')
    sleep(1)
    
    with open(f'{path}.bin', 'wb') as fhand:
        pickle.dump(phonebook, fhand)
    

def show_contacts(contact):
    match = False
    for name, phones in phonebook.items():
        if name.startswith(contact):
            match = True
            print(f'\n  * {name}:')
            for i in range(len(phones)):
                print(f'      - Tel. {i+1}: {phones[i]}')
    
    if not match:  
        print('No hubo coincidencias.')
        sleep(1)
    
    input('\nPersione enter para continuar ...')


def add_contact(first, last, numbers):
    name = f'{last}, {first}'
    phonebook[name] = numbers
    save_phonebook(phonebook_name)
    

def show_all_contacts():
    for name, phones in phonebook.items():
        print(f'\n  * {name}:')
        for i in range(len(phones)):
            print(f'      - Tel. {i+1}: {phones[i]}')
    
    input('\nPersione enter para continuar ...')


def add_phone(contact, phone):
    if contact in phonebook:
        phonebook[contact].append(phone)
    else:
        print(f'ERROR: El nombre de contacto \'{contact}\' es incorrecto!')
        sleep(2)


def delete_phone(contact):
    if contact not in phonebook:
        print(f'ERROR: El nombre de contacto \'{contact}\' es incorrecto!')
        sleep(2)
        return 
    
    if phonebook[contact]:
        phones = phonebook[contact]
        for i in range(len(phones)):
            print(f'[{i+1}] {phones[i]}')
        
        option = input('\nDime qué teléfono deseas borrar: ')
        try:
            if option < 1:
                raise
            print(f'Borrando {phones[int(option)-1]} de \'{contact}\' ...')
            del phones[int(option)-1]
            sleep(2)
        except:
            print('\nERROR: Opción incorrecta')
            sleep(2)
            
    else:
        print(f'\n\'{contact}\' no tiene ningún teléfono asociado.')
        sleep(2)
        

def delete_contact(contact):
    if contact in phonebook:
        print(f'Borrando el contacto \'{contact}\' de la agenda [{phonebook_name}] ...')
        del phonebook[contact]
        sleep(2)
    else:
        print(f'\'{contact}\' No existe.')
        sleep(2)


def secondary_menu():
    while True:
        os.system('clear')
        print(f'  AGENDA TELEFÓNICA: [{phonebook_name}]')
        print('')
        print('    [1] Mostrar contacto')
        print('    [2] Agregar contacto')
        print('    [3] Ver todos los contactos')
        print('    [4] Agregar teléfono a un contacto')
        print('    [5] Borrar teléfono de un contacto')
        print('    [6] Borrar contacto')
        print('    [7] Guardar contactos')
        print('    [8] Menú principal')
        print('')
        
        option = input('Elige una opción: ')
        
        if option == '1': # show contact
            contact = input('Escribe el nombre o parte de él: ')
            if not contact:
                continue 
            show_contacts(contact.lstrip())
        
        elif option == '2': # add contact
            first_name = input('Nombre/s del contacto: ')
            last_name = input('Apellido del contacto: ')
            phones = list()
            while True:
                phone = input(f'Teléfono de {last_name}, {first_name}'
                                ' (enter para terminar): '
                                )
                if not phone:
                    break
           
                phones.append(phone.strip())
                
            add_contact(first_name.strip(), last_name.strip(), phones)
        
        elif option == '3': # show all contact
            show_all_contacts()
        
        elif option == '4': # add phone
            contact = input('Nombre completo del contacto: ')
            phone = input(f'Teléfono para agregar a \'{contact}\': ')
            if phone:
                add_phone(contact.strip(), phone.strip())
        
        elif option == '5': # del phone
            contact = input('Nombre completo del contacto: ')
            delete_phone(contact.strip())
        
        elif option == '6': # del contact
            contact = input('Nombre completo del contacto a borrar: ')
            delete_contact(contact)
        
        elif option == '7': # save
            save_phonebook(phonebook_name)
        
        elif option == '8': # main menu
            save_phonebook(phonebook_name)
            main_menu()
        
        else:
            pass
        

# TODO: Quzás implementar una función para listar las agendas en lugar de hacerlo en el menú
def main_menu():
    while True:
        os.system('clear')
        print()
        print('Welcome to the BEST PHONE BOOK in the entire WORLD :-p')
        print()
        print('    [1] Abrir agenda existente')
        print('    [2] Crear agenda nueva')
        print('    [3] Borrar agenda existente')
        print('    [4] Listar agendas creadas')
        print('    [5] Salir')
        print()
        
        option = input('Elige una opción: ')
        
        if option == '1': # Cargar
            global phonebook
            global phonebook_name
            book_path = input(f'Nombre de la agenda [{phonebook_name}]: ')
            if book_path:
                phonebook = load_phonebook(f'{BOOKS}/{book_path}')
                phonebook_name = book_path
            else:
                phonebook = load_phonebook(f'{BOOKS}/{phonebook_name}')
            
            secondary_menu()
            
        elif option == '2': # Crear
            path = input(f'Ruta y nombre de la agenda [{phonebook_name}]: ')
            if path:
                create_phonebook(path)
            else:
                create_phonebook(phonebook_name)
        
            secondary_menu()
        
        elif option == '3': # Borrar
            path = input(f'Ruta y nombre de la agenda [{phonebook_name}]: ')
            if path:
                delete_phonebook(path)
            else:
                delete_phonebook(phonebook_name)
        
        elif option == '4': # Listar
            print('\n  Agendas disponibles:')
            books = os.listdir(BOOKS)
            for book in books:
                if book.endswith('.bin'):
                    print('    -', book.split('.')[0])
            input('\nPulsa enter para continuar ...')
        
        elif option == '5': # Salir
            print('\nSee you soon ...\n')
            sys.exit()
            
        else: # Otro
            pass
        

if __name__ == '__main__':
    if not os.path.exists(WORKDIR):
        try:
            os.mkdir(WORKDIR)
            os.mkdir(BOOKS)
            print('Creando directorio de trabajo ...')
            sleep(1)
        except:
            print('ERROR: No es posible crear el directorio de trabajo')
            print('       Aún podrá trabajar con la agenda, pero no podrá')
            print('       guardar los cambios realizados.\n')
            input('Presione enter para seguir ...')
    
    if not os.path.exists(BOOKS):
        try:
            os.mkdir(BOOKS)
        except :
            print('ERROR: No es posible crear el directorio de trabajo')
            print('       Aún podrá trabajar con la agenda, pero no podrá')
            print('       guardar los cambios realizados.\n')
            input('Presione enter para seguir ...')
            
    main_menu()










































