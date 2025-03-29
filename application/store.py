import csv

def item_check(item_name):
    """
    % Vheck if the item is present in stock
    """
    with open('Store_negozio_vegano.cvs') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        check = False
        for row in csv_reader:
            if item_name == row['name']:
                check = True
                break

        return check  
    

def update_store(csv_file,data):
    """
    % Update the stock
    """  
    fieldnames = ["name","no_stock_items","purchase_price","no_sold_items","selling_price" ]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)

    return