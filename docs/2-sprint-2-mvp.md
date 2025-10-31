# Sprint 2 - A Minimum Viable Product (MVP)


## Sprint Goals

Develop a bare-bones, working web application that provides the key functionality of the system, then test and refine it so that it can serve as the basis for the final phase of development in Sprint 3.


---

## Implemented Database Schema

The Homework Tracker will be a website where you can create a base subject with teacher and priority of the subject to your studies. Then in each subject you can add work and assessments that you want to track to complete. Being able to display them by priority and add their due dates too!

![Alt text](<screenshots/Sprint-1/Database SQL.png>)


---

## Initial Implementation

The key functionality of the web app was implemented:

![alt text](<screenshots/Sprint-2/Initial Implementation.gif>)

---

## Adding Teacher and Priority (Subjects)

For my project I wanted the user to be able to add their teachers names for each subject and the priority of the subject to them and their studies. Currently all you can do is add subject and thats it. So I am testing adding teacher and priority and making it a part of the form process through post and hopefully it will be added with the subject when the user clicks add.

![alt text](<screenshots/Sprint-2/Teacher and Priority Initial.png>)

### Changes / Improvements

I now added the post method for the forms allowing the user to now add teacher names and priority for each subject. The end-user finds this really useful.

![alt text](<screenshots/Sprint-2/Adding Teacher and Priority Complete.gif>)
### Home.jinja
![alt text](<screenshots/Sprint-2/Adding Teacher and Priority Shot.png>)
### _init_.py
![alt text](<screenshots/Sprint-2/Add Subject (Innit).png>)

---

## Delete Function

I am trying to get a delete function working so the user, once done with subjects, can delete their subject all together. Right now they only stack up on subjects without the option to remove them. I will add it in the home page below the adding function and add a delete trashcan to represent how they delete their subjects.

![alt text](<screenshots/Sprint-2/Delete Function Initial.gif>)

### Changes / Improvements

I have successfully added a delete function and added the message to make sure the user does in fact want to delete their subject. It comes as a trashcan form for the user to click.

![alt text](<screenshots/Sprint-2/Delete Function Complete.gif>)

### Home.jinja
![alt text](<screenshots/Sprint-2/Delete Function Shot.png>)
### _init_.py
![alt text](<screenshots/Sprint-2/Delete Function (init py).png>)

---

## Delete Function (Assessments)

Same as the subjects, I am trying to get a delete function working so the user, once done with their assessments, can delete their assessments they want to get rid of or to remove because of errors when filling the forms. Right now they only stack up on assessments without the option to remove them.

![alt text](<screenshots/Sprint-2/Delete Function Assessments Initial.gif>)

### Changes / Improvements

Delete function complete using same code as the home page to make sure this one works the same. Only now having to add a new block of code to make sure it deletes for this page not the home page. So in my init.py I did just that.

![alt text](<screenshots/Sprint-2/Delete Function Assessments Complete.gif>)
### Subject.jinja
![alt text](<screenshots/Sprint-2/Delete Function Shot(Assessments).png>)
### _init_.py
![alt text](<screenshots/Sprint-2/Delete Function Shot (Assessment) init.py.png>)

---

## Adding Due Date and Priority (Assessments)

I am updating the forms for Assessments to allow the user to add the due date and priority for their assessments for each subjects. The assessments/homework will be organized by priority allowing the user to add their custom due dates to allow time frames.

![alt text](<screenshots/Sprint-2/Adding Due Dates and Priority Initial.gif>)

### Changes / Improvements

I have now added, just like the subjects page, the ability to add your priority and due dates for each assessment. Priority is 1 - 5 while due dates is written out preferably as 2025-29-10.

![alt text](<screenshots/Sprint-2/Adding Due Dates and Priority Complete.gif>)
### Subject.jinja
![Alt text](<screenshots/Sprint-2/Adding Due date and priority shot (assessment).png>)
### _init_.py
![Alt text](<screenshots/Sprint-2/Adding due date and priority (init.py).png>)

---

## Checkboxes

