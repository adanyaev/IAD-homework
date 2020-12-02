import time

def execution_time(f):
	def decorated(*args, **kwargs):
		t1 = time.time()
		r = f(*args, **kwargs)
		print("{} is executed in {} seconds".format(f.__name__, time.time() - t1))
		return r
	return decorated

def save_args_to_file(f):
	def decorated(*args, **kwargs):
		with open('args.txt', 'w') as file:
			file.write("{} function\n".format(f.__name__))
			file.write("Positional args: ")
			for i in args:
				file.write(str(i) + ' ')
			file.write("\nKeyword args: ")
			for i in kwargs:
				file.write("{}={} ".format(i, kwargs[i]))
		r = f(*args, **kwargs)
		return r
	return decorated


def save_args(f):
	results = {}
	def decorated(*args):
		if args in results.keys():
			return results[args]		
		r = f(*args)
		results[args] = r
		return r
	return decorated 


def sleep_n_seconds(n):
	def decorator(f):
		def decorated(*args, **kwargs):
			time.sleep(n)
			r = f(*args, **kwargs)
			time.sleep(n)
			return r
		return decorated
	return decorator


@sleep_n_seconds(1)
def fibonacci(n):
	p = 1
	nx = 1
	for i in range(n-2):
		t = p
		p = nx
		nx += t
	return nx


print(fibonacci(6666))


