def main():
    testcases = int(raw_input())

    for _ in range(testcases):
        coord()

def coord():
    coord = raw_input().split()

    for i in range(len(coord)):
        coord[i] = float(coord[i])

    # A starts 0, B starts 2, C starts 4
    first_part = [(coord[2]-coord[0]),(coord[3]-coord[1])]
    second_part = [(coord[4]-coord[0]), (coord[5]-coord[1])]
    complete = (first_part[0] * second_part[1]) - (first_part[1] * second_part[0])

    output = abs(0.5 * complete)

    print("{0:.3f}".format(output))

if __name__ == "__main__":
    main()