For each subject, as discussed with my end-user, I want to have the user be able to check of their assessments/homework to know what they've completed without having to delete them. Giving them 2 options to have a look at instead of only giving them the one. They can then uncheck them if they have to go back and do it later.

![alt text](<screenshots/Sprint-2/Checkboxes Initial.gif>)

### Changes / Improvements

I tried different methods with end-user on ways I could use checkboxes and what they could look like and where they could be. This proves the best way with help from the teacher to use it similar to a form. Now it sits next to the trash icon to give the user 2 choices with their assessments.

![alt text](<screenshots/Sprint-2/Checkboxes Complete.gif>)
### Subject.jinja
![Alt text](<screenshots/Sprint-2/Checkboxes shot.png>)
### _init_.py
![Alt text](<screenshots/Sprint-2/Checkboxes (init.py).png>)

---

## Displaying the Priority (Assessment)

Currently, as discussed with my end-user, my web page asks for the priority of the assessment. It gives the user choice over what assessments they want at the top of their list vs ones that aren't too worried about but still want to keep checks on. The problem is there isn't any numbers to show what one is what priority. Leaving the user to guess where their new assessment they add in will go in the list.

![alt text](<screenshots/Sprint-2/Priority Display Initial.gif>)

### Changes / Improvements

I have now made it where the assessments priority numbers are displayed on the left of the assessments so the user knows what their list looks like and where they can add their new assessments.

![alt text](<screenshots/Sprint-2/Priority Display Complete.gif>)
### Subjects.jinja
![Alt text](<screenshots/Sprint-2/Displaying priority shot (assessment).png>)

---

## Displaying the Priority (Subjects)

Same as the assessments, my web page asks for the priority of the assessment. It gives the user choice over what subjects they want at the top of their list vs ones that aren't too worried about but still want to keep checks on. The problem is there isn't any numbers to show what one is what priority. Leaving the user to guess where their new subject they add in will go in the list.

![alt text](<screenshots/Sprint-2/Priority Display Initial Subjects.gif>)

### Changes / Improvements

I have now made it where the subjects priority numbers are displayed on the left of the subjects so the user knows what their list looks like and where they can add their new subjects.

![alt text](<screenshots/Sprint-2/Priority Display Complete Subjects.gif>)
### Home.jinja
![Alt text](<screenshots/Sprint-2/Displaying priority shot (subjects).png>)

---

## Drop-Down Menu (Adding Subject and Assessment)

Currently my web-page displays the subjects/assessments and below displays the form you use to add the subjects/assessments. The problem is it doesn't look good. My end-user agrees and it just looks basic. So with help from Mr Copley I will have the option for the user to show the drop-down menu to add subjects/assessments.

![alt text](<screenshots/Sprint-2/Drop Down Initial.gif>)

### Changes / Improvements

I now very easily have a drop down menu with a + icon to signal where the user can click to drop down the form and fill it out to add assessments and subjects.

![alt text](<screenshots/Sprint-2/Drop Down Complete.gif>)
### Home.jinja and Subject.jinja
![Alt text](<screenshots/Sprint-2/Drop-down menu shot.png>)
### Full Form Drop-Down
![Alt text](<screenshots/Sprint-2/Drop-down menu shot 2.png>)

---

## Due Date

After beginning work on my CSS I realized I am wanting to setup my due date form-column to allow the user choice of inputting the day, month and year themselves or click with the menu on hand. It is easy to do and allows the user to easily do the dating of their assignments easier having a procedure to follow.

![alt text](<screenshots/Sprint-2/Due Date Initial.gif>)

### Changes / Improvements

I have now added it where the user can either input their dates themselves or click the calender icon to choose what their due date is from the options provided.

![alt text](<screenshots/Sprint-2/Due Date Complete.gif>)
### Subject.jinja
![Alt text](<screenshots/Sprint-2/Due Date shot (updated code).png>)

---

## Testing FEATURE NAME HERE

Replace this text with notes about what you are testing, how you tested it, and the outcome of the testing

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

### Changes / Improvements

Replace this text with notes any improvements you made as a result of the testing.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**


---


## Sprint Review

Replace this text with a statement about how the sprint has moved the project forward - key success point, any things that didn't go so well, etc.