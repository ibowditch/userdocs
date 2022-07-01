# Internal Procedures (Under construction)

```{margin} Restricted Access
For internal use only
```

## Adding a New Brigade

### Data Required from Brigade

The brigade should provide the following details, preferably in an excel spreadsheet:

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
  * Full name (eg. Wyee Point 1A)
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
  
* WiFI connection
  * SSID and password  


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

Copy the installation package from a thumb drive into folder /home/pi

Open a command Terminal (top menu bar - black box). 

Run the installation procedure as follows:

  ./nfcreader.sh

This can take some time, as it will update the system software.

The installation procedure will do the following:

* Set the Brigade the kiosk will use (when prompted)
  * A server of this name must exist, or the given name will not be accepted.
  * The nfcreader.ini file will be updated with the given validated Brigade name.
* Install sound files (for beeps and buzzes)
* Install python libraries for sound and nfc support.
* Remove unwanted, large packages to free disk space (eg. libreoffice, games, wolfram,... )
* Add kiosk software to /usr/local/bin
* Set boot script in /home/pi/.config/lxsession/LXDE-pi/autostart
* Register the Sony nfc reader
* Register and start the nfcserver service, used to read nfc tags.
* Set up unattended upgrades to keep the system up to date automatically.
* Set up remote.it to enable remote support

Then reboot when finished.

### First login

If all is set up correctly, the first screen shown after reboot should be as follows. Login using 
kiosk user.

:::{figure-md} pi-firstlogin
:class: myclass

<img src="assets/images/pi-firstlogin.jpg" alt="PI first login" width="1467" class="bg-primary mb-1">

PI first login (click to enlarge)
:::

You will be prompted to Save Password - click Save to do this (IMPORTANT).

### Adding a New Tenant Schema

* Make backups of any target databases using pgadmin
  * Make backup of AWS production database (ebdb) on dev system
  * Drop AWS tst system database (ebdb) to clear contents
  * Restore backup of AWS production database to AWS tst database

* In pycharm project bushfire2: 
  * In bushfire/settings/.env set RDS_HOSTNAME=bushfire2-tst6-rds.c5b4rv0axnji.ap-southeast-2.rds.amazonaws.com
  * Check all migrations in all apps saved in github  
  * Run/Edit Configurations
     * Env vars: PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=bushfire.settings.local
     * Working directory: ~/PycharmProjects/bushfire2
     * Script path: /home/ian/PycharmProjects/bushfire2/manage.py
        * createBrigade Parameters: python manage.py createBrigade WyeePt --short WYP --host signin.org
     * Run createBrigade Python environment
  * In Terminal window (note that arguments don't appear to work on command line): 
       * (bushfire2) ian@ian-ThinkPad-T490:~/PycharmProjects/bushfire2$ python manage.py create_tenant_superuser 
       * Enter Tenant Schema ('?' to list schemas): cambewarra 
       * Username (leave blank to use 'ian'): admin
       * Email address: ibowditch@gmail.com
       * Password: 
       * Password (again): 
       * Superuser created successfully.
  * Set Run/Edit Configurations for setupBrigade as for createBrigade  
     * Parameters: python manage.py setupBrigade WyeePt
     * Run setupBrigade environment
  * Set Run/Edit Configurations for set_tenant_domains  
     * Parameters: python manage.py set_tenant_domains
     * Run set_tenant_domains environment
  * Maybe necessary to restart app on AWS after this before possible to login to new tenant
    
* Login to admin in new tenant using admin user
  * Check passwords for utility users kiosk, tagadmin, pager are set, and if not set to correct values
  * Import Members from provided list
  * Set up Officers for previous year with provided details (once set up in dev, export for use in AWS updates)
    * Check Groups assigned properly (esp. Training, Personnel)
  * Set Brigade Details
    * All activity types are valid: deselect External and any others
    * Check social as excluded
    * Set season start date (ignore year)
    * Set activity types
    * Set excluded activities
    * Check and update location, phone number, etc.
  * Import qualifications from RFS list under admin certifications/import
  * Add TD/PD certifications for nominated drivers (manually)
  
* Test logins
  * tagadmin, kiosk, pager
  * Also try one user, with rfsID as password (should prompt to change password)

* Kiosk setup
  * Make server visible on network
    * On kiosk, add signin.org to /etc/hosts
    * On dev system, run on 0.0.0.0, not 1.0.0.127
    * On aws, add redirect for wyeept.rfstag.org and wyeept.rfstag.com (shouldn't be necessary)
  
* Test remote.it
  * If possible, cpnnect PI to external network (eg. SHADOW)
  * In [remote.it console](https://app.remote.it/#/devices) confirm that device is online, and click VNC to connect with it
  * Copy address from connection details (eg. proxy65.rt3.io:37011) and add a connection in VNC viewer with this address.
  * Connect using VNC viewer to confirm connection ok.
 

### Testing

### Full Deployment

### AWS Credits (annual)