from datetime import datetime as dt
from random import randint

class Result:
    def __int__(self, result):
        self.result = dict(result)

    def main_threads(self):
        """ create a function to return even and odd number """
        while True:
            data = randint(10, 20)
            self.result = {"date":dt.now().strftime('%Y-%m-%d %H:%M:%S'), "data":data}
            if data %2 ==0:
                self.result['status'] = "even"
            else:
                self.result['status'] = "odd"

            return self.result
# def main():


if __name__ == '__main__':
    main()


