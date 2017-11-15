import datetime

def time_this(original_function):
    def new_function(*args,**kwargs):
    	print args, kwargs
        before = datetime.datetime.now()  
        x = original_function(*args,**kwargs) 
        after = datetime.datetime.now()  
        print "Elapsed Time = {0}".format(after-before)
        return x
    return new_function()



def addNums(a,b):
	return a+b

addNums = time_this(addNums)

print addNums(2,3)