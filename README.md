# Brendan Doyle Running Club

## Introduction

  - Welcome to the Brendan Doyle Running Club. I have designed this website for my local running club in Co. Longford, Ireland. The website provides information regarding classes, locations, events, and a contact page. The website also provides a members area where approved members can securly access downloadable training routes (.gpx), as well as upload their own favorite routes to share amongst the members.
  - This is my fourth project on the Full-Stack Developer course with the Code Institute, and focuses on Django frameworks, Bootstrap, Database Managment, Agile Methodologies, and CRUD functionality.

---

## Table of Contents
1. [Introduction](#introduction)
2. [UX - User Experience](#ux---user-experience)
    - [Design Inspiration](#design-inspiration)
        - [Colour Scheme](#colour-scheme)
        - [Font](#font)
3. [Project Planning](#project-planning)
    - [Strategy Plane](#strategy-plane)
        - [Site Goals](#site-goals)
    - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [User Stories](#user-stories)
        - [Visitor User Stories](#visitor-user-stories)
        - [Epic - User Profile](#epic---user-profile)
        - [Epic - Articles](#epic---articles)
        - [Epic - Booking](#epic---booking)
        - [Epic - Photo Gallery](#epic---photo-gallery)
        - [Epic - Visit Us/Reviews](#epic---visit-usreviews)
4. [Scope Plane](#scope-plane)
5. [Structural Plane](#structural-plane)
6. [Skeleton & Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
    - [Security](#security)
7. [Features](#features)
    - [User View - Registered/Unregistered](#user-view---registeredunregistered)
    - [CRUD Functionality](#crud-functionality)
    - [Feature Showcase](#feature-showcase)
    - [Future Features](#future-features)
8. [Technologies & Languages Used](#technologies--languages-used)
    - [Libraries & Frameworks](#libraries--frameworks)
    - [Tools & Programs](#tools--programs)
9. [Testing](#testing)
    - [Unit Testing](#unit-testing)
    - [Integration Testing](#integration-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
10. [Deployment](#deployment)
    - [Connecting to GitHub](#connecting-to-github)
    - [Django Project Setup](#django-project-setup)
    - [Cloudinary API](#cloudinary-api)
    - [Elephant SQL](#elephant-sql)
    - [Heroku Deployment](#heroku-deployment)
    - [Clone Project](#clone-project)
    - [Fork Project](#fork-project)
11. [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Additional Reading/Tutorials/Books/Blogs](#additional-readingtutorialsbooksblogs)
    - [Acknowledgements](#acknowledgements)

---

## UX - User Experience

### Design Inspiration

- I wanted to create a website which contained all of the information that a new visitor to the site would want to see, so I included information about the club and it's goals, where and when the classes are held, a contact form for further queries, and entry to the annual race event. The race event is for the general public, not just for club members.
- I also wanted to create a members area where members must be approved before having access to any of the members material, primarily to the gpx file download feature. the gpx files contain routes that have been created by the club for training purposes, or saved routes from members runs. These files incorporate CRUD functionality for the uploader, but are only downloadable by other members. Once downloaded, the gpx files can be synced with other software like strava, garmin, Coros etc., and the course information can be accessed showing the distance, elevation and terrain of the run. The route can be followed in real-time on supported devices. 

#### Colour Scheme
My color choices 

#### Font
Describe the fonts used in the project and their impact on readability and aesthetics.

## Project Planning

### Strategy Plane
#### Site Goals
The primary goals of the 

### Agile Methodologies - Project Management

### User Stories
#### Visitor User Stories
- As a visitor I can easily view where and when the classes are being held so that I can see if they suits my location and schedule.

#### Epic - Members Area
- As a user I can register with the club so that I can access a members area that is not accessible by non-members, and subject to verification.
- As a member I can log into my account so that I can download gpx routes in the members area.

#### Epic - Members Profiles
- As a logged-in member I can view my personal profile so that I can view, edit & delete my account details.

#### Epic - Race Event Entry
- As a user I can view events so that I can book in for a race event.

#### Epic - Contact Us
- As a user I can contact the club so that I can have any further questions answered.

## Skeleton & Surface Planes

### Wireframes
Provide images or links to the wireframes created during the design phase.

### Database Schema
Include the database schema and entity relationship diagram used in the project.

### Security
Detail the security measures implemented to protect user data and ensure safe operations.

## Features

### User Views and Features - Non-members/Members
- Non-members can view info about the club, classes, times and locations.
- Non-members can visit the events page where they can view the annual club race, 
and also natiowide race events not related to the club.
- Non-members can send queries via the Contact page. 
- Members can view the club GPX files & upload their own routes.
- The members area is subject to admin verification. This ensures only club members 
can access the route information. This is an important safety feature. It is important 
that club members feel safe to use the uploaded routes.
- Members have access to running/fitness related podcasts via Spotify.

### CRUD Functionality
Detail the Create, Read, Update, and Delete functionalities implemented in the project.

### Feature Showcase
Highlight the main features of the project with descriptions and screenshots if available.

### Future Features
- Future features would include haldling the race event booking within the club website. 
This would involve a separate signup for race entrants. This feature would keep the race entrants
separate from verified club members. Non-member race entrants should not have access to member related features.
- I would include articles related to running, nutritional support, etc. I did not include this because of it being
too close to the blog walkthrough project.

## Technologies & Languages Used

- HTML
- CSS
- Python
- Javascript

### Libraries, Frameworks & APIs

- Django
- Bootstrap5
- Google Fonts
- Google Maps

### Packages

- Django Allauth
- Crispyforms
- Crispy Bootstrap5
- cloudinary
- Sendgrid
- Psycopg

### Utilities

- Git
- Github
- Heroku
- PostgreSQL
- Balsamiq Wireframes
- Google Chrome Dev Tools
- Favicon
- Perplexity AI


## Testing

### Unit Testing
Explain the unit testing methodologies used to ensure individual components function correctly.

### Integration Testing
Describe the integration testing processes to ensure different components work together as expected.

### User Acceptance Testing
Detail the user acceptance testing to validate the project meets user requirements.

## Deployment

### Connecting to GitHub
Provide instructions for connecting to the GitHub repository.

### Django Project Setup
Explain how to set up the Django project locally.

### Cloudinary API
Describe the integration with the Cloudinary API for media storage.

### Postgres SQL
Detail the use of Elephant SQL for database management.

### Heroku Deployment
Provide steps for deploying the project on Heroku.

## Credits

### Code
Acknowledge the code adaptation from other sources.

### Media
Credit the sources of images, videos, and other media used in the project.

### Acknowledgements
Thank individuals or organizations that contributed to the project.

---

