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
	in_file = sys.argv[1]
	
	out_file = in_file
	if len(sys.argv) > 2:
		out_file = sys.argv[2]
	
	creation_tag = None
	if len(sys.argv) > 3:
		creation_tag = sys.argv[3]
	
	info_type = "delay"
	if len(sys.argv) > 4:
		info_type = sys.argv[4]
	
	# Come up with value range:
	if info_type == "delay":
		values = range(50) + range(64, 113)
	elif info_type == "pedestal":
		values = range(64)
	else:
		print "ERROR: Info types other than 'delay' and 'pedestal' haven't been implemented, yet."
		return False
	
	
	# Read bricks and randomize data:
	bricks = read_bricks(in_file)
	for b in bricks:
		b.randomize_data(values)
		if info_type == "pedestal":		# Pedestal KLUDGE (to make CIDs 0).
			for datum in b.data:
				datum.values += ["0", "0", "0", "0"]
			b.update()
		
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

