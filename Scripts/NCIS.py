from pickle import TRUE
import nvdlib

def checkCVE(searchWord):
    r = nvdlib.searchCPE(keyword=searchWord)
    print(r)

def readDockerFile(path):
    with open(path,"r") as fi:
        id = []
        for ln in fi:
            if ln.startswith("FROM"):
                id.append(ln[5:])

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
    print(result)
    return(result)



# checkCVE('httpd 2.4.50')
check = readDockerFile("/Users/timurzhunusov/Downloads/vulhub-master/httpd/CVE-2021-42013/Dockerfile")
checkCVE(check)