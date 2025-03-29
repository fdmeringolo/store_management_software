from .commands import *
from .store import update_store
from .validation import is_valid_command
import csv


def management_item():
    """
    % Main function of the program
    """
     
    #initializes the file
    with open("Store_negozio_vegano.cvs", 'a+', newline='' ) as csv_file:
        csv_file.seek(0)
        csv_reader = csv.DictReader(csv_file)
        
        data = []
        for row in csv_reader:
            data.append(row)
    
    with open("Store_negozio_vegano.cvs", 'w', newline='' ) as csv_file:
        
        update_store(csv_file,data)
        
    
    #Commands management
    command = ""

    while command != "chiudi":

        command = input("Inserisci un comando:")
        #print("Comando selezionato:", command)
        
        # Command check
        # assert (is_valid_command(command)), "Comando non valido"
        if not is_valid_command(command): 
            print ('''
            I comandi disponibili sono i seguenti: \n\
            \n\
            - aggiungi: aggiungi un prodotto al magazzino \n\
            - elenca: elenca i prodotto in magazzino \n\
            - vendita: registra una vendita effettuata \n\
            - profitti: mostra i profitti totali \n\
            - aiuto: mostra i possibili comandi \n\
            - chiudi: esci dal programma\n
            ''')
            
        elif command == "aggiungi":
            add_item()

        elif command == "elenca":
            list_items()

        elif command == "vendita":
            sell_item()

        elif command == "profitti":
            profits()

        elif command == "aiuto":
            help()
    
    print("Bye bye")
    return










    