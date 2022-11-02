import os

import nvdlib

def checkCVE(searchWord):
    r = nvdlib.searchCPE(keyword=searchWord)
    print(r)

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
check = readDockerFile("/Users/timurzhunusov/Downloads/vulhub-master/httpd/CVE-2021-42013/Dockerfile")
# check = readDockerFile("/Users/timurzhunusov/Documents/GitHub/EC601/Scripts/dockerfile_examples/CentosHttpd")

checkCVE(check)