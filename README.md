# IT5016-Research-Repository
Research repository referencing code from projects I've found through GitHub & a project i've created.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Help Desk Ticketing System (Self Created Project in Python)

This project was created for a course assignment where the scenario was to create a help desk ticketing system prototype for internal staff to submit IT help request tickets to the IT help desk. 

The requirements for the prototype was that it must have the ability to:

- Create a new ticket.
- Respond & resolve an open ticket.
- Reopen a closed ticket.
- Display ticket statistics and information, with statistics changing to reflect current ticket status. 
- Automatically create a new password when "Password Change" is inputted into a ticket.

Generally, creating this prototype proved to be a good beginner project, fun, but also challenging, especially considering that this is 
my first project created utilising Python. In terms of coding this project, it was relatively straight forward with creating 
each individual feature, with the options menu and ticket creation input coding simple to implement. The main challenge I had with coding 
initially was when ticket information and statistics were displayed, they didn't change to reflect the current status of the tickets or 
change when tickets were modified. But with assistance and some modification to both the Main and Ticket classes, the statistics and 
information display correctly when updated. 

------------------------------------------------------------------------------------------------------------------------------------------

Asteroids Game (Project code created by & acknowledgement to user boularbarsmail)

This project was chosen based on an previous asssignment for another tertiary institute, where we had to create the same game but 
utilising Snap! to create it, which was my first introduction to software design and development. This code is for a game known as 
Asteroids, where a player controls a spaceship sprite across a stage and avoids or destroys asteroids and enemy ships to increase their 
score. If they collide with an asteroid or are shot, they lose a life & if there are no more lives, the game is over.

From a general perspective, I found the code to be extensive and thorough, with comments present through out the code detailing fixes or 
descriptions, which makes it easy to identify what each block and line of code does when the game is initialised. 
However, due to the sheer amount of code present and also what seemed to be repeated lines of code which seem redundant or unnecessary, I 
found it to be rather cluttered & unstructured. 

It almost needs to be fully redone to make the code more tidy and structured, with potentially having some of the code blocks presented to be in their own class, if they aren't in any of their supporting sprite files, as the page I'm referring to would be considered the main class. But with some restructure, the code would be clean, tidy and easier to read, which will work well alongside the positive points mentioned above.;l

------------------------------------------------------------------------------------------------------------------------------------------
Blackjack Game (Project code created by & acknowledgement to user StephanieSunshine)

For this project, I decided to go with this based on a recommendation from my tutor and also because I play the game myself. This code is 
for the card game Blackjack, or 21, where a player plays against the computer in order to get a higher card score based on the points 
each card represents. If the player or computer has a higher score than the other or gets exactly 21 points (Blackjack), then that player 
wins, however if they have a lower score or go over 21 points (going bust), then they lose the game.

Initial thoughts on the code for this project is that the code is clean, well structured & spaced and also easy to follow along, with no 
redundant or unnecessary code present as far as can be seen, with each component for the game well defined in the code. The only issue, 
while very minor, were that there was the lack of comments from the creator to explain each aspect of code, which, while personally not 
hard to tell which code block does what function, would make it hard for an individual with no prior or limited programming knowledge to 
understand, with most of the comments present on the file being my own.
