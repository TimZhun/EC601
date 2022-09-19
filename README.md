**Problem Statement/Applications**

The simplest way to explain DevOps, is to imagine it as the idea to help people work together in a convenient way by building and deploying secure software at top speed. DevOps practices enable software developers (devs) and operations (ops) teams to accelerate delivery through automation, collaboration, fast feedback, and iterative improvement [[1]](**[https://about.gitlab.com/topics/devops/](https://about.gitlab.com/topics/devops/)**). It is achieved by refactoring the old monlyth model of development to microservices and cloud-computing. To elaborate, DevOps is not a single tool it is a set of different tools that each team chooses depending on a project that helps them deploy faster. One of the popular examples is Docker, Jenkins, Git, Kubernetes, Ansible, Selenium, ELK, Nagios etc. 

![enter image description here](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/06/DevOps-Tools-DevOps-Tutorial-Edureka-1.png)

Since the 2000s due to its convenience and speed this way of designing, developing and deploying has become favored, basically disrupting other models of developing.

**DevOps application**

Devops can be implemented by any project or team from car manufacturers to the financial sector now it is ubiquitous. According to cloudify - Apple is using 74 different DevOps tools, Stripe and Google 59, and even Docker which is DevOps tool itself uses 55 different DevOps tools. Every major cloud vendor such as AWS, Azure, GCP is using and offering DevOps tools [[2]](https://cloudify.co/blog/our-top-three-devops-challenges/). Great example is the Amazon case -in early stage they used to sell books online using old monolith infrastructure, slowly they realized that to grow faster and scale better they have to move to cloud based systems [[3](https://www.edureka.co/blog/companies-using-devops/)]. And the best option at a time was building it by themselves for themselves. It was their first step in DevOps. It worked out great, microservice architecture recuiered less compute power and they decided to sell excess of it to others. They became so good at it they are now leaders in this field and in 2021 AMS generated 74% of operating profit compared to 26% by other e-commerce sectors [[4]](https://www.visualcapitalist.com/aws-powering-the-internet-and-amazons-profits/).

Netflix- “Netflix is one of the first companies to have successfully migrated from a traditional monolithic to cloud-based microservices architecture [[5]](https://www.geeksforgeeks.org/the-story-of-netflix-and-microservices/) . In fact, Netflix implemented this architecture long before the term microservices was even introduced. It took more than two years for Netflix to achieve complete migration to the cloud. Not only did Netflix perfect the use of microservices but it also managed to open source many of the tools which were used to build it [5]. This to major steps taken by these two companies is one of the reasons where DevOps is today.

**Current research**

Previously the idea of DevOps included two parts dev and ops which are correct, but cybersecurity in modern days is always a mandatory part of any software. Traditional way is to build a project then give it to cybersecurity team which will provide 30 pages recommendations about how to secure the project. What meant refactoring the code again, spending precious time on it.
	In the modern DevOps approach, the cybersecurity team will work with DevOps teams to create the project together. It is necessary for Cybersecurity professionals to participate in the process, communicate with other developers, and provide test cases on the same level as the coding and deployment part [6]. So basically they stuck Sec in the middle of Dev and Ops, sometimes it even written as DevSecOps.

**Container security**

Because cybersecurity is a very difficult subject, the best place to start is from the beginning, hence from service where it all would be deployed. One of the main tools for this is Docker containers and orchestrators. DevOps checks whether the software contains vulnerabilities through static and dynamic tests, fuzz testing, and dependency scanning. Security teams look for ways to identify vulnerabilities during development with actionable information to empower dev to remediate vulnerabilities earlier in the life cycle, one of the earliest stages is building containers [[7]](**[https://about.gitlab.com/topics/devsecops/what-is-fuzz-testing/](https://about.gitlab.com/topics/devsecops/what-is-fuzz-testing/)**).

Container security is important because the container image contains all the written code for applications, libraries and dependencies that will run inside. Losing container security might mean potential breach of data. However container is one of most secure parts of DevOps because it contains bare basic minimum to run trying to keep it simple.

Few common step in securing containers [[8]](**[https://snyk.io/blog/10-docker-image-security-best-practices/](https://snyk.io/blog/10-docker-image-security-best-practices/)**):

1.  Choosing the right base image from a trusted source and keeping it small
2.  Using multi-stage builds
3.  Rebuilding images
4.  Scanning images during development
5.  Scanning images during production
    

  
  
  

AI in cybersecurity

AI and machine learning (ML) are still maturing in their applications for DevOps, but there is plenty for organizations to take advantage of today, including using the technology to make sense of test data [[9]](https://www.veritis.com/blog/ai-powered-ml-driven-the-new-devops-trend/).

There are lots of applications for ML in software development and cybersecurity in DevOps. For example ML can help find vulnerabilities in code before submitting it or scan large log files for inconsistencies and odd behavior.

AI and ML can save developers and operations professionals time by learning how they work best, making suggestions within workflows, and automatically provisioning preferred infrastructure configurations.

**Conclusion**

In conclusion, the use of DevOps as an idea is not limited by software so it can be implemented for any use and because it is dominating over other models of development it has great potential. There are already implementations of Cybersecurity AI and ML in DevOps so for next decade this field has great potential to grow even more broader.

  
  

1 [https://about.gitlab.com/topics/devops/](https://about.gitlab.com/topics/devops/)

2 [https://cloudify.co/blog/our-top-three-devops-challenges/](https://cloudify.co/blog/our-top-three-devops-challenges/)

3 [https://www.edureka.co/blog/companies-using-devops/](https://www.edureka.co/blog/companies-using-devops/)

4 [https://www.visualcapitalist.com/aws-powering-the-internet-and-amazons-profits/](https://www.visualcapitalist.com/aws-powering-the-internet-and-amazons-profits/)

5 ​​https://www.geeksforgeeks.org/the-story-of-netflix-and-microservices/

6 [https://www.lehman.edu/itr/documents/10-reasons-you-should-consider-a-career-in-cybersecurity-upload.pdf](https://www.lehman.edu/itr/documents/10-reasons-you-should-consider-a-career-in-cybersecurity-upload.pdf)

7 [https://about.gitlab.com/topics/devsecops/what-is-fuzz-testing/](https://about.gitlab.com/topics/devsecops/what-is-fuzz-testing/)

8 [https://snyk.io/blog/10-docker-image-security-best-practices/](https://snyk.io/blog/10-docker-image-security-best-practices/)

9 https://www.veritis.com/blog/ai-powered-ml-driven-the-new-devops-trend/
