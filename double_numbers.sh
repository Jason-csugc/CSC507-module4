#!/bin/bash

input_filename='file1.txt'
output_filename='newfile1.txt'

SECONDS=0
start_date_time= date "+%m/%d/%Y %H:%M:%S";
echo $start_date_time;

while read line; do
echo $(($line * 2)) >> $output_filename
done < $input_filename

end_date_time= date "+%m/%d/%Y %H:%M:%S";
echo $end_date_time;
echo "The command took $SECONDS seconds to complete"
