15437 HW4 Feedback
============

#### HW3 Details

 * User can log in without confirming registration. To do this, you should include a registration link in the confirmation email, and new users should be able to log in only after navigating to this link. (-1)
 * Nice job on validating inputs.
 * Following/blocking work fine. From a UI standpoint, you might want to add buttons on each user's profile page that allow other users to follow or block this one. This would be a bit smoother than the current method of having to go to a separate page and then entering user names in a textfield in order to follow certain users.

#### Images

 * Works fine. But you should probably consider resizing the images to some fixed size so that when they are displayed in the grumbl, they don't overflow into nearby grumbls.

#### Password Resets

 * Authenticated "Change Password" function works fine.
 * Able to login using temporary password if I've forgotten password.

#### Ajax
 
 * Works fine but you should get rid of the textbox that keeps saying "submitted via ajax".

#### MySQL
 
 * Works fine.

#### Django

 * Please remove all unnecessary urls from your project "urls.py".
   In other words, please remove "url(r'^polls/', include('polls.urls'))" and "url(r'^calfinal/', include('calfinal.urls'))".
 * Remove all links from the navbar that should be visible only after the user has logged in (eg, Following, Profile, etc.)
 * Get rid of "moneyclub" from INSTALLED_APPS in settings.py; it caused an ImportError since there was no such module.

---

#### Total (99/100)
 * Great work overall!

---

Graded by: Sairam Krishnan (sbkrishn@andrew.cmu.edu)