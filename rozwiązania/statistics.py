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
    if isinstance(data[0], list) or isinstance(data[0], tuple):
        if isinstance(data[0][0], list) or isinstance(data[0][0], tuple):   #args = [(1,1),(2,3)] lub args = [[1,1],[2,3]]
            print("argumentem jest lista2D:",data)
        else:                                                               #args = [1,2,3,4] lub args = (1,2,3,4)
            print("argumentem jest lista1D:", data)
            data_copy = data[0]
    else:                                                                   # args = 1,2,3,4,5
        print("argumentem są warości:", data)
        data_copy = data
    # --- tu liczymy srednią z listy "data_copy"

    return 0


if __name__ == "__main__":
    print(srednia(1.1,1.34,1.21,1.0,-1))
    print(srednia([1,2,3,4]))
    print(srednia([1,2,3,4]))
    print(srednia([(1,2), (3,5), (3,4)], column=1))
    print(srednia(((1,2), (3,5), (3,4)), column=1))
    print(srednia([[1,2], [3,5], [3,4]], column=1))
