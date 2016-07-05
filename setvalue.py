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
	# Arguments:
	## 1: input file
	in_file = sys.argv[1]
	
	## 2: input value
	value = sys.argv[2]
	
	## 3 (optional): output file
	out_file = in_file
	if len(sys.argv) > 3:
		out_file = sys.argv[3]
	
	## 4 (optional): creation tag
	creation_tag = None
	if len(sys.argv) > 4:
		creation_tag = sys.argv[4]
	
	## 5 (optional): info type
	info_type = None
	if len(sys.argv) > 5:
		info_type = sys.argv[5]
	
	# Read in bricks and change values:
	bricks = read_bricks(in_file)
	for b in bricks:
		b.set_value(value)
		if creation_tag:
			b.set_parameter("CREATIONTAG", creation_tag)
		if info_type:
			b.set_parameter("INFOTYPE", info_type)
	
	# Write bricks:
	return write_bricks(bricks, out=out_file)
# :FUNCTIONS

# MAIN:
if __name__ == "__main__":
	main()
# :MAIN

