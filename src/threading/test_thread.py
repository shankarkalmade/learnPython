import threading
import time

def worker():
    print "worker started : %s " % threading.current_thread().getName()
    time.sleep(3)
    print "worker Exiting : %s " % threading.current_thread().getName()
    return


def matser():
    print "master started.. "
    time.sleep(1)
    print "Master Exiting.."
    return




worker_1 = threading.Thread(name="Worker_1", target=worker)
worker_2 = threading.Thread(name="Worker_2", target=worker)
master = threading.Thread(name="Master",target=matser)


worker_1.start()
worker_2.start()
master.start()




