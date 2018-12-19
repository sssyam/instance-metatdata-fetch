#! /usr/bin/python
import os
import datetime
import requests

def parse_MD(path, url):
    files = str(requests.get(url).text).split()
    for i in files:
        if i[-1] == '/':
            if os.path.exists(path + i) == False:
                os.mkdir(path + i)
                parse_MD(path+i, url+i)
            else:
                with open(path + i,"w") as f:
                    content = str(requests.get(url + i).text)
                    f.write(content + "\n")

def main():
    url="http://instance-data/latest/meta-data/"
    home="/meta-data/"

    if os.path.exists(home) == False:
        os.mkdir(home)

    start_time = datetime.datetime.utcnow().strftime("%d %B, %Y at %H:%M:%S UTC")
    with open(home+".start_time","w") as f:
        f.write("Start Time: " + start_time + "\n")

    parse_MD(home, url)

    end_time = datetime.datetime.utcnow().strftime("%d %B, %Y at %H:%M:%S UTC")
    with open(home+".end_time","w") as f:
        f.write("End Time: " + end_time + "\n")

if __name__ == "__main__":
    main()
