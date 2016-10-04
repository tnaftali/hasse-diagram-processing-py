def get_data():
    data = []
    lines = loadStrings("data.txt")
    last = lines.pop(-1)
    for line in lines:
        data.append(add_line(line))
    last_node = []
    last_node.append(int(last.split(';')[0]))
    last_node.append([])
    data.append(last_node) 
    return data
            

def add_line(line):
    result = []
    arr = []
    result.append(int(line.split(';')[0]))
    subnodes = (line.split(';')[1]).split(',')
    for subnode in subnodes:
        subnode = int(subnode)
        arr.append(subnode)
    result.append(arr)
    return result