from pycvesearch import CVESearch


# def checkCVE()
cve = CVESearch('https://cve.circl.lu')
print(cve.cvefor('cpe:/a:microsoft:office:2011::mac'))
