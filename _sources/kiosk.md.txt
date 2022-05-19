(kioskh)=
# The Kiosk

The Kiosk is a small computer (a Raspberry PI), with a screen and a NFC tag reader attached, that 
replaces the old paper Attendance Book, and records attendance in electronic form. It is normally located 
at the front desk of the station. 
:::{figure-md} kiosk-parts
:class: margin

<img src="assets/images/kiosk-parts.jpg" alt="Kiosk parts" width="1000px" class="bg-primary mb-1">

NFC tag, reader, and PI
:::
It is always-on and available 24 hours every day. It requires an internet connection (Wi-Fi or wired) 
to function.

The Kiosk screen shows [events](events.md "described in a later section") that start **or end** on the current day, 
and is automatically updated every night, just after midnight, to show events for the new day.

(keyfobs)=
NFC tags (keyfobs) are issued to all members, and these can can be used to sign-in and sign-out 
of events shown on the kiosk screen.
 
## Basic Operations

(easyway)=
### Signing in - The Easy Way

The Kiosk is designed to make it as quick and easy as possible for Members to sign-in and 
sign-out of activities at the station.

In general, the OIC who has organised an activity should {ref}`set up an event in advance<cal-add-event>`, 
and when you get to the station, you will see something like this on the kiosk screen:

:::{figure-md} kiosk1event
:class: myclass

<img src="assets/images/kiosk1-event-b.jpg" alt="Kiosk with 1 event" class="bg-primary mb-1">

Kiosk screen with 1 event
:::

If the event you need is on the screen, all you have to do is to hold your tag near the reader, 
and you will be signed in. (If the screen is blank or no events are available, jump to {ref}`blank_kiosk`)

:::{figure-md} tagging
:class: margin

<img src="assets/images/tagging2.jpg" alt="tagging" width="1000px" class="bg-primary mb-1">

Hold your tag close to the centre of the reader for 1 second
:::

You should hear a beep as the tag is registered, and the screen will be updated as follows, with your name in 
the event, and the time you signed in.

:::{figure-md} kiosk1event1att
:class: myclass

<img src="assets/images/kiosk-1event-1att-b.jpg" alt="Signed in!" class="bg-primary mb-1">

Signed in!
:::
When you've finished the activity, use your tag again to sign-out. That's it!

:::{admonition} Why you should always sign-in with your tag
:name: usetag
:class: tip

There is a mechanism which allows {ref}`you to sign-in without a tag<notag>` but this should only be used in 
exceptional cases, as the Kiosk is a shared computer, and doesn't know who is at the keyboard. 

Your tag is unique to you, and essentially replaces your signature in the electronic 
attendance records. Using your tag leaves little doubt that it was you who signed-in (which is a 
{ref}`key requirement of the system<main-reqs>`), so it should be used 
whenever possible.

The system records when a tag is used, and if your brigade is strict about using tags, 
your administrator may remind you to use your tag if they see you are repeatedly signing in without it.
:::


(blank_kiosk)=
### What if the Kiosk Screen is Blank?

If the OIC hasn't {ref}`set up an event<cal-add-event>` in advance, no event is available, and you won't be 
able to sign-in immediately. 

Never fear - you can still sign-in, but first you'll need to create a new event on behalf of the OIC. You do this by 
clicking the <span class="badge badge-pill badge-primary">**New Event+**</span> button at the top right of 
the kiosk screen, and then you will then see the following form:

:::{figure-md} kiosk-newevent
:class: myclass

<img src="assets/images/kiosk-newevent-a.jpg" alt="Kiosk new event form" width="2000px" class="bg-primary mb-1">

Kiosk new event form
:::

Once you've entered the details, click <span class="badge badge-pill badge-primary">**Submit**</span> (top left), 
and the kiosk screen should then show the event you just created.

You can now {ref}`sign-in using your tag<easyway>`.

(need-event)=
:::{topic} Why do I need to create an event rather than just sign-in to the station?

Why not just use a Bundy-style clock in?

As with the old Attendance Book, you would normally sign-in to one activity, described in the heading of the 
page (OIC, activity type, date, etc.). If you attended another activity later in the day, you would sign-out of the 
first one and go to the next page and sign-in to the next activity.

This shows that the member participated in a specific activity (see {ref}`Key requirement #2<main-reqs>`), rather 
than just arrived at the station, where there could be a number of activities underway at any time.

