#!/bin/bash                                                                                                                                                                                                 
for file in $1/*
do
    echo $file
    ./RunTranscript.sh $file
done
