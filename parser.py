from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file(fname, points, transform, screen, color):
    file = open(fname)
    lines = file.readlines()
    for i in range(len(lines)):
		if lines[i] == "line\n":
			coordinates = lines[i+1].split(" ")
			add_edge(points, int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3]), int(coordinates[4]), int(coordinates[5]))
		elif lines[i] == "ident\n":
			ident(transform)
		elif lines[i] == "scale\n":
			nums = lines[i+1].split(" ")
			scaler = make_scale(float(nums[0]), float(nums[1]), float(nums[2]))
			matrix_mult(scaler, transform)
		elif lines[i] == "move\n":
			nums = lines[i+1].split(" ")
			trans = make_translate(int(nums[0]), int(nums[1]), int(nums[2]))
			matrix_mult(trans, transform)
		elif lines[i] == "rotate\n":
			commands = lines[i+1].split(" ")
			if commands[0] == "x":
				rot = make_rotX(int(commands[1]))
			if commands[0] == "y":
				rot = make_rotY(int(commands[1]))
			if commands[0] == "z":
				rot = make_rotZ(int(commands[1]))
			matrix_mult(rot, transform)
		elif lines[i] == "apply\n":
			matrix_mult(transform, points)
		elif lines[i] == "display\n":
			for i in range(len(points)):
				for j in range(len(points[0])):
					points[i][j] = int(points[i][j])
			clear_screen(screen)
			draw_lines(points, screen, color)
			display(screen)
		elif lines[i] == "save\n":
			save_extension(screen, lines[i+1].strip())
		elif lines[i] == "quit\n":
			break