In the new system, signing in without an event would be like signing your name in the middle of a blank page in the 
old Attendance Book. You need to fill in the details at the top of the page to give the context, and show 
what activity you are actually attending, and that's essentially what an event gives you.

:::


(notag)=
### Signing in Without a Tag

You really should {ref}`use your tag<usetag>`, but if you don't have it you can still sign-in to 
an event by clicking on the sign-in icon in the event: 

:::{figure-md} signin
:class: myclass

<img src="assets/images/signin.jpg" alt="Kiosk sign-in" width="50px" class="bg-primary mb-1">

[comment]: <> (<span class="fa fa-sign-in fa-xl" style="color:blue; font-size:20px;"></span>)


Kiosk sign-in icon
:::


You can sign-out without a tag by clicking the <span class="badge badge-pill badge-success">Sign Out</span> button next to your name.

## Advanced Operations

```{margin} Forms block sign-in
Forms such as [Changing Event Details](change-event) prevent members 
from signing in, so shouldn't be left uncompleted on the Kiosk screen. 
```

(change-event)=
### Changing Events

Any event on the Kiosk screen can be updated by clicking on the title, in this case: 
<span style="color:blue;">"Assist SES in Hornsby Area"</span>:

:::{figure-md} event2edit
:class: myclass

<img src="assets/images/kiosk1event-edit.jpg" alt="Single event" width="1467" class="bg-primary mb-1">

Event to be updated
:::

The Kiosk will then display a form with all the details of the event. Everything except the date of the 
event can be changed/updated.

Click <span class="badge badge-pill badge-primary">**Submit**</span> when done, and the revised event will 
appear on the Kiosk.


:::{figure-md} event-update
:class: myclass

<img src="assets/images/event-edit-a.jpg" alt="Edit an event" width="1467" class="bg-primary mb-1">

Update Event Form (click to enlarge)
:::

**Notes:**

* Members can be added without start or end times, as a placeholder, if you know in advance who is expected to attend.
  This is useful for planning events when you know who will be coming. These members will still have to sign in 
  when they arrive. Other members can still sign-in to this event, even they are not on the preset list.

* Details such as "K1B driver" can be added for each member to reflect roles allocated by the Crew Leader.

* Member qualifications can be reviewed using the <span class="badge badge-pill badge-warning">**T-Card**</span> 
  {ref}`option<tcard>` (top right)
  
* Vehicles used in the activity can be marked (use the ctrl key to select multiple vehicles) as allocated, which is 
  useful in determining {ref}`vehicle bookings<vehbook>`.

(delatt)=
* Attendees can be removed if necessary using the *Delete* checkbox to the right of their name. This is useful if someone 
  signed in to the wrong event by mistake. Use with caution though, as genuine attendance records should not be deleted.


(change-att)=
### Changing Attendance

If you forgot to sign-in when you arrived at the station, and go back later to sign-in, you can revise the start 
time by *clicking on your name* in the event.

You will then have the option of changing the sign-in time or other details of your attendance at that event. 
Click <span class="badge badge-pill badge-primary">**Submit**</span> to save the new details.

If you sign-out by accident, you can delete the out time using the same method, and you will no 
longer be signed out.

If you sign-in by accident, you can delete your attendance using the {ref}`delete attendance option<delatt>` 
in the event form.


### Deleting Events

If a new event is created by mistake, it can be deleted using the trash 
icon <span class="fa fa-trash fa-lg" style="color:blue;"></span> in the event. 

You may not delete an event which already has members listed as attending (the trash icon will not be shown), to avoid 
accidental loss of attendance records.

### Bulk Transfer of Members to a New Event

The <span class="badge badge-pill badge-info">**Transfer**</span> button, available in the form used to 
change events, allows members to be transferred from one event to another following event. 
This saves the fuss of everyone signing out and then signing in immediately to a new event.

In the following example, the brigade had a general meeting in the morning. The meeting started at 9:30 and 
finished at 10:30, earlier than the planned finish time of 11:00. 
The current time is 10:40, and 3 of the original 10 attendees have already signed out and left. 

The remaining members are available to help in the next activity - Vehicle Maintenance - which will start at the 
current time.

:::{figure-md} prexfer
:class: myclass

<img src="assets/images/prexfer-a.jpg" alt="Monthly Meeting" width="1467" class="bg-primary mb-1">

Monthly Meeting
:::

Open the meeting event by clicking on the 
title <span style="color:blue;">"March General Meeting"</span>, to get to the following form:

