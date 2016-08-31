####################################################################
# Type: SCRIPT                                                     #
#                                                                  #
# Description: Generates an XML configuration file from a          #
# template.                                                        #
# Usage:                                                           #
# python generate_hf_xml.py template.xml values infotype outfile   #
####################################################################

# IMPORTS:
import sys
from volitant.volitant import *
from copy import copy
# :IMPORTS

# CLASSES:
# :CLASSES

# VARIABLES:
# :VARIABLES

# FUNCTIONS:
def main():
	# Arguments:
	in_file = sys.argv[1]		# Template file (i.e. example.xml)
	param_value = sys.argv[2]
	infotype_value = sys.argv[3]
	out_file = infotype_value + '.xml'
	if len(sys.argv) > 4:
		out_file = sys.argv[4]
	
	bricks = read_bricks(in_file)
	len(bricks)
	newBricks = []
	for b in bricks:
		for i in range(1, 19):
			b.set_value(param_value)
			b.set_parameter("INFOTYPE", infotype_value)
			b.set_parameter("CREATIONTAG", "null")
			b.set_parameter("RBX", "HF" + str(i))
			newBricks.append(copy(b))
	write_bricks(newBricks, out=out_file)
	return
# :FUNCTIONS

# MAIN:
if __name__ == "__main__":
	main()
# :MAIN

