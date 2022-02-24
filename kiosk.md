# The Kiosk

## What is the Kiosk?

The Kiosk is a small computer and screen, with a tag reader attached, normally located at the 
front desk of the station. 

It is always-on and available 24h every day. It requires an internet connection (wifi or wired) 
to function.

The Kiosk replaces the old Attendance Book, and records attendance in electronic form.

The Kiosk screen shows events that start **or end** on the current day, and is automatically 
updated every night, just after midnight, to show events for the new day.

NFC tags (keyfobs) are issued to all members, and these can can be used to sign-in and sign-out 
of events shown on the kiosk screen.
 

## Basic Operations

### Signing in - The Easy Way

The Kiosk is designed to make it as quick and easy as possible for members to sign-in and 
sign-out of activities at the station.

In general, the OIC should set up an event in advance, and when you get to the station, 
you will see something like this on the kiosk screen:

<figure: kiosk with one event>

If the screen is blank or no events are available, jump to {ref}`blank_kiosk`.

If the event you need is on the screen, all you have to do it to place your tag on the reader, 
and you will be signed in. 

When you've finished, place your tag on the reader to sign-out. That's it!

:::{admonition} Why you should sign-in with your tag
:name: usetag

Your tag is unique to you, and essentially replaces your signature in the electronic attendance 
records. When you use your tag, there is little doubt that it was you who signed-in, so it should be
always be used where possible.

There is a mechanism which allows {ref}`notag` but this should only be used in exceptional cases, as the Kiosk is a shared computer, and 
doesn't know who is at the keyboard. 

The system records when a tag is used, and if your brigade is strict about using tags, 
your administrator will be aware, and may remind you to use your tag if they see you are
repeatedly signing in without it.

:::

(blank_kiosk)=
### What if the kiosk screen is blank?

If the OIC hasn't set up an event in advance, no event is available, and you won't be able to sign-in. Footnote: this 
would be like signing you name in the middle of a blank page in the old attendance book. You really need to fill in the
details at the top of the page before signin in.

Never fear - you can still sign-in, but first you'll need to create a new event on behalf of the OIC. You do this by 
clicking the New Event+ button at the top right of the kiosk screen, and you will see the following form:

Link to: New Event form (no attendees)


Once you've completed the details, click Submit and the kiosk screen should then show the event you just created.

You can now sign-in by placing your tag on the reader.

(notag)=
### Signing in without a tag

You really should use your tag - see {ref}`use your tag<usetag>`, but if you don't have it you can still sign 
in to an event by clicking on the (sign-in icon) in the event. You will need to provide your name 
and the time you are signing in, then submit, and you're in!

You can sign-out without a tag by clicking the green Sign-out button next to your name.


## Events

Events are a central part of the sign-in system. When you attend the station, you sign-in to an activity that is 
occurring at the station, in the same way that you signed into an activity on the old Attendance Book. The details
of the activity were given at the top of the page in the Attendance Book, including the date, OIC, a description 
of the activity etc.

An Event on the sign-in system is just like a page in the Attendance book. When you create an Event, you provide the
same details as if you were filling in the top of the page in the Attendance book.

When these details have been supplied, you will have a new event that members can sign-in to.


:::{topic} Anatomy of an Event

An event consists of a heading, containing information previously held in the heading of a page in the Attendance Book, 
and a list of attendees, including when they signed-in and signed out.

:::

![Current Event on the Kiosk!](/assets/images/currentevent-a2.jpg "Current Event")

:::{topic} Updating an event on the kiosk

The following actions will update an event on the kiosk:

1. Signing in or signing out with a tag.
2. Signing in using the icon on the top right of the event
3. Signing out using the "Sign-Out" button
4. Clicking the title (event details) to edit the event
5. Clicking a member name to edit their attendance details.

:::

### A Busy Day on the Kiosk

:::{figure-md} full-kiosk
:class: myclass

<img src="assets/images/fullkiosk-a.jpg" alt="Busy Kiosk" width="2000px" class="bg-primary mb-1">

Busy Kiosk screen (click to enlarge)
:::

[Go to the full kiosk!](full-kiosk)

:::{topic} Event Types and Controls

Events come in the following types:

1. Open/available
   
   Events become open 1 hour before their start time and remain open until their end time. When they are open, 
   they will accept sign-ins from members either using a tag, or using the sign-in icon.

1. Closed/completed
   
   Events close when their finish time has passed. They will be shown with a grey background when they are 
   closed, and will not accept sign-in attempts with a tag. The sign-in icon will also be removed.
   
1. Future
   
   Events starting more than 1 hour in the future are shown with a dashed border. They will not be available 
   to sign-in with a tag, and no sign-in icon is shown for future events.

1. Overnight
   
   Normally, events are removed from the kiosk at midnight when the display is updated. However, you can specify
   that an event runs overnight by giving a finish time in the next day. The kiosk shows all events that start 
   **or end** on the current day, so such an event will appear on the start day and on the end day. This allows 
   crew to sign out when they return from night shift.

1. Overlapping
   
   Events can overlap and/or run simultaneously. When they do, members will be asked to choose which event they
   want to attend when they tag in.
   
:::

:::{warning} Set the end time for overnight events

If the OIC doesn't set the end time of an event so that it end the next day, members won't be able to sign-out
when they return from their shift, as the event won't be shown on the kiosk.

If there's any chance you might be out past midnight (like Cinderella), make sure you set the end time past midnight. 
If you get back early, no problem.

:::



:::{topic} Activity Types

activity types and collourss:

1. Open/available
   Events become open 1 hour before their start time and remain open until their end time. When they are open, 
   they will accept sign-ins from members either using a tag, or using the sign-in icon.

1. Closed/completed
   Events close when their finish time has passed. They will be shown with a grey background when they are 
   closed, and will not accept sign-in attempts with a tag. The sign-in icon will also be removed.
   
1. Future
   Events starting more than 1 hour in the future are shown with a dashed border. They will not be available 
   to sign-in with a tag, and no sign-in icon is shown for future events.

1. Overnight
   Normally, events are removed from the kiosk at midnight when the display is updated. However, you can specify
   that an event runs overnight by giving a finish time in the next day. The kiosk shows all events that start 
   **or end** on the current day, so such an event will appear on the start day and on the end day. This allows 
   crew to sign out when they return from night shift.




:::





### Pager callout

:::{topic} Pager calls

Pager Calls are detected by separate system which automagically creates a new event on the server 
as soon as a callout is received for your brigade.

The event should be available for members to sign-in to when they arrive at the station.

:::

![Pager callout alt!](/assets/images/pagercall-a2.jpg "Pager callout event")


## Attendance

## Tagging



