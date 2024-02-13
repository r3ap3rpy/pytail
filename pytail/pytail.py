from time import sleep

def tail(file):
    with open(file) as tailed:
        tailed.seek(0,2)
        while True:
            try:
                line = tailed.readline()
                if line:
                    yield line.strip()
                sleep(.1)
            except KeyboardInterrupt:
                print("\r# End of tailing!")
                break

