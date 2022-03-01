# Administration Procedures (Under construction)

## Setting Up

### Adding a new Brigade

Brigade specific settings
Event types: The original list of options for setting the type of an event contained around 40 categories, 
which was seen as too much by some brigades. To simplify this, brigade administrators can now set up a 
shorter list of options (in admin, under Brigade Settings), and any events created in future will be 
restricted to that shorter list. Past events will retain their original classification.
Member activity: Currently, the Member Activity table shows hours contributed by each member during the specified season. 
This table can now be switched to show the number of events attended by members, as this is the method used by 
some brigades to assess activity. The season start date can also be changed by the brigade administrator 
(previously all brigades had to use the same date), as can the thresholds for attendance criteria for hours and 
number of events. 
These settings are available under admin:Brigade Settings.


### Preparing and Issuing Tags

Preparation

Before you start, make a list of all the new tags you want to prepare, including the member name, and their 
RFS member number

Get a batch of tags to write. You can overwrite old tags if they are no longer in use

Bring a marker pen to write the initials of the member on the tag when it is written

On the Raspberry Pi kiosk terminal, press the F11 key to show the background

Open a new command shell by clicking the black icon on the top row of the screen

Type the command : writetags

The program will prompt you to place a tag on tag reader. 

When you do, it will prompt you to provide an RFS member number. Type this in and hit ENTER

The tag should then be written. When you remove the tag, it will prompt you for another one

Repeat if needed for more tags

On the last tag, if you press ENTER when prompted for an RFS member number the program will terminate.

You can also terminate the program by typing ctrl-c

Checking the tags

Reboot the PI by clicking the top left raspberry symbol (top left of page), then choose reboot

When restarted, add a new event with description “test” and category Social

Then try to sign in to the new event using the new tags. The members name should appear in the new event, 
with the sign-in time

Tag a second time to sign out

You can also check the tag using android mobile phones. If you place the tag on the back of the phone, 
it should detect an NFC device. It will show the RFS member number, 
the date when it was created, and the brigade it belongs to.

### Training Users

### Defining Activity Types

The Member Activity report can now show all activities that were previously excluded, 
if you check the box "Add Excluded Events". All events recorded during the season, without exception, 
will be shown in the table and included in the totals, even if you marked them as excluded in the 
Brigade Settings (see below). 
Unchecking the box will remove all excluded activity types.
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

### Setting Voting Criteria


## Periodic Admin Procedures


### Updating Officers

In the current release, there's a new menu item on the main landing page under Personnel, called Change Officers. 
When you click on that, it will show a list of current officers.

Normally, this will show officers for the current season, and in the rare event of an officer being changed during the 
season, you can change the name associated with a position then save, to update it.

When you pass into a new season (the date of which is defined as Season Start in your Brigade Settings, under admin), 
there won't be any officers defined for the new season, but the officers from the previous season will still be in place 
until they are either re-elected or changed at an election.

In this case, the Change Officers form will show the officers from the previous season, but will also show a button 
that allows you to "Copy Officers to <new season>". If you click this button, the system will create new Officer 
records for all positions in the new season using the same names as the previous season. You can then edit this list 
by changing the names of the officers to match the election results, then Save to update the system.

In summary, the procedure to update officers after this year's election is as follows:
Click the menu item Personnel/Change Officers
Click the button "Copy Officers to 2021"
Change the names under the Member column to match the officers elected in the recent election.
Save


### Set Recurring Events in the Calendar

### Generate Training Reports

### Synchonising Member Qualifications

### AWS Credits (annual)


## Ad-Hoc Admin Tasks

### Adding New Members

Personnel/Add new member

Handles setup of user and contact details as well as new member record

Only available to Personnel Officer

TCard button on all events

A TCard button has been added wherever you see details of an event, 
including the kiosk, and when selecting an event in a calendar.

Shows details needed to fill in a TCard or crew assigned to event

Vehicle details (provided a vehicle is allocated)

Crew list and qualifications

### Deleting Members

Don't! If you do, you will also delete their attendance records, which is against the law.

To stay out of jail, make them inactive instead.

### COVID-19 Report

As we discussed the other week, I reviewed the NSW Government Covid safe record keeping guidelines, and it 
appears that our electronic sign-in system meets the requirements for recording the visitor details needed by 
NSW COVID contact tracing.

Hopefully this will never be needed, but I also added a new report to the sign-in server (see COVID-19 Attendance 
under the Officer menu), which lists details of all members who attended the station over the past 28 days. 
This report uses the template given in NSW COVID-safe record keeping obligations.

Our members are used to signing in and out at the station, and our attendance records are generally quite good, 
perhaps better than records coming from scanning QR codes at the station. If the brigade is ever asked to assist 
with contact tracing, this new report could be used in addition to the QR data.

For now, we are still under instructions from FCC that members need to both sign-in and also scan a QR code at the station. 
Our electronic attendance records for members appear to be sufficient to meet the NSW Government COVID requirements, 
and with this system in place, it may not be strictly necessary for members to also scan the QR code. However, 
we would need to get permission from FCC before telling members they no longer need to scan the QR codes.

Naturally, non-members and other visitors would still need to sign-in using the Attendance Book, and also scan a QR code.



## Vehicles and Equipment

### Driver Activity

### Vehicle Usage
