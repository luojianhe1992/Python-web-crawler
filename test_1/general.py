import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_data_file(project_name, base_url):
    create_project_dir(project_name)
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, '')

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def delete_file_content(path):
    with open(path, 'w') as file:
        file.write("")

# read file content and make it into set
def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as file:
        for line in file:
            result.add(line.replace('\n', ''))
    return result

# read the set content and write it into file
def set_to_file(links, file_name):
    delete_file_content(file_name)
    for link in sorted(links):
        append_to_file(file_name, link)










