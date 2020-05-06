# Sara's Django Issue Tracker 

Heroku live link: 
https://sara-django-issue-tracker.herokuapp.com

## Overview 
This project focuses on incorporating django, in order to provide front-end users with the ability to raise issue tickets, or purchase new feature tickets for an app.

### Issue with username during commits 
There has been an issue with the username that is displayed during commits. When a commit is made it doesn’t display my Github username, it presents ‘usernameusername’ instead. This was due to the fact that my email address was set to private, so Github was unable to identify my username. 

The repo for this project was created at the same time I created the repo for a previous project I was working on, with the issue being evident on both repositories. I was able to successfully solve the issue on the previous project. However, after doing so it then stated that there were two contributors to the project, even though I am the only contributor.  

Therefore in order to maintain the correct number of contributors and the commit history I decided not to implement the solution to this project. 

I have also attached a screenshot of the push message to assure you the commits are mine. 

![commit-issues](screenshots/commit-issues.png)

## UX and UI

The full analysis was completed on a separate document. [Please click here to view it.](UX/UX_UI_analysis.pdf)

### Further analysis
The document mentioned above contains an analysis following Garrett’s elements. It also helped justify the decisions made during the implementation stage. The elements examined were:

* Surface
* Skeleton
    - Wireframes - on a separate document, outlined below.
* Structure
* Scope
    - User stories were looked at in greater detail, along with user tasks and what was implemented to achieve this. 
* Strategy

### Goals
As I was creating a website which allowed users to raise and keep track of issues and features, I wanted to create a theme and design that was inline with the scope of this project. Some of the basic goals outlined included:

* Ease of use:
    - Create a positive experience for the user so they return to the website.

* Quick access to information: 
    - The home page displays all the issues and features.
    - I have created the early workings of progress charts, enabling users to easily identify how many issues/features have been completed and how many are outstanding. 

* Develop a responsive mobile first website.


### User stories
An in-depth analysis of the user stories can be seen on the separate document mentioned above, with the key points mentioned below. 
Developing user stories helped identify the scope and outline the needs and actions of the user. Doing so also helped direct other aspects of the UX and UI planning. 

* As a user I want to:
    - add an issue
    - add a feature
    - pay for a feature request
    - see what other issues and features have been added 
    - be able to add feedback
    - be able to see what progress is made
    - be able to see if any issues and features ever get completed 
    - see which features are in progress 
    - upvote/like an issue/feature

### Wireframes (Skeleton)
[Click here for the wireframe.](UX/djangoTracker.pdf)

## Features
* Created extra models
    - Feedback
    - User profiles

* Added extra fields to models:
    - Date added
    - Last updated
    - Number of likes
    - Created foreign key between orders and users 
    - Added monetary requirement fields for features i.e. money received, money needed, and upvost/like cost. 
    
* Chart.js
    - Previously I had stated that I wanted to delve further when using Javascript, therefore I chose chart.js to display the charts on this website. This allowed me to not only experiment with Javascript, but also experience using scripts in a different manner, such as directly within a HTML document. 
    - This also enabled users to quickly identify progress. 

* FontAwesome
    * Used to display icons.

* Ability for users to interact with the owners of the website via social media
    - In the future I would like to expand on this feature, and allow users to be sent directly to the website's social media pages.

* Feature tickets can be bought for a cost. 

* Features and issues can be upvoted.

* Ability to quickly track the progress of on going issues and features, and identify which ones have been marked as completed. 

* Users can leave feedback as well as see what feedback others have left.

* Created different alerts for different actions:
    - I chose to create alerts displaying messages for that specific action so as to give the website a more personal feel.

* Access to information on the user account page:
    - Account details such as orders, liked issues and features can be viewed, as well as data from the user profiles model. However, this is something I want to expand on and develop further in the future. This has been explained in greater detail below. 

### Features left to implement
> Front-end features
* Profile page:
    - Go into greater detail when displaying orders on the user account.  

* Update the invoice when checkout is complete so a summary of the order is displayed.

* Allow users to see an expected date of completion for features. 

* Allow users to see who the handler is for a given issue or feature.

> Back-end features
* Currently, feedback has been added within the to_do app primarily as it was a small model to add. However, in the future I want to add it as a stand-alone app.

* Gain a general better understanding of what Django is capable of 
    - Experiment with Django admin and models.

* Learn more about the use of slugs 

* Learn backend security methods:
    - Learn more about backend validated in order to increase security.

* Give users the ability to edit their issues
    - I initially was working on a function that would enable users to edit an issue they may have had, but due to time restraints I decided this would be something that would be better to work on in the future.

* Allow users to comment on issues and feature requests.

* Cart changes:
    - I initially allowed users to add tickets to their cart, but then decided on a different approach, whereby users are now sent directly to checkout when submitting or upvoting features, and can directly submit new free issues. 
    - The cart app has remained however, as I want to develop a function that would allow users to add multiple tickets to their cart and make one payment. 

* Have greater control over the feature costs:
    - Currently there are default values set for upvote cost and the amount of money needed. Some have been manipulated in admin. I would like to develop a function whereby new features are given a status of ‘request submitted’ before being sent directly to the main feature request table, and are at that point individually assigned specific values for the factors mentioned above. 

