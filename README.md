RTFPInbox Data Structure Manual1

# RTFPInbox Data Structure Manual

Jordan Boyle

Virginia Tech

## Notice To Reader

This is the User Manual for the RTFPInbox Data Structure. At the time of writing this Data Structure is in Version 1.5.0. If the Version in this Manual does not match the Version being utilized by the User please refer to the Author of this Manual or the Maintainer of the Structure if the Author is no longer available.

## RTFPInbox Data Structure Overview

_Figure 1 RTFPINBOX Data Structure Block Diagram._

This Data Structure was designed for the Use &amp; Abuse of Personal Information Study by members of the Raytheon Technologies Fellowship Program. ![](RackMultipart20211119-4-9ibr0o_html_25ba67fe7ab58fe8.png) ![Shape1](RackMultipart20211119-4-9ibr0o_html_5d5ff8cffc3d4cb3.gif)

## Section 1: Inbox

### ![Shape2](RackMultipart20211119-4-9ibr0o_html_136727cd5afb026b.gif)

_Figure 2 The Inbox Object_

O ![](RackMultipart20211119-4-9ibr0o_html_5e5f823cfe53a7fe.png)
 verview

Each object in this Structure represents one person&#39;s Inbox. The inbox will be known by a unique ID that will be assigned to it upon creation. This ID is the Primary Key for identifying the Inbox, and the User will note that it is identified as such in Figure 1. The Inbox contains the ID of the person it is associated with and their name, both as strings. It contains the Demographics of that person as a Demographics object, and a list of Email objects that makes up the contents of that person&#39;s inbox. It has 3 protected values, size, the number of emails in the inbox as an int, maxdate, the date of the last email received by the inbox, and mindate, the date of the first email received by the inbox. In order for this object to be created only the ID and the Name must be provided. The other values can be added after creation and the protected values are adjusted using the add or remove email methods. With the exception of the protected values, values in the Inbox Object can be accessed via the syntax:

nameofinbox.valuerequested

Where nameofinbox is the name of the inbox and valuerequested is the value the user is trying to access.

### Methods

The Inbox object contains 14 methods.

#### AddEmail(message):

The first method in the Inbox Structure is the AddEmail method. This method creates an email object and adds it to the inbox. It will also update the inbox size and the min and max date accordingly. It requires a single message object, and it will throw an error if the input is not a single message object. This method is called using the syntax:

nameofinbox.addemail(message)

With nameofinbox being the name of the inbox and message being the message object the user is trying to add to the email list. Normally this method is run in a for loop with a list of messages.

#### BySender(sender):

This method finds and returns list of messages sent by sender. It takes a string, which can either be the sender&#39;s email address or their name, and it searches the email list and returns a list of emails sent by the sender the user inputted. This method is called using the syntax:

nameofinbox.bysender(sender)

With nameofinbox being the name of the inbox and sender being the sender the user is searching for.

#### ByDate(start\_date, end\_date, inc):

This method finds and returns list of messages between 2 dates. If the Boolean value inc is true this method is inclusive, otherwise it is non-inclusive. It will throw errors if the inputs are not dates or if the dates are out of bounds. This method is called using the syntax:

nameofinbox.bydate(start\_date, end\_date, inc)

With nameofinbox being the name of the inbox, start\_date being the start date of the search parameters, end\_date being the end date of the search parameters and inc being the Boolean that triggers inclusive or non-inclusive modes.

#### ByNumber(start\_num, end\_num, inc):

This method finds and returns list of messages between 2 indices. If the Boolean value inc is true this method is inclusive, otherwise it is non-inclusive. It will throw errors if the inputs are out of bounds. This method is called using the syntax:

nameofinbox.bynumber(start\_num, end\_num, inc)

With nameofinbox being the name of the inbox, start\_num being the starting index of the search parameters, end\_num being the ending index of the search parameters and inc being the Boolean that triggers inclusive or non-inclusive modes.

#### BySubject(keyword):

This method finds and returns list of messages containing keyword/s. It takes either a string or a list of strings. If the user inputs a string this method will search the subjects of the emails in the email list and return a list of all the emails whose subjects contain the string inputted by the user. If the user inputs a list of strings, it will return a list of messages whose subjects contained all of the strings in the list. This method is called using the syntax:

nameofinbox.bysubject(keyword)

With nameofinbox being the name of the inbox and keyword being the string or list the user is searching for.

#### BySubjectSynonym(keyword):

