def srednia(*data, **kwargs):
    """
    Po napisaniu ta funkcja ma działać tak :

   .. code-block:: python

       srednia(1,2,3,5)
       srednia([1,2,3,5])
       srednia([(1,2), (3,5), (3,4)], column=1)

    :param data: liczby, lista liczb lub lista 2D
    :param kwargs:
      - column : podaje nr kolumny danych
      - start: numer pierwszej obserwacji od 0
      - stop: numer ostatniej obserwacji (do N-1 włącznie)

    :return:
    """
    data_copy = []
    col = kwargs.get("column", 0)
    if isinstance(data[0], list) or isinstance(data[0], tuple):
        if isinstance(data[0][0], list) or isinstance(data[0][0], tuple):   #args = [(1,1),(2,3)] lub args = [[1,1],[2,3]]
            # print("argumentem jest lista2D:",data)
            for d in data:
                data_copy.append(d[0][col])
        else:                                                               #args = [1,2,3,4] lub args = (1,2,3,4)
            # print("argumentem jest lista1D:", data)
            data_copy = data[0]
    else:                                                                   # args = 1,2,3,4,5
        # print("argumentem są warości:", data)
        data_copy = data
    # --- tu liczymy srednią z listy "data_copy"

    suma = 0.0
    for d in data_copy: suma += d

    return suma/len(data_copy)


if __name__ == "__main__":
    print(srednia(1.1,1.34,1.21,1.0,-1))
    print(srednia([1,2,3,4]))
    print(srednia([1,2,3,4]))
    print(srednia([(1,2), (3,5), (3,4.4)], column=1))
    print(srednia(((1,2), (3.5,5.1), (3,4)), column=1))
    print(srednia([[1.5,2], [3,5], [3,4]], column=0))
