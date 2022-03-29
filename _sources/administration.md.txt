# Administration Procedures (Under construction)

```{margin} Restricted Access
Access to most of the Administration procedures below is restricted to genuine system admins, 
and these not generally available to Members or Officers.
```

## Preparing and Issuing Tags

### Preparation

* Before you start, make a list of all the new tags you want to prepare, including the member name, and their 
RFS member number

* Get a batch of tags to write. You can overwrite old tags if they are no longer in use

* Bring a marker pen to write the initials of the member on the tag when it is written

### Making Tags

* On the Raspberry Pi kiosk terminal, press the F11 key to show the background

* Open a new command shell by clicking the black icon on the top row of the screen

* Type the command : **writetags**

* The program will prompt you to place a tag on tag reader. When you do, it will prompt you to provide an RFS member number. 
Type this in and hit ENTER. The tag should then be written. 
  
* When you remove the tag, it will prompt you for another one.  Repeat if needed for more tags

* On the last tag, if you press ENTER when prompted for an RFS member number the program will terminate. You can 
  also terminate the program by typing ctrl-c

### Checking the tags

* Reboot the PI by clicking the top left raspberry symbol (top left of page), then choose reboot

* When restarted, add a new event with description “test” and category Social

* Then try to sign in to the new event using the new tags. The members name should appear in the new event, 
with the sign-in time. Tag a second time to sign out

* You can also check the tag using android mobile phones. If you place the tag on the back of the phone, 
it should detect an NFC device. It will show the RFS member number, the date when it was created, 
  and the brigade it belongs to.

##  Brigade specific settings

If you have full admin privileges, under Brigade Settings, you will see your own Brigade. Select that and then you will
see the following fields:

The following settings should be set before the system goes live for your brigade:

Season Start
: This sets the start of the period when member activity is calculated. The end is exactly 
  1 year (365 days, or 366 in a leap year) later. It should normally be set so that the end is just before the next AGM. 
  The same date applies to all seasons, and the year part can be ignored.

Vote Count Hours
: Check this if you want hours to be the default units in the {ref}`Member Activity report<memb-act>`. If not checked, the default 
unit will be Events. It's only a default, and either unit can still be selected in the Member Activity table.

(set-vote-crit)=
Vote threshold hours
: This defines the number of Hours required to be eligible to vote in Brigade Elections. Voting Criteria are normally
defined in the Brigade Constitution, and if Hours are defined there, set this value to match.

Vote margin hours
: If a member is just below the Vote threshold hours, you can set this to show that they are nearly there 
  (coloured yellow in the table). For example, if set to 10, with Voting Threshold at 60, if a member is between 50-60 
  at the end of the season, they will show as yellow, if below 50 they will be red.

Vote threshold events/Vote margin events:
: Same as Vote Threshold Hours, except used where events are the preferred units rather than Hours.

Activity Types
: This sets the list of activities that are available when creating a new event. Choose your selection from the large 
list available. These will then appear in the dropdown box as options for Activity Type when 
a {ref}`new event is created<kiosk-newevent>`.

  This doesn't affect existing events, and they retain their original activity type. 
  
  You can change this setting in future if you want to add other event types.

Excluded activity types
: Any activity types selected here will be excluded from Member Activity calculations for voting eligibility.
  Generally, only Social/Personal are excluded, but this can be changed as needed.
  There is a checkbox on the {ref}`Member Activity Table<memb-act>` labelled *Add Excluded Events*, that will include 
  these events (they are excluded by default). If you drill down into one of the numbers, Excluded events will be shown in 
  grey (normally they are not shown at all).

## Periodic Admin Procedures

### Set Recurring Events in the Calendar

### Synchronising Member Qualifications

### AWS Credits (annual)


## Ad-Hoc Admin Tasks

### Deleting Members

Don't! If you do, you will also delete their attendance records, which is against the law. To stay out of jail, 
check the **Inactive** box next to the Member's name instead.

### Changes to Vehicle Fleet
