# Fairdressers Website
[View the live project here.](https://fairdressers.herokuapp.com/)

![NB Flag](https://www.stonewall.org.uk/sites/default/files/styles/person_hero/public/1280px-nonbinary_flag.svg_.png?itok=sykEzwb2)

This is a community-driven resource to support hairdressers that offer gender neutral pricing and customers who require it. It is designed to be responsibe and accessible on a range of devices.

# User Goals
## External user’s goal:
* Users want to find and recommend hairdressers(including salons, barbers, etc.) that do not question the gender of the customer.
* Users want to find and recommend hairdressers that do not charge women extra for the same haircut that would cost a men less.
* Users should be able to create a review of any hairdresser
* Users should be able to search for a hairdresser by name or by city
* Users should be able to edit their reviews as necessary
* Users should be able to flag when a hairdresser is using gendered pricing, and recommend a member of staff to talk to if appropriate.

## Site owner's goal:
* Provide support to customers who are inconvenienced by gendered pricing and highlight misogynistic pricing practices.
* Direct customers to businesses who are willing to provide non-gendered pricing in hairdressing services.

## Features to include:
* Create a web application that allows users to upload recommendations of barbers/hairdressers, including establishment name, hairdresser name, link to website and any other relevant fields. Allow users to create reviews about any category of hairdressing service.
* Create the backend code and frontend form(s) to allow users to add new barbers and reviews to the site, edit them and delete them.

# User Experience (UX)
* First Time Visitor Goals
 * As a First Time Visitor, I want to easily understand the main purpose of the site.
 * As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
 * As a First Time Visitor, I want to look for reviews to find recommendations for hairdressers that offer genderless pricing. I also want to access recommendations and articles about this movement.
 * As a First Time Visitor, I want to be able to sign up and write a review.

* Returning Visitor Goals
 * As a Returning Visitor, I want to look for reviews
 * As a Returning Visitor, I want to be able to edit my reviews if required
 * As a Returning Visitor, I want to find community links.
 * As a Returning Visitor, I want to log in to my account.

* Site Owner Goals
 * As site owner, I want to maintain reviews and edit as required
 * As site owner, I want to delete any malicous content
 * As site owner, I want to adjust categories as required

* Design
 * Colour Scheme
Colour scheme indicates that this website serves non binary people by using the colours of the non binary flag, which are black, white, yellow and purple. This colour scheme would be familiar and welcoming to people concerned with gender binary issues.
The flash messages are pink which is a colour synonymous with the LGBT community and the transgender flag.
 * Typography
The font has been taken from Materialize CSS (font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;)
 * Imagery
The imagery throughout the site contains people with short hair, many of whom are female or of ambiguous gender. There are also positive representations of the LGBT/NB/transgender community included throughout. 
 * Wireframes
Home Page Wireframe - [View](https://share.balsamiq.com/c/rXaCaGKear8nzfsohRaAQ5.png)
Reviews Page Wireframe - [View](https://share.balsamiq.com/c/42SLMnoV1Nz8Fqrq4i362u.png)
Profile Page Wireframe - [View](https://share.balsamiq.com/c/mfPS1q8PfEPfkeT1N6w8jn.png)
Login Page Wireframe - [View](https://share.balsamiq.com/c/grepvFodYeTtih3nraJvES.png)
Register Page Wireframe - [View](https://share.balsamiq.com/c/vWYeyr1RMA2BdmH1Bryuyu.png)
Categories Page Wireframe - [View](https://share.balsamiq.com/c/bf5r7PzCcnhL2gn5TWsYQ6.png)
Add Category Page Wireframe - [View](https://share.balsamiq.com/c/qTjyghsFbL7em5LazwKsBh.png)

* Features
Responsive on all device sizes
Interactive elements

# Technologies Used
## Languages Used
* HTML5
* CSS3
* Python
* JavaScript

## Frameworks, Libraries & Programs Used
* jQuery:
jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
Git
Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* GitHub:
GitHub is used to store the projects code after being pushed from Git.
* Materialize css library version 1.0.0:
Materialize was used to assist with the responsiveness and styling of the website.
* Balsamiq:
Balsamiq was used to create the wireframes during the design process.
* Material Design Icons :
courtesy of Google, they are used via an API from Materialize
http://google.github.io/material-design-icons/#icon-font-for-the-web
* Flask:
Flask is a python micro framework that helps to run common operations without writing too much code
* MongoDB:
Thisb is the database used to store data in the format of key value pairs
* Randon Keygen
Used https://randomkeygen.com/ was used to get a fort knox password for connecting to mongodb
 * Jinja
 This is a templating language that allows the writing of python code inside HTML templates, it has been used in this project to insert for-loops and if-statements, as well as inheritance by extending the base template to other templates.
  * [tinypng](https://tinypng.com/)
  Tiny PNG was used to resize photographs for web performance

# Testing
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

W3C Markup Validator - Results
W3C CSS Validator - Results
HTML Validator
CSS Validator
JavaScript Validator
Python Validator
Documentation on using Developer Tools Lighthouse

## Testing User Stories from User Experience (UX) Section
## First Time Visitor Goals
 * As a First Time Visitor, I want to easily understand the main purpose of the site.
  * On arrival at the site, users see a navigation bar to go to the page of their choice.** They are presented immediately with a welcoming page that explains the purpose and ethos of the site, complete with links to further resources.
The user has the option to search through existing reviews or see all reviews.
 * As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
  * The top of each page has the same clean navigation bar, clearly showing where they will go, 
  * The navigation bar does not show irrelevant links and is adjusted to show whether the user is logged in or not, or whether they are able to edit categories.
 * As a First Time Visitor, I want to look for reviews to find recommendations for hairdressers that offer genderless pricing. I also want to access recommendations and articles about this movement.
The user can access reviews via the nav bar at any time and they can also search from the welcome page.
 * As a First Time Visitor, I want to be able to sign up and write a review.
  After the user has read the About page, they will understand the purpose of the reviews. Having seen the examples of what is required they can register and create thrir own reviews.


## Returning Visitor Goals
 * As a Returning Visitor, I want to look for reviews
 Reviews are searchable from the main page and the reviews page.
 * As a Returning Visitor, I want to be able to edit my reviews if required
 When a user logs in they are presented with a list of their own reviews which they can edit as needed.
 * As a Returning Visitor, I want to find community links.
 Users can access a list of resources on the About page as well as the list of reviews from peers on the reviews page.
 * As a Returning Visitor, I want to log in to my account.
 Users can go directly to the login page and enter their credentials to log in.

## Site Owner Goals
 * As site owner, I want to maintain reviews and edit as required
 When logged in as admin, the user can edit any review regardless of who the owner is.
 * As site owner, I want to delete any malicous content
 The admin user is the only accout that has access to delete reviews.
 * As site owner, I want to adjust categories as required
 When logged in as admin, the manage categories page becomes visible in the nav bar. This can be used to create and remove categories as appropriate.


## Further Testing
The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
The website was viewed on a variety of devices such as Desktop, Laptop, phone
A large amount of testing was done to ensure that all pages were linking correctly.
Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Known Bugs



# Deployment

## Create a Heroku App
Heroku is the service being used to host the app. It is possible to deploy using the  Heroku Command Line Interface (CLI) but in this case automatic deployment via GitHub was chosen. The project was deployed to Heroku using the following steps...

1. Log in to Heroku and create a new app (Fairdressers, located in Europe)
1. In the app page go to the deploy tab and choose Git Hub as the deployment method

1. Go into the Heroku app settings page and click to reveal config vars
 1. Enter the below key value pairs:
  * "IP" : "0.0.0.0"
  * "PORT" : "5000"
  * As well as the value for the secret key variable, which was named SECRET_KEY in thai example but can have been assigned any name
1. Set to automatically deploy
 1. Click 'deploy' tab and select 'github'
 1. Search for the repository name that matches the app and click 'connect'


## Create a requirements.txt File
Send the output of the freeze command into a file called requirements.txt. The file contains a list of dependencies such as werkzeug. Flask and jinja will have been installed by PIP but now requirements.txt allows Heroku to detect this app as a Python app
1. In the terminal enter: pip3 freeze --local > requirements.txt.
1. Add the newly created file to the git staging area (by using git add -A, for example)
1. Git commit the change

## Create a PROC file
This tells heroku how to run the application. Heroku can not see any git ignored files including env.py that contains the secret key.
1. To create the procfile type "echo web: python run.py > Procfile"
1. Check that there is no trailing white space in the file
1. Git add the file, commit and push

## Enable automatic deployment
 1. Go back to the deploy tab in the Heroku page
 1. Click to enable automatic deployment, leave the branch as 'main'
 1. At the bottom of the page, under the manual deployment section, choose the same branch again and click 'deploy branch'
 1. Heroku will now build the application with code from github, wait to see a message appear saying "Your app was successfully deployed".

# Credits
## Code
The main framework was inspired by the task manager project and the thorin project
Many of the javascript features came from materialize
All icons used came from google via materialize
The idea to alternate text and images on the about page came from the Thorin project
A standard 12 column fluid responsive grid system from Materialize was used as demonstrated in the Task project and adapted to shape the pages in horizontal stripes like the flag while keeping the site responsive 
The addition of a date field was adapted from code found at https://www.programiz.com/python-programming/datetime/current-datetime

## Content
All content was written by the developer.
The inspiration for the colour scheme can be found at https://outrightinternational.org/content/flags-lgbtiq-community
An alternative design consideration was the gender queer flag and the trans flag but, this site is not intended to serve those communities exclusively,  the focus on this site is the desired absence of gender consideration so the non-binary was most suitable.
The extensive use of black as a header was inspired by [Vice magazine](https://www.vice.com/en/section/tech), which is popular with the LGBT community and conveys a modern and alternative aesthetic.




## Media
All Images were downloaded from pexel.
[Photo by Rachel Claire from Pexels](https://www.pexels.com/@rachel-claire?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)
[Photo by Barcelos_fotos from Pexels](https://www.pexels.com/@barcelos_fotos-1484908?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)
[Photo by Christina Morillo from Pexels](https://www.pexels.com/@divinetechygirl?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)
[Photo by Sharon McCutcheon from Pexels](https://www.pexels.com/@mccutcheon?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)
[Photo by RODNAE Productions from Pexels](https://www.pexels.com/@rodnae-prod?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)
[Photo by Sarah Chai from Pexels](https://www.pexels.com/@sarah-chai?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)
[Photo by Nick Demou from Pexels](https://www.pexels.com/@nick-demou-365778?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)
[Photo by Dmitriy Ganin from Pexels](https://www.pexels.com/@ganinph?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)

## Acknowledgements
My Mentor for continuous helpful feedback.
Tutor support at Code Institute for their support.


