# Technology (Under construction)

## System Architecture

The system is a standard client-server web application, built on the Django framework, with the following major
architectural additions:

* **Multi-tenanting**, to allow the web server to support a number of brigades. 
  
* **Channels/websockets**, that allow bi-directional communication between the client and server. These are used to enable
asynchronous updates of web pages when external events such as tagging in occur.

* **Load balancing** and on-demand scaling, provided by AWS Elastic Beanstalk. Under load, the system will automatically
adjust by adding more servers and network capacity within defined bounds, and will offload these when demand drops.
  
* **Traffic splitting** to allow continuous operations even through system updates.
  
* **Access control** to the web application is through User accounts, with usernames and passwords required for any access 
  to the server. This leverages [Django's excellent User Authentication](https://docs.djangoproject.com/en/4.0/topics/auth/#user-authentication-in-django)
  system, which includes granular permission setting by group and for individual users.
  
* **Fast relational database support** is provided using **PostgreSQL**, which also provides native support for the 
  partitioning used in multi-tenanting. All data is backed up daily inside the secure AWS infrastructure.


## Security

Although RFSTAG does not store particularly sensitive personal data, 
- take security seriously
- 

The RFSTAG web application is built using the Django platform, which has 
[effective protections](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/web_application_security) 
against a number of common threats, including XSS and CSRF attacks.

Details of Django's security features are available [here](https://docs.djangoproject.com/en/4.1/topics/security/), 
but the following is a summary of the main protections:

* Access to the brigade sites requires a registered user name, and password. User names are issued by the brigade 
  administrator, and passwords are set by the user.
  
* Personal data for Members stored on the system is limited to member name (required), email address (required) 
  and mobile phone number (optional). 

  * An email address is required so that the Member can reset their password. It does not have to be the primary email 
    address of the Member, and eg. an RFS email address may be used if preferred.
    
  * Mobile phone numbers are not required, though if they are supplied, they will be shared with other Members 
    for their convenience.
    
* RFSTAG can only be accessed using secure connection (https). This means that the connection between the user and the 
  server is encrypted, and cannot be intercepted. 
  
* Additional protections, including HTTP Strict Transport Security (HSTS), Cross site scripting (XSS), Cross site request 
  forgery (CSRF), and all others directly supported by Django are also included in the web application. 
  
* [RFSTAG](https://observatory.mozilla.org/analyze/rfstag.org) is rated as B (secure), by mozilla, which is higher 
  than most sites, including [activ](https://observatory.mozilla.org/analyze/activ.rfs.nsw.gov.au) (rated F).
  
* Data is held on a Relational Database System (RDS) stored within Amazon Web Services. Only the web application can 
  access the database, and access to the web application is restricted to registered users.
  

    






## Hardware

### Kiosk

### NFC

### Server

t2.medium used as main server. Up to 4 servers can be deployed if demand requires.

## Software

### Django

### Forms

### Calendar

### Channels

(multi-tenant-tech)=
### Multi-tenant

Each brigade has its own database, including the list of members, and you can only login to a brigade system if you 
are a member there. Once you are logged in, you can only access data for your own brigade, and you won't see data for 
any other brigades. 

### Database

PostgreSQL is used as the back-end. [Django's Object-Relational Mapper (ORM)](https://opensource.com/article/17/11/django-orm)
is used to access the database, so there is very little raw SQL in the system.


### Admin

### User Authentication

### html/css

If not completed in 15 minutes, forms will be automatically removed, and the screen will return 
to the normal Kiosk view to allow members to continue signing in and out.

### Configuration Management

### Development Environment

### Automated Testing

### NFC drivers

## Raspberry PI

### Installation of Kiosk

### Networking

### Troubleshooting


## Operations

### AWS Elastic Beanstalk

### Server Deployment

### Cache

### Database

### Security

### Documentation

### Configuration Management (github)

### PI deployment

### PI remote access

### Pager sub-system