This method finds and returns list of messages containing synonyms of the inputted keyword. It takes a single word string and will throw an error if the string is multiple words long. This method is called using the syntax:

nameofinbox.bysubjectsynonym(keyword)

With nameofinbox being the name of the inbox and keyword being the string the user is searching with.

#### InboxHeaderSearch(keyword):

This method finds and returns list of messages containing the header inputted by the user. It takes a string. This method is called using the syntax:

nameofinbox.inboxheadersearch(keyword)

With nameofinbox being the name of the inbox and keyword being the header the user is searching for.

#### RemoveEmail(Index):

This method removes an email located at the inputted index in the email list. It will also update the inbox size and the min and max dates accordingly. It will throw an error if the index is out of bounds. This method is called using the syntax:

nameofinbox.removeemail(index)

With nameofinbox being the name of the inbox and index being the number of the message object that user is trying to remove from the email list.

#### GetSize():

This method returns the number of Emails in the email list. It is called using the syntax:

nameofinbox.getsize()

With nameofinbox being the name of the inbox.

#### IncreaseSize():

This method increases the inbox value \_size. Since size is a protected value the user is not supposed to interact with it directly and instead use the methods here. This method InceaseSize() is only called by the AddEmail method and **should not be called by the user.**

#### DecreaseSize():

This method decreases the inbox value \_size. Since size is a protected value the user is not supposed to interact with it directly and instead use the methods here. This method DeceaseSize() is only called by the RemoveEmail method and **should not be called by the user.**

#### SetMaxMinDate():

This method checks to ensure that all of the dates of all of the emails in the email list have been properly inputted and will through an error if any haven&#39;t been. It will also find the maximum and minimum dates in the email list and assign them to the protected values \_maxdate and \_mindate. This method is called by both Add and Remove Email and can, but does not need to be, called by the user.

#### GetMaxDate():

This method returns latest date of the emails received by the inbox. It is called using the syntax:

nameofinbox.getmaxdate()

With nameofinbox being the name of the inbox.

#### GetMinDate():

This method returns earliest date of the emails received by the inbox. It is called using the syntax:

nameofinbox.getmindate()

With nameofinbox being the name of the inbox.

## Section 2: Demographics

### ![Shape3](RackMultipart20211119-4-9ibr0o_html_8c559087729a251.gif)
 Overview

This object contains the Demographic information of the owner of the Inbox. It contains their first and last name, their email address, phone number, gender, birthday, country and political affiliation as strings, the age as an integer, and the birthplace as a Birthplace object (See [Section 3: Birthplace](#_Section_3:_Birthplace)). All of these values are needed upon creation of this object and if any are unknown, they should be defined as None. With the exception of birthplace (See [Section 3: Birthplace](#_Section_3:_Birthplace)), values in the Demographics Object can be accessed via the syntax:

nameofinbox.demographics.valuerequested

Where nameofinbox is the name of the inbox and valuerequested is the value the user is trying to access.

There are currently no methods for this object.

## Section 3: Birthplace

### Overview

![Shape4](RackMultipart20211119-4-9ibr0o_html_4ef6f6403555828a.gif)

_Figure 5 The US Birthplaces object_

 ![](RackMultipart20211119-4-9ibr0o_html_f8e7a36c0e97512.png)

![Shape5](RackMultipart20211119-4-9ibr0o_html_2b0bb048e4efb6c4.gif)

_Figure 5 The International Birthplaces object_

 ![](RackMultipart20211119-4-9ibr0o_html_3c1066a2b425da86.png)

This object contains the Birthplace information for the Demographics object. It contains the city and the state, for US birthplaces, or the Country, for international birthplaces, where the owner of the inbox was born as strings. This object was created to make it easier for the user to access the values of the inbox owner&#39;s birthplace without having to parse strings. Values in the Birthplace Object can be accessed via the syntax:

nameofinbox.demographics.birthplace.valuerequested

Where nameofinbox is the name of the inbox and valuerequested is the value the user is trying to access.

There are currently no methods for this object.

## Section 4: Email

### Overview

![](RackMultipart20211119-4-9ibr0o_html_abb6467b509f0d8e.png)

_Figure 6 The Email Object_

Each object of the Email Structure represents one email. These emails will be stored in a list inside the Inbox object. The emails will be identified by their number in the list. This number is the Primary Key for the Email object. This object also contains the date it was sent as a date object, the sender as a Sentby object (See Section 7: Sentby), the subject of the email as a string, the email&#39;s headers, as a Headers object (See Section 6: Headers), and the content of the email as a Content object (See Section 5: Content)