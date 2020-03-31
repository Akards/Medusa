'''Driver function for parallel library'''
from celery import Celery
app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x,y):
    return x+y

def main():
    print("Hello World!")

if __name__ == '__main__':
    main()
