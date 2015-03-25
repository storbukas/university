# NOTE: To slow algorithm

def hotell(floors):
    #floors = int(raw_input())
    floor_guests = []
    floor_guests.append(0)

    for i in range(floors):
        floor_guests.append(int(raw_input()))

    while (True):
        action = raw_input().split()
        if(action[0] == "S"):
            print("Slutt for i dag.")
            break
        elif(action[0] == "T"):
            total = 0
            for i in range(int(action[1]), 1+int(action[2])):
                total += floor_guests[i]
            gjest = " gjester"
            etasje = " som bor mellom etasje " + str(int(action[1])) + " og etasje " + str(int(action[2])) + "."
            if(total == 1): gjest = " gjest"
            if(int(action[1]) == int(action[2])):
                etasje = " som bor i etasje " + str(int(action[1])) + "."
            elif(int(action[1]) == 1 and int(action[2]) == floors):
                etasje = " som bor i hotellet."
            print("Det er " + str(total) + gjest + etasje)
        elif(action[0] == "U"):
            floor_guests[int(action[1])] -= int(action[2])
        elif(action[0] == "I"):
            floor_guests[int(action[1])] += int(action[2])
def main():
    while(True):
        floors = int(raw_input())
        if(floors > 0):
            hotell(floors)
        else:
            break

if __name__ == "__main__":
    main()
