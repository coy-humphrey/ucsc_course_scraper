# ucsc_course_scraper
Scrapes the course name, quarter, and professor from UCSC soe course pages.

## Requirements
Using this framework requires BeautifulSoup4 and the Tabula Java Jar.

**To install BeatifulSoup4:** `pip install beautifulsoup4`

**To install Tabula-Java Jar:** <https://github.com/tabulapdf/tabula-java/releases>

## Setup

Put the Tabula-Java Jar in the same folder as the repo source. RunTranscript.sh contains hardlinks to the jar name so modify it if necessary.

To generate the courses json file, run `./fetch_web_pages.sh` which will fetch the hmtl pages from SOE and parse them to generate courses.json.

Use `RunTranscript.sh <UCSC Transcript>.pdf` to generate a txt modified transcript that displays course instructor for the subjects we were interested in (cmps, cmpe, math, etc.). Use `RunTranscriptDir.sh <directory name>` to perform the generation for all files within the directory.

You can modify the subjects in `transcript_parse.py`, although currently it only gets teacher names for the current subjects.
