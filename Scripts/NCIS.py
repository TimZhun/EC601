import os
import sys
import nvdlib

def checkCVE(searchWord):
    cve_item = nvdlib.searchCVE(keyword=searchWord, exactMatch = False)

    for each in cve_item:        
        print('Potential threat: ',each.id)
        print('Score ',each.score)
        print('URL ',each.url)


def checkCVE2():
    # r = nvdlib.searchCVE(cpeName = 'cpe:2.3:a:microsoft:exchange_server:2013:cumulative_update_11:*:*:*:*:*:*', keyword = '1ArcServe', )
    cve_item = nvdlib.searchCVE(keyword = 'httpd 2.4.50', exactMatch = False)
    dict = []
    dict.append(cve_item)
    for each in cve_item:
        for i in each:

         print('Potential threat: ',i)



def readDockerFile(path):
    with open(path,"r") as fi:
        id = []
        user = []
        exposed =[]
        for ln in fi:
            if ln.startswith("FROM"):
                id.append(ln[5:])
            if ln.startswith("USER"):
                user.append(ln[5:])
            if ln.startswith("EXPOSE"):
                exposed.append(ln[7:])

    fFrom = str(id)
  
    if (fFrom.find('/')>0):
        twowords = fFrom.split('/') #removes /
        words = twowords[1].split(':') #removes :

        software = words[0]

        mod_version = str(words[1])
        size = len(mod_version)
        version = mod_version[:size-4]

    else:
        words = fFrom.split(':') #removes :
  
        mod_software = str(words[0])
        size = len(mod_software)
        software = mod_software[2:]

        mod_version = str(words[1])
        size = len(mod_version)
        version = mod_version[:size-4]
    result = software+' '+version

    if user:
        print("User running:", user[0])
    else:
        print("User is not defined running as root!")

    if exposed:
        print("Exposed port:", exposed[0])
    else:
        print("No exposed ports")

    print("Running software:", result)
    print("Possible CVE Vulnerabilities:")
    return(result)


# os.system("docker history python")
# os.system("docker history python > HistoryFile.txt ")
# os.system("docker history --format "{{.ID}}: {{.CreatedBy}}" python --no-trunc > HistoryFile.txt")

 

# checkCVE('httpd 2.4.50')
# check = readDockerFile("/Users/timurzhunusov/Downloads/vulhub-master/httpd/CVE-2021-42013/Dockerfile")
# check = readDockerFile("/Users/timurzhunusov/Documents/GitHub/EC601/Scripts/dockerfile_examples/CentosHttpd")
# /Users/timurzhunusov/Downloads/vulhub-master/base/php/5.4.1/cgi/

# checkCVE(check)
# checkCVE2()


def main():
    
    print("Type the path to Docker Container")
    path=input()
    dir_list = os.listdir(path)
    for each in dir_list:
        if (each == 'Dockerfile'):
            dockerfile = each
    final_path = (path+dockerfile)
    check = readDockerFile(final_path)
    checkCVE(check)


if __name__ == '__main__':
 main()