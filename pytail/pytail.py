from time import sleep

def tail(file, fltr):
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

