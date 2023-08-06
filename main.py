CONTACTS = {}

def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone number please"
        except KeyError:
            return 'User name not exist'
        except TypeError:
            return 'Wrong data type'
    return wrap

@input_error
def hello_handler(data):
    return 'How can I help you?'

@input_error
def add_handler(data):
    name = data[0].title()
    if name.isalpha() == False:
        raise ValueError
    phone = int(data[1])
    CONTACTS[name] = phone
    return f'Contact {name} with phone number {phone} was saved!'

@input_error
def change_handler(data):
    name = data[0].title()
    if name.isalpha() == False:
        raise ValueError
    phone = int(data[1])
    CONTACTS[name] = phone
    return f'Contact {name} with new phone number {phone} was saved!'

@input_error
def phone_handler(data):
    name = data[0].title()
    if name.isalpha() == False:
        raise ValueError
    return f'Contact {name} has phone number {CONTACTS[name]}!'

@input_error
def show_all_handler(data):
    if len(CONTACTS) == 0:
        return 'Contact list is empty'
    return '\n'.join([f"{name}:  {''.join(str(phone))}" for name, phone in CONTACTS.items()])


@input_error
def exit_handler(data):
    return 'Good bye'

@input_error
def command_parser(raw_str: str):
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        for command in value:
            if command.startswith(elements[0].lower() + ' '):
                return key, elements[2:]
            elif elements[0].lower() in command:
                return key, elements[1:]
    return 'Unknown command, try again!'

            
COMMANDS = {
    hello_handler: ['hello'],
    add_handler: ['add'],
    change_handler: ['change'],
    phone_handler: ['phone'],
    show_all_handler: ['show all'],
    exit_handler: ['good bye', 'close', 'exit']
}

@input_error
def main(): # loop question - answer
    while True:
        user_input = input('Input: ')
        if not user_input:
            print("Input can't be empty!")
            continue
        if type(command_parser(user_input)) == str:
            print(command_parser(user_input))
            continue
        func, data = command_parser(user_input)
        result = func(data)
        print(result)
        if func == exit_handler:
            break

if __name__ == "__main__":
    main()