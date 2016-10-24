#!/bin/bash

java -jar tabula-0.9.1-jar-with-dependencies.jar -p all $1 | python generate_transcript.py > $1.txt