from .validation import valid_numerical_input
from .store import item_check, update_store
import csv


def add_item():
    """
    % Add item to the stock
    """
    item_name = input("Nome del prodotto:")
    #print(f"Nome del prodotto: {item_name}")

    #New item, not present in stock
    if not item_check(item_name):
        #New item, not present in stock 
        no_stock_items = valid_numerical_input("Quantità: ", data_type=int)           
        #print(f"Quantità: {no_stock_items}")

        purchase_price = valid_numerical_input("Prezzo di acquisto: ")
        #purchase_price = valid_numerical_input("Prezzo di acquisto: [€]")
        #print(f"Prezzo di acquisto: {purchase_price} €")
        
        no_sold_items = 0
        
        selling_price = valid_numerical_input("Prezzo di vendita: ")
        # selling_price = valid_numerical_input("Prezzo di vendita: [€]")
        # print(f"Prezzo di vendita: {selling_price} €")

        with open("Store_negozio_vegano.cvs", 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([item_name,no_stock_items,purchase_price,no_sold_items,selling_price])
        
        print(f"AGGIUNTO: {no_stock_items} X {item_name} \n")

    #Item present in stock
    else:
        no_stock_items = valid_numerical_input("Quantità: ", data_type=int)    
        #print(f"Quantità: {no_stock_items}")

        with open("Store_negozio_vegano.cvs", 'r+',newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            data = []
            for row in csv_reader:
                if row['name'] == item_name:
                    row['no_stock_items'] = no_stock_items + int(row['no_stock_items'])
                data.append(row)

            csv_file.seek(0)
            update_store(csv_file,data)

        print(f"AGGIUNTO: {no_stock_items} X {item_name} (già presente in magazzino) \n")

    return

def list_items():
    """
    % List the items present in stock
    """
    with open('Store_negozio_vegano.cvs') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        print("PRODOTTO QUANTITA' PREZZO")
        #print("Prodotto - Quantità - Prezzo vendita")
        for row in csv_reader:
            
            print(f"{row['name']}  {row['no_stock_items']}  €{row['selling_price']}€")
            #print(f"{row['name']} - {row['no_stock_items']} - {row['selling_price']}€")

        print(" ")

    return

def sell_item():
    """
    % Sell the items present in stock
    """
    selling_mode = "si"
    to_print = []

    while selling_mode == "si":
        item_name = input("Nome del prodotto:")
        #print(f"Nome del prodotto: {item_name}")

        #Item in stock
        if item_check(item_name):
            
            no_items_to_sell = valid_numerical_input("Quantità: ", data_type=int)  
            #print(f"Quantità: {no_items_to_sell}")
            
            with open("Store_negozio_vegano.cvs", 'r+',newline='') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                
                data = []
                for row in csv_reader:
                    if row['name'] == item_name:
                        sale = int(row['no_stock_items']) - no_items_to_sell
                        if sale < 0:
                            print("Quantità non disponibile \n")
                        else:
                            row['no_stock_items'] = sale
                            row['no_sold_items'] = no_items_to_sell
                            to_print.append([no_items_to_sell, item_name, row['selling_price']])
                            
                    data.append(row)

                csv_file.seek(0)
                update_store(csv_file,data)

        #Item not in stock
        else:
            print("Prodotto non presente in magazzino \n")

        selling_mode = input("Vuoi continuare la spesa? [si/no]:")
    
    if len(to_print) > 0:
        print("VENDITA REGISTRATA")
        tot_cost = 0
        for line in to_print:
            print(f"{line[0]} X {line[1]} : € {line[2]}")
            #print(f"{line[0]} X {line[1]} (costo: {line[2]} €/pezzo)")
            tot_cost += float(line[2])*int(line[0])
        print("Totale: € %.2f \n" % tot_cost)
        #print("Costo totale: %.2f € \n" % tot_cost)   

    return

def profits():
    """
    % Profits generated by sales
    """
    with open("Store_negozio_vegano.cvs", 'r',newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        gross_price = 0 
        net_price = 0
        #["name","no_stock_items","purchase_price","no_sold_items","selling_price" ]

        for row in csv_reader:
            gross_price += float(row['selling_price'])*int(row['no_sold_items'])
            net_price += (float(row['selling_price']) - float(row['purchase_price']))*int(row['no_sold_items'])

        # print("Profitto lordo: %.2f €" % gross_price)
        # print("Profitto netto: %.2f € \n" % net_price)
        print("Profitto: lordo = €%.2f netto = €%.2f \n" % (gross_price,net_price))
                     
    return

def help():
    """
    % List the commands
    """
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
    return

