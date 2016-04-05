from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:

    # class variables, shared by all objects and class
    project_name = ""
    base_url = ""
    domain_name = ""
    queue_file = ""
    crawled_file = ""
    queue = set()
    crawled = set()

    # constructor function
    def __init__(self, project_name, base_url, domain_name):

        # set class variables
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'

        # call the static method of the class
        Spider.boot()
        Spider.crawl_page("First spider", Spider.base_url)


    # define static method for the class
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_file(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    # define static method for the class
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + " is crawling page_url: " + page_url)
            print("Queue: " + str(len(Spider.queue)) +
                  " | Crawled: " + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))

            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)

            Spider.update_files()

    # define static method for the class
    @staticmethod
    def gather_links(page_url):
        html_string = ""
        try:
            response = urlopen(page_url)
            if response.getheader("Content-Type") == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print("Error: can not crawl page.")
            return set()
        return finder.page_links()

    # define static method for the class
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url not in Spider.queue and url not in Spider.crawled and Spider.domain_name in url:
                Spider.queue.add(url)

    # define static method for the class
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)








