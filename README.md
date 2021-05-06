# Coding challenge as part of APAX interview process

Built off of the following prompt:

_Build an interface that prompts a user’s location and displays the current weather info about the location. Integrate whichever weather source you feel comfortable integrating and explain why you selected that source._

_The app should require a user to sign in (does not need to be a full authentication process, just ask for a username to track the user), and the user should be able to setup multiple locations to check weather. When the app updates the weather info, it should update each location. The users and their locations should be stored in a database._

_This task can be solved in whichever language you prefer. Please use whichever language you feel best showcases your skills._

_Commit the code to GitHub, BitBucket, or other hosted Git repository and share it with our team to review._

## Thoughts and comments

This was my first ever project with Django. I enjoyed it. It's certainly doesn't have the absurd level of abstraction that Laravel brings, but it's clearly built on similar concepts. Also, I was very happy to be using python instead of php.

_"...and explain why you selected that source."_\
I chose https://openweathermap.org - I have used it multiple times and knew it would satisfy the needs of the project.

_"When the app updates the weather info, it should update each location."_\
I chose to instead expose the refresh functionality directly to the user. Each user is able to refresh each of their locations' weather data on an individual level or en masse.

## Stretch Goals
API: I went very bare bones with how I used the openweathermap API. Currently,the Refresh All button calls the same endpoint repeatedly, once for each of the user's locations. Ideally it would call a different endpoint that accepts and returns data for all relevant locations.

Front-end: I have done nearly zero aesthetic work on this project. I don't believe this represents my aptitude for such tasks, but it may represent my level of interest in them.

Data Model: The two tables for this project currently have a One to Many relationships. (A User can have many Locations) This means there's potentially duplicate data being stored if multiple users are keeping track of the same location. The solution for this would be to establish a Many to Many relationship so that multiple Users may refer to the same instance of a Location.

Security: This is a horrifically insecure app. There is no real authentication and any of the endpoints can be hit with no restrictions. This was clearly stated as not a requirement, but I want to  mention it so that it's clear I'm aware of the issue.




