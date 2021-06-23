# REST API Architecture

You are tasked with designing, building and managing a global REST API that must be able to scale from 50 requests per second to bursts of 2,000 requests per second. Your team have built the API code and provided it to you. Your task is to build the platform that can serve the requests to the API.

The priority of requirements are listed as follows with the most important first.

1. Uptime/Reliability
2. Low Latency
3. Simplicity
4. Cost


In fewer than 8 paragraphs, describe how you would achieve this. Key things to think about are: Overall design, platform choices, any additional tools, management & maintenance.

1. Uptime/Reliability

for upscaling the system we need to know what kind of business it is, are these requests are write heavy or read heavy? What is more important to us availability, consistantcy and partition tolerance(we can opt for only two, CAP theorm), our data base choice will be affected by it. Also we need to know much data we need to store?

so in prespective of database, to gurantee uptime we at least will need to maintain replica of databases in case of system failure


also we need to make sure that our codebase is also running on multiple machines/containers so that if one machine goes down it doesnt affect our availability 

We also should have auto scaling policies in place based on cpu and meory utilisation. Also logs should be archieved regularly and there should be a central place to see all these logs like kibana

Also depending on the team size and scale, we can decide to move to microservices, advantage would be if somethings fails whole application wont go down. just few component wont be working.

We also need to use something like Nginx to rate limit our servers. so no one bombard our servers. and need to block users and ips based on their request counts to save ourself from ddos attacks

2. Low Latency
for low latency we should use caching for apis and as well as databases queries. we can use something like Redis, mamcached etc. Advantage is low latencny and less load on db and recomputations.

We should index our db tables for fater query results (if read heavy)

if we need data from different microservices we can make call in parallel whenever possible.

3. Simplicity
for Simplicity we need to make sure test cases are in place, so changes can be tested easily, CI CD pipeline can be there for faster and simple deploys. Our code should be well documented and well designed. It should be modular, readble and reusable. We shouldn't repeat ourselfs. we should try to make things configrable which allows us to reuse it. Better understanding of business and future requirements can you to design better systems

4. for cost we need to make sure that we arent using too many resources which is under utilised most of the time. So should have down scaling policies in place too. We should be very careful for over engineering something which might not be used ever. So it is all about a good balance for our requirements 

