from pycvesearch import CVESearch



cve = CVESearch('https://cve.circl.lu')
print(cve.cvefor('cpe:/a:microsoft:office:2011::mac'))
