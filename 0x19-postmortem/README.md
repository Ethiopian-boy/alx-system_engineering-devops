
#  Postmortem

Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

* To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
* And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

##  Issue Summary

On November 10th, 2022 from 11:19 AM to 2:25 PM IST, requests to our site resulted in 500 error response messages. The issue affected 100% of users. Users could continue to access other requests that run on separate infrastructure. The root cause of this outage was a misspelt file name in a configuration file.

## Timeline (all times are Indian Standard Time)

* 11:05 Am Configuration pushed
* 11:15 Am Outage begins
* 11:19 Am Error logs checked by DevOps team
* 12:02 PM Failed configuration change rollback
* 1:45 PM Execute puppet manifest across all servers
* 1: 55 PM Server restart begins
* 2: 23 PM 100% restored and back online


## Root Cause and Resolution

At 11:19 AM IST, a configuration change was released to the production environment without being first released to the testing environment. When no errors were found in log files we rolled back the change. At the end a puppet manifest executed across all servers immediately after restoring the service.

## Corrective and Preventative Measures
 
 After we’ve conducted an internal review and analysis of the outage. It has been decided we can prevent this in the future by:

 * Test before deploying on all servers no matter how small change is
* Modifying the configuration files for more error logging for quick response
* Develop better mechanisms for quickly delivering status notifications during incidents.

`Thanks for your patience and continued confidence in us.`

## Authors

- [@Mulubrhan birhanu](https://github.com/Ethiopian-boy)

