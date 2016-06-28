####################################################################
# Type: SCRIPT                                                     #
#                                                                  #
# Description: [description]                                       #
####################################################################

# IMPORTS:
import sys
from volitant.volitant import *
# :IMPORTS

# CLASSES:
# :CLASSES

# VARIABLES:
# :VARIABLES

# FUNCTIONS:
def main():
	in_file = sys.argv[1]
	v = sys.argv[2]
	out_file = in_file
	if len(sys.argv) > 3:
		out_file = sys.argv[3]
	if len(sys.argv) > 4:
		tag = sys.argv[4]
	else:
		tag = None
	bricks = read_bricks(in_file)
	for b in bricks:
		b.set_value(v)
		if tag:
			b.set_parameter("CREATIONTAG", tag)
	return write_bricks(bricks, out=out_file)
# :FUNCTIONS

# MAIN:
if __name__ == "__main__":
	main()
# :MAIN

