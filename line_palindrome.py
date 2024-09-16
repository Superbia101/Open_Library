def palindrome(lines):
    "Проверяет строку является ли она палиндромом"
    text, temp = '', 0
    for j in lines.lower().split(): # убираем лишнее
        text += j.strip(".,:;-!?")
    for i in range(len(text) // 2): # подсчёт одинаковых значений с начала и конца
        temp += 1 if text[i] == text[len(text) - 1 - i] else 0
    print('Да, это палиндром!') if temp == len(text) // 2 else print('Нет, это не палиндром!')

#t = input('Введите строку: ')
#t = 'казак'
t = ' Я не стар, брат Сеня!'
print(t)
palindrome(t)
