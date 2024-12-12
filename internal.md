# Internal Procedures (Under construction)

```{margin} Restricted Access
For internal use only
```

## Adding a New Brigade

### Data Required from Brigade

The brigade should provide the following details, preferably in an Excel spreadsheet:

* All Member Details (preferably from onerfs "Brigade Personnel Response Analysis" report), including
  * Firezone number
  * First Name
  * Last Name
  * Preferred First Name
  * Mobile number
  * Email address
  * Date Joined
  * Date of Birth
  * Active status (yes/no)
  * Member Type (Operational/Reserve/Social/Administration/Support)

* Member Qualifications 
  * Brigade manager to obtain "Qualification Report" from onerfs Team Reports
  * see here for details: [Member Qualifications](https://rfstag-user.netlify.app/administration.html#synchronising-qualifications-with-sap).

* Current Officers (for all Field and Admin positions)
  * Member Name
  * Member FireZone number 
  * Position Title
  
* Brigade Vehicles
  * Full name (e.g. Wyee Point 1A)
  * Abbrev name, eg. WP-1A
  * Make, eg. Isuzu
  * Category (eg. 1, 7, 9, ...)
  * Year
  * Crew capacity
  * Aircraft Code
    
* Brigade Settings
  * see {ref}`Brigade Settings section<brig-sett>` above
  * This can be done last, after all of the above

### Hardware Order Parts List

* Raspberry PI
  * PI 4 2Gb RAM
  * PI 4 case
  * Micro HDMI cable
  * PI 4 power supply
  * 16Gb SD RAM card
  
* Tags
  * Sony PaSoRi RC-S380 card reader (USB)
  * 100 x 13.56MHz NTAG215 NFC Key Fob Tags

### Equipment to be Provided by Brigade

* Kiosk
  * Computer monitor with HDMI connection (can be touchscreen if available)
  * USB Mouse (preferably wired)
  * USB Keyboard (preferably wired)
  
* Wi-Fi connection
  * SSID and password  


### Adding a New Tenant Schema

Optional steps (when building schema on tst system) shown in <span class="opt">italics</span>.

Overview:

* Make a backup of the latest prd RDS -> bushfire2-prd-YYMMDD

  * [Revised procedure](https://stackoverflow.com/questions/56462616/how-to-use-pg-restore-with-aws-rds-correctly-to-restore-postgresql-database)
    * cd ~/kbfb/aws-backups/tst2$ 
      * **pg_dump** -h bushfire2-prd-rds5.c5b4rv0axnji.ap-southeast-2.rds.amazonaws.com -U ian -Fc ebdb2 > bushfire2-prd-rds2-240731.dump
      * Password: ib15…
  * Create new RDS in ec2 called bushfire2-prd-rds2-240731
    * **pg_restore** -h ec2-13-211-99-59.ap-southeast-2.compute.amazonaws.com -p 5432 --no-owner --no-privileges --role=ian -d bushfire2-prd-rds2-240731 bushfire2-prd-rds2-240731.dump

* Create a new empty database called bushfire2-prd-YYMMDD in the EC2 postgres server
* Restore the prd backup to the new EC2 database
* Make the tpad env point to the new EC2 database
* Run bushfire2 on tpad, and complete set up and population as below
* Update the config of tst6 using the AWS EB Console to point to the new EC2 tst6 database
* Check everything runs ok at <newbrigade>.rfstag.org
* If all ok, repeat the set up and population on the prd AWS RDS
  * Do the initial setup by connecting tpad to the prd AWS RDS
  * Restart the PRD EB instance to clear all caches
  * Check all works on <newbrigade>.rfstag.com

* Make backups of any target databases using pgadmin
  * Make backup of AWS production database (ebdb) on dev system using pgadmin
    * Set inbound rule on RDS security group for MyIP if needed
  * <span class="opt">Create a new empty database bushfire2-prd-YYMMDD on the EC2 postgresql using pgadmin</span>
  * <span class="opt">Restore backup of AWS production database to the new EC2 database using EC2 postgresql</span>

Procedure

* In pycharm project bushfire2: 
  * In bushfire/settings/.env set RDS_HOSTNAME=<span class="opt">"ec2-13-211-99-59.ap-southeast-2.compute.amazonaws.com"</span>
    * Also set RDS_DB_NAME=bushfire2-prd-YYMMDD in .env
  * Check all migrations in all apps saved in github  
  * Add new tenant name to settings.base.CUSTOMER_LIST
  * Run/Edit Configurations
     * Env vars: PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=bushfire.settings.local
     * Working directory: ~/PycharmProjects/bushfire2
     * Script path: /home/ian/PycharmProjects/bushfire2/manage.py
        * createBrigade Parameters: 
          * python manage.py createBrigade <span class="opt">Cambewarra</span> --short <span class="opt">CBW</span> --host <span class="opt">rfstag.com</span>
     * Run createBrigade in a Python runtime environment
  * In Terminal window (note that arguments don't appear to work on command line): 
       * (bushfire2) ian@ian-ThinkPad-T490:~/PycharmProjects/bushfire2$ python manage.py create_tenant_superuser 
       * Enter Tenant Schema ('?' to list schemas): <span class="opt">cambewarra</span> 
       * Username (leave blank to use 'ian'): admin
       * Email address: ibowditch@gmail.com
       * Password: 
       * Password (again): 
       * Superuser created successfully.
  * Set Run/Edit Configurations for setupBrigade as for createBrigade  
     * Parameters: python manage.py setupBrigade <span class="opt">Cambewarra</span>
     * Run setupBrigade environment
  * Set Run/Edit Configurations for set_tenant_domains
     * IMPORTANT!!!
     * Parameters: python manage.py set_tenant_domains
     * Run set_tenant_domains environment

* Add new domain to tpad /etc/hosts
* Login to admin into the new tenant using admin user
*   Change tenant name to readable version, eg. Gosford Bulk (with space) using signin.org
  *    * **NOW RESTART APPLICATION SERVER**
      * All might look ok, but probably isn't
      * Need to clear caches to rds (?)
      * If it doesn't restart, often get weird, scary, server crashes about 36h after adding new tenant

* Login to admin into the new tenant using admin user
  * Check passwords for utility users kiosk, tagadmin, pager are set, and if not set to correct values
  * Import Members from provided list
    * Check that all members have unique email addresses
    * NB: Make sure to generate and use a csv file for member import. xlsx can hang server.
  * Set up Officers for previous year with provided details (once set up in dev, export for use in AWS updates)
    * Check Groups assigned properly (esp. Training, Personnel)
    * Try to get order of DCs (not included in onerfs report)
  * Set Brigade Details
    * All activity types are valid: deselect External and any others
    * Check social as excluded
    * Set season start date (ignore year)
    * Set activity types
    * Set excluded activities
    * Check and update location, phone number, etc.
    * Add pager capcode and region
  * Add tenant name to relevant entry in kbfb/media/public/capcodes.csv (may be deprecated at some point)
  * Import qualifications from RFS list under admin certifications/import
  * Add TD/PD certifications for nominated drivers (manually)
    * Not always clear from either Licences or Administration reports
    * Assume initially that >=MR licence is TD, and anyone with RFD but <MR is PD
  
* Test logins
  * tagadmin, kiosk, pager
  * Also try one user, with rfsID as password (should prompt to change password)

* Kiosk setup
  * Make server visible on network
    * On kiosk, add signin.org to /etc/hosts
    * On dev system, run on 0.0.0.0, not 1.0.0.127
    * On aws, add redirect for wyeept.rfstag.org and wyeept.rfstag.com (shouldn't be necessary)
  
* Test remote.it
  * If possible, connect PI to external network (e.g. SHADOW)
  * In [remote.it console](https://app.remote.it/#/devices) confirm that device is online, and click VNC to connect with it
  * Copy address from connection details (e.g. proxy65.rt3.io:37011) and add a connection in VNC viewer with this address.
  * Connect using VNC viewer to confirm connection ok.
 
* Restart pager server
  * Confirm new brigade registered (check journalctl -b | grep page)

(pi-setup)=
### Setting Up a New Kiosk Raspberry PI

Boot the PI with the NOOBS SD-CARD, and follow the generic instructions in the 
[Official documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html#configuration-on-first-boot).

Use the Raspberry PI Imager application to prepare a new SD card.

- Set up the environment with the home wifi, hostname, and locale (normally from Installer settings)
- Choose the latest image, normally bookworm, but can also use bullseye if available
- Write image to the SD card, then load into the PI

SSH should be enabled by default in the image, though VNC won't be. Set up a secure connection from dev 
machine (tpad) to the PI as follows (assumes 192.168.0.143 is the birthing machine):

- ssh-keygen -f ~/.ssh/**kuringai** -N ""
  - Overwrite if needed
- ssh-keygen -f '/home/ian/.ssh/known_hosts' -R '192.168.0.143'
- ssh-copy-id -i ~/.ssh/**kuringai** pi@192.168.0.143
  - Yes, then fire0000
- ssh pi@192.168.0.143
  - Check connection

Now prepare to install the kiosk software from the dev machine using ansible. 

- cd /home/ian/ansible_quickstart
- ansible-playbook -vi inventory.ini PI_playbooks/setup.yml -e "newhost=**kuringai**" -e "target_hosts=new_pi"
  - wait for reboot
- ansible-playbook -i inventory.ini setup_new_pi.yml -e "newhost=**kuringai**" -e "new_pi_ref_num=25" -e "target_hosts=new_pi"
  - Monitor with separate shell using journalctl -f
- ssh -p 2225 pi@ec2-13-211-99-59.ap-southeast-2.compute.amazonaws.com
  - Tests comms and allows next step
  - Make any updates to config, then sudo shutdown -r now
    - Reboot required to register NFC reader anyway

Then ssh to the new PI, and do the following further configuration:

Basic configuration is controlled by the file **/etc/profile.d/rfstag/base.env**. This should be sufficient in 
most cases.

These settings can be overridden if needed, by copying **/home/pi/.config/rfstag/local-example.env** to local.env in the same
directory, then editing local.env as needed.

This can be used to do the following:

- Change KIOSK_BRIGADE if the hostname is not the brigade name (eg.. multiple kiosks)
- Change KIOSK_LOCATION to a second kiosk name
- Change BUSHFIRE_SERVER to use a test system, eg. rfstag.org, rather than the production server.

#### Setting Up a New Kiosk Raspberry PI - bullseye variant

Same as bookworm, except
After setup.yml, run update_python.yml

Then had to 
- pi@bullseye2:~ $ pyenv global 3.10.12
- pi@bullseye2:~ $ pyenv local 3.10.12
- pi@bullseye2:~ $ pyenv reshash
- \<reboot\>

Headless screen res not set correctly, and VNC was slow
Reset manually, then ok except VNC running slow


### Building the nfcserver2 package

ref: https://earthly.dev/blog/creating-and-hosting-your-own-deb-packages-and-apt-repo/

See /home/ian/PycharmProjects/nfcserver2 for source code. Note that settings from **/etc/apt/apt.conf.d/rfstag.conf** are used when building the package.

Key areas:

- debian
  - contains configuration files for the package, the most significant of which are:
    - changelog: needs to be updated with every release. Can be done manually or using dch
    - install: lists all files included in the package, and where they need to go on the target machine
    - pre/postinst: pre and post installation procedures
    - rules: basic makefile template
- conf
  - Include configuration files for
    - APT (02periodic, 51unattended-upgrades)
    - udev (90-nfcdev.rules) to launch service when nfc device connected
    - base/local.env: rfstag kiosk configuration
    - msmtprc: email server configuration
- src
  - top level scripts, installed in /usr/bin, some called from service file
- systemd
  - launch_kiosk2.service
    - starts a browser at the kiosk page for the brigade
    - Depends on network, and will restart if fails
  - nfserver2.service
    - Runs tag reader in background
    - Launched on startup
    - Stopped if reader disconnected, restarted when reconnected
    - Requires alsa sound system to function for beeps (might not be ready first time on restart, but will retry).

A new deb file is built using the **buildeb** script. It is named after the version number, 
eg. nfcserver2_1.42.0_all.deb, and is placed in the ~/PycharmProjects directory.

The deb file can be tested by scp'ing to a test PI, then **sudo apt install /home/pi/nfcserver2_1.42.0_all.deb**

NB: .deb filename must be spelled out in full - no wildcards. 

ref: https://assafmo.github.io/2019/05/02/ppa-repo-hosted-on-github.html

Once it is ok, it can be placed on the github repository as follows:

- cd ~/rfstag-kiosk
- cp ~/Pyc*/*42*.deb .
- ./rebuild

This will send the new .deb file to the github repository, and it will be available for download by clients after a few minutes.

rfstag kiosks are set to check for updates each night, and unattended-upgrades will automatically download and install kiosk updates.


### On screen keyboard

Normally, a USB keyboard and mouse are connected to the Raspberry PI to allow normal interaction with the Kiosk.

If required, the USB keyboard can be replaced with an on-screen keyboard, similar to those used on mobile phones.

There are several options available: see [3 options](https://www.industrialshields.com/blog/raspberry-pi-for-industry-26/post/top-3-on-screen-virtual-keyboards-for-raspberry-plc-panel-pc-401) here.

[onboard](https://manpages.ubuntu.com/manpages/bionic/man1/onboard.1.html) has been tested and used by one brigade.

To make sure the keyboard is visible while running the kiosk:

* echo "SCREEN_KEYBOARD=/usr/bin/onboard" >> ~/.config/rfstag/local.env

Should be able to replace **onboard** with any other keyboard in the above, but not tested.

#### Running the ACTIV dashboard on the PI

The latest Raspberry PI 4B has 2 HDMI sockets, so a second screen can be attached. If needed, this can be used
to display the ACTIV dashboard, as well as run the normal sign-in Kiosk.

Will need a second HDMI cable with micro-HDMI connection: get from [Core Electronics](https://core-electronics.com.au/raspberry-pi-micro-hdmi-to-standard-hdmi-1m-cable.html).

With a second monitor attached, type **launch_activ** on a command line.

Files:

* /etc/profile.d/rfstag/base.env
  * Offset of second screen set with HDMI2_X_OFFSET=1920
  * Overwrite in /home/pi/.config/rfstag/local.env if needed
  * Depends on resolution of the first monitor. 
* /usr/bin/launch_activ 
  * Uses default of 1920 if HDMI2_X_OFFSET not set.
  * sudo systemctl start 
* /lib/systemd/system/launch_activ 
  * sudo systemctl start launch_activ to set ok
  * enable if ok, so starts at reboot
* /home/pi/Documents/Profiles/1
  * Need to define a second profile for the second screen, separate from kiosk
  * set this in env file: ACTIV_CHROME_PROFILE=/home/pi/Documents/Profiles/1
* Launch page will initially require login
  * Use brigades dashboard login and password
  * Remember credentials


230412: As of this date, the second ACTIV screen config has some problems.

It works, but there are lots of warnings and errors logged in the journal, probably related to having 2 independent 
chromium browsers running in parallel.
launch_kiosk2 files have been updated to remove ACTIV and a seocnd screen until this is fixed properly.
ACTIV support has not been released, and is not generally available at present, and it should stay that way until
further investigations are completed.
NB: Further journal messages are still being generated unless dtoverlay=vc4-fkms-v3d is commented out of /boot/config.txt.
This file can't be included in the APT package, so will require a manual check on each kiosk to ensure it is disabled.
These messages seem benign, but better to remove source if possible.



### First login

If all is set up correctly, the first screen shown after reboot should be as follows. Login using 
kiosk user.

:::{figure-md} pi-firstlogin
:class: myclass

<img src="assets/images/pi-firstlogin.jpg" alt="PI first login" width="1467" class="bg-primary mb-1">

PI first login (click to enlarge)
:::

You will be prompted to Save Password - click Save to do this (IMPORTANT).

### Check remote.it

* Go to https://app.remote.it/#/devices
  * Login as ibowditch on google acocunt
* Check new device is listed in available devices
  * NB: Only 5 available under free account. Will need paid account if need to exceed this
* Connect to new device by clicking on  device, then VNC under Service on LHS
  * Once connected, copy url and make new VNC connections on realVNC
  * Connect with this and check access is ok


### Testing

### Full Deployment to PRD

* Update Platform to latest version in AWS console
  * Do this on test env first to ensure nothing breaks
      * If OK, also do on PRD, indepndent of code changes
  * Don't mix OS upgrade with code changes
  * Hard to undo this, and if fails, difficult to fall back
    * Set OS back to original level in AWS console, and wait for recovery
  * Check main site deployed ok and works with new Platform before proceeding
  
* Check AWS Health checks: Load Balancer Configuration
  Name		  Port	Protocol	HTTP code	Health check path	Stickiness
  default 	  80	HTTP		200		    /indexawsmt		    disabled
  http 		  80	HTTP		200		    /indexawsmthttps	disabled
  websocket 5000	HTTP		200		    /indexawsmtws	    enabled

* Double check all changes since last prd deployment
  * Get last deployment datetime from Running Version, at 
  https://ap-southeast-2.console.aws.amazon.com/elasticbeanstalk/home?region=ap-southeast-2#/environment/dashboard?applicationName=bushfire2&environmentId=e-mccptfvpnq

* Make backups
  * AWS configurations for both tst6 and prd (AWS Console: Actions/Save Configuration)
  * RDS in pgadmin for tst6 and prd: connect to AWS RDS from dev system
  * Snapshot for RDS for tst6 and prd: 
    * See https://ap-southeast-2.console.aws.amazon.com/rds/home?region=ap-southeast-2#databases:
    * Actions/Take Snapshot
  
* Set .ebextensions/02_python.config for PRD, 
  * Comment out # Test settings: bushfire2-tst6
  * Uncomment:  
  * Production settings: bushfire2-prd
    * "SECRET_KEY":  ".................."
    * "RDS_HOSTNAME": "bushfire2-prd-rds2.c5b4rv0axnji.ap-southeast-2.rds.amazonaws.com"
    * "REDIS_SERVER": "bushfire2-prd.pgfstu.0001.apse2.cache.amazonaws.com"
    * "AWS_STORAGE_BUCKET_NAME": "bushfire2-prd"
    * "AWS_ACCESS_KEY_ID": ".............."
    * "AWS_SECRET_ACCESS_KEY": "................"

* Deploy from pycharm terminal:
  * eb deploy bushfire2-prd --timeout 30
  
* Check server logs and emails for any signs of failure
  * New migrations might cause some messages while in transition, but check errors carefully in case


## Create new Elasticache on AWS

* Start at https://ap-southeast-2.console.aws.amazon.com/elasticache/home?region=ap-southeast-2#/redis
* Configure and Create New cluster
* Cluster Mode: Disabled
* Provide cluster name
* Location: AWS Cloud
* Node type: cache.t2.micro
* Port:  6379 (default)
* Replicas: 0 (switches off Multi-AZ)
* Subnet group: bushfire2-prd-ec-sng (vpc-f4221493)
* Encryption: Off
* Security group: sg-bbc0cbc4 (default)
* Backup enabled - 1 Day
* No logs
* Shards: shows 1 for latest redis (6.2.6), 0 otherwise, even if Cluster Mode==Off

* Add to 02_python.conf in deployment settings


## RDS

### Copy prd RDS to dev env

* Check access available to AWS RDS
  * Select RDS DB instance from https://ap-southeast-2.console.aws.amazon.com/rds/home?region=ap-southeast-2#databases:
  * Select VPC Security Group : normally default (sg-bbc0cbc4)
  * Click Edit Inbound Rules
    * Update inbound rule for buckraYYMMDD
    * Click Source=Custom, and select My IP - this will update home IP if changed.
    * **NB: Check that default security group** (normally sg-bbc0cbc4) is included with a PostGresql rule in inbound rules
      * This allows all instances in my EB domain to access the RDS
* Open pgadmin on dev machine
  * Make backup of current prd RDS on AWS
    * Select and open AWS prd server - currently bushfire2-prd2-rds2
    * Right click Database ebdb and select Backup
    * Provide filename for backup - eg. /home/ian/kbfb/aws-backups/bushfire2-prd-rds-220916
      * Format=Custom
      * Role Name=ian
    * Click Backup
  * Restore AWS prd backup to local database
    * Make new database under server Thinkpad (dev machine), named eg. bushfire2-prd-220916
    * Right click new local RDS and then Restore
      * Provide name of AWS prd backup file
* Prepare for use in dev env
  * Run management command to localise local RDS to dev env (not really necessary)
    * python manage.py set_tenant_domains
    * NB: This only really necessary for prd or tst environments on AWS
      * Local dev env should still be listed as a valid domain, even if not Primary
  * Point dev env to new RDS 
    * Edit bushfire/settings/.env
    * Set RDS_DB_NAME=bushfire2-prd2-220916  (for example)
  * Run local app and confirm latest RDS in use

### Updating Models/Migrations

- On dev system, run the following in a Pycharm terminal:

    * python manage.py makemigrations
    * python manage.py migrate_schemas

- Then check for any new files under migrations folder in each module, and add them to git.

- Next deployment will run migrate_schemas, and will include the changes providing the new migrations file is in git.
  
## AWS Credits (annual)

For Ku-ring-gai:

* Login to https://www.connectingup.org/ as user admin@kbfb.org.au (use saved password)
* Search for AWS
* Order the Amazon Web Services Credits for Nonprofits - was $136 + GST
* Complete order and pay with own card

Then redeem credits on AWS Credits page:
  * https://us-east-1.console.aws.amazon.com/billing/home?region=ap-southeast-2#/credits
  * logging in with account:
    * Account Id: 373346640794 
    * Seller: Amazon Web Services Australia Pty Ltd 
    * Account Name: Ku-ring-gai Bush Fire Brigade 
    * Password: *****

## Updating userdocs

* Make any necessary updates and check ok on local version http://127.0.0.1:5500/index.html
  * First do make clean html

* Save any changes into git using Commit on top level userdocs directory
  * Do NOT Commit and Push until next steps are completed
  
* Remove Internal section by editing this line in conf.py
  * Use this to keep internal documentation private. Comment out for local use.
  *   exclude_patterns += ['internal*']
  * Repeat make clean html
  
* Check Internal section not visible on dev machine

* Save in Git
  * ghp-import -n -p -f _build/html
    * NB: will need latest GIT token as password: see https://github.com/settings/tokens
    * Use the google authenticator app to get access when prompted.

* Commit and Push whole thing
  * This will update both git version at https://ibowditch.github.io/userdocs
    and reference version at https://rfstag-user.netlify.app/index.html


## Adding a New Pager Sub-system

Pager messages are monitored using a Raspberry PI, with an RTL-SDR (Software Defined Radio) USB dongle
set to receive messages broadcast on the RFS Pager frequency (see <https://www.rtl-sdr.com/rtl-sdr-tutorial-pocsag-pager-decoding/>.

Received messages are checked, and if one contains an Incident Call for a customer of rfstag, the pager sub-system 
will send a request to the rfstag server to create a new event for the brigade, so that responding members can
sign-in immediately without having to first create a new event.

The new event has the pager message as the title, the activity type as Incident-Fire, and the OIC as the callout 
Officer or SDC. The event start time is the time of the pager call, and the end time is 3 hours later.

Pager message transmissions are strong, but a single receiver can't cover all of NSW, so additional 
listening stations are needed if a brigade's pager signals can not be received in Sydney.

These instructions show how to set up an additional pager listening station in another region.

* Obtain and set up a Raspberry PI 3B in the  {ref}`same way as for a kiosk<pi-setup>`

* Obtain an RTL-SDR and setup according to supplier instructions, 
  with a dipole antenna. see <https://secomms.com.au/product/rtl-sdr-r820t2-rtl2832u-software-defined-radio-dipole-antenna-kit/>
  * No need to install software or dependencies, just get the hardware set up.
  * Setup the dipole antenna to roughly 1m span, vertically aligned.

* If necessary, generate a self-extracting installation script for the latest pager software 
  by running the following command in a linux shell:
    * **cd ~/Pycharmprojects/nfcserver**
    * **makeself --notemp ./pager pager220928.sh fred ./pagerinstall**
  
* Copy the self-extracting installation script to the target PI:
    * **scp pager2220928.sh pi@192.168.0.59://home/pi**
  
* VNC or ssh to the target pi, and run the self-extracting installer in a linux shell:
    * **./pager220928.sh**
  
* This will do the following:
  * Create a new working directory ~/pager
  * Backup existing files using the **pagermanifest** file as a guide
  * Copy the pager.ini file to ~
  * Install the necessary SDR software using **sdrinstall.sh**
      * Install all dependencies, and then download and build the following:
        * **rtl_fm** 
          * Used to tune the RTL-SDR dongle, and receive messages on the RFS pager frequency
        * **multimon-ng**
            * Used to decode messages from rtl_fm into text 
            * page_to_journal.sh then passes these on to page_to_journal
      * Copy these programs to /usr/local/bin for general use
      
  * Install all python modules, using **requirements.txt** as a guide
  * Remove large, unnecessary apps (wolfram, office, games, etc.)
  * Copy main scripts into place at /usr/local/bin:
    * **page_to_journal**.[py,sh] 
        * Logs all received pager messages to system journal
    * **pager_relay**.[py,sh] 
        * Forwards messages to pushover, compressing adjacent identical messages, using cc:
        * Creates incidents on rfstag when needed for rfstag customers.
  * Installs system services in **/lib/systemd/system** 
      * Main scripts are then launched on system startup
  * Installs automated **unattended-upgrades** and email notification using **msmtp**
  * Installs **remote.it** client to allow remote access
  
* Reboot, and run the following checks:
  * Check main scripts are running correctly:
    * **sudo systemctl status page_to_journal**
    * **sudo systemctl status pager_relay**
  * Monitor system journal for pager messages with:
    * **journalctl -f | grep page**
    * This will show pager messages as they are received
  
* Important pager.ini settings
  * BUSHFIRE_SERVER = rfstag.com
  * PAGER_REGION = sydney
  
* Operational Notes
  * Capcodes are downloaded from the rfstag server using public url rfstag.com/capcodes
  * Brigades using rfstag in this PAGER_REGION are downloaded using public url rfstag.com/brigades/{PAGER_REGION} 
  * Automated updates are available (not yet fully implemented) using public url rfstag.com/update/pager


## PI won't boot

If nothing is shown on the screen, and the PI LED is solid red, it's likely that the SD card is corrupted. This 
prevents the PI from booting up, as it can't read the operating system from the SD card.

SD card corruption can be caused by wear and tear, extensive long term usage (read/writes), or by incorrect
shutdown procedures. Always shutdown the PI properly (ctrl-alt-del, then shutdown) rather than just powering off.

To replace the SD card, you need to:

1. Purchase a new SD card

- 32Gb recommended
- Recommended models at https://www.tomshardware.com/best-picks/raspberry-pi-microsd-cards
- Recommended to buy pre-loaded SD card: 32GB MicroSD Card with NOOBS for all Raspberry Pi Boards
see https://core-electronics.com.au/32gb-microsd-card-with-noobs-for-all-raspberry-pi-boards.html?gclid=CjwKCAiAk--dBhABEiwAchIwkeJNDdNBnoeqsqydU7FNzhWiyUOdbMh0WV1al7JQ1KDvvGrV-bEEfhoCt9kQAvD_BwE
- 
2. Image

For a raw card, follow the procedure at https://www.raspberrypi.com/software/ to load the new SD card with the
Raspberry O/S.

3. Now set up the PI from scratch using the procedure above.



# AWS Deployment

The django web application for RFStag can be run on a PC, using an IDE like pycharm. It works fine like this, and is 
very useful for developing and debugging code, but at some point it needs to be deployed to an external server so that 
brigades and members can connect to it and use it.

The django web application requires the following resources to run properly:

1. [**Relational database**](internal#relational-database-postgres-rds) (postgres) - to store all the brigade models and data
1. [**Cache**](#cache-redis-elasticache) - to improve response times and manage django channels (server sent events)
1. [**Static file storage**](#static-file-storage-s3-bucket) - to store js, css, images, and other artifacts
1. [**Logging**](#logging-rotating-linux-logs) - to record activity and assist in diagnosis of problems and debugging
1. [**IP routing**](#ip-routing-route-53-hosted-zones) - to route traffic to the web application domain
1. [**SSL certification**](#ssl-certification-aws-certificate-manager) - to enable secure connections
1. [**Processor, disc and memory**](#processor-disc-and-memory-elastic-beanstalk) - to run the web application

Some of these are optional when running in a development environment, but all are mandatory when running in a public 
server.

Early in the development process, I selected [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) 
as the hosting platform for the RFStag application, for the following reasons:

a. Widely used and adopted in the industry

b. Provides scalability, stability, reliability, and good performance

c. Expensive, but non-profit grants available for credits

d. Good support for django prerequisites, including linux, python and postgres

e. Support for django channels (unavailable in most environments 5 years ago)

f. Extensive documentation both from AWS and in stackoverflow

g. Support provided (at a fee)

That said, it was still an enormous learning curve to go from basic deployment to reliable and repeatable devops.

## AWS Deployment Checklist

1. [Set up the required AWS resources](#aws-resources)

1. [Set up a github actions environment](#github-actions-secrets-and-variables) with the required values

1. [Create a new AWS EB environment](#processor-disc-and-memory-elastic-beanstalk)

1. [Deploy to the AWS WEB environment via github actions](#deploying-to-aws-eb-with-github-actions)



## Settings for Web Application Deployment 

Deployment to a hosting environment like AWS is a complex process, and requires a clear specification of the environment 
in which the web application is to run. The locations and configuration of all the resources needs to be well specified, 
and defined in a way that can be easily and unambiguously verified.

Details of how the resources required for RFStag will be specified in later sections. First, let's cover the methods 
used to specify django settings.


### Django Settings

One of the first things that django does when a web application is started is to read the settings to be used by the application.
These settings are normally specified using the environment variable [DJANGO_SETTINGS_MODULE](https://docs.djangoproject.com/en/5.0/topics/settings/#django-settings). For example in the pycharm 
run configuration kbfb2, **DJANGO_SETTINGS_MODULE=bushfire.settings.local**.

Project folder **bushfire** has a sub-directory called **settings** which contains the following configuration files
  
* **base.py** - basic configuration used in all environments using **from bushfire.settings.base import** *
* **local.py** - used in local development environment
* **awseb.py** - used in AWS Elastic Beanstalk environment

These are python files that define variables used by django. Rather than having a different django settings file for every 
single type of deployment, e.g. test, production, staging, etc., it is better to obtain some django settings from the 
external environment, using environment variables.

### Environment Variables as settings

Using the python package [django-environ](https://django-environ.readthedocs.io/en/latest/#welcome-to-django-environ-documentation), 
it is possible to feed operating system environment variables into the django settings to give greater control over the 
run time environment (see [Twelve-factor methodology](https://www.12factor.net/) for more details).

For example, this allows us to define the location of the database to be used by the django web application as **env('RDS_HOSTNAME')**, 
and this is used in the **DATABASES** setting in base.py. This avoids hard-coding environmental values into configuration files, 
and gives us the flexibility to change the operating environment without updating any code - just change an environment 
variable and restart the web application.

As well as the database values, we can also define the location of the other resources listed above (e.g. cache, logging, etc.) 
in terms of environment variables, so that only these environment values have to be changed when we need to update the 
cache or other operations, and no code changes are needed.

#### Django Setting ALLOWED_HOSTS

It is critical that ALLOWED_HOSTS is set correctly when running on AWS, otherwise normal requests will cause the web 
app to crash with a 500 error.

**django-tenants** middleware checks ALLOWED_HOSTS while trying to determine the tenant to route the request to. If the 
host in the request is not included in ALLOWED_HOSTS, django-tenants will fail, and this exception will percolate up 
as a 500 error.

**bushfire/settings/awseb.py** has an elaborate scheme to calculate ALLOWED_HOSTS using a variety of environment settings 
and AWS functions. It seems to work for now, but that may change.


#### Development Environment Variables

Environment variables for the development environment are defined in the file **bushfire/.env.local**, and this follows a 
naming convention of specifying the environment using the suffix in **DJANGO_SETTINGS_MODULE**, which for the development 
environment is "local" (from bushfire.settings.local).

The development environment is fully defined in **bushfire/.env.local**, and it must contain all the values required 
to run the web application. These can be changed, for example we can use a database on AWS rather than a local database, 
just by changing these settings in this file.

#### Deployment Environment Variables

Deployment to AWS is complex, and requires fine control over the environment variables to be used by the hosted web application.

In general, there are 2 distinct environments used on AWS - one for production, and one for staging/testing. 

Some resources such as cache can be shared across environments (to reduce hosting costs), but others such as the RDS must 
be kept separate to minimise risk to production systems.

In early 2024, after a number of battles with AWS deployment, I decided to adopt a continuous integration and 
deployment (CI/CD) approach to AWS deployment, and settled on [github actions](https://docs.github.com/en/actions) as the tool to use for this. 
This gives fine control over deployment and implements CI/CD.  

A full description of github actions usage is given [below](#deploying-to-aws-eb-with-github-actions), 
but a key part is the definition of variables and secrets, sets of which must be defined for different deployment types.

Github action **variables** are used to define the environment variables passed to AWS during the deployment process. 
These values can be seen on AWS in the Elastic Beanstalk Environment Configuration page, but they are stored on github, 
and transferred to AWS as part of the deployment process (see awseb.yml). So any environment changes need to be made on github, then
a new deployment made to implement the changes.

Githib action **secrets** are used for confidential information such as **RDS_PASSWORD**. These are encrypted and can't be 
read in github (or anywhere else - except AWS EB configuration) after they are set.

Github variables and secrets are referenced by the github configuration file **.github/workflows/awseb.yml**, 
which defines the deployment process and builds the commands used to deploy to AWS.



## AWS Resources

The final resource - Elastic Beanstalk - is clearly the most critical, and it is left until last. First, we need to 
set up all the other resources required by the django web application.

### Relational database (postgres RDS)

postgres was selected as the database because it is well-supported by django, and also provides the best implementation
of a multi-tenanted database server, which is required by the architecture of RFStag.

There is an option to specify an RDS as an integral part of an AWS EB environment, but this has many disadvantages. Instead, even though
it was initially harder to set up, it's best to create and use an external RDS.




#### RDS Setup

For the moment, we are using a dedicated RDS on AWS. This is expensive ($USD24 ~= $AU35/month), but backups/snapshots 
are automated.

Another option is to use a [dedicated EC2 instance to run postgres](#creating-a-low-cost-ec2-rds), and use that instead of a dedicated RDS. This option 
is much cheaper, and seems to be just as responsive, but backups will need to be automated before this is used for production.

The [EC2 postgres server](#creating-a-low-cost-ec2-rds) should be used for all other non-critical database needs.


To create a new RDS, go to [AWS RDS](https://ap-southeast-2.console.aws.amazon.com/rds/home?region=ap-southeast-2#), select DB instances, 
and the Create Database. Refer to settings for production RDS, and copy them in general, but note the following:

- Choose a database creation method: Standard
- Engine options: PostgreSQL (NB: Aurora [PostgreSQL Compatible] not tested ATM, and v expensive)
- Engine Version: 14.10 (or same as production)
- Templates: Free Tier
- Settings/DB instance identifier: eg. bushfire2-prd-rds6
- Settings/Credentials/Master username: **RDS_USERNAME**
- Settings/Credentials/Self Managed
- Settings/Credentials/Master password: **RDS_PASSWORD**
- Instance Configuration:DB Instance Class: **db.t3.micro**
- Connectivity/Compute Resource: Don’t connect to an EC2 compute resource
- Connectivity/Public Access: **Yes**
- Connectivity/VPC Security Group: **Create New**
- Connectivity/Existing VPC security groups: default
- Connectivity/Database port: **RDS_PORT**
- Additional configuration/Initial database name: **RDS_DB_NAME**
- Additional configuration/Backups: On
- Additional configuration/Encryption: On

For new VPC security group, we will need to set Inbound Rules for any instances that need to use it.

**NB: Check that the default security group (normally sg-bbc0cbc4) is included with a PostGresql rule in inbound rules. 
This allows all instances in my EB domain to access the RDS**

Also provided access to dev machine, home IP address, so can be accessed with pgadmin.



### Cache (REDIS Elasticache)

Caches are used both for the [django cache framework](https://docs.djangoproject.com/en/5.0/topics/cache/), and to 
support [django channels](https://channels.readthedocs.io/en/1.x/backends.html#redis) in production use on AWS EB.

In AWS, a single [Elasticache](https://ap-southeast-2.console.aws.amazon.com/elasticache/home?region=ap-southeast-2#/redis) 
is shared across multiple applications. Key collisions are avoided by careful use of the 
**REDIS_KEY_PREFIX** in settings.base which is calculated using the AWS EB hostname, plus the **RDS_DB_NAME** 
and **RDS_HOSTNAME**, making it unique to each AWS EB environment.

**REDIS_KEY_PREFIX** is used in **settings.base.CHANNEL_LAYERS** and **settings.base.CACHES**.

Also, we need to provide caching across multiple tenants/brigades, so a function **kbfb/cache.make_key** combines the 
REDIS_KEY_PREFIX with the tenant name to make cache entries unique to each tenant as well.

The redis cache needs to provide read/write access to all web apps, and this is done by adding the Security Group **default**
to the cache definition, and ensuring that Inbound Rules on default allow the necessary access.

Apart from that, setup of the cache is straightforward, and should not cause problems, If necessary, use settings from 
and existing cache as a guide.


* **REDIS_SERVER**: Use the Primary Endpoint name for this

* **REDIS_PORT**: 6379 (default value)

NB: The entire REDIS cache is cleared each time a new version is deployed to AWS. Unfortunately, this means deploying 
to a tst environment will clear the prd cache, for the moment, until a smarter method is used.


### Static file storage ([S3 bucket](https://ap-southeast-2.console.aws.amazon.com/s3/home?region=ap-southeast-2#))

Django uses [static files](https://docs.djangoproject.com/en/5.0/howto/static-files/#how-to-manage-static-files-e-g-images-javascript-css) 
to store javascript, css, images, and other artifacts. A management command **collectstatic** is called from 
.platform/hooks/postdeploy/02_django_setup.sh each time the app is deployed, and this keeps the static files updated.

There are a number of settings used for static files. These are quite simple in a development environment, but 
complex for production. [django-storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) is used to support storage in AWS S3 buckets, but there also 
a number of CSP and other security  settings relating to js and css files.

Most AWS S3 settings are defined in **settings.awseb**, as they are not used anywhere other than on AWS EB.

The most important ones are defined in github actions:

* **AWS_STORAGE_BUCKET_NAME** =   env('AWS_STORAGE_BUCKET_NAME')
* **AWS_ACCESS_KEY_ID** =         env('AWS_ACCESS_KEY_ID')
* **AWS_SECRET_ACCESS_KEY** =     env('AWS_SECRET_ACCESS_KEY')

It is quite tricky setting up S3 bucket permissions. A clear indication that this has not been done correctly 
is when formatting of pages looks wrong, especially in admin which uses a lot of css. 
There may aso be errors in the browser console that indicate problems loading static files.

NB: **AWS_ACCESS_KEY_ID** refers to the User who owns the bucket, and appropriate permissions must be set for that user.

It is best to copy an existing bucket, including permissions, to avoid these problems.

Changed Object Ownership (permissions) should have ACLs enabled, Bucket owner preferred


### Logging (rotating linux logs)

This mostly set up and controlled by scripts in .platform/hooks. It is still work in progress.

Ideally logs would be compressed and transferred to a S3 bucket for long term storage, but this
hasn't been worked out yet.


### IP routing (Route 53 hosted zones)

Define a [hosted zone](https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones?region=ap-southeast-2#) for each registered domain name, that includes all valid hostnames, e.g. *.rfstag.com and rfstag.com.

The key values are for A type records, that define where traffic to the dmain name will be routed. The target will be
the AWS EB environment with the required web app version.

Note that when changing the target, you need to change for rfstag.com and *.rftstag.com (both A-records).

You also need to wait until the remapping is complete (view status), then advised to run a test to the domain name, 
e.g. killara.rfstag.com, and confirm valid response is given.

### SSL certification (AWS Certificate Manager)

A security requirement is that **https** must always be used, rather than http. This requires an SSL certificate, which can be issued by 
the [AWS Certificate Manager](https://ap-southeast-2.console.aws.amazon.com/acm/home?region=ap-southeast-2#/certificates/list)

The certificate used should cover all domains used in the application, e.g. *.rfstag.com, and *.rfstag.org.

It needs to be specified in the AWS EB Configuration of Instance Traffic Scaling/Load Balancer/Listeners section, for port 443 (https).

This is done in file **.ebextensions/00_eb_setup.config**, but can also be set in the AWS EB console.

### Processor, disc and memory (Elastic Beanstalk)

Last but not least, we need to define an Elastic Beanstalk environment to run the web application.

An AWS EB environment is contained in an EB application, so the application must be set up first. This can be done in 
the AWS console, with little more than an application name being required.

Before creating a new EB environment, ensure that all code updates are saved in github. The **eb create** command below will
initialise the new environment with the latest version of bushfire2 code on the current github branch (usually **master**).

To add a new AWS EB environment, use the **[eb create](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-create.html)** 
command from the terminal command line in pycharm.

Responses:

* Environment name: e.g. bushfire2-tst7
* DNS CNAME prefix: (as above)
* Load Balancer Type: **application**
* Enable Spot Fleet requests: N

This will create the new EB environment with the latest code base, including the configuration defined 
in .ebextensions (see below).

It will not go through github actions, so **no environment will be set**.

The resulting environment will have the following characteristics:

1. It should be shown as healthy

1. It won't run correctly, since the environment is not yet set up. This can be verified by looking at the environment configuration on AWS console.

1. It is not yet linked to a valid domain such as rfstag.com or rfstag.org, so nginx will not allow any traffic to reach it.

1. eb ssh to the new environment should work, so the linux image can be checked.


To finish the deployment, you need to complete following steps:

1. [Deploy the system](#deploying-to-aws-eb-with-github-actions) to the required AWS EB using github actions.

1. [Redirect traffic](#ip-routing-route-53-hosted-zones) to the new AWS EB using AWS Route 53


Note that the **Application Load Balancer (ALB)** is a critical part of the EB environment. It is set up
automatically during the eb create process, and takes a lot of config values from .ebextensions/00_eb_setup.config.

The ALB can be seen in the [EC2](https://ap-southeast-2.console.aws.amazon.com/ec2/home?region=ap-southeast-2#Home:)
section of AWS, in the Load Balancer menu on the left. The target env can be quickly determined
by looking at the load balancer tags.

The ALB attributes should be checked to ensure that they are set up properly, in particular, **Connection Idle Time** should 
be set from the default 60s to 300s to prevent server timeouts eg. when exporting large data sets.



#### Deploying to AWS EB with Github Actions

AWS EB deployments were fraught with difficulty, with many problems relating to preparing and connecting the right 
resources, in the right way, at the right time, when an update was applied.

There are some guides to deploying django application to AWS EB, but the landscape changes rapidly and many of them 
are out of date.

Additional complexity is introduced by the requirements of RFStag for server-sent events (SSE) via django-channels, which 
relies on websockets (not properly supported in AWS EB until recently), multi-tenanting to support many brigades 
using django-tenants and postgresql, and security requirements such as Content Security Policy (CSP).

Initially, the various connections were made with a mixture of .ebextensions, settings files, guesswork, and a great deal 
of luck when it worked.

Finally, when I was unable to change the RDS used by the production system, I realised I needed to radically improve the 
deployment process to make it more reliable and predictable.

There were several options, but I landed on [github actions](https://docs.github.com/en/actions) for the following reasons:

1. Already using github for source management

1. github actions is vendor independent, and can be made to work for AWS EB or any other hosting solution

1. Still free/low cost

1. Allows centralised storage of environment values and encryption of secrets

1. Allows switching between git branches and AWS EB environments

1. Allows scripted deployment procedures which can be tailored to the environment and can incorporate variables and secrets from github itself before deployment.


##### Github Actions Settings

[Github actions](https://docs.github.com/en/actions) is very powerful, and RFStag only uses a small part of the available functionality.

A single workflow is defined in **.github/workflows/awseb.yml** which does the following:

1. Checks out the current code base from the required git branch

1. Extracts variables and secrets from github actions and adds them to an AWS EB .extensions file to be used in deployment

1. Sends the deployment package to AWS to be stored in a S3 bucket

1. Triggers the AWS deployment process with the new deployment package

1. [Good documentation](https://docs.github.com/en/actions)



##### Github Actions Secrets and Variables

The variables and secrets defined in github are used to define and characterise the resources used on AWS, such as 
database (RDS), cache (REDIS), etc.

There are few [secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) (only passwords), 
and everything else is defined as a [variable](https://docs.github.com/en/actions/learn-github-actions/variables) and can be viewed 
in [github actions](https://github.com/ibowditch/bushfire2/settings/secrets/actions). 

As a general policy, settings defined in github actions should not have defaults when read from the environment (**env**('xxx')), 
and should not be defined anywhere else (for example in a separate .env file like **bushfire/.env.awseb**). This forces
the required values to be set in github actions, and if they are not, then there will an obvious error, e.g. the app 
will fail immediately if no RDS settings are provided.

It also means that any environment variables required for the development environment, which doesn't get deployed 
through github actions, need to be defined in **bushfire/.env.local**

Many of the actions variables and secrets are standard django values defined in [django settings](https://docs.djangoproject.com/en/5.0/ref/settings/) 
or in the associated django package, such as [django-channels](https://channels.readthedocs.io/en/stable/introduction.html), 
[django-tenants](https://django-tenants.readthedocs.io/en/latest/), etc.

Many [variables](https://docs.github.com/en/actions/learn-github-actions/variables), and a few secrets are defined as 
Repository variables, rather than environment variables. Respository variables are the same for all environments, 
and only need to be defined once. They can be overridden in a specific environment, which gives priority to 
environment rather than repository variables when resolving them.


The other significant ones are as follows:

* **DEPLOY_ENV**: defines the name of the github actions environment where specific env variables and secrets are defined. 
  Also gives the name of the AWS EB environment to deploy to. Generally set to the test environment, and only prd on special occasions.

* **DOMAIN_[ROOT,SUFFIX]**: Defines the full domain name, so should be ROOT=rfstag, SUFFIX=org for test, SUFFIX=com for prd

* **AWS_ENV_SUFFIX**: when appended to **EB_APP_NAME**, gives the name of the AWS EB environment, e.g. bushfire2-prd2




#### Elastic Beanstalk Extensions

Most of the basic required configuration so far has been done with **[.ebextensions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.html)**. 

In particular **.ebextensions/00_eb_setup.config**, sets up the following:

* EC2 security group default
* Application Load Balancer (ALB) Listener for 443 (https), including valid SSL Certificate
* ALB Process **default** which handles all http traffic (including health checks)
* ALB Process **websocket** which handles all websocket traffic including django channels
* ALB Listener rule for websockets
* EC2 Key Name to allow ssh connections to instance

The above settings are the same for all environments in the application, and should not be changed for a particular environment.

**.ebextensions/django.config** also sets up **WSGIPath**, and **.ebextensions/secrets.config** is also needed as a placeholder for 
AWS EB configuration settings (see [above](#github-actions-settings)).

**No other .ebextensions should be used.**


:::{admonition} Why use .ebextensions?

.ebextensions were the only way to [extend AWS EB configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.html) 
until fairly recently, and RFStag used them in the early years.

Then AWS introduced Linux 2, which allowed control via platform hooks, which are linux scripts run during the 
deployment process, as well as finer control over the nginx reverse proxy.

.ebextensions are still used, but they must be used with great care, and very sparingly. 
Sometimes they are applied, and sometimes not. Platform 
hooks are the recommended way to change settings and configuration, so I now avoid using .ebextensions where possible.

**.ebextensions/00_eb_setup.config** is the exception, since it is generic and applies to all environments within an 
EB application and is also useful for initialising an environment, especially the ALB which can be very tricky to do
otherwise.

:::


#### AWS EB .platform settings

Since the introduction of linux 2 platforms in AWS EB, [.platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.html) 
has been the main way to tailor AWS EB configurations. RFStag uses the following **.platform** configurations to set up the AWS EB instances:


##### .platform confighooks

1. confighooks/postdeploy/set_env: This makes the EB environment variables available in an ssh session

##### .platform hooks

1. hooks/postdeploy/*logging*: set up log rotation and bundling by editing EB files in situ

1. hooks/postdeploy/django_setup: Creates logging directories, runns collectstatic and migrate_schemas to update everything

1. hooks/postdeploy/reset_cache: Erases the cache to force refresh of all pages using the new environment

##### .platform nginx

[NGINX](https://docs.nginx.com/) is the reverse proxy used by default on all AWS EB environments. It is the first 
point at which requests can be examined, and it is used to filter out invalid and irrelevant requests. It can handle 
high volumes of requests quicker than django, so it improves performance and responsiveness, as long as it is set up 
properly (which is something of a black art). 

RFStag nginx settings were modelled on a [github gist](https://gist.github.com/henhan/2943013c9064606425b0ee5bb1ca8c99), 
with some additional modifications. The configuration does the following:

1. Enforces **https** for all external communications (internal AWS health checks excluded)

1. Logs, and rotates, all requests in **/var/log/nginx** files.

1. Filters out any non-conformant urls/hosts using nginx_env.conf **$gd_host**, and returns http code 400 if rejected

1. Diverts websocket requests to the **daphne** process that handles django-channels (see also **Procfile**)


Any requests that pass through this initial nginx filter are passed on to django.


##### Django Middleware

If they pass through the nginx reverse proxy filtering process, requests will be passed through to RFStag middleware 
(see settings.base.MIDDLEWARE).

This is mostly boilerplate, with the following exceptions:

1. **csp.middleware.CSPMiddleware**: Used to check Content Security Policy - see security below

1. **tenants.middleware2.TenantAWSMiddleWare**: Used to route requests to the appropriate tenant.

1. **kbfb.middleware2.LoginRequiredMiddleware**: Used to enforce login required for each tenant


:::{admonition} Unexpected 404 errors

The most likely cause of unexpected 404 errors is that one of the settings is not set correctly, 
starting with DJANGO_SETTINGS_MODULE.

You can see all settings on the AWS EB console/Configuration, or alternatively, run the url /crash500 and an email 
will be sent with a full listing of all settings.

Further investigations can be done by adding or enabling DEBUG output from middleware, by changing the
relevant settings.base.LOGGING[loggers][level], or adding more logging to middleware if needed.

:::


### Creating a low-cost EC2 RDS


[ref](https://aws-postgresql-docs.beliciarodriguez.com/launching-instance/overview)

230808

Ec2 db experiment: summary of steps

* Create a new ec2 instance
* Create a new key pair and use that for connection
* Create a new security group using the wizard
* Set inbound rules for this new security group to allow connection from My IP
* Ssh to new instance
* Find instance on aws ec2 dashboard
* Click connect
* Copy template ssh command
* In shell, Paste ssh command to command line
* Edit to change location of .pem file
* Result: ssh -i ".ssh/aws-postgres-ec2.pem" ubuntu@ec2-52-62-233-21.ap-southeast-2.compute.amazonaws.com


* Install postgres
  sudo apt-get update -y && sudo apt-get upgrade -y
  sudo apt install postgresql -y
* Edit postgres config files: see https://betterprogramming.pub/how-to-provision-a-cheap-postgresql-database-in-aws-ec2-9984ff3ddaea
  sudo nano /etc/postgresql/14/main/postgresql.conf
  sudo nano /etc/postgresql/14/main/pg_hba.conf
  sudo systemctl restart postgresql
  * Setup roles for ubuntu and ian
  ubuntu@ip-172-31-7-181:~$ sudo -u  postgres psql
  could not change directory to "/home/ubuntu": Permission denied
  psql (14.8 (Ubuntu 14.8-0ubuntu0.22.04.1))
  Type "help" for help.


  postgres=# psql -U postgres -c "CREATE ROLE ubuntu;"
  postgres-# psql -U postgres -c "ALTER ROLE  ubuntu  WITH LOGIN;"
  postgres-# psql -U postgres -c "ALTER USER  ubuntu  CREATEDB;"
  postgres-# psql -U postgres -c "ALTER USER  ubuntu  WITH PASSWORD 'ubuntu';"
  postgres-# exit
  Use \q to quit.
  postgres-# \q


* For ian
  ubuntu@ip-172-31-7-181:~$ sudo -u  postgres psql
  could not change directory to "/home/ubuntu": Permission denied
  psql (14.8 (Ubuntu 14.8-0ubuntu0.22.04.1))
  Type "help" for help.


    postgres=# CREATE ROLE ian;
    postgres=# ALTER ROLE  ian  WITH LOGIN;
    ALTER ROLE
    postgres=# ALTER USER ian  CREATEDB;
    ALTER ROLE
    postgres=# ALTER USER ian  WITH PASSWORD 'ib151258';
    ALTER ROLE
    postgres=# \q


* Restart postgres
  ubuntu@ip-172-31-7-181:~$ sudo systemctl restart postgresql


* Connect to instance using pgadmin with user ian
  Pgadmin new connection:
  General
  Name: aws-postgres-ec2
  Connection:
  Host: ec2-52-62-233-21.ap-southeast-2.compute.amazonaws.com
  Port: 5432
  Maintenance Database: postgres
  Username: ian
  Password (first time) ib15..


* Connect to ec2 with this connection (important that user=ian)
  Create database, with owner ian
  Then restore into new db from a prd backup, e.g. /home/ian/kbfb/aws-backups/bushfire2-prd-rds-230804
  Set tpad to connect to this db


* /home/ian/PycharmProjects/bushfire2/bushfire/settings/.env
* 
* aws-postgresql-ec2
RDS_HOSTNAME=ec2-52-62-233-21.ap-southeast-2.compute.amazonaws.com
RDS_DB_NAME=rfstag3-ec2
…
RDS_USERNAME=ian
RDS_PASSWORD=ib151258
Run bushfire2 and login to http://kuringai.signin.org:8069/bfb/
User tagadmin





### Security Settings [Mozilla Observatory](https://observatory.mozilla.org/)

[ref1 ](https://blogthedata.com/post/how-to-get-a-perfect-mozilla-observatory-score/)

[ref2 ](https://blogthedata.com/post/how-to-implement-subresource-integrity-django/)



## AWS EB Platforms

In general, the [latest available EC2 platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-python.html)
should be used for testing and production where possible. 

This avoids major jumps between versions, and the compatibility problems that brings. 

Leave the production version on a LTS (long term support) version where possible, rather than a minor release.

RFStag has limited automatic testing available, and regression testing is rudimentary, so staying current 
with latest releases reduces the risk of major problems by identifying them early.

### EC2 Platform Version Upgrades

Platform **version upgrades** can normally be done safely using the AWS EB [environment console](https://ap-southeast-2.console.aws.amazon.com/elasticbeanstalk/home?region=ap-southeast-2#/environments)

Occasionally, version upgrades go wrong, so it's important to upgrade the version first using a test environment. Check the logs for 
any errors or suspicious messages, and make sure all is well before deploying to production.

### Upgrading EC2 Platform

There are many different platforms available for EC2 instances. The python platforms normally have a python version number, and a linux type - 
see [Python Platform History](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-python.html) for details.

It isn't possible to change the platform for an environment once it has been deployed. Changing version is ok 
(using the AWS EB environment console), but if a new platform is needed, and new environment must be created.

To do that, follow these steps:

1. In pycharm terminal, [**eb platform select**](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-platform.html)

* Choose the new platform branch to use for subsequent environments. This value will be stored in 
  **.elasticbeanstalk/config.yml** as global:**default_platform**.

2. Now create the new environment using [**eb create**](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-create.html)

* Choose the environment name carefully, as it will be used in the github deployment chain. e.g. for (existing) 
EB application bushfire2, choose bushfire2-tst8.
* Choose an application load balancer
* eb create will set up all the infrastructure required to run the environment.
* It will also pass on the latest source package, so make sure all files have been checked into github.
* NB: The github deployment procedure will NOT be followed when using eb create, so many critical environment 
variables, which are set in the github deployment script **.github/workflows/awseb.yml** will not be set in the
new EB environment. The deployment will only partially work, and will probably show failing health.

3. Set up the github deployment environment

* Go to [github environments](https://github.com/ibowditch/bushfire2/settings/environments) and create a new environment
* Copy values from an existing environment. 
* Re-use secrets for S3 buckets
* Generate a new Django secret
* Make sure AWS_ENV_SUFFIX is set to match the new envronment name suffix (e.g. tst8)
* Make sure the DOMAIN_SUFFIX is set correctly (usually org)
* Probably create a new RDS in EC2 RDS, and set django RDS* variables pointing to it.
* Re-use the existing REDIS server (keys will be different, so easy to share)
* Finally, make sure repository variable **DEPLOY_ENV** is set to the appropriate value, i.e. the new github 
environment name (bushfire2-tst8).

4. Deploy to the new environment via github

* If needed, make a dummy edit to a file, then Commit and Push the latest version to github.
* This will trigger the github deployment script **.github/workflows/awseb.yml**.
* Environment variables will be set in github, and then passed on to the new EB environment.
* If all variables are set correctly, the new environment should now show good health.

5. Redirect the host domain to the new environment

* Go to [Route 53 dashboard](https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones?region=ap-southeast-2#) 
  and select the required hosted zone.
* Edit the A-type records for eg. **rfstag.org** and **.rfstag.org** to point to the new environment.
* Wait until the change is completed
* Test the record to ensure and OK value is returned.
* Now try running the appropriate host, eg. [kuringai.rfstag.org](https://kuringai.rfstag.org), and confirm working as expected.


### Common Issues when Upgrading EC2 Platform

* Python dependencies. Check messages.log, eb-engine.log, rfstag.log for hints. Update **Pipfile** if needed.
* channels/daphne: try running daphne on the ec2 command line and see if running. Check systemctl status websocket
* Caching: cache should be cleared on deployment by .platform/hooks/postdeploy/04_reset_cache.sh, but confirm this.
* Environment variables not set correctly. These can be viewed in the AWS env configuration - check carefully. 
Investigate, and check awseb.yml is working as expected, and github variables set properly.




