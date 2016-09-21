#!/bin/bash

OUTPUTDIR=/nfshome0/elhughes/xml/default/he

python generate_he_xml.py template_single_brick_he.xml '38 0 0 0 0' PEDESTAL $OUTPUTDIR/pedestal_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml 0 DELAY $OUTPUTDIR/delay_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml 1 TDCTHRESHOLD $OUTPUTDIR/tdcthreshold_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml '1 2' LVDS $OUTPUTDIR/lvds_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml 1 DISCRIMON $OUTPUTDIR/discrimon_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml 1 DISCON $OUTPUTDIR/discon_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml '0 0' TDCGAINREF $OUTPUTDIR/tdcgainref_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml '0 0' FIXRANGE $OUTPUTDIR/fixrange_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml '0 0' BIAS $OUTPUTDIR/bias_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml 0 SHUNT $OUTPUTDIR/shunt_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml 0 CALMODE $OUTPUTDIR/calmode_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml 1 CLKOUTEN $OUTPUTDIR/clkouten_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml 0 TDCMODE $OUTPUTDIR/tdcmode_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml 5 RINSEL $OUTPUTDIR/rinsel_default_he.xml &&
python generate_he_xml.py template_single_brick_he.xml 0 HYSTERIS_SEL $OUTPUTDIR/hysteris_sel_default_he.xml
