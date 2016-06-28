#!/bin/bash

for i in {0..50}
do
	python setvalue.py template.xml "$i" /nfshome0/elhughes/ngrbx/xml/delay/delay_$i.xml delay_$i DELAY
done

for i in {64..112}
do
	python setvalue.py template.xml "$i" /nfshome0/elhughes/ngrbx/xml/delay/delay_$i.xml delay_$i DELAY
done
