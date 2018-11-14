import socket
import threading
import pickle

def factorial(num):
	if num<=1: return 1
	return num * factorial(num-1)

def fibo(limit):
	nums = []
	a, b = -1, 1
	for i in range(0, limit):
		c = a + b
		nums += [c]
		a, b = b, c
	return nums

available_functions = dict()
available_functions['factorial'] = factorial
available_functions['fibo'] = fibo

class ClientHandler(threading.Thread):
	def __init__(self, client):
		threading.Thread.__init__(self)
		self.__client = client

	def run(self):
		client = self.__client
		while True:
			input = client.recv(1024)
			input = pickle.loads(input)
			fn_name = input['function_name']
			if fn_name == 'quit': break
			fn = available_functions.get(fn_name)
			if fn!=None:
				args = input.get('args')
				output = fn(*args)
				output = pickle.dumps(output)
				client.send(output)

		client.close()


def main():
	server = socket.socket()
	addr = ('', 9090)
	server.bind(addr)
	server.listen()


	while True:
		cl_socket, cl_addr = server.accept()
		ClientHandler(cl_socket).start()

if __name__ == '__main__':
	main()
