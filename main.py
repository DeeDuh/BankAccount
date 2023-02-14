import sys
sys.path.append(r"/home/sasha/PycharmProjects/pythonProject/venv/")
from bankaccount import BankAccount

def main():
  while True:
    #Получить начальный остаток
    start_bal = float(input('Введите свой начальный остаток: '))
    #Создать объект BankAccount
    savings = BankAccount(start_bal)
    #Внести на счет зп пользователя:
    pay = float(input('Сколько вы получили на этой неделе? '))
    savings.deposit(pay)
    print(('Вношу эту сумму на ваш счет.'))
    # Показать остаток:
    print(f'Ваш остаток составляет: ${savings.get_balance():,.2f}.')
    #Получить сумму для снятия с банковского счета:
    cash = float(input('Какую сумму вы желаете снять со счета? '))
    savings.withdraw(cash)
    print('Снимаю эту сумму с Вашего банковского счета.')
    # Показать остаток:
    print(f'Ваш остаток на счете составляет: ${savings.get_balance():,.2f}.')
    esc = int(input('Продолжить работу? Если нет, нажимаем 0, если да, то другие цифры: '))
    print(esc)
    if esc == 0:
     print('До свидания! Наша встреча была ошибкой, пайтон!!!!!!!!')
     break

if __name__ == '__main__':
   main()
