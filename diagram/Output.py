# from graphviz import Digraph


def save_diagram(array, matrix):
    file = open('data.txt', 'w')
    # dot = Digraph(comment='Hasse Diagram for divisibility relation of ' + str(number))
    for i in range(len(array)):
        # dot.node(str(array[i]), str(array[i]))
        line = str(int(array[i])) + ';'
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                # dot.edge(str(array[i]), str(array[j]))
                if i + 1 < len(array) and array[j] != array[i]:
                    line += str(int(array[j]))
                    if j + 1 < len(matrix[i]):
                        line += ','
        file.write(line)
        file.write('\n')
    file.close()
    # print(dot.source)


def print_matrix(matrix):
    print("------------")
    for i in range(len(matrix)):
        print(matrix[i])
    print("------------")
