#!/bin/bash

TARGET_DIR="./web_pages"
SUBJECTS=( "cmps" "cmpe" "ee" "ams" "cmpm" )
PAGE_URL="https://courses.soe.ucsc.edu/courses/"
WEB_PARSER="python web_parse.py"
RESULTS_FILE="courses.json"

mkdir -p ${TARGET_DIR}

for year in `seq 1998 2016`;
do
    echo $year
    for subject in ${SUBJECTS[*]};
    do
	FILE_NAME="${TARGET_DIR}/${subject}_${year}.html"
	if [ ! -f ${FILE_NAME} ]
	then
	    curl  "${PAGE_URL}${subject}?year=${year}"  > "${FILE_NAME}"
	fi
    done
done

${WEB_PARSER} ${TARGET_DIR}/* > ${RESULTS_FILE}
