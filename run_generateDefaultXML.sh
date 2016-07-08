#!/bin/bash

OUTPUTDIR=/nfshome0/elhughes/ngrbx/xml/default/qie10

python generateDefaultXML.py singleBrickTemplate.xml '38 0 0 0 0' PEDESTAL $OUTPUTDIR/pedestal_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml 0 DELAY $OUTPUTDIR/delay_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml 1 TDCTHRESHOLD $OUTPUTDIR/tdcthreshold_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml '1 2' LVDS $OUTPUTDIR/lvds_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml 1 DISCRIMON $OUTPUTDIR/discrimon_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml 1 DISCON $OUTPUTDIR/discon_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml '0 0' TDCGAINREF $OUTPUTDIR/tdcgainref_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml '0 0' FIXRANGE $OUTPUTDIR/fixrange_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml '0 0' BIAS $OUTPUTDIR/bias_default_qie10.xml &&
#python generateDefaultXML.py singleBrickTemplate.xml 0 SHUNT $OUTPUTDIR/shunt_default_qie11.xml &&
python generateDefaultXML.py singleBrickTemplate.xml 0 CALMODE $OUTPUTDIR/calmode_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml 1 CLKOUTEN $OUTPUTDIR/clkouten_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml 0 TDCMODE $OUTPUTDIR/tdcmode_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml 5 RINSEL $OUTPUTDIR/rinsel_default_qie10.xml &&
python generateDefaultXML.py singleBrickTemplate.xml 0 HYSTERIS_SEL $OUTPUTDIR/hysteris_sel_default_qie10.xml
