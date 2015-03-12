def getKey(data):
    # sorts by the show ending, by adding first and second element
    return (data[0] + data[1])

def main():
    testcases = int(raw_input())
    for _ in range(testcases):
            nr_of_shows = int(raw_input())
            data = []

            # read in values for nr_of_shows, and append to data
            for _ in range(nr_of_shows):
                data.append(raw_input().split())

            # used to convert every value in data from string to int
            for i in range(len(data)):
                data[i][0] = int(data[i][0])
                data[i][1] = int(data[i][1])
                data[i][2] = int(data[i][2])

            # sort by our own sort method getKey()
            data = sorted(data, key=getKey)

            # length of knap-array based on last element of data's end time
            length = data[len(data)-1][0] + data[len(data)-1][1]

            knap = [0] * (length + 1) # creates an array with 0's

            # go through all the shows ( in data[] )
            for i in range(len(data)):
                show = data[i]          # current show
                start = show[0]         # start of show
                points = show[2]        # nr of points
                end = start + show[1]   # end of show

                # find next shows ending, if not (exception),
                # set equal to the len of the knap-array
                next_end = 0

                try:
                    next_end = data[i+1][0] + data[i+1][1] # set equal end of next show
                except IndexError:
                    next_end = len(knap)-2 # len of knap - 2 spots because for loop ( next_end + 1 )

                # calculate the value
                val = max(knap[start] + points, knap[end]) # don't update if knap[start] + points < knap[end]
                knap[end] = val

                # set 'val' up until next shows ending
                for j in range(end, next_end+1): # needs + 1 because to get range 'end to and with next_end'
                    knap[j] = val


            # print result located in end of knap-array
            print(knap[len(knap)-1])

if __name__=="__main__":
    main()
