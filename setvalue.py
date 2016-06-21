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
	bricks = read_bricks(in_file)
	for b in bricks:
		b.set_value(v)
		b.set_parameter(parameter,v)
	return write_bricks(bricks, out=out_file)
# :FUNCTIONS

# MAIN:
if __name__ == "__main__":
	main()
# :MAIN

