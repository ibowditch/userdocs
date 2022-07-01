# Introduction

The RFStag system is a web application that allows RFS members to sign-in and sign-out at their station using a small 
NFC keyfob tag, rather than writing their details in the Attendance Book. 

Tags are issued to all members, and they can sign-in just by tapping their tag on a reader attached to a 
{ref}`terminal<kioskh>` at the station entrance. They can sign-out when they have finished the activity by tapping 
their tag on the reader a second time.

All attendance records are stored electronically, and reports and summaries of attendance are available to members and 
officers through a {ref}`web portal<serverh>` which can be accessed from anywhere, on any device with an internet 
connection and a browser (login required).

The system records attendance for all members, but visitors who do not have a tag should still record their details in
the (paper) Attendance Book.

(attbook-records)=
## Requirements

All RFS brigades are required, 
by [State Law](https://www.rfs.nsw.gov.au/__data/assets/pdf_file/0007/44098/1.4.3-Public-Access-to-Government-Information-v1.0.pdf), 
to ensure that all members and visitors record their attendance when participating in brigade activities.

Traditionally, attendance was recorded in an Attendance Book, normally placed at the 
front of the station. Brigade Officers completed the details of the activity at the top of each page, 
then members who attended recorded their details, including arrival and departure times and 
their signature.

This may seem like a pointless chore, but it is in place to protect Members. 

**The main reason for keeping attendance records is to ensure that there is a reliable record of Member activity 
that can be used in cases of accident or misadventure, especially when a Workers Compensation Claim is lodged. They are 
also occasionally referred to in Coronial enquiries.**


### Attendance Record Keeping

The paper Attendance Book provided a way to collect and preserve attendance records in a secure, controlled, and 
organised way, so that these records would be available for future reference whenever needed.

Used correctly, the Attendance Book provides solid, lasting, evidence that a Member was involved in an activity. The 
following table shows how the Attendance Book meets these requirements, and also how RFSTag does the same:

(main-reqs)=
| # | Key Requirement                                                                                    | Attendance Book                                                                                                                                                           | RFSTag                                                                                                                                                                                    |
|---|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. | **Unique identification** of the Member                                                            | Member's signature on the attendance record                                                                                                                               | Members sign-in with their {ref}`NFC tag<keyfobs>`, which is unique to them.                                                                                                               |
| 2. | **Participation** in the activity is clear and unambiguous                                         | Member's name and signature are recorded as part of an activity described at the top of the Attendance Book page.                                                         | Members {ref}`sign-in<easyway>` to a named activity/event on arrival at the station.                                                                                                      |
| 3. | **Physical presence** of the Member at the Station                                                 | Confirmed by the Member's signature in the Attendance Book, which is kept at the Station.                                                                                 | Members can only sign-in to an activity using the {ref}`Kiosk<kioskh>`, which is located at the Station.                                                                                  |
| 4. | **Official confirmation** of participation                                                         | The Officer In Charge (OIC) signs-off on attendance records for activities that they organise, to confirm that they are accurate and complete.              | The OIC reviews any events they run and {ref}`signs them off<off-signoff>` electronically using the web portal.                                                                            |
| 5. | **Secure storage** of the Attendance records, so that they cannot be altered at a later date.      | OIC draws a line under the records, and initials any later changes if they are approved.                                                                                  | After an event is completed, {ref}`only the OIC can amend the attendance records<off-signoff>` for an event.                                                                              |
| 6. | **Long Term storage** of records so that they may be accessed at a later date.                     | Archived by District. Attendance records are [State Records](https://legislation.nsw.gov.au/view/pdf/asmade/act-1998-17), and must be [kept for at least 25 years](https://www.rfs.nsw.gov.au/__data/assets/pdf_file/0003/171471/2.1.7-Management-of-Brigade-Records.pdf).                                                                                            | Attendance records can be {ref}`exported for printing or electronic storage<annual-att>` for archiving by the District.                                                                   |


:::{admonition} Why not use RFS ACTIV?

RFS ACTIV is an excellent system for relaying callouts to members, and assisting with forming crews 
for these callouts. 

However, at the moment, it does not have a reliable way of recording attendance at the station.

It can detect your proximity to the station from the GPS on your phone (including when driving past the station), 
but this is not the same as attendance, and it does not meet some key requirements above.

It relies on all members having mobile phones switched on at all times, and for those phones to have GPS tracking 
enabled at all times, which may not be feasible, or even acceptable for some members.

:::

### Drawbacks of the Attendance Book

Even though the paper Attendance Book meets all the above requirements, there are some significant drawbacks with 
keeping handwritten attendance records:

* Often written records are messy, sometimes illegible, inconsistent or inaccurate, and require 
  interpretation and follow-up to correct.

* The Attendance Book is always physically at the station, and the information it holds is not 
  available anywhere else. 

* There is no backup - if the Attendance Book is lost or damaged, important records will be lost forever.

* Keeping a physical Attendance Book can be unhygienic, as it (and the often shared pen) is 
  touched by many Members, and could be a vector for infections such as flu or COVID-19.

RFSTag addresses all these issues by collecting and storing attendance records electronically at the {ref}`Kiosk<kioskh>`, 
and providing access to these records and reports using the {ref}`web portal<serverh>`.


### Additional System Requirements

As well as meeting the above requirements, this is what I was aiming to do with the new system:

(availreq)=
1. Provide an easy and quick way for members to sign-in to activities at the RFS station, modelled on existing 
   procedures used with the Attendance Book.

1. Capture attendance details in electronic form to eliminate the need to transcribe attendance data.
  
1. Simple admin procedures, with minimal intervention required by brigade management to keep the system up to date 
   and running.
  
1. Improve visibility and availability of attendance data to all brigade members and management.

1. Further reduce admin effort by automatically producing useful reports, based on attendance data.

1. Provide a low-cost solution, using off-the-shelf hardware, and a modest annual subscription fee.

1. Provide high availability, reliability, and data security, including regular automatic backups.

1. Ensure data privacy, with user accounts and passwords required for access. 


### Unlocking the Value of Attendance Data

The original Attendance Book is generally fine for the purpose of meeting the legal requirements to record attendance.

However, Attendance Records also contain information that is useful for brigade management, for example:

* Gauging participation of members, especially to recognise outstanding contributions, but also to
  easily identify members who are no longer active.

* Gaining visibility on who is doing what in the brigade (and how much), especially for identifying opportunities 
  to "share the load".
  
* Capacity planning - review the membership and check the brigade has sufficient numbers and skills to meet expectations 
  and commitments in all areas.
  
* Training planning - lack of participation in certain areas can indicate that training is needed, to prevent 
  loss of skills.
  
* Determining who is entitled to vote in brigade elections, if there is some attendance criteria 
  for this (e.g. minimum of 60 hours during the years) 
  
* Summarising activity for reporting purposes, to identify trends in types of activity, and to inform
  district headquarters and other stakeholders.
  
* Real time updates of who is at station can be provided to Officers, Members and HQ if attendance records 
  are available on-line.
  
* Real-time updates of Crew Strength, including Field Officers and Response Drivers, can easily be provided to Computer
  Aided Dispatch (CAD) systems, without the need for stations to repeatedly update Crew Strength with Fire Control 
  over the radio. 


To realise the value of attendance data, many brigades transcribe the information from the Attendance Book 
into a spreadsheet or database, so that it can be analysed and summarised. This is a slow and tedious manual 
process, which requires a great deal of effort on the part of volunteer members. 

RFSTag utilises the attendance records collected at the {ref}`Kiosk<kioskh>` to provide access to all the above 
data to all members via the {ref}`web portal<serverh>`, without the need to collect or transcribe any additional data.

<!--  
:::{topic} Switching to Electronic Sign-In

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

:::
-->


## About the Project

This project to build an electronic sign-in system started in 2018, when I decided to build a web application to 
help automate some admin tasks that were taking a lot of volunteer time at my local brigade.

It started with capturing attendance records, then grew to include reporting, scheduling, and various other odds and ends.

My background both as a software engineer (in a past life) and as a former Deputy Captain, came in handy, but there was 
still a big learning curve, and I continue to improve the application as the technology evolves, and as I find better 
ways of doing things.

The system first went live in November 2018, and has been running (almost) continuously since then, including through 
the major fires of 2019-2020. 

The user base started with my home brigade (~70 members), then grew to include another 6 brigades, and it now supports 
more than 500 users.


## Site Map

This website describes following aspects of the electronic sign-in system:

1. [Introduction](background.md)

  > This section describes the origin of the system, the requirements (legal and otherwise). There is also a brief 
  > overview of the objectives of the system. 

2. [The Kiosk](kiosk.md)

  > The Kiosk collects attendance records in place of the Attendance Book, and is used by most people 
  > on a day-to-day basis. This section provides an overview of the Kiosk, along with a user guide.

3. [Events](events.md)

  > Events are a key part of the system, analogous to a page in the old Attendance Book. This section describes the
  > various types of events, and the ways they can be defined and updated.

4. [The Web Portal](server.md)

  > The system runs on a cloud server (the Kiosk is connected to the server using a web interface). This section gives a 
  > review of the features available on the web portal, which can be accessed by officers and members of the brigade 
  > from any device (login required).

5. [Administration Procedures](administration.md)

  > A brief overview of the main procedures used by system administrators to set up and run the system.


5. [Technology](technology.md)

  > A brief overview of the main technologies - both hardware and software - used in the system.


