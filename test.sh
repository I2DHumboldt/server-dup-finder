#!/usr/bin/env bash

./duplicados.sh ./_tests_/testData/A ./_tests_/testData/B reporte.csv 8
./informacion.sh  reporte.csv reporte_info.csv ./_tests_/testData/A

#El reporte debe mostrar los siguiente archivos repetidos
