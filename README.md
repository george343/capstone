#1. Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.

My program uses django for the backend with a few javascript functions and 2 models.
It is a (not very beautiful) copy of Youtube.

#2. What’s contained in each file you created.

In video folder there are the following files:
1. Folders
    - static which contains main.js and style.css. The first contains all the javascript code used in the app and the
      second all the CSS style.
    - templates contains the HTML code for every page in the web app.
    

2. Files
    - <b>admin.py</b> contains the VideoAdminand and CommentAdmin classes represanting the fields of the models showing in the
      admin page.
    - <b>models.py</b> contains the User class which inherits from the AbstractUser class and uses it as it is. Video class
      which represents every video contained in the app and Comment class, connected to Video, holds the comments for 
      every video.
    - <b>serializers.py</b> contains two classes, CommentSerializer and VideoSerializer, which serialize the data from the
      model classes to pass them to the api calls.
    - <b>urls.py</b> has every url used by the app for returning the html files as well as the api urls.
    - <b>views.py</b> contains the following functions:
        - <b>index</b> returns the "index.html"
        - <b>login_view</b> receives a username and password and authenticate the user permitting or denying access to the app.
        - <b>logout_view</b> handles the logout of the user.
        - <b>register</b> receives a username a password and a password confirmation, checks the 2 fields of password and 
          confirmation, as well as the username if it already exists, and if everything is correct creates a new account.
        - <b>show_comments</b> is an api call which returns all the comments.
        - <b>show_category</b> filters the database for the category passed as argument and returns all the videos in this
          category.
        - <b>show_profile</b> shows the videos the user has uploaded or liked. Additionaly the user can upload new videos to
          the app.
        - <b>show_all</b> returns all the videos from the database.
        - <b>show_video</b> shows a specific video whose id is past as an argument. Additionally, it returns the comments 
          associated to the video and all the videos from the same category. You can also post a new comment.
        - <b>like_video</b> is an api call which using the PUT method changes the value "likes" of a specific video.  

#3. How to run your application.

From the first page you can either login or register a new account<br>
You are then redirected to the home page where you can find the video categories. Clicking on any of them can take you 
to the videos of the selected category <br>
There is also a page where you can see all the videos from all categories.<br>
Clicking on any video will direct you to the video page where you can watch the video, choose other videos from the same
category, like it or comment.<br>
Going to your profile you can upload a video, see the videos you uploaded and liked.
Below the menu is the search bar where you can type anything and search for videos that contain what you typed.

#4. Any other additional information the staff should know about your project.

Nothing.