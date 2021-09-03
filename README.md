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
The font has been taken from Materialize CSS
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
Bootstrap 4.4.1:
Bootstrap was used to assist with the responsiveness and styling of the website.
Hover.css:
Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
Google Fonts:
Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
Font Awesome:
Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
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
Flask is a python framework that helps to run common operations 
* MongoDB:
Thisb is the database used to store data in the format of key value pairs
* Randon Keygen
Used https://randomkeygen.com/ was used to get a fort knox password for connecting to mongodb

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

