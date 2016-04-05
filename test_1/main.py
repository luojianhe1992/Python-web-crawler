import threading
from queue import Queue

from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'thenewboston'
HOME_PAGE = "http://thenewboston.com/"
DOMAIN_NAME = get_domain_name(HOME_PAGE)

QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'

NUMBER_OR_THREADS = 8

# thread queue
queue = Queue()

# first basic Spider
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

def create_workers():
    # using for loop to create 8 workers
    for _ in range(NUMBER_OR_THREADS):
        # create new thread
        t = threading.Thread(target=work)
        # when we close the main function, the thread close
        t.daemon = True
        # start the thread
        t.start()

# define the work functino for the crawler worker to work
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

# if
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " links in the queue")
        create_jobs()


create_workers()
crawl()





