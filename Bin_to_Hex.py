import re
import numpy as np


class BinToHex:
    def __init__(self):
        self.hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
        self.binar = []

    def convert(self):

        while True:
            binaryNum = input('Enter your binary Number: ')
            numB = re.findall('[^0-1]', binaryNum) #find all number and letter except 0 or 1


            try:
                if not (numB):
                    binaryNum = [int(i) for i in binaryNum]
                    hexaValue = []
                    for i in binaryNum:
                        binar.insert(0, int(i))


                    length_Loop = 0
                    if (len(binar)) <= 4:
                        length_Loop = 1
                    elif len(binar) > 4:
                        length_Loop = len(binar) // 4
                        if (len(binar) % 4) < 4 and (len(binar) % 4) > 0:
                            length_Loop += 1


                    first = 0
                    last = 4
                    for _ in range(0, length_Loop):
                        exponent = [1, 2, 4, 8]
                        separateBinary = binar[first:last]
                        exponentMultiply = [exponent[i] for i in range(len(binar[first:last]))]
                        resultExponent = np.multiply(separateBinary, exponentMultiply)
                        hexaValue.append(self.hexa[sum(resultExponent)])

                        first += 4
                        last += 4

                    hexaValue.reverse()
                    print(hexaValue)
                    hexaValue.clear()
                else:
                    print('Invalid input, try again!')
            except Exception as e:
                print(e)

b = BinToHex()
b.convert()