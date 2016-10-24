#!/bin/bash                                                                                                                                                                                                 
for file in $1/*
do
    echo $file
    java -jar tabula-0.9.1-jar-with-dependencies.jar -p all $file | python PyTranscript.py > $file.txt
done
