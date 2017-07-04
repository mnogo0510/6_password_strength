# http://pythonfiddle.com/password-strength-tester/

def get_password_strength(password, pre_pass, name_f, name_s):
    lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    special_characters = [' ', '!', '#', '$', '%', '&', '"', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                          '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', "'"]

    popular_passwords = ['123456', '123456789', 'qwerty', '111111', '1234567', '666666', '12345678', '7777777',
                         '123321', '654321', '1234567890', '123123', '555555', 'vkontakte', 'gfhjkm', '159753',
                         '777777', 'TempPassWord', 'qazwsx', '1q2w3e', '1234', '112233', '121212', 'qwertyuiop',
                         'qq18ww899', '987654321', '12345', 'zxcvbn', 'zxcvbnm', '999999', 'samsung', 'ghbdtn',
                         '1q2w3e4r', '1111111', '123654', '159357', '131313', 'qazwsxedc', '123qwe', '222222', 'asdfgh',
                         '333333', '9379992', 'asdfghjkl', '4815162342', '12344321', 'любовь', '88888888', '11111111',
                         'knopka', 'пароль', '789456', 'qwertyu', '1q2w3e4r5t', 'iloveyou', 'vfhbyf', 'marina',
                         'password', 'qweasdzxc', '10203', '987654', 'yfnfif', 'cjkysirj', 'nikita', '888888', 'йцукен',
                         'vfrcbv', 'jdm', 'qwertyuiop', 'qwe123', 'qweasd', 'natasha', '123123123', 'fylhtq', 'q1w2e3',
                         'stalker', '1111111111', 'q1w2e3r4', 'nastya', '147258369', '147258', 'fyfcnfcbz',
                         '1234554321', '1qaz2wsx', 'andrey', '111222', '147852', 'genius', 'sergey', '7654321',
                         '232323', '123789', 'fktrcfylh', 'spartak', 'admin', 'test', '123', 'azerty', 'abc123',
                         'lol123', 'easytocrack1', 'hello', 'saravn', 'holysh!t', 'Test123', 'tundra_cool2', '456',
                         'dragon', 'thomas', 'killer', 'root', '1111', 'pass', 'master', 'aaaaaa', 'monkey', 'daniel',
                         'asdasd', 'changeme', 'computer', 'jessica', 'letmein', 'mirage', 'loulou', 'lol', 'superman',
                         'shadow', 'admin123', 'secret', 'administrator', 'sophie', 'kikugalanetroot', 'doudou',
                         'liverpool', 'hallo', 'sunshine', 'charlie', 'parola', '100827092', 'michael', 'andrew',
                         'password1', 'fuckyou', 'matrix', 'cjmasterinf', 'internet', 'hallo123', 'eminem', 'demo',
                         'gewinner', 'pokemon', 'abcd1234', 'guest', 'ngockhoa', 'martin', 'sandra', 'asdf', 'hejsan',
                         'george', 'qweqwe', 'lollipop', 'lovers', 'q1q1q1', 'tecktonik', 'naruto', '12', 'password12',
                         'password123', 'password1234', 'password12345', 'password123456', 'password1234567',
                         'password12345678', 'password123456789', '000000', 'maximius', '123abc', 'baseball1',
                         'football1', 'soccer', 'princess', 'slipknot', '11111', 'nokia', 'super', 'star', '666999',
                         '12341234', '1234321', '135790', '159951', '212121', 'zzzzzz', '121314', '134679', '142536',
                         '19921992', '753951', '7007', '1111114', '124578', '19951995', '258456', 'qwaszx', 'zaqwsx',
                         '55555', '77777', '54321', 'qwert', '22222', '33333', '99999', '88888', '66666']

    length = int()
    lower = int()
    upper = int()
    special = int()
    number = int()
    like_past = int()
    f_name = int()
    s_name = int()
    popular = int()
    password_strength = 0

    if len(password) >= 8:
        length = 1
    for i in lower_alphabet:
        if i in password:
            lower = 1
    for i in upper_alphabet:
        if i in password:
            upper = 1
    for i in special_characters:
        if i in password:
            special = 1
    for i in numbers:
        if i in password:
            number = 1

    # if len(password) >= 8:
    #     length = 1
    # if password.islower():
    #     lower = 1
    # if password.isupper():
    #     upper = 1
    # if password.isdigit():
    #     number = 1
    # for i in special_characters:
    #     if i in password:
    #         special = 1
    # for i in popular_passwords:
    #     if i not in password:
    #         popular = 1



    for i in popular_passwords:
        if i.lower() in password.lower():
            popular = -1
            break

    if name_f.lower() not in password.lower():
        f_name = 1
    if name_s.lower() not in password.lower():
        s_name = 1
    if pre_pass.lower() not in password.lower():
        like_past = 1

    if length == 1:
        password_strength += 1
    if lower == 1:
        password_strength += 1
    if upper == 1:
        password_strength += 1
    if special == 1:
        password_strength += 2
    if f_name != 1:
        password_strength -= 2
    if s_name != 1:
        password_strength -= 2
    if popular != 1:
        password_strength -= 3
    if like_past != 1:
        password_strength -= 1

    password_rank = str()

    if password_strength >= 5:
        password_rank = 'Very Strong'
    elif password_strength == 4:
        password_rank = 'Strong'
    elif password_strength == 3:
        password_rank = 'OK'
    elif password_strength == 2:
        password_rank = 'Not Good'
    elif password_strength == 1:
        password_rank = 'Bad'
    elif password_strength < 1:
        password_rank = 'Awfle'
    print('\nI think that your password is ', password_rank)
    issues = [length, lower, upper, special, number, like_past, f_name, s_name, popular, password_rank]
    return issues


if __name__ == '__main__':

    password = 'йцукен$4'
    pre_pass = 'Qweadfzxcv'
    name_f = 'Ivan'
    name_s = 'Ivanov'

    issues = get_password_strength(password, pre_pass, name_f, name_s)
    why = input('\nIf you would like to find out why type why? and press enter: ')
    if why.lower() == 'why?':
        if issues[0] != 1:
            print("It's too short")
        if issues[1] != 1:
            print("It doesn't have a lower case character in it")
        if issues[2] != 1:
            print("It doesn't have an upper case character in it")
        if issues[3] != 1:
            print("It doesn't have a special character in it")
        if issues[4] != 1:
            print("It doesn't have a number in it")
        if issues[5] != 1:
            print("It's like your old password")
        if issues[6] != 1:
            print("It's got your first name in it")
        if issues[7] != 1:
            print("It's got your last name in it")
        if issues[8] != 1:
            print('It has popular words')
        if issues[9] == 'Very Strong':
            print('There is nothing wrong with it!')
