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
	out_file = None
	if len(sys.argv) > 2:
		out_file = sys.argv[2]
	return convert(in_file, out=out_file)
# :FUNCTIONS

# MAIN:
if __name__ == "__main__":
	main()
# :MAIN

