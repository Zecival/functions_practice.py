def hello():
    print("hello")

def pack(a,b,c):
    return(a,b,c)

def eat_lunch(my_list):
    if len(my_list) > 0:
        print(f'First I eat {my_list[0]}')
        for index, item in enumerate(my_list):
            if index > 0:
                print(f'Next, I eat {item}')
    else:
        print('My lunchbox is empty')

hello()
my_list = pack('Apple', 'Banana', 'Carrot')
eat_lunch(my_list)

