def adjacent(x,y,data):
    neighbours = []
    breakpoint = False

    if(valid(x+1,y,data)):
        if(data[x+1][y] == "." or data[x+1][y] == "#"):
            neighbours.append((x+1,y))
        elif(data[x+1][y] == "T"):
            breakpoint = True

    if(valid(x-1,y,data)):
        if(data[x-1][y] == "." or data[x-1][y] == "G"):
            neighbours.append((x-1,y))
        elif(data[x-1][y] == "T"):
            breakpoint = True

    if(valid(x,y+1,data)):
        if(data[x][y+1] == "." or data[x][y+1] == "#"):
            neighbours.append((x,y+1))
        elif(data[x][y+1] == "T"):
            breakpoint = True

    if(valid(x,y-1,data)):
        if(data[x][y-1] == "." or data[x][y-1] == "#"):
            neighbours.append((x,y-1))
        elif(data[x][y-1] == "T"):
            breakpoint = True


    if(breakpoint):
        neighbours = []

    return neighbours


def valid(x,y,data):
    #print("valid " + str(x) + "," + str(y) + ": " + str(data[x][y]))
    return ((x >= 0 and x < len(data)) and (y >= 0 and y < len(data[x])))
    #return ((y >= 0 and y < len(data)) and (x >= 0 and x < len(data[y])))

def dfs(x,y,data,stack):
    counter = 0

    cur_list = []
    cur_list = adjacent(x,y,data)

    for i in temp_list:
        stack.add(i)

    while(not stack==set()):
        element = stack.pop()

        if(data[element[0]][element[1]] == "G"):
            counter += 1

        data[element[0]][element[1]] = "D"
        temp_list = []
        temp_list = adjacent(element[0],element[1],data)

        for i in temp_list:
            stack.add(i)

def main():
    dimensions = map(int, raw_input().split())
    data = list(range(dimensions[1]))
    counter = 0

    for i in range(dimensions[1]):
        data[i] = list(raw_input())


    liste = {}
    stack = set()

    for x in range(len(data)):
        for y in range(len(data[x])):
            if(data[x][y]=="P"):
                print(data[x][y])
                data[x][y]="D"

                #liste[(x,y)]=adjacent(x,y,data)

                #for i in liste:
                #    stack.add(i)

                counter = dfs(x,y,data,stack)

    print(counter)

if __name__ == "__main__":
    main()
