# The Kiosk

The Kiosk is a small computer and screen, with a tag reader attached, that replaces the old Attendance Book, 
and records attendance in electronic form. It is normally located at the front desk of the station. 

It is always-on and available 24h every day. It requires an internet connection (wifi or wired) 
to function.

The Kiosk screen shows events that start **or end** on the current day, and is automatically 
updated every night, just after midnight, to show events for the new day.

NFC tags (keyfobs) are issued to all members, and these can can be used to sign-in and sign-out 
of events shown on the kiosk screen.
 

## Basic Operations

(easyway)=
### Signing in - The Easy Way

The Kiosk is designed to make it as quick and easy as possible for members to sign-in and 
sign-out of activities at the station.

In general, the OIC who has organised an activity should set up an event in advance, and when you get to the station, 
you will see something like this on the kiosk screen:

:::{figure-md} kiosk1event
:class: myclass

<img src="assets/images/kiosk1-event-b.jpg" alt="Kiosk with 1 event" class="bg-primary mb-1">

Kiosk screen with 1 event
:::

If the event you need is on the screen, all you have to do it to place your tag on the reader, 
and you will be signed in. 

```{margin} Blank screen?
If the screen is blank or no events are available, jump to {ref}`blank_kiosk`
```

You should then hear a beep as the tag is registered, and the screen will be updated as follows, with your name in 
the event, and the time you signed in.



:::{figure-md} kiosk1event1att
:class: myclass

<img src="assets/images/kiosk-1event-1att-b.jpg" alt="Signed in!" class="bg-primary mb-1">

Signed in!
:::

When you've finished the activity, place your tag on the reader to sign-out. That's it!

:::{admonition} Why you should always sign-in with your tag
:name: usetag

There is a mechanism which allows {ref}`you to sign in without a tag<notag>` but this should only be used in 
exceptional cases, as the Kiosk is a shared computer, and doesn't know who is at the keyboard. 

Your tag is unique to you, and essentially replaces your signature in the electronic attendance 
records. Using your tag removes any doubt that it was you who signed-in, so it should be used whenever possible.

The system records when a tag is used, and if your brigade is strict about using tags, 
your administrator may remind you to use your tag if they see you are repeatedly signing in without it.

:::


(blank_kiosk)=
### What if the kiosk screen is blank?

If the OIC hasn't set up an event in advance, no event is available, and you won't be able to sign-in. 

Never fear - you can still sign-in, but first you'll need to create a new event on behalf of the OIC. You do this by 
clicking the New Event+ button at the top right of the kiosk screen, and you will then see the following form:

:::{figure-md} kiosk-newevent
:class: myclass

<img src="assets/images/kiosk-newevent-a.jpg" alt="Kiosk new event form" width="2000px" class="bg-primary mb-1">

Kiosk new event form
:::

Once you've completed the details, click Submit, and the kiosk screen should then show the event you just created.

You can now {ref}`sign-in by placing your tag on the reader<easyway>`.


:::{topic} Why do I sign-in to an event rather than just sign-in to the station?

As with the old Attendance Book, you would normally sign-in to one activity, described in the heading of the 
page (OIC, activity type, date, etc.). If you attended another activity later in the day, you would sign-out of the 
first one and go to the next page to sign-in to the next activity.

Signing in without an event would be like signing your name in the middle of a blank page in the old Attendance Book. 
You really need to fill in the details at the top of the page to give the context, and show what you are actually 
attending, and that's essentially what an event gives you.

:::


(notag)=
### Signing in without a tag

You really should {ref}`use your tag<usetag>`, but if you don't have it you can still sign 
in to an event by clicking on the sign-in icon: 

:::{figure-md} signin
:class: myclass

<img src="assets/images/signin.jpg" alt="Kiosk sign-in" width="50px" class="bg-primary mb-1">

Kiosk sign-in icon
:::


You can sign-out without a tag by clicking the green Sign-out  button next to your name.

## Advanced Operations

### Changing attendance details

If you forgot to sign-in when you arrived at the station, and go back later to sign-in, you can revise the start 
time by clicking on your name in the event. 

You will then have the option of changing the sign-in time or other details of your attendance at that event. 
Click Submit to save the new details.

### Deleting events

If a new event is created by mistake, it can be deleted using the trash icon in the event. 

You may not delete an event which already has members listed as attending (the trash icon will not shown), to avoid 
accidental loss of attendance records.

### Multiple simultaneous events

On a busy day, it is possible that events will overlap in time, or there may be several events running at the same time
(eg. Maintenance, and Training). 

If that's the case, when you present your tag to sign-in, the system will ask you to 
choose which of the available events you wish to join. Just click on the appropriate event and you will be signed in 
to that.

### Tips for organising a busy day

* Where possible, avoid overlapping events, as they will slow down the sign-in process for all members. 
  
* Choose the start and end times for events to match the expected duration of the event. Members can sign-in up to 1 
  hour before the start time, and can sign-out at any time after that (even after the end time).
  
* If necessary, the end time for an event can be set earlier than the expected finish to avoid overlaps with other events. 
  Make sure that it is set to allow any latecomers to sign-in (they can't sign-in after the end time), but it doesn't 
  have to go right to the expected end of the activity if it will cause an overlap with other events.

### Resetting the Kiosk

If, for any reason, the Kiosk becomes unresponsive, or is not working as intended, it can be restarted by using the
"three finger salute" - control-alt-delete, then choose Reboot. This will restart the Kiosk safely, and it should be
back up and running in a minute or so.

:::{warning}

Do not just turn the power off and then on again to reset the Kiosk. If the Kiosk is not shutdown properly, there 
is a risk that it will be damaged, and it may not restart.

:::

### Kiosk beeps

The Kiosk will beep when a tag is registered, as follows:

* Single high pitched tone for signin in
* Single low pitched tone for signin out
* Multiple tones when a choice of events if required


