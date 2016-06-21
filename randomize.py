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
	out_file = in_file
	if len(sys.argv) > 2:
		out_file = sys.argv[2]
	bricks = read_bricks(in_file)
	for b in bricks:
		b.randomize_data(range(50)+range(64,113))
	return write_bricks(bricks, out=out_file)
# :FUNCTIONS

# MAIN:
if __name__ == "__main__":
	main()
# :MAIN

