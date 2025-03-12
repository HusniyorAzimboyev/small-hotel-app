mehmonlar = [{"name":'Sobir','room':17,'type':'standart'},{"name":'Harry','room':18,'type':'lyuks'}]
def remove():
    a = input('Kim ketmoqchi? ')
    for yesornot in mehmonlar:
        if yesornot['name']==a:
            mehmonlar.remove(yesornot)
            print(f'{a} listdan o`chirildi')
            return
    print('Notogri ism')
def add():
    todo = 'none'
    new_guest_data = {}
    mehmonlarlisti,roomnumbers = [],[]
    for check in mehmonlar:
        mehmonlarlisti.append(check['name'])
        roomnumbers.append(check['room'])
    while todo!='done':
        a= input('Yangi mehmon: ')
        if a not in mehmonlarlisti:
            new_guest_data['name']=a
            todo = 'done'
        else:
            print('Xatolik, boshqa ism kiriting.')
    todo2 = 'none'
    while todo2 != 'done':
        b = input('Xona raqami: ')
        if int(b) in roomnumbers:
            print('Bu xona band')
        else:
            todo2 = 'done'
            new_guest_data['room']=b
    c=input('Qaysi turdagi xona?\noddiy: o\nStandart: s\nLyuks: l\n>>>')
    if c == 'o':
        new_guest_data['type']='oddiy'
    elif c=='s':
        new_guest_data['type'] = 'standart'
    else:
        new_guest_data['type'] = 'lyuks'
    mehmonlar.append(new_guest_data)
    print('Bajarildi✅')
print('A.Husniyor mehmonxonasiga hush kelibsiz!\nBuyruqlar:\nmehmon qo`shish-1\nmehmon ketmoqchi-2\nmehmonlar ro`yhati-3\n\nchiqish-0')
def startapp():
    a=int(input('Buyruqni tanglang: '))
    if a==1:
        add()
    elif a==2:
        remove()
    elif a==3:
        print('Ismi          Xona raqami         Xona turi\n')
        for i in mehmonlar:
            print("{:<12}   {:<12}     {:<12}".format(i['name'],i['room'],i['type']))
        print('')
try:
    while True:
        startapp()
except Exception as e:
    print("Xatolik!!!",e)
