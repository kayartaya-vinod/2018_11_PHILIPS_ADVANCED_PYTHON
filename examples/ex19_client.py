import socket
import pickle

def main():
	client = socket.socket()
	addr = ('localhost', 9090)
	client.connect(addr)

	while True:
		print('1 - Factorial')
		print('2 - Fibonacii')
		print('3 - Quit')

		choice = int(input('Enter your choice: '))

		if choice<1 or choice>3:
			print('Invalid input. Please try again!')
			continue

		request = {}
		
		if choice==3: 
			request['function_name'] = 'quit'
			request = pickle.dumps(request)
			client.send(request)
			break
		
		num = int(input('Enter a number: '))
		request['args'] = [num]
		
		if choice==1: 
			request['function_name'] = 'factorial'
		elif choice==2:
			request['function_name'] = 'fibo'


		request = pickle.dumps(request)
		client.send(request)
		response = client.recv(1024)
		response = pickle.loads(response)
		print('Response from server:', response)


if __name__ == '__main__':
	main()