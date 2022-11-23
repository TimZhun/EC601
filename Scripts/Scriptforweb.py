import os
import subprocess

def pulldocker(docekrcontainer):
    # os.system("docker pull " + docekrcontainer)
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
    print(finalVersion)

pulldocker("mysql")


# result = []
# result = os.popen('docker image history mongo --format \"table{{.CreatedBy}}\" --no-trunc').read()
# print(result)
# # os.system("docker history python --no-trunc > HistoryFile.txt")
# # for rows in result:
    
# #     print(rows)

            
#             if os.system(str(cline)):
#     raise RuntimeError('program {} failed!'.format(str(cline)))
# blast_out=open(type+".BLAST")
