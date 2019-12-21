#!/usr/bin/env python
import time

if __name__ == '__main__':
        while 1:

                file = open('/dev/myled0','w')
                file.write('1\n')
                time.sleep(0.2)

                file = open('/dev/myled0','w')
                file.write('2\n')
                time.sleep(0.2)

                file = open('/dev/myled0','w')
                file.write('3\n')
                time.sleep(0.2)

                file = open('/dev/myled0','w')
                file.write('4\n')
                time.sleep(0.2)
                
                file = open('/dev/myled0','w')
                file.write('5\n')
                time.sleep(0.2)
