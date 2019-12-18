'''
写一个函数完成三次登录功能,在写一个函数完成注册功能,并将信息保存在文件中
下面的代码没有实现用户名同名检查
'''


def user_reg_input():  # 注册模块,返回名字及口令给user_register模块
    while True:
        input_name = input('Please Enter Your Register name:')
        input_psd = input('Please Enter Your Password')
        if input_name.lower() == 'user_name':
            print('The name has been Registered,,Please try again')
        elif input_psd.lower() == 'user_psd':
            print('The password has illegal characters,Please try again ')
        else:
            break
    return input_name, input_psd


def user_register(input_name, input_psd):  # 将用户信息存入文件中
    with open('user_register_message', 'r+', encoding='utf-8') as fls:

        if len(fls.readline()) == 0:
            fls.write('user_name|user_psd\n')
            fls.write(input_name + '|' + input_psd + '\n')
        else:
            fls.write(input_name + '|' + input_psd + '\n')


# 将用户输入信息与user_register_message文件进行比对
def user_login(user_name, user_psd, input_name, input_psd):
    mark = 3
    while mark:
        if user_name == input_name and user_psd == input_psd:
            print('welcome Back' + str(user_name))
            break
        else:
            print(
                'Your login name or password is wrong,Please try again(You can try {} times)'.format(mark))
        mark -= 1


def user_message(full_message):

    with open('user_register_message', 'r', encoding='utf-8') as fls:
        for line in fls:
            if line == 'user_name|user_psd\n':
                continue
            elif line == full_message:
                lst = line.strip().split('|')
                break
        user_name = lst[0]
        user_psd = lst[1]

    return user_name, user_psd  # 返回用户的已注册信息


def login_judge(input_name, input_psd):
    with open('user_register_message', 'r', encoding='utf-8') as fls:
        full_message = input_name + '|' + input_psd + '\n'
        for line in fls:
            if line == full_message:
                return full_message

        else:  # 没有在文件内找到用户名
            return False


def console():
    print('{:-^40}'.format("Welcome"))
    print('{:-^40}'.format("choise list"))
    fmt = "{{0:<{}}}{{1:>{}}}".format('20','20')
    print(fmt.format('1.', 'login'))
    print(fmt.format('2.', 'Registe'))
    print(fmt.format('3.', 'Exit'))
    # print('{0:<20}{1:>20}'.format('1.', 'login'))
    # print('{0:<20}{1:>20}'.format('2.', 'Register'))
    # print('{0:<20}{1:>20}'.format('3.', 'Exit'))
    num = input('Please choose list')
    if num == '1':
        input_name = input("Please Enter Your name")
        input_psd = input("Please Enter Your Password")
        full_message = login_judge(input_name, input_psd)
        if full_message == False:  # 如果没有在文件内找到用户名则选择是否注册
            print("You're not registered")
            mark = input('Do you need registration information?Enter Y/N')
            if mark.lower() == "y":
                input_name, input_psd = user_reg_input()
                user_register(input_name, input_psd)
                back = input('return to login?Please Enter Y/N')
                if back.lower() == "y":
                    console()
                else:
                    exit()
        else:
            user_name, user_psd = user_message(full_message)
            user_login(user_name, user_psd, input_name, input_psd)
    elif num == '2':
        input_name, input_psd = user_reg_input()
        user_register(input_name, input_psd)
        back = input('return to login?Please Enter Y/N')
        if back.lower() == "y":
            console()
        else:
            exit()
    else:
        exit()


console()





