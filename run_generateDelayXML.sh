#!/bin/bash

for i in {10,20}
do
	python setvalue.py pedestalAllxx.xml "$i 0 0 0 0" pedestalAll$i.xml 
done








