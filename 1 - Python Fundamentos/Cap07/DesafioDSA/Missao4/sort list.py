def sort(data):
    if len(data) <= 1:
        return data

    if not data:
        raise Exception("data nao pode ser None")

    lst_ordenada = []
    for index, num_entrada in enumerate(data):
        if index == 0:
            lst_ordenada.append(num_entrada)
        else:
            for index_atual, num_atual in enumerate(lst_ordenada):
                if num_entrada <= num_atual:
                    lst_ordenada.insert(index_atual, num_entrada)
                    break
                if num_entrada >= max(lst_ordenada):
                    lst_ordenada.append(num_entrada)
                    break
    return lst_ordenada

if __name__ == "__main__":
    data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
    print(sort(data))
    print(sorted(data))
