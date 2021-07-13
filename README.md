# Finance Mind Learning Application

## Introduction
The Finance Mind application is a platform that allows a company to provide learning content to its staff in an easy to use format. The idea was developed based on my own want for such an application in my current job that would also ensure data security. 

View Live Website [here](https://learning-platform-ms3.herokuapp.com/)

![Finance Mind on different devices](static/images/readme_images/mockup.png)

Image created using [Am I responsive](http://ami.responsivedesign.is/)

## Table of Contents

- [UX](#ux)
  - [Strategy](#strategy)
    - [User Needs](#user-needs)
        - [As a site user](as-a-site-user)
        - [As the business owner](as-the-business-owner)
  - [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
- [Testing](#testing)
    - [Development Issues](#development-issues)
    - [Code Validation](#code-validation)
        - [Html](#html)
        - [CSS](#css)
        - [Javascript](#javascript)
    - [Performance Testing](#performance-testing)
    - [User Stories Testing](#user-stories-testing)
    - [Functionality Testing](#functionality-testing)
    - [Validation Testing](#validation-testing)
    - [Compatibility Testing](#compatibility-testing)
        - [Different devices](#different-devices)
        - [Different Browsers](#different-browsers)
        - [Different Operating Systems](#different-operating-systems)
- [Technologies Used](#technologies-used)
    - [Frameworks and Libraries](#frameworks-and-libraries)
    - [Version Control](#version-control)
    - [Other Programs](#other-programs)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)


## UX

The 5 planes of User Experience:

### Strategy
Finance Mind was created with the purpose of providing an innovative solution to allow a company's trainning team provide relevant and informative finance content to their employees in a secure platform, to assist with self learning. 

#### User Needs

##### As a site user
- I want to be able to understand the site purpose immediately.
- I want to be able to register and login, so that I can access the learning content.
- I want to be able to easily naviage the site, ensuring I can acess the desired content with ease. 
- I want to be able to search articles to show relevant results only.
- I want to be able to favourite articles for quick access in the future.
- I want to be able to contact the site admin if needed.
- I want to be able to update my own user details, such as password without needing to contact the site admin.
- I want to be able to create short personal notes, that only I have access to.


##### As a site admin
- I want to be able to create site content such as articles that allow the inclusion of resources such as images and links. 
- I want to be able to edit all site library contents, even if another admin created it. 
- I want to be able to amend all users' details, to enable a change in user access rights or if user has issue logging in. 
- I want to be able to remove a user from the platform and all their stored data.
- I want to be informaed of users reaction to content. 


##### As the business owner
- I want to enable my employees to learn on the go.
- I want my employees to stay up to date on relevant topics.
- I want to see feedback from users engaging with content. 

### Scope

#### Features 

The following features are in scope for this project.
- Register Functionality.
  - Validated form to allow user create a profile for accessing the application. 
- Login Functionality.
  - Validated form that checks the users stored details and logs user in only if a successful match. 
- Navigation Menu.
  - A navigation menu will be presented on all pages on application. 
- Responsive Design.
  - Application is responsive on all device size and browsers.
- CRUD Functionality.
  - Application enables the functionality to Create, Read, Update and Delete data.
- Database to store app data.
  - MongoDB database will be used to store all application data. 
- Contact Form.
  - Contact form to enable user to send message to admin. 
- Library with searchable content.
  - Search bar that allows user query to filter the articles to shown those with a match only. 
- Favourite article.
  - Allow user to create a quick link on their profile that redirects to the article that was favoured.
- Article like and dislike feedback.
  - like and dislike button that records the total like and dislikes of an article.
- Profile Page.
  - Unique profile for each user that shows their favoured articles and sticky notes.
- Add sticky note on profile page.
  - Option to create a new sticky note when on profile page.
- Edit sticky note on profile page.
  - Edit selected note where data is prefilled on form.
- Admin content creation. 
  - Form to create site contents that only admin has access to. 
- Admin content edit. 
  - Edit selected article where data is prefilled on form.
- Admin user management 
  - Page that shows all registered users and allows admin user to edit or delete users.
- User settings page.
  - Page that user can amend their own profile settings. 
- 404 Error Page
  - A custom 404 error page if the user navigate to a resourse that doesnt exist with a button to return home. 


#### Future Features 

I would like to include the following future features.
- Messaging functionality for admin to users.
  - The feature when an admin user could choose a user to send a private message to.
- Push notifications about new content been added.
  - The option to send a notification to all site users when new articles added to encourage their continued learning. 

### Structure

During the planning stage, it was decided that the following pages would be needed to ensure the user needs are meet:

- Landing Page with elements:
  - To tell vistior what the application is for.
  - To allow user to register.
  - To allow user to login.
  - To allow user to contact site admin.

- Content Library with elements:
  - To allow user to search library.
  - To allow user to like and dislike article.
  - to favourite article.
  - To read content and interact with it as needed.
  - For an admin user to allow them to edit or delete content. 

- Profile Page with elements:
  - Welcome message.
  - To create a new sticky note.
  - To edit an existing note.
  - To view articles favored and ability to click and be redirected to article. 
  - Ability to remove favourites.
  - To be able to edit user profile settings.

- User Management Page with elements (only for admin user):
  - To see all registered users.
  - To edit users.
  - To delete users.

- Add site content page with elements (only for admin user):
  - Forum to fill in:
    - Category
    - Title
    - Content body
    - Keywords
    - Picture
    - External resource
  - Content body to preserve formatting as entered by user. 


### Skeleton

#### Wireframes

Wireframes for this project were created using Balsamiq and can be viewed at below link.

Link to [Wireframe](static/wireframes/wireframes.pdf)

#### Database Design

This application uses Mongo DB to store and retrieve the user data. Mongo DB is a non-relational databse. This application consists of 4 collections as shown in the schema diagram below. 

The users collection is populated when a user succesfully registers and is used to verify a user upon login.The content collect stores the data for articles that appear on the library page. Only an admin user can add to this collection. The posts collection stores the data for a users stick notes that are displayed on their profile. The favourites collection takes record of a users favoured articles. 

![Finance Mind Schema](static/images/readme_images/schema.png)

### Surface

The Finance Mind application was designed to reinforce learning and create a sense of trust among learners using soft tones. 

#### Colour Scheme

Shades of blue were used to create the impression of trust and loyalty. Turquoise was used to represent open communication, creativity and calming nature. The combination of shades between blue and green are widely used in financial websites. A ligther shade creates the association while also looking modern. 

The colours used are shown below:
![Color Schema](static/images/readme_images/colors.png)
The navbar is a gradient of these colors to give a fresh appearance by mergining the colors. 

#### Typography

Fonts used are Playfair Display for Headings and Open sans for paragraph elements. These fonts look professional while maintaining readability. 


## Testing

A summary of testing conducted is shown in the table below. 

![Testing Summary](static/images/readme_images/testsummary.png)


### Code Validation

#### Html

Html pages were validated with [W3C Html Checker](https://validator.w3.org/nu/). To obtain the HTML code on live pages, the safari developer tools were used to open the page source html and this was copied and pasted into the text input field on W3C for validation.

The pages validated are shown below.

![Html pages validated](static/images/readme_images/htmlvalidation.png)

A warning appeared on all pages that the flash message section lacked a heading. This warning can be ignored as the section contains a heading element where the elements html is injected with jinga templating language when needed. Any pages where an error was found are detailed below.

##### Landing Page 

The only error present was that their was an unmatched trailing div. This was removed and the code rechecked. 

#### Home

On first check, there was 3 errors. The first error was that the image elements were missing an alt attribute. I added this in. The second error is that the article icons all had the same ID. I replaced this with class as each article would have 3 occurances of this value and this violates the definition of a unique ID. The last error is that their was an unclosed div element. I located the element and corrected this. 

#### Content

Two errors were present. The first was that the attribute pattern is not allowed on a textarea element. I removed this attribute and have custom javascript to validate this field when white space is present only. The second error is that there was a stray div present. I checked the file and removed this. 

All pages now sucessfully pass through the validator as shown in the image below.

![Html pass](static/images/readme_images/htmlpass.png)

#### CSS

CSS page was validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

No errors were present.

![CSS pass](static/images/readme_images/validcss.png)

#### Javascript

Javascript files were validated with [JSHint](https://jshint.com/)

Missing semi-colons were added and the scripts retested. No errors or warnings present.

![Javascript results](static/images/readme_images/validJS.png)

#### Python

Python files were validated with [PEP8 online](http://pep8online.com)

![First validation results](static/images/readme_images/pep8fail.png)

The error present was that the app.py file had several occurances where a line was greater than 79 characters. I reformatted the app.py file to ensure no line was more than 79 characters and retested.

The file is now PEP8 compliant.

![Final validation results](static/images/readme_images/pep8pass.png)

### Performance Testing

Performance was tested using Lighthouse, one of Google's web developer tools.

#### Home Page



### User Stories Testing

The user's needs are met as follows:




### Functionality Testing

I tested the functionality of the site on a laptop first. Each page was tested and results are given below:

 
   
### Validation Testing

contact form

### Compatibility Testing

#### Different devices

Using Google Developer tools, I viewed the website on the following devices:
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5/6/7/8 & Plus
- iPhone X
- iPad & iPad Pro
- Surface duo
- Galaxy fold



#### Different Browsers

I tested the website on:

- Google Chrome
- Safari
- Firefox
- Microsoft Edge
- Internet Explorer

Differences discovered across browsers:




#### Different Operating Systems

The above testing was conducted on below operating systems:

- Windows 8.1
- MacOS Big Sur 11.2.3
- iOS 14.4.2
- Android

There were no differences detected on those operating systems. [Browser Stack](live.browserstack.com) was used to view and check the functionality across a wide range of devices and operating systems.


### Development Issues

- 

## Technologies Used

### Frameworks and Libraries

- [Google Fonts](https://fonts.google.com/) was used to import the font selectedfor the website.
- [jQuery](https://jquery.com/) was used as a Javascript library.


### Version Control

- [Git](https://git-scm.com/) was used as a version control system.
- [GitHub](https://github.com/) was used for the repository hosting.
- [Gitpod](https://www.gitpod.io/) was used as the developer platform.

### Other Programs

- [Balsamiq](https://balsamiq.com/) was used to create a mock-up of the website after exploring the strategy and scope planes of user experience for this project.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS code.
- [W3C Html Checker](https://validator.w3.org/) was used to validate HTML code.
- [Pic Resize](https://picresize.com/) was used to resize images available on the website, improving its performance.
- [Ligthhouse](https://github.com/GoogleChrome/lighthouse) was used to audit my website. The results of the audit were considered when making improvements to the website's performance etc.
- [Am I responsive](http://ami.responsivedesign.is/) was used to view the website across several devices at once.
- [W3C Spell checker](https://www.w3.org/2002/01/spellchecker) was used to check the spelling of the website.
- [Can I use](https://caniuse.com/) was used to check browser supports range and potential compability issues and known bugs. 
- [Browser Stack](live.browserstack.com) was used to test the website on different operating systems and browsers.
- [Favicon from Pics](http://favicon.htmlkit.com/favicon/) was used to create a favicon to be used in the address bar.


## Deployment



## Credits

### Code



### Content

### Media


### Acknowledgements
