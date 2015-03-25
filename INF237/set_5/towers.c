#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

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
        int first_input;
        int second_input;
        
        scanf("%c%d%d", &command, &first_input, &second_input);
        
        // not finished
        switch(command) {
            case 'I':
                break;
            case 'U':
                break;
            case 'T':
                break;

            default:
                printf("%s", FINISHED);
        }
    }
}
