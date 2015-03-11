#include <stdlib.h>
#include <stdio.h>
#include <omp.h> // remember to compile with -fopenmp
#include <time.h> // used for the generation of random numbers (seed)
#include <string.h>
#include <unistd.h>

// method declaration
void radix_sort(int n, int shift, int mask, int* data, int* dummy, int* prefix, int* bucket_size);
int sorted(int *data, int n);

/**
 * @author  Lars Erik Storbukås
 * @mail    lst111@student.uib.no
 * @date    06/03 - 2015
 * @course  INF236 Paralell Programming
 * @task    Assignment 1 - Task 3
 *
 **/
int main(int argcv, char *argv[]) { // command line arguments
	srand(time(NULL)); // give random a seed

	int i, n, bits;

	// check for correct amount of arguments
	if(argcv < 2) {
		exit(1);
	}
	else {
		// converts to integer values
		n = atoi(argv[1]);
		bits = atoi(argv[2]);
	}

	// find mask based on nr of bits (by bitshifting)
	int mask = (1 << bits) - 1;
	int nr_of_buckets = mask + 1;
	
	// maximum number of threads
	int max_threads = omp_get_max_threads();

	// create array to contain data
	int* data = malloc(n * sizeof(int));
	int* dummy = malloc(n * sizeof(int));
	
	// create pointer to pointers to hold thread prefix
	int** thread_prefix = malloc(max_threads * sizeof(int*));
	int** thread_bucket_size = malloc(max_threads * sizeof(int*));
	
	// assign size based on nr_of_buckets
	for(i = 0; i < max_threads; i++) {
		thread_prefix[i] = malloc(nr_of_buckets * sizeof(int)); // create 'nr_of_buckets' thread_prefix'es
		thread_bucket_size[i] = malloc(nr_of_buckets * sizeof(int));
	}
	
	// keep track of prefixes for total bucket-count after threads has sorted
	int *bucket_count = malloc(nr_of_buckets * sizeof(int));
	
	// read random values to data
	for(i = 0; i < n; i++) {
		data[i] = rand();
	}
	
	// get start time
	double time = omp_get_wtime();
	
	// run trough all the bit values and sort according to that bit value
	int current_bit;
	for(current_bit = 0; current_bit < 32; current_bit += bits) {
		// parallelize each chunk of data based on nr of threads
		#pragma omp parallel for
		for(i = 0; i < max_threads; i++) {
			int start_thread = (n/max_threads)*i;
			int end_thread = (n/max_threads)*(i+1);
			
			// last thread
			if(i == max_threads-1)
				end_thread = n;
			
			// send chunks of code to radix sort  to be sorted
			radix_sort(end_thread-start_thread, current_bit, mask, &data[start_thread], &dummy[start_thread], thread_prefix[i], thread_bucket_size[i]);
		}

		int j;
		memset(bucket_count, 0, sizeof(int) * nr_of_buckets); // reset memory with 0's
		
		// calculate bucket size after parallized radix sort
		// private(j) because j defined outside pragma
		#pragma omp parallel for private(j)
		for (i = 1; i < nr_of_buckets; i++) 
			for (j = 0; j < max_threads; j++)
				bucket_count[i] += thread_bucket_size[j][i-1];
		
		// calculate prefix based on size of buckets
		// must be done sequentially
		for (i = 1; i < nr_of_buckets; i++)
			bucket_count[i] += bucket_count[i-1];

		// merge the buckets that is located in each of the threads locale buckets
		// private(j) because j defined outside pragma
		#pragma omp parallel for private(j)
		for (i = 0; i < nr_of_buckets; i++){
			int dataindex = 0; // used for keeping track of storage location
			for (j = 0; j < max_threads; j++) {
				// calculate values used for copying bucket content at correct location
				int start_thread = (n/max_threads)*j;
				int length = thread_bucket_size[j][i];
				int bucket_start = thread_prefix[j][i] - length;
				
				// copy sorted content from dummy back to data
				memcpy(&data[bucket_count[i] + dataindex], &dummy[start_thread+bucket_start], length * sizeof(int));			
				dataindex += thread_bucket_size[j][i]; // update prefix
			}
		}
	}
	
	// calculate end time
	time = omp_get_wtime() - time;	

	// check if sorted
	printf("%s%f\n", "finished in: ", time);
	if(sorted(data, n) == 1) printf("data is sorted\n");
	else printf("not sorted\n");

	return 0;
}

// radix sort
void radix_sort(int n, int shift, int mask, int* data, int* dummy, int* prefix, int* bucket_size) {
	int i, bucket, nr_of_buckets;
	
	nr_of_buckets = mask + 1;

	prefix[0] = 0; // first prefix
	memset(bucket_size, 0, sizeof(int) * nr_of_buckets); // reset memory with 0's
	
	// count size of buckets
	for(i=0; i<n; i++) {
		bucket = ((data[i]>>shift) & mask);
		bucket_size[bucket]++;
	}
	
	// update prefix
	for(i=1; i<nr_of_buckets; i++) {
		prefix[i] = prefix[i-1] + bucket_size[i-1];
	}
	
	// assign values
	for(i=0; i<n; i++) {
		bucket = (data[i]>>shift) & mask;
		dummy[prefix[bucket]++] = data[i];
	}
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
