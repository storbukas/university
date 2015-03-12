def main():
    nr_of_inputs = int(raw_input())
    f = []

    for i in range(nr_of_inputs):
        f.append(raw_input().split())

    for i in range(len(f)):
        f[i][0] = int(f[i][0])
        f[i][1] = int(f[i][1])


    upper_limit = 0
    lower_limit = 100000

    optimise = 0

    for i in range(len(f)):
        if(f[i][1] < lower_limit):
            lower_limit = f[i][1]
        upper_limit += f[i][1]

    upper_limit /= len(f)

    optimise = (lower_limit + upper_limit) / 2
    prev_opt = 0

    outer_counter = 0
    current_fish = 0
    next_fish = 0

    while(True):
        current_fish = f[0][1]
        next_fish = f[1][1]

        for position in range(len(f)-1):
            next_fish = f[position+1][1]

            if(current_fish > optimise):
                resources = current_fish - optimise
                leftover = resources - (f[position+1][0] - f[position][0])
                if(leftover > 0):
                    next_fish += leftover
            elif(current_fish < optimise):
                resources = optimise - current_fish
                distance = f[position+1][0] - f[position][0]
                next_fish -= (resources + distance)

            current_fish = next_fish

        if(prev_opt == optimise):
            break
        elif(optimise == current_fish):
            break

        outer_counter += 1
        prev_opt = optimise

        if(current_fish > optimise):
            lower_limit = optimise + 1
        elif(current_fish < optimise):
            upper_limit = optimise - 1

        optimise = (lower_limit + upper_limit) / 2

    print(optimise)

if __name__=="__main__":
    main()
