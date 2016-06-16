####################################################################
# Type: MODULE                                                     #
#                                                                  #
# Description: A module containing the brick class and conversion  #
# functions.                                                       #
####################################################################

# IMPORTS:
import sys
import csv		# For writing and reading tables.
import collections
from xml.dom import minidom		# I would prefer to use "xml.etree.ElementTree", but that's implemented in Python 2.5.
from xml.dom.ext import PrettyPrint
from StringIO import StringIO
import random
# /IMPORTS

# CLASSES:
class brick:
	def __init__(self, dom_element):
		self.dom_element = dom_element
		self.params = {
			"RBX": False,
			"INFOTYPE": False,
			"CREATIONTAG": False,
			"CREATIONSTAMP": False,
		}
		for parameter in dom_element.getElementsByTagName("Parameter"):
			name = parameter.attributes["name"].value
			if name in self.params:
				self.params[name] = parameter.firstChild.nodeValue
		for key, value in self.params.items():
			setattr(self, key.lower(), value)
		self.data = self.get_data()
	
	def update(self):
		doc = minidom.Document()
		de_brick = doc.createElement("CFGBrick")
		doc.appendChild(de_brick)
		for param, value in self.params.items():
			de_parameter = doc.createElement("Parameter")
			de_parameter.setAttribute("name", param)
			de_parameter.setAttribute("type", "string")
			de_brick.appendChild(de_parameter)
			contents = doc.createTextNode(value)
			de_parameter.appendChild(contents)
		for datum in self.data:
			datum.update()
			de_brick.appendChild(datum.dom_element)
		self.dom_element = de_brick
		return True
	
	def Print(self):
		stream = StringIO()
		PrettyPrint(self.dom_element, stream=stream, encoding='utf-8')
		print stream.getvalue().strip()
	
	def get_data(self):
		return [data(de) for de in self.dom_element.getElementsByTagName("Data")]
	
	def write(self, out="test.txt"):
		return write_bricks([self], out=out)
	
	def set_value(self, v):
		for datum in self.data:
			datum.set_value(str(v))
		return self.update()
	
	def randomize_data(self, possible_values):
		for datum in self.data:
			datum.randomize(possible_values)
		self.update()
		return True


class data:
	def __init__(self, dom_element):
		self.dom_element = dom_element
		for attr, value in dom_element.attributes.items():
			setattr(self, attr, value)
		self.value = dom_element.firstChild.nodeValue
		self.values = self.value.split()
		self.elements = int(dom_element.attributes["elements"].value)
		self.qie = dom_element.attributes["qie"].value
		self.card = dom_element.attributes["card"].value
		self.encoding = dom_element.attributes["encoding"].value
	
	def Print(self):
		stream = StringIO()
		PrettyPrint(self.dom_element, stream=stream, encoding='utf-8')
		print stream.getvalue().strip()
	
	def set_value(self, v):
		self.value = str(v)
		self.values = self.value.split()
		return self.update()
	
	def randomize(self, possible_values=range(50)):
		if self.elements != 1:
			print "ERROR: Not implemented, yet."
			return False
		
		self.values = [str(random.choice(possible_values)) for i in range(self.elements)]
		self.value = "\t".join(self.values)
		self.update()
		return self.values
	
	def update(self):
		doc = minidom.Document()
		de_datum = doc.createElement("Data")
		de_datum.setAttribute("elements", str(self.elements))
		de_datum.setAttribute("encoding", self.encoding)
		de_datum.setAttribute("card", self.card)
		de_datum.setAttribute("qie", self.qie)
		contents = doc.createTextNode("\t".join(self.values))
		de_datum.appendChild(contents)
		self.dom_element = de_datum
		return True
# :CLASSES

# FUNCTIONS:
def convert(in_file, out=None):
	name = in_file.split(".")[0]
	ext = in_file.split(".")[-1]
	if not out:
		out = name + (".txt", ".xml")[ext == "txt"]
	print "Converting " + in_file + " to " + out
	return write_bricks(read_bricks(in_file), out=out)


def write_bricks(bricks, out="test.txt"):
	# Given a list of brick objects, write them to a file named "out". The supplied file extension tells the code what to do.
	ext = out.split(".")[-1]
	if ext == "txt":
		output = open(out, "w")
		writer = csv.writer(output, delimiter="\t")
		for b in bricks:
			for datum in b.data:
				row = [b.infotype, b.creationtag, b.creationstamp, b.rbx, datum.card, datum.qie]
				row += datum.values
				writer.writerow(row)
		output.close()
		return True
	elif ext == "xml":
		doc = minidom.Document()
		de_brick_set = doc.createElement("CFGBrickSet")
		doc.appendChild(de_brick_set)
		for b in bricks:
			de_brick_set.appendChild(b.dom_element)
		stream = StringIO()
		PrettyPrint(doc, stream=stream, encoding='utf-8', indent="\t")
		output = open(out, "w")
		output.write(stream.getvalue().strip())
		return True


def create_brick(params, data):
	# Create a brick object from simple variables: params is a list corresponding to "names" (inside) and data is a list of data.
	if len(params) != 4:
		print "ERROR (volitant.crate_bricks): You supplied the following paramters: " + str(params) + ". You need 4 total."
		sys.exit()
	
	# Variables:
	names = ["RBX", "INFOTYPE", "CREATIONTAG", "CREATIONSTAMP"]
	
	doc = minidom.Document()
	de_brick = doc.createElement("CFGBrick")
	doc.appendChild(de_brick)
	for i, param in enumerate(params):
		de_parameter = doc.createElement("Parameter")
		de_parameter.setAttribute("name", names[i])
		de_parameter.setAttribute("type", "string")
		de_brick.appendChild(de_parameter)
		contents = doc.createTextNode(param)
		de_parameter.appendChild(contents)
	for datum in data:
		de_datum = doc.createElement("Data")
		de_datum.setAttribute("elements", str(len(datum[2])))
		de_datum.setAttribute("encoding", "dec")
		de_datum.setAttribute("card", datum[0])
		de_datum.setAttribute("qie", datum[1])
		de_brick.appendChild(de_datum)
		contents = doc.createTextNode(" ".join(datum[2]))
		de_datum.appendChild(contents)
	
	return brick(de_brick)


def read_bricks(in_file):
	# Get brick objects from either a "txt" or "xml" file.
	ext = in_file.split(".")[-1]
	if ext == "xml":
		x = minidom.parse(in_file)
		return [brick(de) for de in x.getElementsByTagName("CFGBrick")]
	elif ext == "txt":
#		print "ERROR (read_bricks): Reading " + ext + " isn't implemented, yet."
		f = open(in_file)
		reader = csv.reader(f, delimiter="\t")
		order = []		# This is a KLUDGE because ordereddicts don't work with this Python version.
		info = {}
		for row in reader:
			params = (row[3], row[0], row[1], row[2])
			if params not in info:
				order.append(params)
				info[params] = []
			info[params].append(row[4:6]+[row[6:]])
		bricks = []
		for key in order:
			bricks.append(create_brick(key, info[key]))
		return bricks


def print_summary(in_file):
	# Print a summary of a parameter file (either "xml" or "txt")
	bricks = read_bricks(in_file)
	ext = in_file.split(".")[-1]
	print ext.upper() + " file: " + in_file
	print str(len(bricks)) + " brick(s):"
	for i, b in enumerate(bricks):
		print  "\t" + str(i) + ": " + str(b.params) + " (" + str(len(b.data)) + " data)"
# :FUNCTIONS
