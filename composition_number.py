def content(num):
    "определяет сколько в целом числе различных цифр и выводит на экран"
    a = dict()
    while num != 0:
        a[num % 10] = a.get(num % 10,0) + 1
        num //= 10
    for k, v in sorted(a.items()):
        print(k," - ",v)
    
n=int(input('Введите целое число большой разрядности'))
content(n)

