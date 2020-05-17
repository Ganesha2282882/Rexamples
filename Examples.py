def fserver():
  from flask import Flask
  app = Flask('app')

  @app.route('/')
  def hello_world():
    return 'Hello, World!'

  app.run(host='0.0.0.0', port=8080)

def nput():
  name = input('What is your name?\n')
  print('Hi, %s.' % name)

def ftorial():
  def factorial(n):
    if n == 0:
      return 1
    else:
      return n * factorial(n - 1)
  print(factorial(5))

def hello():
  print('Hello World!')

def floop():
  for i in range(5):
    print('A number:', i)

if __name__ == '__main__':
  print("Oops, you need to run this as a package!")
