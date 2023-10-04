# Testing

This is the Testing section of the [README.md](README.md) file. It contains all the testing information for the project "Books for Life".

Return to [README.md](README.md)
## Table of Contents

[Testing](#testing)
[Table of Contents](#table-of-contents)
+ [Testing User Stories](#testing-user-stories)
+ [Manual Testing](#manual-testing)
+ [Automated Testing](#automated-testing) 
    - [Code Validation](#code-validation)
    - [Lighthouse Validation](#lighthouse-validation)
    - [Browser Validation](#browser-validation)
+ [User Testing](#user-testing)

[Back to top ⇧](#table-of-contents)

### Testing User Stories
***
1. As a ***new user***, I want to ***be able to register for an account on the "Books for Life" website***, so that I can ***log in with username or email, and password***.

- **Acceptance Criteria**
***Registration Form:***
- [x] There is a registration form accessible from the website's homepage.
- [x] The registration form includes fields for username, email address, password, and password confirmation.
- [x] Passwords are required to meet minimum default complexity requirements.
***Validation:***
- [x] Users are alerted with clear error messages if they submit incomplete or invalid data.
- [x] Users receive an error message if the chosen username is already in use.
- [x] Users receive an error message if the provided email address is already registered.
***Password Security:***
- [x] Passwords are securely hashed and salted before being stored in the database.
- [x] The system enforces password complexity requirements.
***User Data Storage:***
- [x] User data (username, hashed password, email, etc.) is stored securely in the database upon successful registration.
***User Feedback:***
- [x] Upon successful registration, the user receives a confirmation message.
- [ ] Optionally, an email confirmation link is sent to the user's provided email address.
***Login Functionality:***
- [x] After registration, users can log in using their username and password.
- [x] Users receive an error message if they enter incorrect login credentials.
***Session Management:***
- [x] User sessions are managed securely, allowing users to stay logged in until they choose to log out.

***

2. As a ***registered user***, I want to ***be able to edit my profile information***, so I can ***easily change a password, and a profile picture***.

- **Acceptance Criteria**

- [x] When logged in as a registered user, I should see an option to access my profile settings.
- [x]  Within the profile settings, I should see fields for editing my email, password, and uploading a new profile picture. If the profile picture field doesn't exist, I should see a placeholder image.
- [x] The password field should allow me to change my password with appropriate validation rules (e.g., minimum length, complexity requirements).
- [x] After making changes, I should be able to save my updated profile information.
- [x] Once saved, my profile information should reflect the changes on my user profile page.

***

3. As a ***registered user***, I want ***the option to delete my user profile*** so I can ***decide to leave the website***.


- **Acceptance Criteria**

- [x] When logged in as a registered user, I should see an option to access my account settings.
- [x] Within the account settings, there should be a clear and easily accessible option to delete my user profile.
- [x] Clicking the "Delete Profile" option should prompt me to confirm my decision.
- [x] After confirming, my user profile and all associated data should be permanently deleted.
- [x] Upon deletion, I should be logged out, and I should receive a confirmation message indicating that my profile has been deleted.

***

4. As a ***registered user***, I want to ***add a new book to the website***, so that ***its details would be added to the database***.

- **Acceptance Criteria**

- [x] The user must be logged in as a registered user to access the "Add Book" feature.
- [x] There should be a clearly visible option or button for adding a new book on the website.
- [x] The user should be able to enter the following information for the book: Title (mandatory), Author (mandatory), Image (mandatory), Short Description (mandatory, limited character count), Full Description (mandatory), Image (optional).
- [x] The title and the author should provide a slug, but there should be a validation to generate different slug if there are books with the same  title.
- [x] The image upload should support common image formats (e.g., JPG, PNG) and have a file size limit. Invalid image formats or oversized images should be rejected with a clear error message.
- [x] After submitting the book details, the book should be saved in the database with a unique identifier.
- [x] The newly added book should be displayed on the website immediately after submission.
- [x] The user should receive a confirmation message after successfully adding a book.

***

[Back to top ⇧](#table-of-contents)


5. As a ***registered user***, I want to ***be able to update the the books I've added***, so I can ***correct the information of the record (title, author, image, descriptions)***.

- **Acceptance Criteria**

- [x] The user must be logged in as a registered user to access the book update feature.
- [x] There should be a visible and accessible option or button to edit/update a book's information.
- [x] When the user clicks the edit/update option for a book, they should be directed to a book editing form.
- [x] The editing form should display the current information of the book (title, author, image, descriptions).
- [x] The user should be able to modify the title, author, image, and descriptions fields.
- [x] The form should have validation to ensure that required fields are not left empty.
- [x] The user should have the option to cancel the editing process and return to the book details page without saving any changes.
- [x] Upon saving the changes, the book's information (title, author, image, descriptions) should be updated in the database.
- [x] A confirmation message should be displayed to the user after successfully updating the book's information.

***

6. As a ***registered user***, I want to ***be able to delete book details from my profile***, so it ***will no longer be accessible***.

- **Acceptance Criteria**

- [x] When I am logged in as a registered user and I navigate to my profile, I should see a list of books associated with my profile.
- [x] Next to each book entry in my profile, there should be "Edit" and "Delete" buttons that I can click on to initiate the book deletion process.
- [x] When I click the "Delete" button for a specific book, a confirmation dialog or prompt should appear to ensure that I want to delete the book.
- [x] If I confirm the deletion, the book details should be permanently removed from my profile and should no longer be visible.
- [x] After successfully deleting a book, I should receive a confirmation message or notification indicating that the deletion was successful.
- [x] If I cancel the deletion from the confirmation dialog, the book should remain on my profile, unchanged.
- [x] The deletion process should be quick and responsive, ensuring a smooth user experience.
- [x] The system should handle any errors gracefully and provide appropriate error messages if the deletion process fails for any reason.

***

7. As a ***registered user***, I want to ***be able to like a book review*** so that I can ***keep track of my favorite books***.

- **Acceptance Criteria**
- [x] The user must be logged in to their registered account.
- [x] In search results there should be a  "Like" or "Favourite" button.
- [x] Clicking the "Like" button should add the book details to the user's list of liked/favourite books.
- [x] Clicking the "Like" button again should remove the book presentation from the user's liked/favorite books.
- [x] The user should see a visual indication (e.g., change in button color or icon) when a book presentation is liked.
- [x] The user should see a visual indication (e.g., change in button color or icon) when a book presentation is unliked.
- [x] The liked/favourite book presentations should be stored and associated with the user's account.
- [x] The user should be able to easily access their list of liked/favourite books from their user profile.
- [x] If the user unlikes a book presentation, it should be immediately removed from their liked/favourite list.

***

8. As a ***registered user***, I want to ***see a list of all the books I've added to the website*** for ***easy reference***.

- **Acceptance Criteria**

- [x] User Authentication: The feature should only be accessible to registered users who are logged in.
- [x] Navigation: There should be a clear and easily accessible link or button in the user interface that takes the user to their list of added books.
- [x] Book List Display: When the user accesses their list, they should see a clear and organized list of all the books they have added to the website.
- [x] Each book entry should display at least the book title, author, and category.
- [x] Detail View: Users should be able to click on a book in the list to view more details about that book, including a description, and any other relevant information.
- [x] Edit and Delete Options: Users should be able to edit the information of a book in their list.
- [x]  Users should also have the option to delete a book from their list.
- [x] Responsive Design: The feature should be accessible and user-friendly on various devices and screen sizes (e.g., desktop, tablet, mobile).
- [x] Performance: The page should load reasonably quickly, even if the user has a large number of books in their list.

***

[Back to top ⇧](#table-of-contents)

9. As a ***bibliophile*** and a ***registered user***, I want to ***access a dedicated "Favourites" page***, so I can ***see all the books I've liked in one place***.

- **Acceptance Criteria**

- [x] When I log in as a registered user, there should be a "Favourites" option visible in the navigation menu.
- [x] Clicking on the "Favourites" option should take me to a dedicated page that displays all the books I've marked as favorites.
- [x] On the "Favourites" page, I should see a clear and user-friendly list of the books I've liked, including their titles, authors, and cover images.
- [x] If I haven't marked any books as favorites yet, the page should display a friendly message indicating that my list is empty and encouraging me to explore and like books.
- [x] Each book displayed on the "Favourites" page should have a button or link that allows me to remove it from my favourites list.
- [x] When I remove a book from my favourites list, it should be immediately removed from the "Favourites" page without requiring a page refresh.
- [x] The "Favourites" page should be responsive and work well on both desktop and mobile devices.

***

10. As a ***bibliophile*** and a ***registered user***, I want to ***search for books on the website***, so that I can ***browse and discover new books added by all users on the website***.

- **Acceptance Criteria**

- [x] The website should have a search bar prominently displayed on the homepage.
- [x] As a registered user, I should be able to access the search functionality without any issues.
- [x] When I type a search query into the search bar and press "Enter" or click the search button, the website should display a list of relevant books based on my query.
- [x] The search results should include book titles, authors, and category of each book.
- [x] Each search result should be clickable, allowing me to view more details about the book when I click on it.
- [x] The search functionality should be responsive and work well on both desktop and mobile devices.
- [x] The search should support basic search features such as partial matching (e.g., "macbeth" should return results for books with "Macbeth" in the title).
- [x]  The search should make me able to like a certain book.

***

11. As a ***registered user***, I want to ***be able to use a contact form***, so I can ***reach out to the website administrators with questions, feedback, or concerns***.

- **Acceptance Criteria**

- [x] The contact form should be accessible to registered users when they are logged in.
- [x] The contact form should have fields for the user to input their name, email address, subject, message, and an optional attachment field.
- [x] The name and email address fields should be pre-filled with the user's registered information.
- [x] There should be a "Submit" button to send the message to the website administrators.
- [x] Upon submitting the form, the user should receive a confirmation message indicating that their message has been sent successfully.
- [x] Website administrators should receive an email notification with the user's message, subject, and contact information when a user submits the form.
- [x] Users should not be able to submit the form if any required fields are left blank or if the attachment exceeds the maximum size.
Users should receive an error message if there are any issues with their submission (e.g., invalid email address, attachment too large) and should be prompted to correct the errors.
- [x] The contact form should be responsive and visually appealing on different devices (e.g., desktop, tablet, mobile).
- [x] The contact form should be accessible to users with disabilities, following WCAG guidelines.

***

[Back to top ⇧](#table-of-contents)


### Manual Testing
#### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Navbar

![Navbar Test](./docs/images/manual_testing/navbar.gif)

- Footer

![Footer Test](./docs/images/manual_testing/footer.gif)

- Favicon

![Favicon Test](./docs/images/manual_testing/favicon.png)

#### Functionalities testing
- Login

![Login Test](./docs/images/manual_testing/login.gif)

- Register

![Register Test](./docs/images/manual_testing/registration.gif)

- Logout

![Logout Test](./docs/images/manual_testing/logout.gif)

- Profile Update

![Profile Update Test](./docs/images/manual_testing/profile_update.gif)

- Profile Delete

![Profile Delete Test](./docs/images/manual_testing/profile_delete.gif)

- Verify Profile Deletion (and all book records associated with the user)

![Verify Profile Deletion Test](./docs/images/manual_testing/delete_verify.gif)

- Add Book

![Add Book Test](./docs/images/manual_testing/add_book.gif)

- Edit Book

![Edit Book Test](./docs/images/manual_testing/edit_book.gif)

- Delete Book

![Delete Book Test](./docs/images/manual_testing/delete_book.gif)

- Find Book

![Find Book Test](./docs/images/manual_testing/find_book.gif)

- Book Details

![Book Details Test](./docs/images/manual_testing/book_details.gif)

- Favourites Page

![Favourites Page Test](./docs/images/manual_testing/favourites.gif)

- Contact Page

![Contact Page Test](./docs/images/manual_testing/contact.gif)

## Automated Testing
### Code Validation

#### HTML Validation
The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the `HTML`.

These are the results of the validation:

- Homepage
![Homepage HTML Validation](./docs/images/html_css_validation/homepage_html.png)

- Login Page
![Login Page HTML Validation](./docs/images/html_css_validation/login_html.png)

- Register Page
![Register Page HTML Validation](./docs/images/html_css_validation/register_html.png)

- Contact Page
![Contact Page HTML Validation](./docs/images/html_css_validation/contact_html.png)

- Find Book Page
![Find Book Page HTML Validation](./docs/images/html_css_validation/find_book_html.png)

- Add Book Page
![Add Book Page HTML Validation](./docs/images/html_css_validation/add_book_html.png)

- User Page (My Books Page)
![User Page (My Books Page) HTML Validation](./docs/images/html_css_validation/user_page_html.png)

- Book Details Page
![Book Details Page HTML Validation](./docs/images/html_css_validation/book_detail_html.png)

- Edit Book Page (Update Book)
![Edit Book Page HTML Validation](./docs/images/html_css_validation/edit_book_html.png)

- Delete Book Page
![Delete Book Page HTML Validation](./docs/images/html_css_validation/delete_book_html.png)

- User Favourites Page
![User Favourites Page HTML Validation](./docs/images/html_css_validation/favourites_html.png)

- User Profile Page
![User Profile Page HTML Validation](./docs/images/html_css_validation/user_profile_html.png)

- Update Profile Page
![Update Profile Page HTML Validation](./docs/images/html_css_validation/user_profile_update_html.png)

- 404 Page (Manual Insertion)
![404 Page HTML Validation](./docs/images/html_css_validation/404_html.png)

[Back to top ⇧](#table-of-contents)

#### CSS Validation
The [CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used for `CSS` code.

These are the results of the validation:

- Homepage CSS File
![Homepage CSS Validation](./docs/images/html_css_validation/homepage_css.png)

- General CSS File
![General CSS Validation](./docs/images/html_css_validation/style_css.png)

[Back to top ⇧](#table-of-contents)


The [JSHint JavaScript Code Quality Tool](https://jshint.com/) was used to validate the sites `JS` code.

- Contact JS File
![Contact JS Validation](./docs/images/js_validation/contact_js_validation.png)

- Find Book JS File
![Find Book JS Validation](./docs/images/js_validation/search_js_validation.png)

- Script JS File
![Script JS Validation](./docs/images/js_validation/script_js_validation.png)


#### Python Validation
For Python code, the [CI PEP8 online validator](https://pep8ci.herokuapp.com/) was used to validate the code.

Because there are so many, the developer includes here only the results of the validation of the `settings.py` file. All other Python files were validated and passed the test with same results.

- Settings.py File
![Settings.py Validation](./docs/images/python_validation/settings_py.png)

[Back to top ⇧](#table-of-contents)


### Lighthouse Validation
The [Lighthouse](https://developers.google.com/web/tools/lighthouse) tool was used to measure the performance of the website.

These are the results of the validation:

- Homepage

![Homepage Lighthouse Validation](./docs/images/lighthouse/home_lighthouse.png)

- Login Page

![Login Page Lighthouse Validation](./docs/images/lighthouse/login_lighthouse.png)

- Register Page

![Register Page Lighthouse Validation](./docs/images/lighthouse/register_lighthouse.png)

- Contact Page

![Contact Page Lighthouse Validation](./docs/images/lighthouse/contact_lighthouse.png)

- Find Book Page

![Find Book Page Lighthouse Validation](./docs/images/lighthouse/search_lighthouse.png)

- Add Book Page

![Add Book Page Lighthouse Validation](./docs/images/lighthouse/add_book_lighthouse.png)

- User Page (My Books Page)

![User Page (My Books Page) Lighthouse Validation](./docs/images/lighthouse/user_page_lighthouse.png)

- Book Details Page

![Book Details Page Lighthouse Validation](./docs/images/lighthouse/book_detail_lighthouse.png)

- Edit Book Page (Update Book)

![Edit Book Page Lighthouse Validation](./docs/images/lighthouse/edit_book_lighthouse.png)

- Delete Book Page

![Delete Book Page Lighthouse Validation](./docs/images/lighthouse/delete_book_lighthouse.png)

- User Favourites Page

![User Favourites Page Lighthouse Validation](./docs/images/lighthouse/favourites_lighthouse.png)

- User Profile Page

![User Profile Page Lighthouse Validation](./docs/images/lighthouse/user_profile_lighthouse.png)

- Update Profile Page

![Update Profile Page Lighthouse Validation](./docs/images/lighthouse/update_profile_lighthouse.png)

- 404 Page couldn't be tested with Lighthouse

[Back to top ⇧](#table-of-contents)

### Browser Validation
The website was tested with **pass** on the following browsers:
Google Chrome, Microsoft Edge, Mozilla Firefox, Opera, Safari, Vivaldi, Brave.
The website was tested with **pass** on the following devices:
- Laptop ThinkPad x270 on Linux Manjaro 3.0 Uranos
- Ipad Air 2 on iOS 16.7
- Iphone 12 on iOS 16.7
- Xiaomi Mi Note 11 Pro on Android 14.0.1

### User Testing
The website was tested by differen users, with different devices and browsers. The feedback was positive and the website was easy to use and navigate.
There were several suggestions for improvement, which were implemented in the future. The bugs discovered were fixed.

[Back to top ⇧](#table-of-contents)



