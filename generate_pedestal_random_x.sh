#!/bin/bash

for i in {1..20}
do
	python randomize.py template.xml /nfshome0/elhughes/ngrbx/xml/pedestal/pedestal_random_$i.xml pedestal_random_$i pedestal
done
