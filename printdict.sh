#/bin/bash
if [ $1 = quote ]
then
  cat output.txt | sort -n | awk 'BEGIN {FS=":"}{print "\"" $2 "\",\"" $3 "\""}'
else
  cat output.txt | sort -n | awk 'BEGIN {FS=":"}{print $2 "," $3 }'
fi
echo $1
