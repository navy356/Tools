import string
import Cursors
import sys 

class Helpers:
    @staticmethod
    def binSearch(low: int, high: int, check, display: bool, **kwargs):
        mid = 0
        arr = kwargs.get('arr',None)
        i = kwargs.get('index',None)

        while low <= high:
            mid = (low+high)//2

            if arr:
                if display:
                    sys.stdout.write("Trying {} - {}\r".format(arr[mid],mid))
                    sys.stdout.flush()
                    sys.stdout.write(Cursors.ERASE_LINE)
                if check(i,arr[mid]): #true is high
                    low = mid + 1

                elif check(i,arr[mid]): #false is low
                    high = mid - 1

                else:
                    return mid

            else:
                if display:
                    sys.stdout.write("Trying {}\r".format(mid))
                    sys.stdout.flush()
                    sys.stdout.write(Cursors.ERASE_LINE)

                if check(mid): #true is high
                    low = mid + 1

                elif check(mid): #false is low
                    high = mid - 1

                else:
                    return mid

        
        return -1

    @staticmethod
    def getOptions():
        dict={
            "warning" : True,
            "charset" : string.printable,
            "compareChar" : None,
            "checkChar" : None,
            "display" : True,
            "len" : -1,
            "compareLen" : None,
            "checkLen" : None,
            "maxLen" : 100,
            "minLen" : 0,
            "flag" : ''
        }
        return dict
