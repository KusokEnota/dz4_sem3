"""Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список."""

def actionx(action, count_plus):
    if action % 50 != 0:
        return -1

    conditions = [
        (count_plus % 3 == 0, action * 0.03),
        (action >= 5_000_000, action * 0.1)
    ]

    for condition, deduction in conditions:
        if condition:
            action -= deduction

    return action


def withdrawal(action, count_minus, balance):
    if action % 50 != 0:
        return -1

    min_commission = max(30, action * 0.015)
    max_commission = action * 0.1 if action >= 5_000_000 else 600

    commission = min(max_commission, max(min_commission, action * 0.015))
    total_amount = action + commission

    if count_minus % 3 == 0:
        total_amount += action * 0.03

    if balance >= total_amount:
        balance -= total_amount

    return balance


def handle_deposit(count_plus, balance):
    action_amount_input = input('Введите сумму пополнения (кратно 50 у.е.): ')
    if action_amount_input.isdigit():
        action = actionx(float(action_amount_input), count_plus)
        if action == -1:
            print('Сумма должна быть кратна 50 у.е.!')
        else:
            balance += action
            history_use.append(('Пополнение', action))
    else:
        print('Некорректный ввод. Введите число.')


def handle_withdrawal(count_minus, balance):
    action_amount_input = input('Введите сумму снятия (кратно 50 у.е.): ')
    if action_amount_input.isdigit():
        action = withdrawal(float(action_amount_input), count_minus, balance)
        if action == -1:
            print('Сумма должна быть кратна 50 у.е.!')
        else:
            history_use.append(('Снятие', balance - action))
            balance = action
    else:
        print('Некорректный ввод. Введите число.')


use = 0
balance = 0
count_plus = 0
count_minus = 0
history_use = []

while True:
    action_input = input('\nВыберите действие:\n1. Пополнить\n2. Снять\n3. Выйти\n4. История\n')

    if action_input == '1':
        count_plus += 1
        action_amount_input = input('Введите сумму пополнения (кратно 50 у.е.): ')
        if action_amount_input.isdigit():
            action = actionx(float(action_amount_input), count_plus)
            if action == -1:
                print('Сумма должна быть кратна 50 у.е.!')
            else:
                balance += action
                history_use.append(('Пополнение', action))
        else:
            print('Некорректный ввод. Введите число.')
            continue

        print(f'Ваш баланс: {balance} у.е.')

    elif action_input == '2':
        count_minus += 1
        print(f'Ваш баланс: {balance} у.е.')
        action_amount_input = input('Введите сумму снятия (кратно 50 у.е.): ')
        if action_amount_input.isdigit():
            action = withdrawal(float(action_amount_input), count_minus, balance)
            if action == -1:
                print('Сумма должна быть кратна 50 у.е.!')
            else:
                history_use.append(('Снятие', balance - action))
                balance = action
        else:
            print('Некорректный ввод. Введите число.')
            continue

        print(f'Ваш баланс: {balance} у.е.')

    elif action_input == '3':
        break

    elif action_input == '4':
        print('История операций:')
        for operation, amount in history_use:
            print(f'{operation}: {amount} у.е.')