* Develop the search function further 

## Methods used
* HTML
* CSS
* Bootstrap
* Django
* Python
* Javascript & jQuery

## Testing techniques

- Overview:
1. Manual testing
2. Django tests
3. Form validation 
4. In-person user testing

### 1. Manual testing

> Front-end testing 

* W3C was used to validate HTML: https://validator.w3.org

* Chrome’s responsive web tester was used in order to ensure the website was responsive on different devices as well as various screen sizes. 
    - https://chrome.google.com/webstore/detail/responsive-web-design-tes/bdpelkpfhjfiacjeobkhlkkgaphbobea.

* The website was also tested on various browsers:
    - Firefox
    - Google
    - Safari

* Items and features are separated based on those marked as ‘in progress’ and ‘done’. I checked this was occurring correctly by creating test items and features and altering their progress status.

* Charts displayed the correct pieces of information by displaying the right numbers.

> Back-end testing

* Manually testing all functions worked as expected:
    - Added a new issue and new feature.
    - Marked issues and features as done and ensured they were then only displayed in the tables for completed items. 
    - Checking the count functions added or subtracted correctly. 
    - The correct number of expected items were added to the basket and any changes were correctly displayed in the cart product count.

* Tested models:
    - Checked the ‘date added’ and ‘last updated’ models were displaying the correct dates by altering details of a specific item and making sure the right model edited its date. 

    - Tested feedback model 
        - Added feedback and ensured it was added to the list in admin. 
        - Checked that feedback would be displayed randomly on the feedback page. 
        - Developed the need for the name to come from the user profile, and also the logic for an 'anonymous' name input if the name field is left empty. 
    
    - Upvote logic:
        - Upvoted an issue and feature and checked the total amount upvoted was correct. 
        - Upvoted a feature request and checked the amount_received was the right amount.
        - Users can’t like an item or feature unless they’re logged in, so I attempted to do so and ensured an alert was displayed in the browser prompting the user to login. 
        

### 2. Django testing 
* Django tests were created to test some of the models, views and forms.
    - Can be seen through the files:
        - test_models.py
        - test_views.py
        - test_forms.py

### 3. Form Validation
* Account related validation
    - **Login form**:
        - If login details are incorrect it alerts the user. I registered a new account and entered the incorrect details, and was successfully given error messages. 
    - **Registration form**: 
        - If registering for an account, if the user attempts to use an email that is already associated with another user then an error message will successfully be displayed informing the user the email address is already in use.
        - Attempted to register with certain details missing, and the user is successfully given an alert prompting them to provide the necessary information. 
    - **Password criteria**: 
        - Passwords have to match when registering and logging in. To check this I entered passwords that didn’t match and ensured an error message was displayed notifying the user.
    - **Checkout form**: 
        - Users have to be logged in before they can checkout. To test this I tried to checkout without being logged in, and an alert successfully prompts the user to login.
        - Attempted to buy items with invalid card details and missing information, and an alert is successfully displayed telling the user to check their details and provide the information that is missing. 
        - Tested whether the checkout form identified the correct amount of products to be paid for.

### 4. In-person User Testing 

* As part of the UX and UI testing, I conducted in-person user tests. This allowed me to observe natural user interactions. I was able to identify what users found difficult, and if any roadblocks existed. 
* This lead to the following changes:
    - Created a separate page for issues and features that were completed. This prevented information overload on the home page, and also allowed the user to quickly identify which issues and features were currently still open and pending.

## Deployment
Github and Heroku were used for the deployment of this project.

Heroku live link: 
https://sara-django-issue-tracker.herokuapp.com

Heroku deployment method:
1. Create a Heroku account if you don’t already have one: 
https://www.heroku.com
2. Install Heroku CLI on your local machine: 
https://devcenter.heroku.com/articles/heroku-cli
3. Check that Heroku has successfully been installed by typing this in your terminal:


```sh
heroku –version 
```

4. Now login to your Heroku account from your terminal. This will allow you to connect to the Heroku CLI you’ve installed. 

```sh
heroku login 
```

### Loading my Heroku app on your local machine 

#### Through Github 
1. Download the project:
    1. As a zip file
    OR
    2. Git clone the project 

2. Install the requirements from the requirements.txt file:
    ```sh
        pip3 install -r requirements.txt 
    ```
3. Run the project:
    ```
        python3 -m flask run
    ```

### Linking Github and Heroku pushes 
1. Log on to Heroku and locate the project. 
2. When you are on the main dashboard of the project, locate the deploy tab.
3. Once you have clicked this and have been redirected, scroll down to the option that allows you to connect your Github repo to Heroku. 
4. Once connected you will then be able to enable automatic deploys. 

* Now pushing to Github will also push changes to Heroku. 

## Credits

* A bootstrap theme has been used and modified in order to take advantage of its sidebar feature.
* The code for the charts from chart.js was partially implemented from a tutorial from ‘CodingEntrepreneurs’.

### Media
All the media for this project has been obtained from Google.  

### Acknowledgements
Feedback from my mentor: Dick Vlaanderen

This is for educational purposes.