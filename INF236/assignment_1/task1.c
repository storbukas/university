#include <stdlib.h>
#include <stdio.h>
#include <omp.h> // remember to compile with -fopenmp
#include <time.h> // used for the generation of random numbers (seed)
#include <string.h>
#include <unistd.h>

// method declaration
void radix_sort(int* data, int n, int b);
int sorted(int *data, int n);

/**
 * @author  Lars Erik Storbukås
 * @mail    lst111@student.uib.no
 * @date    06/03 - 2015
 * @course  INF236 Paralell Programming
 * @task    Assignment 1 - Task 1
 *
 **/
int main() {
    srand(time(NULL)); // give random a seed
    
    int b = 0; // nr of bits to represent one digi
    int n = 0; // nr of elements to be sorted/read in
    int i = 0; // index counter
    
	// get n from user
    printf("%s", "Number of elements to be sorted: ");
    scanf("%d", &n);
	
	// get b from user
    printf("%s", "Number of bits to be evaluated as one digit: ");
    scanf("%d", &b);

    // read values into data-array
    int *data = (int *) malloc(n * sizeof(int));
    
    for(i = 0; i < n; i++) {
        data[i] = (int)rand();
        //scanf("%d", &data[i]); // used for debugging, let user plot own values
    }
    
    // radix sort data-array
    radix_sort(data, n, b);
  	
	// check if sorted
    if(sorted(data, n) == 1) { // sorted
        printf("data is sorted\n");
    }
    
	// free up memory
    free(data);
    return 0;
}

// radix sort
void radix_sort(int* data, int n, int b) {
    int i, bit, nr_of_buckets, shift=0;
    nr_of_buckets = 1 << b; // equal to mask + 1

    int bucket[nr_of_buckets];
    int *dummy = (int*) malloc(n * sizeof(int)); // dummy array used for changing locations
    
    // used for time taking with pragma omp (openmp)
    double time = omp_get_wtime();

	// run through all bits (in b increments)
    for(bit = 0; bit < 32; bit += b) {
        memset(bucket, 0, nr_of_buckets * sizeof(int)); // reset memory with 0's
	    
		// count bucket sizes
        for(i = 0; i < n; i++) {
         	bucket[(data[i] >> bit) & (nr_of_buckets-1)] += 1;
        }
	
		// prefix sum
		int current_bucket = 0;
	    int next_bucket = 0;
	    for(i = 0; i < nr_of_buckets; i++) {
         	next_bucket += bucket[i];
          	bucket[i] = current_bucket;
		    current_bucket = next_bucket;
        }
	    
		// allocate values in correct buckets and update
        for(i = 0; i < n; i++) {
         	shift = (data[i] >> bit) & (nr_of_buckets-1);
          	dummy[bucket[shift]++] = data[i];
        }
	
		// copy back to data array
        for(i = 0; i < n; i++) {
            data[i] = dummy[i];
        }
    }

	// calculate time
    time = omp_get_wtime() - time;

	// print time used on radix sort
    printf("%f\n", time);
	
	// free up memory
    free(dummy);
}

// method for checking if an array is sorted
int sorted(int *data, int n) {
	int i = 1;
	for(i = 1; i < n; i++) {
		if(data[i] < data[i-1]) { // is element befor larger than this?
			return 0; // array is not sorted
		}
	}
	return 1; // array is sorted
}
