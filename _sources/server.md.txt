# Sign-in Server (Under construction)

The entire system is a web application, which runs on a server in the cloud (in our case, this is a server in a 
data centre run by Amazon Web Services in Sydney).

All interactions with the system, including from the Kiosk (which runs in a web browser), are made through this 
web application. The Kiosk is the "shop front" of the system, and is used most frequently by most users day-to-day, and is covered in an
{ref}`earlier section<eventsection>`.

Brigade members can also access the web application directly, using their phone, tablet, or PC, as long as it has 
an internet connection and a browser available. This section describes the services available on the Sign-in server.

## Logging In

```{margin} Multiple Tenants
The system architecture is what is known as *multi-tenanted*. This allows the same server to support multiple brigades,
with each being a distinct "tenant". The brigade name in the url signifies which tenant/brigade you want to use.

Each brigade has it's own database, including the list of members, and you can only login to a brigade system if you 
are a member there. Once you are logged in, you can only access data for your own brigade, and you won't see data for 
any other brigades. 
```

The sign-in server can be reached at <https://brigade.rsftag.com/bfb>. Note that you need to substitute the word 
**brigade** in this url with the actual name of your brigade (eg. westleigh).

You will be challenged to provide a username and password before you can login to the system.

By default, your username is the same as the email address that you use to communicate with your brigade. 

The first time you login, your default password will be the same as your RFS member number - you will then be asked to 
change this password before proceeding.

If you ever need to change your password (eg. if you forget it), you can change it by clicking on the *Lost password?* 
link on the login page. The system will then email you a link, and then you can change your password.

## Landing/home page

When you have logged in the system will take you to the brigade home page, an example of which is shown below:

:::{figure-md} home-page
:class: myclass

<img src="assets/images/homepage.jpg" alt="Landing page" width="1467" class="bg-primary mb-1">

Home/landing page on server (click to enlarge)
:::

Navigation bar 
: Used to access most functions. The {ref}`following sections<menu>` describe each of these in detail.

Membership Summary
: Shows the total number of active members broken down by their skills set. 
  
  It also shows, in red, the number of members currently on duty, ie. currently signed in at the station 
  (but not yet signed out). These figures are updated live, whenever anyone signs in or out at the station.

Upcoming events
: Shows details of future events in the calendar, including the number of members who have indicated 
  that they will be attending. Further details are available by clicking on the event Details. Members can indicate 
  their intention to attend these events in the Brigade Calendar (see below)
  
Shortcuts 
: The "At Station" shortcut shows a read-only replica of the Kiosk screen, and you can also access the
  Brigade Calendar. Both of these are also available under the Members menu in the Navigation bar.


(menu)=
## Menu of Services

### Members

#### Member List

For internal use only, members have access to a summary of basic contact details of all active members through the
Member List menu item, an excerpt of which is shown below. This can be printed to PDF format from your browser 
if a hard-copy is required.

```{Warning} Member Privacy:

If members do not wish their contact details to be shared with other members they can instruct the 
Personnel/Membership Officer to remove those details from this list. 

Also, this list is for Brigade use only, and should not be shared outside the Brigade.

```

:::{figure-md} memb-list
:class: myclass

<img src="assets/images/memblist-a.jpg" alt="Landing page" width="1467" class="bg-primary mb-1">

Member List (excerpt) (click to enlarge)
:::

**Notes**

* Members only appear once on this list, in the first section they fit in to. It has the following sections:
  * Field Officers
  * Crew Leaders (CL, but not currently Field Officers)
  * Tanker Drivers (Neither Field Officers or Crew Leaders)
  * Drivers (None of above, but personnel vehicle qualified)
  * Members (None of the above)

Qualifications
: This shows any qualification in the following areas (expired qualifications shown in lower case):
* Driving
  * TD - Tanker driver
  * PD - Personnel/light vehicle driver
* First Aid (FAA, etc.)
* Safe working on roofs - SWR
* Chainsaw Operator - (TFT, TFI, etc.)
* Village Firefighter - VF
* Highest qualification - Group Leader (GL), Crew Leader (CL), Advanced Firefighter (AF), Basic Firefighter (BF)

Rank
: This shows Field Officer positions in order of rank. All other members are shown as FF (Firefighter).

RfsID
: This is the RFS Membership number issued by the RFS.

#### Member Activity

Select season - year season started
Shows hours recorded for each member in attendance book
Good for awards end of year
Also see who is not showing up
Drill down in any number to see details, including totals

The Member Activity report can now show all activities that were previously excluded, if you check the box 
"Add Excluded Events". All events recorded during the season, without exception, will be shown in the table and 
included in the totals, even if you marked them as excluded in the Brigade Settings (see below). 
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
Also in Brigade Settings, beside the Activity Types for New Events list is the list of Activity Types excluded 
from Member Activity Report. If you check an item in this list, all activities of this type will be excluded from 
the Member Activity Report. You would normally exclude Social: Social/Personal, but you can also exclude all Incidents, 
or External activities, or anything else you want. As noted above, activities that would normally be excluded 
(and not shown), can be revealed temporarily with the new "Add Excluded Events" button.

#### At Station

Read only replica  of kiosk
Updated at same time as kiosk
Look, don’t touch (except OIC)


#### Events calendar

Well organised brigade has a calendar of upcoming events
Ideally members can indicate their intention to attend
OIC can see who to expect
See what’s happened and what’s coming up
View by day/week/month
Click on event for details
Can indicate that will be attending (may be useful for call out)
Can also drop out
Officers can create new events here
Members can only look, or nominate to attend

### Training

#### Courses Available

#### Quarterly Return

#### Driver Training (placeholder)

#### Training Materials (placeholder)

#### Training Calendar

### Secretary (placeholder)

### Officers

#### Add New Event (deprecated - see Calendar)

#### Review past events (deprecated - see Calendar)

#### Review Future Events (deprecated - see Calendar)

#### Officer Calendar

#### COVID-19 Attendance

#### Admin (deprecated)

### Vehicles

#### Update Vehicle Log

#### Update Vehicle Log Sheet

#### Vehicle Movements

#### Driver Activity

#### Vehicle Bookings

#### User Docs