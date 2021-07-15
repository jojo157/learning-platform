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
        - [As a site user](#as-a-site-user)
        - [As a site admin](#as-a-site-admin)
        - [As the business owner](#as-the-business-owner)
  - [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
    - [Wireframes](#wireframes)
    - [Database Design](#database-design)
  - [Surface](#surface)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
- [Testing](#testing)
    - [Code Validation](#code-validation)
        - [Html](#html)
          - [Landing Page](#landing-page)
          - [Home](#home)
          - [Content](#content)
        - [CSS](#css)
        - [JavaScript](#javascript)
        - [Python](#python)
    - [Performance Testing](#performance-testing)
    - [User Stories Testing](#user-stories-testing)
      - [Site user](#site-user)
      - [Site admin](#site-admin)
      - [Business owner](#business-owner)
    - [Functionality Testing](#functionality-testing)
    - [Validation Testing](#validation-testing)
    - [Access Testing](#access-testing) 
    - [CRUD Testing](#crud-testing)
    - [Compatibility Testing](#compatibility-testing)
        - [Different devices](#different-devices)
        - [Different Browsers](#different-browsers)
        - [Different Operating Systems](#different-operating-systems)
- [Technologies Used](#technologies-used)
    - [Frameworks and Libraries](#frameworks-and-libraries)
    - [Version Control](#version-control)
    - [Other Programs](#other-programs)
- [Deployment](#deployment)
  - [Run local](#run-local)
  - [Fork repository](#fork-repository)
- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)


## UX

The 5 planes of User Experience:

### Strategy
Finance Mind was created with the purpose of providing an innovative solution to allow a company's training team provide relevant and informative finance content to their employees in a secure platform, to assist with self-learning. 

#### User Needs

##### As a site user
- I want to be able to understand the site purpose immediately.
- I want to be able to register and login, so that I can access the learning content.
- I want to be able to easily navigate the site, ensuring I can access the desired content with ease. 
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
- I want to be informed of users reaction to content. 


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
  - Application will be responsive on all device size and browsers.
- CRUD Functionality.
  - Application will enable the functionality to Create, Read, Update and Delete data.
- Database to store app data.
  - MongoDB database will be used to store all application data. 
- Contact Form.
  - Contact form to enable user to send message to admin. 
- Library with searchable content.
  - Search bar that will allow user query to filter the articles to shown those with a match only. 
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
  - Form to create site contents that only admin will has access to. 
- Admin content edit. 
  - Prefilled form that will allow an admin user edit an existing article.
- Admin user management 
  - Page that will show all registered users and allow an admin user to edit or delete users.
- User settings page.
  - Page that will allow a user to amend their own profile settings. 
- 404 Error Page
  - A custom 404 error page if the user navigates to a resource that doesn't exist with a button to return home. 


#### Future Features 

I would like to include the following future features.
- Messaging functionality for admin to users.
  - A feature where an admin user could choose another user to send a private message to.
- Push notifications about new content been added.
  - The option to send a notification to all site users when new articles added to encourage their continued learning. 

### Structure

During the planning stage, it was decided that the following pages would be needed to ensure the user needs are meet:

- Landing Page with elements:
  - To tell visitor what the application is for.
  - To allow user to register.
  - To allow user to login.
  - To allow user to contact site admin.

- Content Library with elements:
  - To allow user to search library.
  - To allow user to like and dislike article.
  - To allow user to favourite article.
  - To read content and interact with it as needed.
  - To allow an admin user to edit or delete content. 

- Profile Page with elements:
  - Welcome message.
  - To create a new sticky note.
  - To edit an existing note.
  - To view articles favoured and ability to click and be redirected to article. 
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

This application uses Mongo DB to store and retrieve the user data. Mongo DB is a non-relational database. This application consists of 4 collections as shown in the schema diagram below. 

The users collection is populated when a user successfully registers and is used to verify a user upon login.The content collect stores the data for articles that appear on the library page. Only an admin user can add to this collection. The posts collection stores the data for a user's sticky notes that are displayed on their profile. The favourites collection takes record of a user's favoured articles. 

![Finance Mind Schema](static/images/readme_images/schema.png)

### Surface

The Finance Mind application was designed to reinforce learning and create a sense of trust among learners using soft tones. 

#### Colour Scheme

Shades of blue were used to create the impression of trust and loyalty. Turquoise was used to represent open communication, creativity and calming nature. The combination of shades between blue and green are widely used in financial websites. A lighter shade creates the financial association while also looking modern. 

The colours used are shown below:

![Color Schema](static/images/readme_images/colors.png)

The navbar is a gradient of these colours to give a fresh appearance by merging the colours. 

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

A warning appeared on all pages that the flash message section lacked a heading. This warning can be ignored as the section contains a heading element where the elements html is injected with Jinga templating language when needed. Any pages where an error was found are detailed below.

##### Landing Page 

The only error present was that there was an unmatched trailing div. This was removed and the code rechecked. 

##### Home

On first check, there was 3 errors. The first error was that the image elements were missing an alt attribute. I added this in. The second error is that the article icons all had the same ID. I replaced this with a custom data attribute as each article would have 3 occurrences of this value and this violates the definition of a unique ID. The last error is that there was an unclosed div element. I located the element and corrected this. 

##### Content

Two errors were present. The first was that the attribute pattern is not allowed on a text area element. I removed this attribute and have custom JavaScript to validate this field when white space is present only. The second error is that there was a stray div present. I checked the file and removed this. 

All pages now successfully pass through the validator as shown in the image below.

![Html pass](static/images/readme_images/htmlpass.png)

#### CSS

CSS page was validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

No errors were present.

![CSS pass](static/images/readme_images/validcss.png)

#### JavaScript

JavaScript files were validated with [JSHint](https://jshint.com/)

Missing semi-colons were added and the scripts retested. No errors or warnings present.

![Javascript results](static/images/readme_images/validJS.png)

#### Python

Python files were validated with [PEP8 online](http://pep8online.com)

![First validation results](static/images/readme_images/pep8fail.png)

The error present was that the app.py file had several occurrences where a line was greater than 79 characters. I reformatted the app.py file to ensure no line was more than 79 characters and retested.

The file is now PEP8 compliant.

![Final validation results](static/images/readme_images/pep8pass.png)

### Performance Testing

Performance was tested using Lighthouse, one of Google's web developer tools.
To improve the SEO of the app, I added a meta description. Additionally I added the attribute rel="noopener" to all 'a' elements to increase the app security.

For the Library Page (home), the best practices score was 87% due to images been displayed with the incorrect aspect ratio. I changed the CSS to preserve the aspect ratio of the images. This resulted in the best practices score increasing to 100% and improved the layout for user experience. 

example output from Ligthhouse audit for page home

![Home Page Audit Results](static/images/readme_images/homeAudit.png)

The final results for each page are shown in the below table.

![Final validation results](static/images/readme_images/ligthhouseTable.png)



### User Stories Testing

The user's needs are met as follows:

#### Site user

> I want to be able to understand the site purpose immediately.

The Landing Page describes the purpose of Finance Mind clearly. Some of the features are highlighted to give a user a flavour of what is possible on the platform. Two call to action buttons show the user they can sign up or login. Additionally the navbar, again reinforces the option to register or login.


> I want to be able to register and login, so that I can access the learning content.

An easy to understand form is provided to create an account. If an entered value does not match what is required, the user is presented with an error message to help them complete registration. 

![Form validation message](static/images/readme_images/formVal.png)

A registered user can login to their profile by providing the registered username and password. This data is securely saved in the MongoDB database and upon a login request, the entered values are checked. If they match the database data, the user is logged in, if incorrect the user is given a warning message. If user is still having difficult they can contact the site admin, who will be able to reset their password.

![Unsuccessful login attempt](static/images/readme_images/login.png)


> I want to be able to easily navigate the site, ensuring I can access the desired content with ease. 

Upon login, a user is automatically redirected to the library page where all the articles are present. All pages contain a navbar with navigation links that will redirect a user to their desired location. If a user tries to navigate to a resource that doesn't exist. A custom 404 page will be displayed with a button to return to home page. 

![General user Navaigation Bar](static/images/readme_images/userNav.png)


> I want to be able to search articles to show relevant results only.

A search bar is present on the Library page that allows a user to enter a query that will filter the articles to show any matching results. If no result is found, the user is advised. Additionally, a user is given a reset button to clear the search bar, returning the page to show all.

![Search Bar with no results for query](static/images/readme_images/search.png)


> I want to be able to favourite articles for quick access in the future.

Each article has a favourite icon (the widely associated bookmark icon). When a user clicks this, they get a message to say that the article was favoured and a quick link added to their profile. When the fav button on the users profile is clicked, it loads the favoured article only. 

![General users article actions](static/images/readme_images/articleActions.png)

![Users Profile favourites section](static/images/readme_images/favSection.png)


> I want to be able to contact the site admin if needed.

The site admin can be contacted by filling out a form on the contact page. Upon submission the user is advised that the message was sent and admin will contact them shortly. The admin will recieve a message contining the users form details (Name, email and message) and an additonal value of username. If user is logged it, the value is equal to their username and if not, the value is equal to guest.


> I want to be able to update my own user details, such as password without needing to contact the site admin.

On the users profile page there is an icon of a user with cog wheel. If user hovers over this it informs them to edit their user profile. When clicked, a form is prefilled with the user details and they can edit the available fields and click update. The users details in the database will be updated accordingly. The user gets a success message once updated. 

![User Settings update Icon](static/images/readme_images/userSettings.png)


> I want to be able to create short personal notes, that only I have access to.

The users profile page has a section called your notes. A plus icon advises the user they can add a new note. Once clicked a form is presented to the user and once submitted a new note is added to the users profile in date order.

![A Users Note Section on profile](static/images/readme_images/userNotes.png)


#### Site admin

> I want to be able to create site content such as articles that allow the inclusion of resources such as images and links. 

An admin user is presented with additional navigation options. One is to add site content. When clicked this will load a form that allows an admin user to create a new article for the site library. The form allows optional images and external resource links as further reading.

![Navigation bar for admin user](static/images/readme_images/navAdmin.png)


> I want to be able to edit all site library contents, even if another admin created it. 

An admin user is presented with an edit and delete button on all articles on the library page. A general user does not have this functionality. These buttons enable the ability for admin to edit the article on a prefilled form or delete the article with a confirm message. 

![Article as viewed from admin profile](static/images/readme_images/articleAdmin.png)


> I want to be able to amend all users' details, to enable a change in user access rights or if user has issue logging in. 

The User Management page shows all registered users on the app in alphabetical order. An admin user can choose to amend a user by clicking the edit button on that user. A prefilled form allows the details to be updated with a success message on completion. This functionality is only accessible to an authorised admin user.

![User Management Page](static/images/readme_images/usermanagement.png)


> I want to be able to remove a user from the platform and all their stored data.

An admin user can click the delete button to remove a user and this will remove all their data from the database. A confirm message is presented on all delete functionality. 


> I want to be informed of users reaction to content. 

All articles show the number of likes and dislikes. The admin team can use this information to create similar content to what has been liked the most. As per the image of an article above, the number of likes and dislikes is shown on the article. 


#### Business owner

> I want to enable my employees to learn on the go.

The application is responsive across all devices and a registered user can access the app once they have internet connection. This enables on the go learning.

> I want my employees to stay up to date on relevant topics.

The ability for the admin / content moderators to edit and create new content helps ensure relevant topics are being pushed to employees. Articles are shown in date order of newest material at the top. 

> I want to see feedback from users engaging with content. 

All articles show the number of likes and dislikes. The admin team can use this information to create similar content to what has been liked the most. 


### Functionality Testing

I tested the functionality of the site on a laptop and mobile device. Each page was tested and final results are given below:

| **Page**     | **Functions checked** | **Working Correctly Desktop** | **Working Correctly Mobile** |
| --- | --- | --- | --- |
| **Landing** | | | |
|           | Signup button opens registration form| ✓| ✓|  
|           | Login button opens login form| ✓| ✓|  
|           | Navigation links open correct page| ✓| ✓|  
|           | Click on logo redirect to landing page| ✓| ✓|  
|           | Footer links navigate to correct page in new window| ✓| ✓|  
| **Register** | | | |
|           | If enter valid data, user created and logged in| ✓| ✓| 
|           | If enter username already in database, given error that username already exists. | ✓| ✓|  
| **Login** | | | |
|           | If valid details, logged in and redirect to Library page| ✓| ✓|  
|           | If invalid details, not logged in and error message given| ✓| ✓| 
| **Contact** | | | |
|           | User not allowed to send empty form| ✓| ✓| 
|           | When submitted, user gets message to advise message sent.| ✓| ✓| 
|           | Admin receives message that was sent.| ✓| ✓| 
| **Library** | | | |
|           | Search bar filters articles based on query| ✓| ✓| 
|           | If no matching results, message shown to user| ✓| ✓| 
|           | Reset button clears search| ✓| ✓| 
|           | Search button submits query for search| ✓| ✓| 
|           | Article like button increases score by 1 when clicked | ✓| ✓| 
|           | Article dislike button increases score by 1 when clicked | ✓| ✓| 
|           | Article favourite icon adds the clicked article to favourite section on profile| ✓| ✓| 
|           | Article expand button expands article to view its contents| ✓| ✓| 
|           | Further Reading button opens resource in new window| ✓| ✓| 
|           | Clicking on the expand icon when expanded closes the section| ✓| ✓| 
|           | Admin - edit button on article opens prefilled content form| ✓| ✓| 
|           | Delete button on article gives confirm message and if press ok,article removed from library| ✓| ✓|  
| **Profile** | | | |
|           | User settings page loads when click the icon, with the correct data shown | ✓| ✓| 
|           | Favourite article link when clicked redirects to correct article | ✓| ✓| 
|           | The plus icon under notes opens the add note form| ✓| ✓| 
|           | The edit button on note, opens prefilled note form| ✓| ✓| 
|           | The delete button gives user delete confirm message and when press ok, note deleted.| ✓| ✓| 
|           | Notes shown in date order| ✓| ✓| 
| **Logout** | | |
|           | users data is removed from session when click log out| ✓| ✓| 
| **Note** | | |
|           | Valid form creates a new note on the users profile| ✓| ✓| 
| **Edit Note** | | |
|           | The prefilled note, can be edited and once user pressed update, the note shows the new information| ✓| ✓|  
| **User Management** | | | |
|           | All registered users are shown to an admin user alphabetically based on first name| ✓| ✓| 
|           | Admin - click edit button opens form with the selected users details| ✓| ✓| 
|           | Admin - click delete button - confirm prompt and then user removed from users screen| ✓| ✓| 
| **Add Site Contents** | | | |
|           | Valid form can be submitted| ✓| ✓| 
|           | New article created on the Library page in date order of creation| ✓| ✓| 
| **404** | | | |
|           | If try to navigate to page that does not exist, 404 page is rendered| ✓| ✓| 
|           | Button to return home, navigates user home| ✓| ✓| 

### Validation Testing

All forms were manually tested and the result of the testing are shown in the below table.

![Form Validation Testing Results](static/images/readme_images/formValidation.png)

### Access Testing

To ensure that only authorised users can access or modify a resource. Testing was needed using a general user account, an admin user account and staying logged out and trying to hard access a resource through the browser address.

Based on the results, I added additional checks to ensure that the edit or delete note is only actioned if the session user matches the requested notes author. I also added a 500 internal error page as this occurred during testing for unauthorised access requests. 

The results are shown below.

![Access Testing Results](static/images/readme_images/accessTesting.png)

### CRUD Testing

The Create, Read, Update and Delete actions on the Mongo DB database were tested by logging in as an admin user and checking the result of each CRUD execution in the relevant collection on the database to verify the data has been modified as necessary.

This testing identified a bug in the favourite article function. Previously, the condition checked if an article  had be favoured already in the favourites collection but this did not take the username into consideration, meaning that each article was only allow to be favoured once and the next users request was not recorded. I updated the code to check the favourite based on username and article id and this resolved the bug. Now each user can favourite each article once. 

A summary of the testing is shown below.

![CRUD Testing Results](static/images/readme_images/crudTesting.png)

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

Based on the user experience I added some more margin on the landing page and altered the layout of the user management page for smaller devices to ensure the layout is maintained. The application is responsive on all devices.

#### Different Browsers

I tested the website on:

- Google Chrome
- Safari
- Firefox
- Microsoft Edge
- Internet Explorer

Differences discovered across browsers:
The only difference noted was the scroll bar style which is dependent on the browser. 

#### Different Operating Systems

The above testing was conducted on below operating systems:

- Windows 8.1
- MacOS Big Sur 11.2.3
- iOS 14.4.2
- Android

There were no differences detected on those operating systems. [Browser Stack](live.browserstack.com) was used to view and check the functionality across a wide range of devices and operating systems.

## Technologies Used

### Frameworks and Libraries

- [Google Fonts](https://fonts.google.com/) was used to import the font selected for the website.
- [jQuery](https://jquery.com/) was used as a JavaScript library.
- [jQuery Aplus](http://japlus.simplit.it/) is a plugin that was used for confirmation messages.
- [Materialize](https://materializecss.com/) was used as a framework for layout and responsiveness to create this application.


### Version Control

- [Git](https://git-scm.com/) was used as a version control system. This following commands were used:
  - git add filename
    - This command adds the file to the staging area.
  - git commit -m "commit message"
    - This command commits our changes to our local repository.
  - git push
    - This command pushes our changes to the remote repository.
- [GitHub](https://github.com/) was used for the repository hosting.
- [Gitpod](https://www.gitpod.io/) was used as the developer platform.

### Other Programs

- [MongoDB](https://www.mongodb.com/1) was used to create the document based databases used as data storage for this application.
- [Heroku](https://id.heroku.com/) was used to deploy this application.
- [Balsamiq](https://balsamiq.com/) was used to create a mock-up of the website after exploring the strategy and scope planes of user experience for this project.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS code.
- [W3C Html Checker](https://validator.w3.org/) was used to validate HTML code.
- [Pic Resize](https://picresize.com/) was used to resize images available on the website, improving its performance.
- [Ligthhouse](https://github.com/GoogleChrome/lighthouse) was used to audit my application. The results of the audit were considered when making improvements to the website's performance etc.
- [Am I responsive](http://ami.responsivedesign.is/) was used to view the website across several devices at once.
- [W3C Spell checker](https://www.w3.org/2002/01/spellchecker) was used to check the spelling of the website.
- [Can I use](https://caniuse.com/) was used to check browser supports range and potential compatibility issues and known bugs. 
- [Browser Stack](live.browserstack.com) was used to test the website on different operating systems and browsers.
- [Favicon from Pics](http://favicon.htmlkit.com/favicon/) was used to create a favicon to be used in the address bar.


## Deployment

The project files were created in Gitpod using the Code Institute Full Template. 

This project was deployed to Heroku. The steps are listed below.

First an application needs to be created using the following steps:

- Login to Heroku.
- Click the new button.
- Select create new app.
- Enter a name for your app.
- Select the relevant region.

Once the above steps are complete you now need to create a connection to the Github repository for your application.

- Click the deploy tab.
- Select profile Github.
- Add repository name, click search.
- Click connect to this app.

We now need to set our environment variables for Heroku to be able to deploy our app successfully.

- Click the settings tab.
- Click Reveal Config Vars button.
- Enter the environment variables.

Once Added we can enable automatic deployment by:
- Click on the deploy tab.
- Under automatic deploy, choose the branch.
- Click enable automatic deploys.

### Run local

To run this application locally, one requires an env.py file with the environment variables.

The steps are:
- Log into GitHub and locate the Finance Mind repository.
- Click the "Code" button, click HTTPS and copy the link shown.
- Open terminal and change the working directory to where you want the clone repository to be.
- In the terminal, type git clone, and then paste the URL you copied earlier.
- Press enter and your local clone is now created.

You will then need to install the requirements.txt. This can be done using the command
> pip install -r requirements.txt 

### Fork repository

To copy the repository so that you have access to available files and any new changes will not affect the original repository follow the below steps:

- Log into GitHub and locate the Finance Mind repository.
- On the top far right click on the fork button.
- This will add a copy of Finance Mind to your repository.


## Credits

### Code

- I used this [Blog](https://blog.teclado.com/flashing-messages-with-flask/) for help with add different categories for flash messages for style purposes. 
- I used this [tutorial](https://www.youtube.com/watch?v=QKcVjdLEX_s) for learning purposes of using fetch with flask.
- I used this [resource](https://stackoverflow.com/questions/34548311/data-from-textarea-with-line-breaks-to-database) to solve the issue where the white space on submitting an article was not being preserved.
- I used this users [code](https://stackoverflow.com/questions/32237379/python-flask-redirect-to-https-from-http) to convert http to https. 
- Sean from tutoring for the JavaScript code that prevents only space characters being validated on a text area input. 

### Content

- The Code Institute content helped greatly with this project.
- Real python was a great resource to understand PEP8.
- Materalize documentation was used extensively. 
- Content for the articles was obtained from the below sources
  - Risk versus return content credit to [Finra](https://www.finra.org/investors/learn-to-invest/key-investing-concepts/reality-investment-risk) .
  - What is a pension? content credit to [Irish Life](https://www.irishlifecorporatebusiness.ie/what-is-a-pension) .
  - Pension Tax Relief content credit to [Revenue](https://www.revenue.ie/en/jobs-and-pensions/pensions/tax-relief-for-pension-contributions.aspx) .
  - What is investing content credit to [Investopedia](https://www.investopedia.com/articles/basics/06/invest1000.asp).

### Acknowledgements

- I would like to thank my mentor Spencer Barriball for his help, encouragement and advice.
- I would like to thank Code Institute's Tutor support for their help throughout the course.
- I would like to thank my fellow students for their help on slack.
- I would like to thank my wife Leticia for her continued support.
- I would like to thank Stack Overflow and W3Schools for their content when trouble shooting as these resources were essential to work out how to correct my code.