from multiprocessing import Process,Array,Value
def square_list(mylist,result,square_sum):
	for idx, num in enumerate(mylist):
		result[idx]=num*num
	square_sum.value=sum(result)
	print("Result(in process p1): {}".format(result[:]))
	print("Sum of Squares(in process p1): {}".format(square_sum.value))
if __name__=="__main__":
	mylist=[1,2,3,4]
	#creating array of int data type with 4 size
	'''
	VERYYYY IMPORTANTTT

	'''
	result=Array('i',4)
	#creating value of int data type
	square_sum=Value('i')
	#creating new process
	p1=Process(target=square_list, args=(mylist,result,square_sum))
	p1.start()
	p1.join()
	print("Result(in main program): {}".format(result[:]))
	print("Sum of Squares(in main program): {}".format(square_sum.value))