:::{figure-md} updxfer
:class: myclass

<img src="assets/images/updxfer2.jpg" alt="Update Monthly Meeting" width="1467" class="bg-primary mb-1">

Update Monthly Meeting (Click to enlarge)
:::

Then click the <span class="badge badge-pill badge-info">**Transfer**</span> button at the top right. 

In the Transfer form, fill in the details of the next event (Maintenance - Vehicle Checks).

:::{figure-md} inxfer
:class: myclass

<img src="assets/images/inxfer-a.jpg" alt="Transfer from Monthly Meeting" width="1467" class="bg-primary mb-1">

Transfer from Monthly Meeting (Click to enlarge)
:::

<span class="badge badge-pill badge-primary">**Submit**</span> the Transfer form with the new details, 
then you will return to the main Kiosk screen:

:::{figure-md} postxfer
:class: myclass

<img src="assets/images/postxfer.jpg" alt="Transfer Complete" width="1467" class="bg-primary mb-1">

Transfer Complete (Click to enlarge)
:::

All remaining members (who hadn't already signed out from the Meeting event), have been transferred from the 
Meeting event to the new Maintenance event. They have been automatically signed out of the Meeting event, and 
signed into the new Maintenance event. They only need to sign-out once, when they leave.

If anyone was transferred to the new Maintenance event, but has to leave, they can just sign-out anyway.

The Meeting event end time is adjusted to the time of the transfer, and is now closed, so no-one else 
can sign-in to it.

Members who had already signed out of the Meeting event at the time of transfer, are not transferred to the 
new Maintenance event. They can sign-in to the new event if they hadn't really left.

(tcard)=
### T-Cards

In the top right of the {ref}`event form<event-update>` (top right) you will see a 
<span class="badge badge-pill badge-warning">**T-Card**</span>  button. 
This is used to retrieve most of the information needed to complete a T-Card. 
It's not really intended for use on the Kiosk, but an OIC can access this 
information in the front seat of a truck using their phone, so it might be handy then.


### Multiple Simultaneous Events

On a busy day, it is possible that events will overlap in time, or there may be several events running at the same time
(e.g. Maintenance, and Training). 

If that's the case, the system needs to {ref}`work out which event you want to join<flowchart-pic>`.

When you present your tag to sign-in, the system will ask you to choose which of the available events you wish 
to join. Just click on the appropriate event, and you will be signed in to that.


### Tips for Organising a Busy Day

* Where possible, *avoid overlapping events*, as they will slow down the sign-in process for all members. 
  
* Choose the start and end times for events to match the expected duration of the event. Members can sign-in up to 1 
  hour before the start time, and can sign-out at any time after that (even after the end time).
  
* If necessary, the end time for an event can be set earlier than the expected finish to avoid overlaps with other events. 
  Make sure that it is set late enough to allow any latecomers to sign-in (they can't sign-in after the end time), 
  but it doesn't have to go right to the expected end of the activity if it will cause an overlap with other events.

### Resetting the Kiosk

If, for any reason, the Kiosk becomes unresponsive, or is not working as intended, it can be restarted by using the
*three finger salute* - ctrl-alt-delete - then choose Reboot. This will restart the Kiosk safely, and it should be
back up and running in a minute or so.

:::{admonition} Do not turn the power off and then on again to reset the Kiosk
:class: warning
If the Kiosk is not shutdown properly, there is a risk that it will be damaged, and it may not restart.
:::

### Kiosk Beeps

The Kiosk will beep when a tag is registered, as follows:

* Single high-pitched tone for signing in
* Single low-pitched tone for signing out
* Multiple tones when a choice of events is required

(flowchart)=
### Tagging Flowchart

When you place your tag on the reader to sign in, the system goes through the following steps to work out an 
appropriate action:

1. Check if you are an active member of this brigade. If not, you can't sign-in.

2. Check if you are already signed in to an event today. If you are, your tag will sign you out of that event.

3. If you aren't signed in to anything, it will check what events are available. If there's only one, then you will be
   signed into that immediately.
   
4. If there is more than one event available (overlapping events), you will be asked to choose which one you want to 
   enter.
   
5. If there are no events available, you will be prompted to create a new event before you can sign in.


:::{figure-md} flowchart-pic
:class: myclass

<img src="assets/images/tag-flowchart.jpg" alt="Tagging flowchart" width="1680px" class="bg-primary mb-1">

Tagging flowchart
:::


