#pupose: we are doing round robin here.
import multiprocessing
def print_cube(num):
    print("Cube:",(num*num*num))
def print_square(num):
    print("Sqaure:",(num*num))
if __name__=="__main__":
    p1=multiprocessing.Process(target=print_square,args=(10,))
    p2=multiprocessing.Process(target=print_cube,args=(10,))
    #starting process 1
    p1.start()
    #starting process 2
    p2.start()
# wait until process 1 is finished
#p1.join()
# wait until process 2 is finished
#p2.join()
print("Done")
