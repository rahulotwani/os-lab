# -eq equal
# -ne not equal
# if ends with fi
echo "Enter your username"
read username
if [ "$username" = "krishan" ]
then echo "You are a legend"
else echo "Sorry, wrong user"
fi
