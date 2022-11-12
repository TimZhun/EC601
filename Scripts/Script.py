from pycvesearch import CVESearch




cve = CVESearch('https://cve.circl.lu')
# print(cve.browse('microsoft'))
print(cve.cpe23('cpe:2.3:a:microsoft:office:2011:-:mac'))
