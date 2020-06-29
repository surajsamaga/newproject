from scrape import getdata
import sys
if __name__=='__main__':
    if len(sys.argv) ==2:
        getdata(sys.argv[1])
        sys.exit()
    else:
        print('one argument only!')
        sys.exit()