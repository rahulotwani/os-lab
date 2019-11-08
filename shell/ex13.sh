a1=3
mod=$((a1%2))
if [ $mod -eq 0 ]
then echo even
else echo odd
fi
