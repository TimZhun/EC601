import os
import subprocess
import time
import sys
import nvdlib

API_KEY = os.getenv("GITGUARDIAN_API_KEY", "")
FILENAME = ".env"
API_KEY="91Fa973FaC8fAadEc478726def6d9C0Aedf3Aa1049eaDa397C8aC5B6c13dDd1586d665d"
DOCUMENT = """
    import urllib.request
    url = 'http://jen_barber:correcthorsebatterystaple@cake.gitguardian.com/isreal.json'
    response = urllib.request.urlopen(url)
    consume(response.read())"
"""

# Checks in CVE database
def checkCVE(searchWord):
    cve_item = nvdlib.searchCVE(keywordSearch=searchWord, keywordExactMatch = False)

    for each in cve_item:        
        print('Potential threat: ',each.id)
        print('Score ',each.score)
        print('URL ',each.url)
    if not cve_item:
        print("Nothing found")

# Second check for testing
def checkCVE2():
    # r = nvdlib.searchCVE(cpeName = 'cpe:2.3:a:microsoft:exchange_server:2013:cumulative_update_11:*:*:*:*:*:*', keyword = '1ArcServe', )
    cve_item = nvdlib.searchCVE(keywordSearch = 'httpd 2.4.50', keywordExactMatch = False)
    dict = []
    dict.append(cve_item)
    for each in cve_item:
        for i in each:

         print('Potential threat: ',i)


# Reads DockerFile
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
        print("No ports assigned in Dockerfile, please check for opened ports")
    print("Ports used by Docker right now:")
    os.system("docker ps")
    print(" ")

    print("Running software:", result)
    print("Possible CVE Vulnerabilities:")
    return(result)

# Calling docker pull and then scanning
def pulldocker(docekrcontainer):
    os.system("docker pull " + docekrcontainer)
    cmd = subprocess.Popen('docker image history '+docekrcontainer+' --format \"table{{.CreatedBy}}\" --no-trunc', shell=True, stdout=subprocess.PIPE)
    # print(cmd.stdout)
    hExpose = []
    hVersion = []
    for line in cmd.stdout:
        if (bytes("EXPOSE", 'utf-8') in line):
            hExpose = line[26:].decode("utf-8")
            
        if (bytes("/bin/sh -c #(nop)  ENV ", 'utf-8') in line):
            if (bytes("_VERSION", 'utf-8') in line):
                hVersion.append(line[23:].decode("utf-8") )
                
    
    finalVersion = []
    for rows in hVersion:
        index = rows.find ( "_VERSION" )
        index2 = rows.find(".el8\n")
        if index > 0:
            finalVersion.append(rows[:index]+" "+rows[index+9:index2])
    print("Exposed ports: ",hExpose)
    for soft in finalVersion:
        print("Vulnerabilies for: ",soft)
        checkCVE(soft)
        time.sleep(5)

# os.system("docker history python")
# os.system("docker history python > HistoryFile.txt ")
# os.system("docker history --format "{{.ID}}: {{.CreatedBy}}" python --no-trunc > HistoryFile.txt")

 

# checkCVE('httpd 2.4.50')
# check = readDockerFile("/Users/zta/Documents/GitHub/EC601_Project1/Scripts/dockerfile_examples/CVE-2021-41773/")
# check = readDockerFile("/Users/timurzhunusov/Documents/GitHub/EC601/Scripts/dockerfile_examples/CentosHttpd")
# /Users/timurzhunusov/Downloads/vulhub-master/base/php/5.4.1/cgi/

# checkCVE(check)
# checkCVE2()


def main():
    # checkCVE2()
    print("Please press a for scaning a folder")
    print("Please press b for scanning dockerhub container")
    x = input()
    print(x)
    if x == "a":
        print("Type the path to Docker Container")
        path=input()
        dir_list = os.listdir(path)
        goodcheck = 0
        for each in dir_list:
            if (each == 'Dockerfile'):
                dockerfile = each
                goodcheck = 1
        if (goodcheck):
            final_path = (path+dockerfile)
            check = readDockerFile(final_path)
            checkCVE(check)
            print("Search for secrets:")
            os.system('ggshield secret scan --show-secrets path --recursive "%s"' % path)
        else:
            print("Couldnt find Dockerfile in directory",path);
    if x == "b":
        print("Please enter the name of dockercontainer")
        container = input()

        pulldocker(container)
        print("Search for secrets:")
        os.system('ggshield secret scan docker "%s"' % container)
        

        

if __name__ == '__main__':
 main()

