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
	in_file = sys.argv[1] #template file (i.e. example.xml)
	param_value = sys.argv[2]
	out_file = in_file
	if len(sys.argv) > 3:
		out_file = sys.argv[3]
	bricks = read_bricks(in_file)
	for b in bricks:
		b.set_value(param_value)
		b.set_parameter("CREATIONTAG","delay_"+str(param_value))
	return write_bricks(bricks, out=out_file)
# :FUNCTIONS

# MAIN:
if __name__ == "__main__":
	main()
# :MAIN

