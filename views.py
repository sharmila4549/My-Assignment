from django.shortcuts import render
import timeit


def demo(request):

	return render(request,'index.html')


def fib(request):

	start = timeit.timeit()
	m = "Please enter integer number"
	
	
	n = int(request.POST['num'])
		
	s = 1
	s1 = 1
	for i in range(n):
		if i == 0:
			c = s

		elif i == 1:
			c = s1

		else:

			c = s1 + s
			s = s1
			s1 = c 

	end = timeit.timeit()

	total_time = end - start


	return render(request,'result.html',{'res':c,'time':total_time})


		 
