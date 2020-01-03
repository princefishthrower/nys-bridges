#!/bin/bash
for f in data/*.pdf; do
	sudo java -jar /Users/chris/Downloads/tabula-1.0.1-jar-with-dependencies.jar -p all -a 14.22,58.94,553.2,769.47 -o $f.csv $f
done
