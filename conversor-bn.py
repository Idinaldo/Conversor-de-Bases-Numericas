while True:
    print('-' * 50)
    print('Conversor de Bases Numéricas'.center(50))
    print('-' * 50)
    num = str(input('Digite um número: \033[33m'))

    # tratando possíveis erros
    if num.count('-') == 1:
        if num.replace('-', '').isnumeric():
            print('\033[31mERRO! \033[33mNúmeros negativos não são permitidos.\033[m')
            continue

    if not num.isnumeric():
        print('\033[31mERRO! \033[33mPor favor, digite apenas números.\033[m')

    elif num.isnumeric():
        num = int(num)
        print('\033[m-' * 50)
        print('\033[33mEscolha uma das bases númericas abaixo: \n'
              '[1] Hexadecimal \n'
              '[2] Binário \n'
              '[3] Octal\033[m')
        print('-' * 50)

        while True:
            choice = str(input('Digite sua escolha: \033[33m'))
            print('\033[m-' * 50)
            # tratando possíveis erros
            if choice.count('-') >= 1:
                choice = choice.replace('-', '')
                if choice.isnumeric():
                    print('\033[31mEscolha inválida! \033[33mPor favor, digite apenas números de 1 a 3.\033[m')
                    print('-' * 50)
                    continue

            if not choice.isnumeric():
                print('\033[31mERRO! \033[33mPor favor, digite apenas números.\033[m')

            if choice.isnumeric():
                choice = int(choice)

            # tratando erros
            if choice < 1 or choice > 3:
                print('\033[31mEscolha inválida! \033[33mPor favor, digite apenas números de 1 a 3.\033[m')
                print('-' * 50)
            else:
                break

        if choice == 1:
            print(f'\033[33m{num} representado em Hexadecimal é {hex(num)}\033[m')
            print('-' * 50)
            while True:
                follow = str(input('Deseja continuar? [S/N] ')).strip().upper()
                if follow in 'SN':
                    break
                print('\033[31mERRO! \033[33mPor favor, digite apenas S ou N.\033[m')
            if follow in 'N':
                break

        if choice == 2:
            print(f'\033[33m{num} representado em Binário é {bin(num)}\033[m')
            print('-' * 50)
            while True:
                follow = str(input('Deseja continuar? [S/N] ')).strip().upper()
                if follow in 'SN':
                    break
                print('\033[31mERRO! \033[33mPor favor, digite apenas S ou N.\033[m')
            if follow in 'N':
                break

        if choice == 3:
            print(f'\033[33m{num} representado em Octal é {oct(num)}\033[m')
            print('-' * 50)
            while True:
                follow = str(input('Deseja continuar? [S/N] ')).strip().upper()
                if follow in 'SN':
                    break
                print('\033[31mERRO! \033[33mPor favor, digite apenas S ou N.\033[m')
            if follow in 'N':
                break

# código feito por Idinaldo
