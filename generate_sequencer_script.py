####################################################################
# Type: SCRIPT                                                     #
#                                                                  #
# Description: [description]                                       #
####################################################################

# IMPORTS:
import sys, os
# :IMPORTS

# CLASSES:
# :CLASSES

# VARIABLES:
# :VARIABLES

# FUNCTIONS:
def main():
	# Arguments:
	info_type = "pedestal"		# Type of scan
	if len(sys.argv) > 1:
		info_type = sys.argv[1].lower()
	
	n = 1000		# Number of events per step in scan
	if len(sys.argv) > 2:
		n = int(sys.argv[2])
	
	out_file = "sequencer_script_" + info_type + ".txt"
	if len(sys.argv) > 3:
		out_file = sys.argv[3]
	
	# Construct the script:
	in_dir = "/nfshome0/elhughes/ngrbx/xml/" + info_type
	if info_type == "pedestal":
		values = range(64)
	else:
		print "ERROR: info_type == " + info_type + " hasn't been implemented, yet."
		return False
	
	script = ""
	for value in values:
		creation_tag = info_type + "_" + str(value)
		script += creation_tag + " : " + str(n) + " (NAME_ENCODED)\n"
		script += "\tdbload " + info_type + " xmlfile:/" + in_dir + "/" + creation_tag + ".xml " + creation_tag + "\n"
	
	# Write the script:
	out = open(out_file, "w")
	out.write(script)
	out.close()
# :FUNCTIONS

# MAIN:
if __name__ == "__main__":
	main()
# :MAIN

