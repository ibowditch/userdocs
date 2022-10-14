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

* Make backups of any target databases using pgadmin
  * Make backup of AWS production database (ebdb) on dev system using pgadmin
    * Set inbound rule on RDS security group for MyIP if needed
  * <span class="opt">Drop AWS tst system database (ebdb) to clear contents</span>
  * <span class="opt">Restore backup of AWS production database to AWS tst database</span>

* In pycharm project bushfire2: 
  * In bushfire/settings/.env set RDS_HOSTNAME=<span class="opt">bushfire2-tst6-rds.c5b4rv0axnji.ap-southeast-2.rds.amazonaws.com</span>
  * Check all migrations in all apps saved in github  
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
   * **NOW RESTART APPLICATION SERVER**
      * All might look ok, but probably isn't
      * Need to clear caches to rds (?)
      * If don't restart, often get weird, scary, server crashes about 36h after adding new tenant
    
* Login to admin into the new tenant using admin user
  * Check passwords for utility users kiosk, tagadmin, pager are set, and if not set to correct values
  * Import Members from provided list
    * Check that all members have unique email addresses
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
  * If possible, connect PI to external network (eg. SHADOW)
  * In [remote.it console](https://app.remote.it/#/devices) confirm that device is online, and click VNC to connect with it
  * Copy address from connection details (eg. proxy65.rt3.io:37011) and add a connection in VNC viewer with this address.
  * Connect using VNC viewer to confirm connection ok.
 
(pi-setup)=
### Setting Up a New Kiosk Raspberry PI

Boot the PI with the NOOBS SD-CARD, and follow the generic instructions in the 
[Official documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html#configuration-on-first-boot).

Use the following settings where required:

:::{figure-md} pi-country
:class: myclass

<img src="assets/images/pi-country.jpg" alt="PI Country settingst" width="1467" class="bg-primary mb-1">

PI country settings (click to enlarge)
:::

Password set to this by convention (but can be changed if needed):

:::{figure-md} pi-password
:class: myclass

<img src="assets/images/pi-password.jpg" alt="PI Country settings" width="1467" class="bg-primary mb-1">

PI password (click to enlarge)
:::

Network connections normally via station wifi, but can be hard-wired too. Provide the wifi password, and 
it will be remembered for next time.

:::{figure-md} pi-network
:class: myclass

<img src="assets/images/pi-wifi.jpg" alt="PI Network settings" width="1467" class="bg-primary mb-1">

PI network (click to enlarge)
:::

Update software - don't skip this step, but it will take a while.

Configuration settings 

In system settings tab, make sure Wait for Network is checked, and change Hostname to the same 
name as brigade

:::{figure-md} pi-settings1
:class: myclass

<img src="assets/images/pi-settings1.jpg" alt="PI System settings" width="1467" class="bg-primary mb-1">

PI System configuration (click to enlarge)
:::

In Interface settings tab, Enable SSH and VNC to allow remote support:

:::{figure-md} pi-settings2
:class: myclass

<img src="assets/images/pi-settings2.jpg" alt="PI Interface settings" width="1467" class="bg-primary mb-1">

PI interface configuration (click to enlarge)
:::

Reboot after changing PI configuration when prompted.

### Installing the Kiosk Software

Copy the installation package from a thumb drive into folder /home/pi, or use (in tpad shell, not pycharm):

* cd /home/ian/PycharmProjects/nfcserver
* makeself --notemp nfcreader nfcreader220920f.sh bushfire ./nfcinstall 

* scp /home/ian/PycharmProjects/nfcserver/nfcreader220920f.sh pi@192.168.0.226://home/pi

Open a command Terminal (top menu bar - black box). 

Run the installation procedure as follows:

  ./nfcreader220920f.sh

This can take some time, as it will update the system software.

The installation procedure will do the following:

* Set the Brigade the kiosk will use (when prompted)
  * A server of this name must exist, or the given name will not be accepted.
  * The nfcreader.ini file will be updated with the given validated Brigade name.
* Install sound files (for beeps and buzzes)
* Install python libraries for sound and nfc support.
* Remove unwanted, large packages to free disk space (e.g. libreoffice, games, wolfram,... )
* Add kiosk software to /usr/local/bin
* Set boot script in /home/pi/.config/lxsession/LXDE-pi/autostart
* Register the Sony nfc reader
* Register and start the nfcserver service, used to read nfc tags.
* Set up unattended upgrades to keep the system up to date automatically.
* Set up remote.it to enable remote support

Then reboot when finished.

Then test nfc using:

   python3 -m nfc

If there's an error (likely), you'll need to type the following commands to clear the error, then reboot again:

   sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\", ATTRS{idProduct}==\"06c3\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'
   udevadm control -R


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
  
* Check Internal section not visible on dev machine

* Save in Git
  * ghp-import -n -p -f _build/html
    * NB: will need latest GIT token as password: see https://github.com/settings/tokens

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
