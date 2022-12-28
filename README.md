# Welcome to **[GAA Stories](https://p4-gaa-stories.herokuapp.com/)**

![Responsive Image](media/images/responsive%20image.jpg)

This purpose of this blog page is for people who are interested in talking and hearing about all the latest news within the GAA. Users can interact with posts by liking or commenting on a post there intersted in (only registered users can do these actions). A registered user can also create there own posts for the community to see.

Check the deployed page [here](https://p4-gaa-stories.herokuapp.com/).

***

## User Experience (UX)

First Time User Goals

* As a First Visit User, I understand the purpose of the blog straight away.
* As a First Visit User, I find it easy to navigate throughout the website.
* As a First Visit User, I can register for an account.
* As a First Visit User, I can read all the blog posts.
* As a First Visit User, I can contact the site owner.

Registered User Goals

* As a Registered User, I can log in to my account so that I can start liking and commenting on posts.
* As a Registered User, I can logout of my account for security reasons.
* As a Registered User, I can modify and update my posts.
* As a Registered User, I can delete my posts if necessary.

Admin User Goals

* As an Admin, I can create, read, update and delete posts from the admin panel.
* As an Admin, I can approve or disapprove any comments.
* As an Admin, I can approve all new blog posts, so that i can make sure the post is appropriate.
* As an Admin, I can determine specific level of priviledge of users in order to post blogs.

***

## Design 

### Wireframe
The first thing i drew up was a very rough wireframe to get a feel for the base layout. I didnt want to do much with the wireframe as I wanted to see what felt right as I went on with the project. 

<details>
<summary>Wireframe</summary>

![Wireframe](media/images/Wireframe.png)
</details>

### Color Palette

The color pallette I used was generated from a picture of croke park which is the header image on the home page. The colors generated can be seen below.

<details>
<summary>Color Palette</summary>

![Color palette](media/images/Color%20palette.png)
</details>

### Fonts

The fonts I used for this project are 'Oxygen' for the body and 'Prompt' for page title.


### Database Schema
To create my back-end database I have used ElephantSQL. I have designed my database using [drawSQL](https://drawsql.app/), this is a free-to-use software however quite limited, as some fields didn’t allow me to overwrite them, such as image fields. To help with the authentication Django has a built-in user Model Allauth which helps save time creating my own Model.

I have created three models for this project Post Model, Comment Model and the Contact Us Model.

<details>
<summary>Models Diagram</summary>

![Models Diagram](media/images/models%20diagram.jpg)
</details>

***


## Features

### Home Page
When you enter the site for the first time you are greeted with a header image of the home of the GAA (Croke Park). Within the image there is some text to give a first time user a clear view as to what the blog is about. 
![Home page](media/images/home%20page%20header.jpg)

### Navbar
There is a very clear navbar which sticks to the top of the page so is always available for use. The navbar changes depending on whether the user has logged in or not. If not logged in a user will have the option to register(if they dont already have an account) or to login. If the user has logged in then they can add a post direct from the navbar or logout of there account.
![Nabvar 1](media/images/navbar1.jpg)
![Navbar 2](media/images/navbar2.jpg)


### Contact Us
(need to set this page up)

### Blog 
On this page the user can see 6 posts per page with the most recent blog posts showing up first. The user can then click any post they wish to view which will bring them to view the full post.
![Blog page](media/images/blog%20post%20page.jpg)

### Blog post full view
When the user clicks into a post they will see the title, author and date/time it was posted. Then they will see the full content of the post and also how many likes and comments the post has. However if the user is not logged in they cannot like or view comments on the post.
![Blog page logged out](media/images/blog%20post%20full%20view%20logged%20out.jpg)
<br>

If the user is logged in they will be able to like the post and cooment on it. Also if the post is one of the currently logged in users then the will have the funtionality to edit or delete the current post.
![Blog page logged in](media/images/blog%20post%20full%20view%20logged%20in.jpg)
<br>

This is comment section the user will see if logged in. They have the ability to create there own comment and can also see all the previous comments along with who wrote it and they date they wrote it.
![Blog page comment section](media/images/blog%20post%20comment%20section.jpg)


### Create a post
When the user wishes to create there own blog post they will be directed to this page which is a form for them to fill out with all the information they would like to include in there post. Once they click add it will have to be reviewed by the site owner before it will be visiable for everyone to see.
![Create a post](media/images/Create%20a%20post.png)


### Sign Up
This page allows the user to sign up for there own personal account. They must create there own username and password. Once the form is completed they will be redirected back to the home page where they can start interacting with blog posts. If a user already has an account they can click the "sign in" link in the line of text.
![Sign Up](media/images/sign%20up.jpg)


### Sign In
When a user has an account this is the page they can log in from. The simply have to input there username and password. If a user doesnt already has an account they can click the "sign up" link in the line of text to sign up for an account first.
![Sign In](media/images/sign%20in.jpg)


### Sign Out
When a user clicks the logout button they will be redirected to this page to confirm that they want to log out.
![Sign Out](media/images/sign%20out.jpg)


### Edit Post
When the author of the post clicks the edit button they will be met with the same form as when they added the post except this time all the fields will be prepopulated with the information that was filled in already making it very easy for the user to edit the post.
![Edit Post](media/images/Edit%20post.png)


### Delete Post
When a user wishes to delete a post and they hit the "Delete Post" button they will be directed to this page to confirm that they wanna delete the selected post.
![Delete Post](media/images/delete%20post.jpg)

***

## Tech Stack 

### Languages
Main programming languages used are:

- Python
- HTML
- CSS
- Javascript
- Django

### Tools
- [Github](https://github.com/) for store and version control of the code.
- [Gitpod](https://gitpod.io/workspaces) for editing code.
- [Heroku](https://heroku.com/) for deployment.
- [Cloudinary](https://cloudinary.com) for store the images and css files used in this project.
<!-- - [techsini.com](https://techsini.com/multi-mockup/index.php) for generating the mock up. -->
- [Bootstrap](https://getbootstrap.com/) was used to speed up the design the style and responsiveness of the website.
- [Google](https://www.google.ie/) was used to source the images for the page.
- [Font Awesome](https://fontawesome.com/) was used for the like button and the comment icon.
- [Google Fonts](https://fonts.google.com/) was used to get the fonts used in the project. 
- [Coolors](https://coolors.co/) was used to generate a color palette from an image I used.

***

## Testing

Testing was done throughout the development of this site through trial and error with Google Dev tools. Testing and code validation can be found in the following [TESTING.md](TESTING.md).

***

## Deployment
 
To deploy your own project through Heroku follow the below steps:

* Sign Up/ Log In to Heroku
* On the Dashboard page select 'New' and the 'Create New App'.
* Provide your new app a suitable name which is unique as it cant be in use already, and select the region.


* I used [ElephantSql](https://www.elephantsql.com/) for my database.
* Create your ElephantSql account.
* Then navigate to the 'Create New Instance' tab.
* Name your database and select 'Tiny Turtle' in the 'plan' dropdown as it is the free option.
* Hit the 'Select region' button to continue.
* From the 'Data center' dropdown select the option which is closest to your region.
* Hit the 'review' button to review your plan and if its all good then hit 'create instance' to create your database.


* Within the repository in GitPod create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL ElephantSQL.
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here". Add the secret key just created to the Heroku Config Vars as SECRET_KEY as the key and "your secret key" as the value.
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url insert the line if os.path.isfile("env.py"): import env remove the insecure secret key with SECRET_KEY = os.environ.get('SECRET_KEY') replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}.
* In the terminal migrate the models over to the new database and sign up/log in to cloudinary.
* In cloudinary copy the CLOUDINARY_URL to the clipboard and paste this into the env.py as follows: os.environ["CLOUDINARY_URL"] = "Url copied here".
* In Heroku, add the CLOUDINARY_URL and value copied from the clipboard to the config vars in settings. Also add the KEY - DISABLE_COLLECTSTATIC with the Value - "1". (This must be removed prior to final deployment)
* Add the cloudinary libraries to the list of installed apps just above above 'django.contrib.staitcfiles' and cloudinary goes below.
* In the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Heroku needs to be added to the allowed_hosts list followed by 'localhost'.
* Create a new file on the top level directory - Procfile. Within this file ensure the following code is added: web: guincorn PROJECT_NAME.wsgi
* Ensure ALL changes have been added, committed and pushed to GitHub.
* Return to Heroku and look for the deployment tab. Click Deploy branch manually (this can be changed to automatic at later date).
* If there are no build log errors you should see a notification advising ' Your App was successfully deployed' with a link to the live site.

```
Go to "Settings" then "Config Vars" and click the button "Reveal Config Vars". 
Make sure your Config Vars look as follows:

    * DATABASE_URL - (will be copied from ElephantSql)
    * SECRET_KEY - (this is what ever value you gave it in settings.py)
    * CLOUDINARY_URL - (copy the URL from your account on Cloudinary) 
    * DISABLE_COLLECTSTATIC - (1)
    * PORT - (8000)
```

***

## Credits

- The initial site functionality was made using the 'I Think There For I Blog' walkthrough by Matt Rudge via Code Institute. The code was adapted for what I needed.

- The [Django Documentation](https://docs.djangoproject.com/en/4.1/) was an invaluable source of information throughout this project

- The [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was a big source of information when the styling of the website was created.

- This [video series](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) helped me alot throughout the project.

- Online resources such as:
    - [W3School](https://www.w3schools.com/)
    - [Fontawsome](https://fontawesome.com/)
    - [Markdown best practices](https://www.markdownguide.org/basic-syntax/)
    - [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    - [Stackoverflow](https://stackoverflow.com/)

- The Code Institute Slack channel for always being helpful and full of information.
