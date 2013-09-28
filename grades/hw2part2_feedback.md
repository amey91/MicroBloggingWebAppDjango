HW2 part 2 Feedback
============

 * Empty url (localhost:8000/) does not route correctly. Please route the empty url to the login page in your urls.py. In HW3, this will be a requirement.
 * Minor point but all the titles are "Bootstrap 101 Template" (which should be cited in your README if you use templates)
 
#### Login/Registration

 * Minor point but email field is not validated (which wasn't a requirement), you could use HTML input=email to do this easily. 

#### Home Stream Page

 * Displaying grumbls has some strange behavior, on the first view after registering > login, there are a bunch of predefined grumbls which I'm assuming are meant to be other users. When refreshing the page, they all disappear.
 * Related, there doesn't seem to be any way to see follower grumbls (besides the above).
 * No search feature?
 * For some reason, grumbls display "User 15" etc. instead of the username, as you'd expect. Looking at your template, it's because item.id is displayed instead of item.user.username or something similar.
 * On the home stream, the grumbls display "Post-1" after each for some reason. 
 * The grumbls are in earliest to latest order, whereas in most social networking sites, you see posts in latest to earliest order. You can achieve this in a number of ways either in the template or modifying the request context.

#### View/Edit Profile Page

 * No profile? Don't really see a profile or editing features. 
 
### Django
 
 * The Grumbl model should include a DateTimeField in order to display the posting time and make reverse chronological ordering easier.
  You can use auto_now_add=True argument in the model to do this automatically

---

#### Total (65/80)

 * -6 for no real follower stream
 * -12 for not having a real view profile nor edit profile page 
 * -6 for no search feature
 * -1 for not displaying the username per grumbl

---

#### Overall

 * The site looks good, but there are a lot of unimplemented features. I strongly suggest finishing them before trying to start HW3. If you need an extension on HW3 because of this, feel free to ask any of the TAs.

Graded by: Jason Tsay (jtsay@andrew.cmu.edu)

To view this file with formatting, visit the following page: https://github.com/CMU-Web-Application-Development/aghadiga/blob/master/grades/hw2part2_feedback.md
