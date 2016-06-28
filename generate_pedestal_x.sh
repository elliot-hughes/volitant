#!/bin/bash

for i in {0..63}
do
	python setvalue.py template.xml "$i 0 0 0 0" /nfshome0/elhughes/ngrbx/pedestal/pedestal_$i.xml pedestal_$i PEDESTAL
done


