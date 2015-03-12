import math

class Point:
	def __init__(self, x, y):
        	self.x = x
		self.y = y

	def __str__(self):
		return ("point: " + str(x) + ", " + str(y))

def distance(p1, p2):
	distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
	return distance

def intersections(p1, p2, bombs, radius):
	distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
	diameter = radius*2 # radius must me declared

	if (distance > diameter):
		return
	else:
		a = (distance)/(2)
		h = math.sqrt(radius*radius - a*a)


		x2 = p1.x + a * (p2.x - p1.x)/distance
		y2 = p1.y + a * (p2.y - p1.y)/distance

		p3 = Point(x2+h*(p2.y - p1.y)/distance, y2 - h * (p2.x - p1.x)/ distance )
		p4 = Point(x2-h*(p2.x - p1.x)/distance, y2 + h * (p2.x - p1.x)/ distance )

		# how to fix this
		bombs.append(p3)
		bombs.append(p4)

def results(bombs, ladies, radius):
	current = 0
	results = 0
	for p in bombs:
		for i in range(len(ladies)):
			if (distance(p, ladies[i]) <= radius):
				current += 1

		if (current > results):
			results = current

		current = 0

	return results

def activist():
    input = raw_input().split()
    nr_of_ladies = int(input[0])
    radius = float(input[1])

    if(nr_of_ladies == 0 and radius == 0.0): return -1

    # array to keep ladies locations
    ladies = []
    bombs = []

    # read in ladies coordinates
    for i in range(nr_of_ladies):
        (x,y) = raw_input().split()
        ladies.append(Point(float(x), float(y)))

    # iterate ladies
    for i in ladies:
	for j in ladies:
        	if(not i is j):
	        	intersections(i,j, bombs, radius)

    return results(bombs, ladies, radius)

def main():
	max_val = 0
	while(True):
		val = activist()
		if(val > max_val): max_val = val
		elif(val < 0.0): break

	print(max_val)

if __name__=="__main__":
	main()
