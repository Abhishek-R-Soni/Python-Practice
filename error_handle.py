def get(a,b):
	try:
		ans = a/b
	except(ZeroDivisionError,TypeError) as err:
		print("not divisible by Zero!")
		print(err)
	else:
		print(ans)
	finally:
		print("In Finally")

get(2,1)
get(2,0)
