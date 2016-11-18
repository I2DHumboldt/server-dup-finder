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
./duplicados.sh folderA folderB output minSize
```

# Parámetros

 folderA: El primer folder a analizar
 folderB: El segundo folder a analizar
 output: El archivo de salida con la lista de archivos repetidos
 minSize: El tamaño mínimo en kilobytes de los archivos a analizar (16 kb por defecto) 


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

Adicionalment el programa imprime en la consola un log del proceso. Este log contiene información importante sobre el número de archivos
repetidos y el total de espacio utilizado por estos. Ej: 

```
./duplicados.sh ~/Documents ~/Dropbox reporte.csv 16
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
2953 / 12311 current files sizes: 384  kb (repeated files: 312 space in disk; 445488 kb)
3076 / 12311 current files sizes: 380  kb (repeated files: 314 space in disk; 446248 kb)
3199 / 12311 current files sizes: 380  kb (repeated files: 314 space in disk; 446248 kb)
3322 / 12311 current files sizes: 376  kb (repeated files: 316 space in disk; 447008 kb)
3445 / 12311 current files sizes: 364  kb (repeated files: 316 space in disk; 447008 kb)
3568 / 12311 current files sizes: 356  kb (repeated files: 319 space in disk; 448088 kb)
3691 / 12311 current files sizes: 352  kb (repeated files: 319 space in disk; 448088 kb)
3814 / 12311 current files sizes: 348  kb (repeated files: 319 space in disk; 448088 kb)
3937 / 12311 current files sizes: 340  kb (repeated files: 319 space in disk; 448088 kb)
4060 / 12311 current files sizes: 332  kb (repeated files: 319 space in disk; 448088 kb)
4183 / 12311 current files sizes: 324  kb (repeated files: 319 space in disk; 448088 kb)
4306 / 12311 current files sizes: 316  kb (repeated files: 325 space in disk; 449992 kb)
4429 / 12311 current files sizes: 296  kb (repeated files: 354 space in disk; 458832 kb)
4552 / 12311 current files sizes: 268  kb (repeated files: 366 space in disk; 462096 kb)
4675 / 12311 current files sizes: 252  kb (repeated files: 388 space in disk; 467968 kb)
4798 / 12311 current files sizes: 228  kb (repeated files: 395 space in disk; 469652 kb)
4921 / 12311 current files sizes: 212  kb (repeated files: 411 space in disk; 473228 kb)
5044 / 12311 current files sizes: 196  kb (repeated files: 416 space in disk; 474220 kb)
5167 / 12311 current files sizes: 184  kb (repeated files: 423 space in disk; 475548 kb)
5290 / 12311 current files sizes: 168  kb (repeated files: 425 space in disk; 475908 kb)
5413 / 12311 current files sizes: 156  kb (repeated files: 438 space in disk; 478044 kb)
5536 / 12311 current files sizes: 144  kb (repeated files: 449 space in disk; 479692 kb)
5659 / 12311 current files sizes: 132  kb (repeated files: 462 space in disk; 481468 kb)
5782 / 12311 current files sizes: 124  kb (repeated files: 473 space in disk; 482832 kb)
5905 / 12311 current files sizes: 116  kb (repeated files: 479 space in disk; 483552 kb)
6028 / 12311 current files sizes: 104  kb (repeated files: 487 space in disk; 484428 kb)
6151 / 12311 current files sizes: 96  kb (repeated files: 497 space in disk; 485436 kb)
6274 / 12311 current files sizes: 88  kb (repeated files: 513 space in disk; 486896 kb)
6397 / 12311 current files sizes: 80  kb (repeated files: 523 space in disk; 487752 kb)
6520 / 12311 current files sizes: 72  kb (repeated files: 540 space in disk; 489072 kb)
6643 / 12311 current files sizes: 72  kb (repeated files: 541 space in disk; 489144 kb)
6766 / 12311 current files sizes: 68  kb (repeated files: 545 space in disk; 489424 kb)
6889 / 12311 current files sizes: 64  kb (repeated files: 554 space in disk; 490036 kb)
7012 / 12311 current files sizes: 60  kb (repeated files: 565 space in disk; 490728 kb)
7135 / 12311 current files sizes: 56  kb (repeated files: 577 space in disk; 491416 kb)
7258 / 12311 current files sizes: 52  kb (repeated files: 608 space in disk; 493144 kb)
7381 / 12311 current files sizes: 48  kb (repeated files: 616 space in disk; 493552 kb)
7504 / 12311 current files sizes: 48  kb (repeated files: 622 space in disk; 493840 kb)
7627 / 12311 current files sizes: 44  kb (repeated files: 636 space in disk; 494464 kb)
7750 / 12311 current files sizes: 40  kb (repeated files: 642 space in disk; 494728 kb)
7873 / 12311 current files sizes: 40  kb (repeated files: 642 space in disk; 494728 kb)
7996 / 12311 current files sizes: 40  kb (repeated files: 676 space in disk; 496088 kb)
8119 / 12311 current files sizes: 36  kb (repeated files: 678 space in disk; 496160 kb)
8242 / 12311 current files sizes: 36  kb (repeated files: 686 space in disk; 496448 kb)
8365 / 12311 current files sizes: 36  kb (repeated files: 696 space in disk; 496808 kb)
8488 / 12311 current files sizes: 36  kb (repeated files: 696 space in disk; 496808 kb)
8611 / 12311 current files sizes: 32  kb (repeated files: 699 space in disk; 496904 kb)
8734 / 12311 current files sizes: 32  kb (repeated files: 699 space in disk; 496904 kb)
8857 / 12311 current files sizes: 32  kb (repeated files: 705 space in disk; 497096 kb)
8980 / 12311 current files sizes: 32  kb (repeated files: 707 space in disk; 497160 kb)
9103 / 12311 current files sizes: 32  kb (repeated files: 707 space in disk; 497160 kb)
9226 / 12311 current files sizes: 28  kb (repeated files: 709 space in disk; 497216 kb)
9349 / 12311 current files sizes: 28  kb (repeated files: 709 space in disk; 497216 kb)
9472 / 12311 current files sizes: 28  kb (repeated files: 710 space in disk; 497244 kb)
9595 / 12311 current files sizes: 28  kb (repeated files: 712 space in disk; 497300 kb)
9718 / 12311 current files sizes: 28  kb (repeated files: 724 space in disk; 497636 kb)
9841 / 12311 current files sizes: 28  kb (repeated files: 724 space in disk; 497636 kb)
9964 / 12311 current files sizes: 28  kb (repeated files: 724 space in disk; 497636 kb)
10087 / 12311 current files sizes: 28  kb (repeated files: 724 space in disk; 497636 kb)
10210 / 12311 current files sizes: 24  kb (repeated files: 724 space in disk; 497636 kb)
10333 / 12311 current files sizes: 24  kb (repeated files: 724 space in disk; 497636 kb)
10456 / 12311 current files sizes: 24  kb (repeated files: 724 space in disk; 497636 kb)
10579 / 12311 current files sizes: 24  kb (repeated files: 726 space in disk; 497684 kb)
10702 / 12311 current files sizes: 24  kb (repeated files: 729 space in disk; 497756 kb)
10825 / 12311 current files sizes: 24  kb (repeated files: 736 space in disk; 497924 kb)
10948 / 12311 current files sizes: 24  kb (repeated files: 736 space in disk; 497924 kb)
11071 / 12311 current files sizes: 24  kb (repeated files: 736 space in disk; 497924 kb)
11194 / 12311 current files sizes: 20  kb (repeated files: 738 space in disk; 497964 kb)
11317 / 12311 current files sizes: 20  kb (repeated files: 738 space in disk; 497964 kb)
11440 / 12311 current files sizes: 20  kb (repeated files: 738 space in disk; 497964 kb)
11563 / 12311 current files sizes: 20  kb (repeated files: 738 space in disk; 497964 kb)
11686 / 12311 current files sizes: 20  kb (repeated files: 739 space in disk; 497984 kb)
11809 / 12311 current files sizes: 20  kb (repeated files: 739 space in disk; 497984 kb)
11932 / 12311 current files sizes: 20  kb (repeated files: 750 space in disk; 498204 kb)
12055 / 12311 current files sizes: 20  kb (repeated files: 766 space in disk; 498524 kb)
12178 / 12311 current files sizes: 20  kb (repeated files: 766 space in disk; 498524 kb)
12301 / 12311 current files sizes: 20  kb (repeated files: 766 space in disk; 498524 kb)
countComparison  660176
resume: 766 files 498524 Kb
   Done
Done
```

## Agregar descripción y palabras clave para archivos de texto

```
./informacion.sh  reporte.csv reporte_info.csv folderA
```

* reporte.csv: Nombre del archivo de salida del script *./duplicados.sh*
* reporte_info.csv: Archivo de salida
* folderA: Primer directorio de entrada del script *./duplicados.sh* (Primer parámetro)
