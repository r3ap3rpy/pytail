from time import sleep
from errno import EACCES
def tail(file, fltr):
    try:
        with open(file) as tailed:
            tailed.seek(0,2)
            while True:
                try:
                    line = tailed.readline()
                    if line:
                        if fltr:
                            if not fltr.upper() in line.upper():
                                continue
                        yield line.strip()
                    sleep(.1)
                except KeyboardInterrupt:
                    print("\r" + ("#" * 30))
                    print("# End of tailing!")
                    break
    except IOError as x:
        if x.errno == EACCES:
            print(f"# The specified file: {file} cannot be read!")
        else:
            print(f"# Other error: {x}")
        print("#"*30)
        exit(-1)
