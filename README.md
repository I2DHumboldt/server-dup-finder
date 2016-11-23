# server-duplicados
Tool that compares and list, recursively, all the files in the given folders that are repeated.
Una herramienta para comparar y listar de forma recursiva y eficiente todos los archivos repetidos entre dos carpetas dadas

## Instalación

Para la instación de este script es necesario tener python 2.7 o superior y el manejador de paquetes de python pip y git

```
#Ubuntu

 sudo apt-get install git
 sudo apt-get install python-setuptools python-dev build-essential
 sudo easy_install pip
 sudo pip install --upgrade virtualenv

#Centos y fedora
 sudo yum install git
 sudo yum install python-setuptools python-dev build-essential
 sudo easy_install pip
 sudo pip install --upgrade virtualenv
 
```

```
git clone https://github.com/I2DHumboldt/server-duplicados.git
cd server-duplicados
sudo pip install python-docx
```

## Ejecución

```
./duplicados.sh folderA folderB output minSize
```

## Parámetros

 folderA: El primer folder a analizar
 folderB: El segundo folder a analizar
 output: El archivo de salida con la lista de archivos repetidos
 minSize: El tamaño mínimo en kilobytes de los archivos a analizar (16 kb por defecto) 

## Salida

Un archivo separado por comas con todos los archivos repetidos entre el forlderA y el folderB
 
```
5860	_tests_/testData/A/javascript-books/You Beyond.pdf	_tests_/testData/B/book1.pdf
3488	_tests_/testData/A/javascript-books/Grammar.pdf	_tests_/testData/B/Grammar.pdf
2556	_tests_/testData/A/javascript-books/Prototypes.pdf	_tests_/testData/B/Prototypes.pdf
336	_tests_/testData/A/ComparisonofNMRsimulators.docx	_tests_/testData/B/ComparisonofNMRsimulators.docx
100	_tests_/testData/A/Reporte_Servidor_SDA.doc	_tests_/testData/B/Reporte_Servidor_SDA.doc	
12	_tests_/testData/A/javascript-books/zlib.txt	_tests_/testData/B/zlib.txt
12	_tests_/testData/A/solvent1H.xlsx	_tests_/testData/B/solvent1H.xlsx
```

Adicionalment el programa imprime en la consola un log del proceso. Este log contiene información importante sobre el número de archivos
repetidos y el total de espacio utilizado por estos. Ej: 

```
./duplicados.sh ~/Documents ~/Dropbox reporte.csv 230
/Users/acastillo/git/server-duplicados
Step 1/2: listing files...
     working on A
     working on B
Done
Step 2/2: Finding matches
Considering files of min:  16  kb
Folder A:  /Users/acastillo/Documents 12311
Folder B:  /Users/acastillo/Dropbox 2137
   Step 2.1/2: Matching file sizes
124 / 12311 current files sizes: 6052  kb (repeated files: 1 space in disk; 27692 kb)
247 / 12311 current files sizes: 3216  kb (repeated files: 11 space in disk; 72304 kb)
370 / 12311 current files sizes: 1956  kb (repeated files: 74 space in disk; 218712 kb)
493 / 12311 current files sizes: 1412  kb (repeated files: 106 space in disk; 272784 kb)
616 / 12311 current files sizes: 1028  kb (repeated files: 182 space in disk; 366556 kb)
739 / 12311 current files sizes: 816  kb (repeated files: 193 space in disk; 376732 kb)
862 / 12311 current files sizes: 684  kb (repeated files: 228 space in disk; 402344 kb)
985 / 12311 current files sizes: 572  kb (repeated files: 235 space in disk; 406752 kb)
1108 / 12311 current files sizes: 512  kb (repeated files: 289 space in disk; 434720 kb)
1231 / 12311 current files sizes: 464  kb (repeated files: 304 space in disk; 442216 kb)
1354 / 12311 current files sizes: 452  kb (repeated files: 304 space in disk; 442216 kb)
1477 / 12311 current files sizes: 444  kb (repeated files: 304 space in disk; 442216 kb)
1600 / 12311 current files sizes: 436  kb (repeated files: 305 space in disk; 442660 kb)
1723 / 12311 current files sizes: 428  kb (repeated files: 307 space in disk; 443524 kb)
1846 / 12311 current files sizes: 420  kb (repeated files: 307 space in disk; 443524 kb)
1969 / 12311 current files sizes: 416  kb (repeated files: 307 space in disk; 443524 kb)
2092 / 12311 current files sizes: 408  kb (repeated files: 307 space in disk; 443524 kb)
2215 / 12311 current files sizes: 404  kb (repeated files: 307 space in disk; 443524 kb)
2338 / 12311 current files sizes: 400  kb (repeated files: 308 space in disk; 443928 kb)
2461 / 12311 current files sizes: 400  kb (repeated files: 308 space in disk; 443928 kb)
2584 / 12311 current files sizes: 396  kb (repeated files: 308 space in disk; 443928 kb)
2707 / 12311 current files sizes: 392  kb (repeated files: 310 space in disk; 444712 kb)
2830 / 12311 current files sizes: 388  kb (repeated files: 312 space in disk; 445488 kb)
...
...
4798 / 12311 current files sizes: 228  kb (repeated files: 395 space in disk; 469652 kb)
countComparison  660176
resume: 395 files 469652 Kb
   Done
Done
```

