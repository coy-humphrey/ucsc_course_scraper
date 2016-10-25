#!/bin/bash

TARGET_DIR="./web_pages"
SUBJECTS=( "cmps" "cmpe" "ee" "ams" "cmpm" )
PAGE_URL="https://courses.soe.ucsc.edu/courses/"

mkdir -p ${TARGET_DIR}

for year in `seq 1998 2016`;
do
    echo $year
    for subject in ${SUBJECTS[*]};
    do
	curl  "${PAGE_URL}${subject}?year=${year}"  > "${TARGET_DIR}/${subject}_${year}.html"
    done
done
