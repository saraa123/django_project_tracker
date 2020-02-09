# Sara's django issue tracker 

Heroku live link: 
https://sara-django-issue-tracker.herokuapp.com

## Overview 
This project focuses on incorporating django, in order to provide front-end users with the ability to raise issue tickets, or purchase new feature tickets for an app.

## UX and UI
As I was creating a website which allowed users to raise and keep track of issues and features, I wanted to create a theme and design that was inline with the scope of this project. 
* Ease of use:
    - I incorporated a Bootstrap theme which showcased a dashboard in order for users to easily be able to access different pieces of information 
* Quick access to information: 
    - The home page displays all the issues/features, as well as their progress. 
    - I have created the early workings of progress charts, enabling users to easily identify how many issues/features have been completed, and how many are outstanding. 

## Features
* Created my own extra models
    - Date added
    - Last updated
    - Number of likes
* Chart.js
    - Previously I had stated that I wanted to delve further when using Javascript, therefore I chose chart.js to display the charts on this website. This allowed me to not only experiment with Javascript, but also experience using scripts in a different manner, such as directly within a HTML document. 
* FontAwesome
    * Used to display icons.
* Ability for users to interact with the owners of the website via social media
    - In the future I would like to expand on this feature, and allow users to be sent directly to the website's social media pages.
* Users are able to purchase feature tickets that incur a cost. They can also purchase urgent issue tickets. There is also an option to request a free non-urgent issue ticket that doesn’t require the user to checkout. 
* Ability to quickly track the progress of on going issues and features, and identify which ones have been marked as completed. 


### Features left to implement
> Front-end features
* Give users the ability to edit their issues and add comments
    - I initially was working on a function that would enable users to edit an issue they may have add, but due to time restraints I decided this would be something that would be better to work on in the future. 
* Allow users to leave feedback 
    - Currently feedback is hardcoded. However, in the future I would like to learn how to develop a real feedback section for users, as well as have snippets of this feedback presented on the progress page. 

> Back-end features
* Gain a general better understanding of what Django is capable of 
    - Experiment with Django admin and models.
* Learn more about the use of slugs 
* Learn backend security methods:
    - Learn backend validated in order to increase security.
 

## Methods used
* HTML
* CSS
* Bootstrap
* Django
* Python
* Javascript & jQuery

## Testing techniques

### Manual testing
A lot of manual testing has been implemented during the building stage of this project. 

* Chrome’s responsive web tester was used in order to ensure the website was responsive on different devices as well as various screen sizes. 
* The website was also tested on various browsers.
* Manually testing all forms and functions work as expected:
    - Includes checkout form, registration form and ensuring the correct amount of products are added to the basket. 
    - Checking the count functions added or subtracted correctly. 
* Charts displayed the correct pieces of information by displaying the right numbers.


### Django testing 
* I created Django tests to test some of the models, views and forms.

### Validation
* W3C was used to validate HTML: https://validator.w3.org
* Form validation was completed:
    > Account related validation
        - If login details are incorrect it alerts the user. I registered a new account and entered the incorrect details, and was successfully given error messages. 
        - If registering for an account, if the user attempts to use an email that is already associated with another user then an error message will successfully be displayed informing the user the email address is already in use.
        - Passwords have to match when registering and logging in. To check this I entered passwords that didn’t match and ensured an error message was displayed notifying the user.
* Users can’t like an item or feature unless they’re logged in, so I attempted to do so and ensured an alert was displayed in the browser prompting the user to login. 
* Items and features are separated based on those marked as ‘in progress’ and ‘done’. I checked this was occurring correctly by creating test items and features and altering their progress status.  
* Checked the ‘date added’ and ‘last updated’ models were displaying the correct dates by altering details of a specific item and making sure the right model edited its date. 
* Users have to be logged in before they can checkout. To test this I tried to checkout without being logged in, and an alert successfully prompts the user to login. 
    

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

## Credits

* A bootstrap theme has been used and modified in order to take advantage of its sidebar feature.
* The code for the charts from chart.js was partially implemented from a tutorial from ‘CodingEntrepreneurs’.

### Media
All the media for this project has been obtained from Google.  

### Acknowledgements
This is for educational purposes.