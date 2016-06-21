#!/bin/bash

for i in {0,10,20,23,24,25,30,40,45,64,74,84,87,88,89,94,104,109}
do
	python generateDelayXML.py delayAllxx.xml $i delayAll$i.xml 
done








