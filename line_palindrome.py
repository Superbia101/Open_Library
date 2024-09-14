def palindrome(lines):
    "Проверяет строку является ли она палиндромом"
    text, temp = '', 0
    for j in lines.lower().split():
        text += j.strip(".,:;-!?")
    for i in range(len(text)):
        temp += 1 if text[i] == text[len(text) - 1 - i] else 0
        if temp == len(text) // 2:
            print('Палиндром!')
            break
    else:
        print('Не палиндром!')

#t = input('Введите строку: ')
#t = 'казак'
t = ' Я не стар, брат Сеня!'
print(t)
palindrome(t)
