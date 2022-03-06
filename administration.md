# Administration Procedures (Under construction)

```{margin} Restricted Access
Access to most of the Administration procedures below is restricted to genuine system admins, 
and these not generally available to Members or Officers.
```

## Adding a new Brigade

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

If you have full admin privileges, under brigade Settings, you will see your own Brigade. Select that and then you will
see the following fields:

Location - used in landing page
Phone - used in landing page
Bio - used?

### Season Start Date

If you go to admin - Brigade Settings - then choose your brigade, you can set the following:

1. Season Start: This sets the start of the period when member activity is calculated. 
   The end is exactly 1 year (365 days, or 366 in a leap year) later. It should normally be set so that the end is just before the next AGM. The same date applies to all seasons, and the year part can be ignored.

2. Vote Count Hours: check this if you want hours to be the default units in the Member Activity report. 
   Should be checked for Ku-ring-gai, but eg. Westleigh count events instead. 
   It's only a default, and either unit can still be selected in the Member Activity table.

3. Vote threshold hours: our current rules require members to contribute 60 hours each season, so set that here.

4. Vote margin hours: If a member is just below the Vote threshold hours, you can set this to show that they are nearly there (coloured yellow in the table). 
   I set this to 10 so if you are between 50-60 at the end of the season, you will show as yellow, if below 50 you will be red.

5. Vote threshold events, margin events: same as above, except used for events rather than hours.

6. Activity Types: This sets the list of activities that are available when creating a new event. At the moment, 
   it includes the full list that we used for the past 2 years, with Village being added as well. 
   You can make a smaller list by selecting only those you want (use the control key to do multiple selections). 
   This doesn't affect existing events, and they retain their original activity type. 
   You can change this in future if you want to add other event types.

7. Excluded activity types: Any activity types selected here will be excluded from Member Activity calculations. 
   At the moment, only Social/Personal are excluded, but this can be changed as needed.


### Activity types 

The original list of options for setting the type of an event contained around 40 categories, 
which was seen as too much by some brigades. To simplify this, brigade administrators can now set up a 
shorter list of options (in admin, under Brigade Settings), and any events created in future will be 
restricted to that shorter list. Past events will retain their original classification.


Member activity: Currently, the Member Activity table shows hours contributed by each member during the specified season. 
This table can now be switched to show the number of events attended by members, as this is the method used by 
some brigades to assess activity. The season start date can also be changed by the brigade administrator 
(previously all brigades had to use the same date), as can the thresholds for attendance criteria for hours and 
number of events. 

These settings are available under admin:Brigade Settings.

The Member Activity report can now show all activities that were previously excluded, 
if you check the box "Add Excluded Events". All events recorded during the season, without exception, 
will be shown in the table and included in the totals, even if you marked them as excluded in the 
Brigade Settings (see below). 
Unchecking the box will remove all excluded activity types.

### Activity Type Groupings

Activity types are organised in groups, and these groups are shown as headings in the Member Activity Report. 
If all event types in a group are excluded in Brigade Settings, and the check box "Add Excluded Events" is not checked, 
the group heading, eg. External, will not be shown in the Member Activity table.

If you drill down on any item in the Member Activity table, it will show a list of events represented by that item. 
This page also has a "Show Excluded Events" check box, and if it is checked, it will show events that would normally 
be excluded in grey, otherwise, they will not be shown at all.

The admin page for Brigade Settings has been tidied up. Activity Types for New Events shows the activity types that 
will appear in the drop down box when creating a new event. This list is now shown as checkboxes - check each item 
you want to appear when creating new events.  The list also shows the group the activity belongs to, 
eg.  Additional: Meeting, belongs to group "Additional".

Also in Brigade Settings, beside the Activity Types for New Events list is the list of Activity Types excluded from 
Member Activity Report. If you check an item in this list, all activities of this type will be excluded from 
the Member Activity Report. You would normally exclude Social: Social/Personal, but you can also exclude all Incidents, 
or External activities, or anything else you want. As noted above, activities that would normally be excluded (and not shown), 
can be revealed temporarily with the new "Add Excluded Events" button.

### Setting Season Details

(set-vote-crit)=
### Setting Voting Criteria


## Periodic Admin Procedures

### Set Recurring Events in the Calendar

### Synchonising Member Qualifications

### AWS Credits (annual)


## Ad-Hoc Admin Tasks

### Deleting Members

Don't! If you do, you will also delete their attendance records, which is against the law.

To stay out of jail, make them inactive instead.


### Changes to Vehicle Fleet
