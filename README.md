# Books for Life

[![Books for Life logo](./docs/images/android-chrome-192x192.png)](https://books-4-life-2d26bdf04dec.herokuapp.com/)
[![Am I Responsive Mockup](./docs/images/amiresponsive.png)](https://books-4-life-2d26bdf04dec.herokuapp.com/)

## Table of Contents

[Books4Life](#books4life)
  * [Table of Contents](#table-of-contents)
  * [Introduction](#introduction)
  * [User Stories](#user-stories)
  * [UX](#ux)
    + [Typography](#typography)
    + [Wireframes](#wireframes)
  * [Accessibility](#accessibility)
  * [Database Design](#database-design)
  * [Features](#features)
  * [Existing Features](#existing-features)
    + [Custom Error Page](#custom-error-page)
    + [Favicon](#favicon)
    + [Future Features](#features-features)
  * [Issues and Bugs](#issues-and-bugs)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
    + [Testing User Stories](#testing-user-stories)
    + [Manual Testing](#manual-testing)
    + [Automated Testing](#automated-testing) 
        - [Code Validation](#code-validation)
        - [Browser Validation](#browser-validation)
        - [Lighthouse Validation](#lighthouse-validation)
    + [User Testing](#user-testing)
  * [Deployment](#deployment)
    + [Local Deployment](#local-deployment)
    + [Heroku Deployment](#heroku-deployment)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
  * [Acknowledgements](#acknowledgements)


## User Stories

1. As a new user, I want to be able to register for an account on the "Books for Life" website so that I can log in with a username and password.


2. As a registered user, I want to be able to edit my profile information, including my name, password, and profile picture.

3. As a registered user, I want the option to delete my user profile if I decide to leave the website.

4. As a registered user, I want to add a new book to the website, including its title, author, image, short description, and full description.

5. As a registered user, I want to be able to update the information (title, author, image, descriptions) of the books I've added.

6. As a registered user, I want to be able to delete book details from my profile, so it will no longer be visible.

7. As a registered user, I want to be able to like a book presentation so that I can keep track of my favourite books.

8. As a registered user, I want to see a list of all the books I've added to the website for easy reference.

9. As a bibliophile and a registered user, I want to browse and discover new books added by other users on the platform.

10. As a registered or new (unregistered) user, I want to be able to use a contact form to reach out to the website administrators with questions, feedback, or concerns.


## UX

### Development Planes

#### Strategy
- **Objective:** Create a user-centric site that encourages users to share and explore book recommendations, fostering a sense of community among book enthusiasts.
- **User Research:** Conduct surveys and user interviews to understand the needs, preferences, and pain points of both new and experienced book lovers.
- **Competitor Analysis:** Analyse similar platforms to identify gaps and opportunities in the market.
- **Persona Creation:** Develop user personas representing various types of users, including new users, registered users, and bibliophiles.
- **Goals:** Define measurable goals, such as increasing user engagement, time spent on the platform, and user-generated content.

##### Target Audience
**Roles:**
- New Users (unregistered)
- Registered Users
- Bibliophiles (Book Lovers)
- Administrators

**Demographics:**
- Desire to learn
- Desire to read more
- Book Lovers (Bibliophiles) 
- Self-learning individuals
- All ages

**Psychographics:**
- Personality & Attitudes:
- Curious
- Eager to learn
- Bibliophile

**Values:**
- Knowledge
- Self-improvement
- Community

**Lifestyles:**
- Interest in books
- Creative
- Knowledgeable

##### User and Client Needs
|User Needs|Client Needs|
|:---|:---|
|Register/Login to account|Provide a Book Database|
|Search for books|Log into administrator account for defensive design|
|View Book Details|Use website themselves|
|View Favourite Books||
|Get in Contact with Admin||

##### Importance/Viability Tables
![User Management](./docs/images/vt_user_management.png)

![Books Management](./docs/images/vt_books_management.png)

![Other Features](./docs/images/vt_other_features.png)

#### Scope
- **Features:** user registration, profile management, book addition, editing and deletion, liking books, viewing user-added books, a favourites page, contact form, and book search.
- **Content:** Book Review will contain book titles, authors, images, and descriptions (short and full).
- **User Flow:** The user will be able to register for an account, log in, add books, edit books, delete books, like books, view their books, view their favourites, and contact the admin.

<!-- TODO: Diagram -->

- **Technical Requirements:** Front-End: HTML, CSS, Javascript, Bootstrap 5, Font Awesome; Back-End: Python, Django 4.1, PostgreSQL For deployment, the project will be hosted on Heroku, with static files stored on Cloudinary and the database hosted on ElephantSQL.The whole project will be version controlled using Git and GitHub.
Milestones: The whole project is broken down into smaller milestones, which are then broken down into tasks. The project will be managed using Github Project.The three milestones are: MVP Release, User Profile Issues, Project Refinement.


### Typography