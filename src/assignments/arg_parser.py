import getopt, sys

def parse_arg():
    print "parsing"

    try:
        opts , args = getopt.getopt(sys.argv[1:],"ho:v",["help", "output="])
    except getopt.GetoptError as error:
        print str(error)
        sys.exit(2)

    output = None
    verbose= False

    for o, a in opts:
        if o =="-V":
            verbose = True
        elif o in ("-h", "-help", "--help", "--h"):
                print "requesting help"
        elif o in ("-o", "--o"):
            output =a
    if verbose == True:
        print "asking for verbose"
    if output != None:
        print "output file" + a






if __name__ == "__main__":
    parse_arg()




















