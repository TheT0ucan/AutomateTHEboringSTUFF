birthday = {
    'alice': 'Apr 1',
    'joe' : 'Dec 12 ',
    'Michael' : 'Mar 14'
}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == "":
        break 

    if name in birthday:
        print(birthday[name] + ' is the birthday of '+ name )
    else:
        print ('I do not have birthday information for' + name )
        print('what is their birthday ')
        bday = input()
        birthday[name] = bday 
        print ('Birthdya database update.'
        )