# Agregar descripción y palabras clave para archivos de texto

Esta herramienta permite agregar información adicional al archivo de salida de duplicados. El programa agrega 1 columna extra con información sobre el tipo de archivo (document, table, image, plain, other) basado en la extensión del archivo. Esto permite filtrar las entradas del archivo por tipo de documentos y facilita el análisis.

```
//Tabla de equivalencias con base en la extensión del archivo

{".png":"image", ".jpg":"image", ".tiff":"image", ".bmp":"image", ".eps":"image", ".svg":"image", ".gif":"image", ".doc":"document", ".docx":"document", ".xls":"table", ".xlsx":"table", ".csv":"table", ".pdf":"document", ".rtf":"document", ".txt": "plain"}
```

Para los documentos .docx se agrega una columna adicional con la concatenación de las palabreas clave de la siguiente lista que contiene el documento. Esto permite dar una idea inicial sobre el contenido del documento.

```
//Lista de palabras clave que se deben buscar en el cuerpo del documento

keywords = ["informe final ", "documento final", "consultoria",  "presupuesto", "contrato", "convenio", "cronograma", "propuesta", "informe"]
```
## Ejecución

```
./informacion.sh  reporte.csv reporte_info.csv folderA
```

## Parámetros

* reporte.csv: Nombre del archivo de salida del script *./duplicados.sh*
* reporte_info.csv: Archivo de salida
* folderA: Primer directorio de entrada del script *./duplicados.sh* (Primer parámetro)

## Salida

Un archivo de texto con la siguiente estructura:

```
5860	_tests_/testData/A/javascript-books/You Beyond.pdf	_tests_/testData/B/book1.pdf	document
3488	_tests_/testData/A/javascript-books/Grammar.pdf	_tests_/testData/B/Grammar.pdf	document
2556	_tests_/testData/A/javascript-books/Prototypes.pdf	_tests_/testData/B/Prototypes.pdf	document
336	_tests_/testData/A/ComparisonofNMRsimulators.docx	_tests_/testData/B/ComparisonofNMRsimulators.docx	document	reporte final
100	_tests_/testData/A/Reporte_Servidor_SDA.doc	_tests_/testData/B/Reporte_Servidor_SDA.doc	contrato, reporte final
12	_tests_/testData/A/javascript-books/zlib.txt	_tests_/testData/B/zlib.txt	plain	compression
12	_tests_/testData/A/solvent1H.xlsx	_tests_/testData/B/solvent1H.xlsx	table
```

