<img style="width: 100%;" src="/docs/Title.png">
<h1>Description</h1>
<p>
  movie_review_app (official title: Reel Review) is a web app 
  which allows users to view reviews on movies written by other users. 
  Users need to sign up in order to review, but can navigate without sigining up.
  This project is built on Django with postgreSQL on the back-end, and Vanilla JavaScript
  on the front-end. The goal of this project was to apply as much of the skills that
  I've learned in the past year to a real-world applications.
</p>
<br>
<img style="width: 100%;" src="/docs/browse_page.gif">
<h1>Features</h1>
<ul>
  <li>An Appealing UI with a responsive design</li>
  <img style="width: 50%;" src="/docs/responsive_example.gif">
  <li>Customized admin page that allows users an all-in-one location to add movies</li>
  <img style="width: 50%;" src="/docs/add_movie.gif">
  <li>
    CustomUser model inheriting from AbstractUser. This is created early to make changing the user
    model easy down the line if required.
  </li>
  <li>
    Profile authentication done through django-allauth to handle user registration, password reset, and email changes.
    Also included is a profile page to allow users one place to handle most of these functions.
  </li>
  <img style="width: 50%;" src="/docs/profile_example.gif">
  <li>
    Fetch implementation from JavaScript Vanilla for both GET requests (used in the searchbar) and POST requests 
    (used in submitting reviews).
  </li>
  <li>
    Functioning searchbar to help navigate through movies.
  </li>
  <img style="width: 50%;" src="/docs/searchbar_example.gif">
</ul>
<h1>Getting Started</h1>
<p>movie_review_app works with python 3.6 on any platform. <a href="https://thereelreview.herokuapp.com">Demo This Project Here</a></p>
<h3>Installation</h3>
<ol>
  <li>git clone https://github.com/andydandy21/movie_review_app</li>
  <li>cd movie_review_app</li>
  <li>pip install pipenv</li>
  <li>pipenv install --system</li>
  <li>pipenv shell</li>
  <li>python manage.py runserver</li>
</ol>
<h3>Usage</h3>
<ul>
  <li>Username: demouser</li>
  <li>Password: testing321</li>
  <li>The admin page is located at /admin-hubspace/</li>
</ul>
