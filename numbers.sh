#!/bin/bash

SECONDS=0
start_date_time= date "+%m/%d/%Y %H:%M:%S";
echo $start_date_time;

for i in $(seq 1 1000000);
do
	echo $RANDOM >> file1.txt
done

end_date_time= date "+%m/%d/%Y %H:%M:%S";
echo $end_date_time;
echo "The command took $SECONDS seconds to complete"
