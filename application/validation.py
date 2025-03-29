def valid_numerical_input(question, data_type=float):
    """
    % Check if the input number is a positive int/float according to the parameter of the function
    """
    number = ""
    
    while not (type(number) in [int,float] and number >= 0): #is_valid_number(number):
        try: 
            if data_type == int:
                number = int(input(question))
            else:
                number = float(input(question))
            
            if number >=0:
                return number
            else:
                print("Input non valido. Inserire un numero valido")
                
        except:
            print("Input non valido. Inserire un numero valido")

    #return number


def is_valid_command(command):
    """
    % Check if the command is valid
    """
    commands_list = ["aggiungi","elenca","vendita","profitti","aiuto","chiudi"]
    return command in commands_list