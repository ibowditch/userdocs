# Project Background

This project to build an electronic sign-in system started in 2018, when I decided to build a web application to 
help automate some admin tasks that were taking a lot of volunteer time at my local brigade.

It started with capturing attendance records, then grew to include reporting, scheduling, and various other odds and ends.

My background as a software engineer (in a past life) came in handy, but there was still a big learning curve, and I 
continue to improve the application as the technology evolves, and as I find better ways of doing things.

The system first went live in November 2018, and has been running (almost) continuously since then, including through 
the major fires of 2019-2020. 

The user base started with my home brigade (~70 members), then grew to include another 3 brigades, and it now supports 
more than 300 users.

## Requirements

Brigades have an obligation, {ref}`under law<legalreqs>`, to collect and maintain attendance records. 
Given that we have to do this, how can we make the collection of these records more efficient, and what can 
we do with these records once they are collected?

(legalreqs)=
### Legal Requirements

The Executive at all RFS brigades are required, 
by [State Law](https://www.rfs.nsw.gov.au/__data/assets/pdf_file/0007/44098/1.4.3-Public-Access-to-Government-Information-v1.0.pdf), to ensure that all members and visitors 
record their attendance when participating in brigade activities.

Traditionally, attendance was recorded in an Attendance Book, normally placed at the 
front of the station. Officers completed the details of the activity at the top of each page, 
then members who attended recorded their details, including arrival and departure times and 
their signature.

Attendance records are [State Records](https://legislation.nsw.gov.au/view/pdf/asmade/act-1998-17), and must be 
[kept for at least 25 years](https://www.rfs.nsw.gov.au/__data/assets/pdf_file/0003/171471/2.1.7-Management-of-Brigade-Records.pdf). 
They are occasionally required during Coronial or other enquiries, and as such they 
must be an accurate record of who attended and for what purpose. The Officer In Charge (OIC) of 
each activity is required to check and sign-off on attendance records for activities that they 
organise.

### System Requirements

This is what I was aiming to do with the new system:

1. Provide an easy and quick way for members to sign-in to activities at the RFS station, modelled on existing 
  procedures used with the Attendance Book.

1. Capture attendance details in electronic form to reduce admin load for volunteers at RFS brigades
  
1. Simple admin procedures, with minimal intervention required by brigade management to keep the system up to date 
  and running.
  
1. Improve visibility and availability of attendance data to all brigade members and management.

1. Futher reduce admin effort by automatically producing reports based on attendance data.

1. Low cost solution, using off-the-shelf hardware and a small annual subscription fee.

(availreq)=
1. High availability and reliability, including regular automatic backups.

1. Secure solution with password required for access. 


## Attendance Records

### The Attendance Book

For many years, the  {ref}`RFS has required<legalreqs>` each brigade to keep an Attendance Book in their station, 
and all members have had to sign in and out of activities at the station.

Keeping handwritten attendance records has some significant drawbacks:

* Often written records are messy, sometimes illegible, inconsistent or inaccurate, and require 
  interpretation and follow-up to correct.

* The Attendance Book is always physically at the station, and the information it holds is not 
  available anywhere else. 

* There is no backup - if the Attendance Book is lost or damaged, important records will be lost forever.

* Keeping a physical Attendance Book can be unhygienic, as it (and the shared pen) is 
  touched by many Members, and could be a vector for infections such as flu or COVID-19.


### The Value of Attendance Data

The original Attendance Book is generally fine for the purpose of meeting the legal requirements to record attendance.

However, Attendance Records also contain information that is useful for brigade management, for example:

* Gauging participation of members, especially to recognise outstanding contributions, but also to
  identify members who are no longer active.

* Gaining visibility on who is doing what in the brigade (and how much), especially for identifying opportunities 
  to "share the load".
  
* Capacity planning - review the membership and check the brigade has sufficient numbers and skills to meet expectations 
  and commitments in all areas.
  
* Training planning - lack of participation in certain areas can indicate that training is needed, to prevent 
  loss of skills.
  
* Determining who is entitled to vote in brigade elections, if there is some attendance criteria 
  for this (eg. minimum of 60 hours during the years) 
  
* Summarising activity for reporting purposes, to identify trends in types of activity, and to inform
  district headquarters and other stakeholders.

Because of this, many brigades transcribe the information from the Attendance Book into a spreadsheet 
or database, so that it can be analysed and summarised. This is a slow and tedious manual process, which requires 
a great deal of effort on the part of volunteer members. 


## Switching to Electronic Sign-In

Collecting attendance records electronically reduces admin overheads, and allows brigades to more easily extract 
the useful data they contain to help run the brigade more efficiently.


| Attendance Book              | Electronic sign-in                                                                                                                    |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Slow, manual process         | Fast, convenient recording of sign-in and sign-out using NFC* tag                                                                     |
| Messy, illegible, incomplete | All data collected electronically in structured form                                                                                  |
| No electronic data           | All data recorded in system database which can be accessed and used by all Members and Officers. Import/export available for reports. |
| Only available at Station    | Attendance information can be accessed from anywhere, on any device with an internet browser, by authorised users.                    |
| Inconvenient for scheduling  | Events can be scheduled and attendance planned and agreed on-line in advance, without the need for excessive email exchanges          |
| [COVID] Cross-infection risk | Touch free sign-in and out using electronic tag                                                                                       |



:::{admonition} Why not use ACTIV?

ACTIV is an excellent system provided by the RFS for relaying callouts to members, and assisting with forming crews 
for these callouts. 

However, at the moment, it does not have a reliable way of recording attendance at the station.

It can detect your proximity to the station from your phone (including when driving past the station), 
but this is not the same as attendance, and does not meet the current requirements of the SOPs and legislation for
reliable and accurate attendance records.

The GPS solution on your phone would also have to be always-on, meaning the good folks at ACTIV could track your 
movements much of the time. No thanks.

:::


### Using the System to Sign In

All Brigade Members are issued with a small key fob tag, which will be used for signing in and 
out at the Station.

The OIC organising an activity schedules the event online in advance, using a phone, tablet or PC.

On the day of the activity, Members arriving at the Station will see the activities planned 
for that day on a screen at the entrance of the Station.

Members will then tap their tag on a reader to sign-in. If there is a only one activity 
planned at that time, they will be automatically signed in. If there is more than one 
activity planned at that time, they will be asked to choose their activity.

When a Member has finished, they should tap their tag on the reader to sign-out.

