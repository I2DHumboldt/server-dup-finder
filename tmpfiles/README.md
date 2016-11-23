# tmpFiles

En esta carpeta se guardan los archivos temporales de la ejecución del script que encuentra los duplicados. Los archivos lsA.txt y lsB.txt son
la salida del comando `find $X -type f -exec du -ak {} + | sort -n -r > tmpfiles/lsX.txt` donde X es la ruta de absoluta a las carpetas que se quieren
comparar.

Los archivos no se borran automáticamente, porque pueden ser usados en otros procesos.
