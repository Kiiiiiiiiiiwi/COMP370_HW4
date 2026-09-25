#!/bin/bash

main="$1"
output_file="$2"

count=$(grep "$main" data/clean_dialog.csv | wc -l)
total=$(wc -l < data/clean_dialog.csv)

percentage=$(echo "scale=4; $count / $total" | bc)

echo "$main, $count, $percentage" >> $output_file