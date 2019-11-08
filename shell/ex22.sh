Hello(){
	echo "Hello, world"
	echo "arguments $1 $2"
	return 10
}
Hello test1 test2
ret=$?
echo "return value is $ret"
