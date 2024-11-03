def disclosure_list(lists: list) -> list:
    """Раскрывает многомерный список любой вложенности.
    
    :param lists: arg
    :type lists: list
    
    :rtype: list
    :return: lists
    """
    for index, elem in enumerate(lists):

        if isinstance(elem, (list, tuple)):
            lists[index: index + 1] = elem[:]
            disclosure_list(lists)

    return lists


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print('Ответ:', disclosure_list(nice_list))
