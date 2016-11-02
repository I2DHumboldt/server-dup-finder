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
...
```

```
git clone https://github.com/I2DHumboldt/server-duplicados.git
cd server-duplicados
sudo pip install python-docx
```

## Ejecución

```
./duplicados.sh folderA folderB reporte.csv
```

## Salida
 Un archivo separado por comas con todos los archivos repetidos entre el forlderA y el folderB
 
```
5860	_tests_/testData/A/javascript-books/You Beyond.pdf	_tests_/testData/B/book1.pdf	document
3488	_tests_/testData/A/javascript-books/Grammar.pdf	_tests_/testData/B/Grammar.pdf	document
2556	_tests_/testData/A/javascript-books/Prototypes.pdf	_tests_/testData/B/Prototypes.pdf	document
336	_tests_/testData/A/ComparisonofNMRsimulators.docx	_tests_/testData/B/ComparisonofNMRsimulators.docx	document	reporte final
100	_tests_/testData/A/Reporte_Servidor_SDA.doc	_tests_/testData/B/Reporte_Servidor_SDA.doc	contrato, reporte final
12	_tests_/testData/A/javascript-books/zlib.txt	_tests_/testData/B/zlib.txt	plain	compression
12	_tests_/testData/A/solvent1H.xlsx	_tests_/testData/B/solvent1H.xlsx	table
```

## Agregar descripción y palabras clave para archivos de texto

```
./informacion.sh  reporte.csv reporte_info.csv
```
