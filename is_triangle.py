def is_triangle(side_one, side_two, side_three):
	a = side_one + side_two <= side_three
	b = side_two + side_three <= side_one
	c = side_one + side_three <= side_two
	if a | b | c:
		print "No"
	else:
		print "Yes"
		
is_triangle(3, 4, 5)

is_triangle(1, 1, 12)


def is_triangle2(side_one, side_two, side_three):
	sides = [side_one, side_two, side_three]
	sides.sort()
	a = (sides[0] + sides[1] <= sides[2])
	if a:
		print "No"
	else: 
		print "Yes"

is_triangle2(3, 4, 5)

is_triangle2(1, 1, 12)


def triangle_prompt():
	side_one = int(raw_input("How long is side one? > "))
	side_two = int(raw_input("How long is side two? > "))
	side_three = int(raw_input("How long is side three? > "))
	is_triangle(side_one, side_two, side_three)
	
triangle_prompt()

triangle_prompt()