#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// string definition
#define GUESTS " gjester"
#define GUEST " gjest"
#define MULTIPLE_FLOORS_1 " som bor mellom etasje "
#define MULTIPLE_FLOORS_2 " og etasje "
#define FLOOR " som bor i etasje "
#define ALL_FLOORS " som bor i hotellet."
#define FINISHED "Slutt for i dag."

// method declaration
void hotel_manager(int nr_of_floors);

/**
 * @author  Lars Erik Storbukås
 * @mail    lst111@student.uib.no
 * @date    25/03 - 2015
 * @course  INF237 Algorithm Engineering
 * @task    Towers - Set 5
 * 
 **/

// NOTE: Not finished yet

int main() {
    while (1) {
        int nr_of_floors = 0;
        scanf("%d", &nr_of_floors);

        if(nr_of_floors != 0) {
            hotel_manager(nr_of_floors);
        }
        else {
            break;
        }
    }
    return 0;
}

void hotel_manager(int nr_of_floors) {
    int floors[2 * nr_of_floors]; // double size to create counting tree (fenwick tree)

    // read data to array
    int i = nr_of_floors;
    for(; i < 2 * nr_of_floors; i++) {
        scanf("%d", &floors[i]);
    }

    // sum up according to counting tree structure
    for(i = nr_of_floors - 1; i > 0; i--) {
        floors[i] = floors[2 * i] + floors[(2 * i) + 1];
    }

    bool keep_going = true;
    while(keep_going) {
        char command;
        int a;
        int b;
        
        scanf("%c%d%d", &command, &a, &b);

        // not finished
        if(command == 'I') {
            floors[nr_of_floors + a - 1] += b;
            for(i = (nr_of_floors + a - 1) / 2; i > 0; i = (i / 2))
                floors[i] += b;
        }

        else if(command == 'U') {
            floors[nr_of_floors + a] -= b;
            for(i = (nr_of_floors + a) / 2; i > 0; i = (i / 2)) 
                floors[i] -= b;
        }

        else if(command == 'T') {
            int total = 0;
            
            int start = a + nr_of_floors - 1;
            int end = b + nr_of_floors;
            total = floors[start];

            while(start / 2 != end / 2) {
                if(start % 2 == 0)
                    total += floors[start+1];
                if(end % 2 == 1)
                    total += floors[end-1];

                start /= 2;
                end /= 2;
            }

            char* guest;
            guest = (total == 1) ? " gjest" : " gjester";
            
            // one floor or whole hotel
            if(a == 1 && b == nr_of_floors) printf("%s%d%s%s\n", "Det er ", total, guest, " som bor i hotellet.");
            else if(a == b) printf("%s%d%s%s%d%s\n", "Det er ", total, guest, " som bor i etasje ", b, ".");
            // multiple floors
            else printf("%s%d%s%s%d%s%d%s\n", "Det er ", total, guest, " som bor mellom etasje ", a, " og etasje ", b, ".");
        }
        else if(command == 'S') { // command == S
            printf("Slutt for i dag.");
            keep_going = false;
        }
    }
}
