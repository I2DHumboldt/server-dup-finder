# src_python

Esta carpeta contiene los scripts de python que realizan la comparación de los archivos para encontrar los archivos duplicados y para agregar la
información que describe cada archivo repetido.

## compare.py

Este es el script que realiza la comparación de los archivos para determinar los elementos repetidos. El algoritmo consta de 2 partes: En la primera
se filtran solo aquellos archivos cuyo tamaño sea superior al especificado por el parámetro de entrada *min_size* y posteriormente se buscan todos los
archivos cuyo tamaño en bytes el mismo; En la segunda parte el programa realiza una comparación a nivel de contenido de todos aquellos archivos que hayand
sido detectados como candidatos en la etapa 1.

De esta forma es posible encontrar todos los archivos repetidos, sin necesidad de realizar una comparación de todos contra todos, ni de abrir todos los
archivos.

## addinfo.py

Este script agrega una columna extra con el tipo de cada documento basado en la extensión de los archivos. Adicionalmente agrega una columna extra para los
documentos de texto plano y docx con la concatenación de una lista de palabras clave que pueden contener. 

## readDoc.py

Es el script que lee el texto contenido en los archivos docx
