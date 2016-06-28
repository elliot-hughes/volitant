#!/bin/bash

for i in {1..20}
do
	python randomize.py template.xml /nfshome0/elhughes/ngrbx/xml/delay/delay_random_$i.xml delay_random_$i delay
done
