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
