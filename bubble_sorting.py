def bubble_sorting(list_x: list[int | float]) -> list[int | float]:
    """Сортировка методом пузырька в порядке возрастания."""
    for _ in range((len(list_x)+1) // 2):
        for index in range(1, len(list_x)):
            if list_x[index - 1] > list_x[index]:
                list_x[index], list_x[index - 1] = list_x[index - 1], list_x[index]
    return list_x




list_num: list[int] = [5, 2, 8, 1, 0, 4, 5, 7, 2, 3, 9, 6, 0]
print(bubble_sorting(list_num))
