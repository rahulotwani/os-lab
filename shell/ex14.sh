read age
if [ $age -ge 60 ]
then echo senior
elif [ $age -ge 18 ]
then echo adult
else echo child
fi
