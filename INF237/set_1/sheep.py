def adjacent(x,y,data):
    neighbours = []

    if(valid(x+1,y,data) and data[x+1][y] == "#"):
        neighbours.append((x+1,y))

    if(valid(x-1,y,data) and data[x-1][y] == "#"):
                neighbours.append((x-1,y))

    if(valid(x,y+1,data) and data[x][y+1] == "#"):
                neighbours.append((x,y+1))

    if(valid(x,y-1,data) and data[x][y-1] == "#"):
                neighbours.append((x,y-1))

    return neighbours


def valid(x,y,data):
    return ((x >= 0 and x < len(data)) and (y >= 0 and y < len(data[x])))

def dfs(data,stack):
    while(not stack==set()):
        element = stack.pop()
        data[element[0]][element[1]] = "."
        for i in adjacent(element[0],element[1],data):
            stack.add(i)



def sheep():
    dimensions = map(int, raw_input().split())
    data = list(range(dimensions[0]))
    counter = 0

    for i in range(len(data)):
        data[i] = list(raw_input())

    liste = {}
    stack = set()

    for x in range(len(data)):
        for y in range(len(data[x])):
            if(data[x][y]=="#"):
                data[x][y]="."

                liste[(x,y)]=adjacent(x,y,data)

                for i in liste:
                    stack.add(i)

                counter += 1

                if(len(liste[(x,y)]) == 0):
                    continue
                else:
                    dfs(data,stack)

    #print(counter)
    return counter

def main():
    testcases = int(raw_input())
    liste = []
    for i in range(testcases):
        liste.append(sheep())

    for i in liste:
        print(i)

if __name__ == "__main__":
    main()
