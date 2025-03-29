# Store Management Software for Vegan Products

BioMarket s.a.s has hired you to develop a small management software for their new shop. The software must have the following functionalities:

- Register new products, with name, quantity, selling price, and purchase price.
- List all available products.
- Record sales made.
- Display gross and net profits.
- Show a help menu with all available commands.

The software is text-based, so it will be used via the command line.

**Attention**: the interaction is in italian as shown by the following instructions.

### Example interaction with the program

Inserisci un comando: aiuto
I comandi disponibili sono i seguenti:
aggiungi: aggiungi un prodotto al magazzino
elenca: elenca i prodotto in magazzino
vendita: registra una vendita effettuata
profitti: mostra i profitti totali
aiuto: mostra i possibili comandi
chiudi: esci dal programma


Inserisci un comando: aggiungi
Nome del prodotto: latte di soia
Quantità: 20
Prezzo di acquisto: 0.80
Prezzo di vendita: 1.40
AGGIUNTO: 20 X latte di soia


Inserisci un comando: aggiungi
Nome del prodotto: tofu
Quantità: 10
Prezzo di acquisto: 2.20
Prezzo di vendita: 4.19
AGGIUNTO: 10 X tofu


Inserisci un comando: aggiungi
Nome del prodotto: seitan
Quantità: 5
Prezzo di acquisto: 3
Prezzo di vendita: 5.49
AGGIUNTO: 5 X seitan


Inserisci un comando: elenca
PRODOTTO    QUANTITA'   PREZZO
latte di soia   20  €1.4
tofu    10  €4.19
seitan  5   €5.49


Inserisci un comando: vendita
Nome del prodotto: latte di soia
Quantità: 5
Aggiungere un altro prodotto ? (si/no): si
Nome del prodotto: tofu
Quantità: 2
Aggiungere un altro prodotto ? (si/no): no
VENDITA REGISTRATA
- 5 X latte di soia: €1.40
- 2 X tofu: €4.19
Totale: €15.38


Inserisci un comando: elenca
PRODOTTO        QUANTITA'   PREZZO
latte di soia   15          €1.4
tofu            8           €4.19
seitan          5           €5.49


Inserisci un comando: vendita
Nome del prodotto: seitan
Quantità: 5
Aggiungere un altro prodotto ? (si/no): no
VENDITA REGISTRATA
5 X seitan: €5.49
Totale: €27.45


Inserisci un comando: elenca
PRODOTTO        QUANTITA'   PREZZO
latte di soia   15          €1.4
tofu            8           €4.19


Inserisci un comando: profitti
Profitto: lordo=€42.83 netto=€19.43


Inserisci un comando: storna
Comando non valido
I comandi disponibili sono i seguenti:
aggiungi: aggiungi un prodotto al magazzino
elenca: elenca i prodotto in magazzino
vendita: registra una vendita effettuata
profitti: mostra i profitti totali
aiuto: mostra i possibili comandi
chiudi: esci dal programma


Inserisci un comando: chiudi
Bye bye


### NOTES

- Try to write good code by organizing the various functionalities into appropriate functions.
- Before writing the code, think about the best data structures to use: lists, tuples, dictionaries, or combinations of them like lists of dictionaries.
- The program must be persistent, meaning the information entered by the user must be retained between different executions of the program. To achieve this, you can use a text file and choose the encoding for the information.
- Ensure that the inputs entered by the user are valid, for example, that numbers are indeed numbers. Handle invalid cases with exceptions and error messages.
- During a purchase, verify that the purchased products are actually available in the inventory. If not, display an error message to the user.
- When adding to the inventory, check if the product to be added is already present. If so, add the quantity to the existing stock without requiring the purchase and selling prices again. Otherwise, register it as a new product.
- Gross profit is the total sales, i.e., everything the customers paid. Net profit is the gross profit minus the purchase cost of the products.
- In this work, it is essential to always follow the specifications given to the letter. Therefore, the program must contain exactly the specified functions and produce exactly the output shown in the example if it receives the same input.
- Variable, function, and method names must always be written in English using snake_case. CamelCase should only be used for class names. Do not mix Italian and English; always use English only.
- Use docstrings to document functions, classes, and methods.