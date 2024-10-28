# The Luxury Blog
Portfolio Project 4: Full-Stack Toolkit - Code Institute

**Disclaimer: This fictional project is intended solely for educational purposes and is not suitable for practical real-world usage other than academic assessment.**

View the deployed site at [https://the-luxury-blog.onrender.com/](https://the-luxury-blog.onrender.com/)

Important: Please note that Render.com has a feature that automatically pauses services when they are not in active use. As a result, it may take about a minute for the site to load.

Luxury Blog web application preview screenshot:

![Luxury Blog preview screenshot](readme/images/luxury-blog-preview.png)

## Agile Methodology

This project was planned using Agile project management through Epics, Descriptions, User Stories, Story Points, MoSCoW prioritization, Acceptance Criteria, and Tasks.

A Kanban board has been set up and used for this purpose, providing an organized overview. It can be accessed at: [https://github.com/users/linobollansee/projects/6](https://github.com/users/linobollansee/projects/6)

A screenshot of The Luxury Blog Kanban Board during active development phase usage:

![Luxury Blog Kanban Board](readme/images/luxury-blog-kanban-board.png)

### Epics

Epic 1: Plan and Design the Full-Stack Web Application using an MVC Framework
- Description: This epic focuses on planning and designing the Full-Stack application, ensuring adherence to Agile methodology, UX principles, and accessible design.
  - User Stories:
    - User Story 1.1: Design Front-End for a Data-Driven Web Application
    - User Story 1.2: Plan Agile Development Using an Agile Tool
    - User Story 1.3: Ensure Code Quality Standards

Epic 2: Implement Data Model and Application Features
- Description: This epic focuses on building the core application features, including database models, CRUD functionality, and business logic.
  - User Stories:
    - User Story 2.1: Build the Data Model and Database Structure
    - User Story 2.2: Implement CRUD Functionality
    - User Story 2.3: Handle Notifications for Data Changes

Epic 3: Authentication and Authorization
- Description: This epic addresses user authentication and permissions for accessing the application.
  - User Stories:
    - User Story 3.1: Implement Role-Based Authentication
    - User Story 3.2: Secure Restricted Content

Epic 4: Testing the Full-Stack Web Application
- Description: This epic focuses on ensuring that the application is thoroughly tested, both manually and automatically.
  - User Stories:
    - User Story 4.1: Implement Manual and Automated Tests

Epic 5: Version Control and Documentation
- Description: This epic ensures proper version control using Git, and documentation for the codebase and repository.
  - User Stories:
    - User Story 5.1: Maintain Version Control with Git
    - User Story 5.2: Document the Development Process

Epic 6: Deploy Application to Cloud
- Description: This epic covers deploying the application to a cloud platform and ensuring the final version is secure and matches the development version.
  - User Stories:
    - User Story 6.1: Deploy the Application to a Cloud Platform
    
Epic 7: Apply Object-Oriented Principles
- Description: This epic focuses on the use of object-oriented programming concepts within the project.
  - User Stories:
    - User Story 7.1: Design Efficient Models Using OOP

Epic 8: Enhance User Experience with Advanced Features
- Description: This epic focuses on delivering extra features to improve the overall experience for the users, including social sharing, customizable UI, and advanced filtering, beyond the basic project requirements.
  - User Stories:
    - User Story 8.1: Enable Social Media Sharing for User Content
    - User Story 8.2: Customize Dashboard Layout
    - User Story 8.3: Advanced Filtering and Search Options
    - User Story 8.4: Multi-Language Support

### User Stories

Please read this section thoroughly, as it includes important and comprehensive information on how the User Stories and their Tasks were accomplished for this project.

User Story 1.1: Design Front-End for a Data-Driven Web Application (Must Have, Story Points: 5)
- Description: As a user, I want a user-friendly front-end that follows accessibility guidelines and UX principles so that I can easily interact with the application.
  - Acceptance Criteria:
    - Front-end meets UX and accessibility guidelines.
    - Wireframes, mockups, and diagrams are documented.
  - Tasks:
    - Create wireframes and mockups for the front-end design.
    - Design HTML templates with consistent structure.
    - Implement CSS for responsive design.
    - Review and validate the front-end design against accessibility standards.
  - How Tasks were respectively completed:
    - Balsamiq software was used to create the wireframes, and web browser screenshots were taken for the mockups.
    - The {% extends 'base.html' %} tag was used to create a consistent structure throughout the Django templates by inheriting the base layout.
    - The Bootstrap Framework with predefined grid classes with built-in responsive design was used to implement CSS for responsive design.
    - Google Lighthouse was utilized to assess and verify the front-end design's compliance with accessibility standards.

User Story 1.2: Plan Agile Development Using an Agile Tool (Must Have, Story Points: 8)
- Description: As a developer, I want to plan and track all tasks and user stories in an Agile tool so that I can manage the project efficiently.
  - Acceptance Criteria:
    - All user stories, epics, and tasks documented in the Agile tool.
  - Tasks:
    - Set up an Agile tool for task tracking.
    - Document all user stories, epics, and tasks in the tool.
    - Create a project board with priorities.
  - How Tasks were respectively completed:
    - A new GitHub project was started to be used as an Agile tool.
    - GitHub project issues were created to document user stories, epics, and tasks.
    - GitHub project labels with MoSCoW criteria were applied to create a project board with priorities.

User Story 1.3: Ensure Code Quality Standards (Must Have, Story Points: 3)
- Description: As a developer, I want the code to conform to PEP8 and validated HTML/CSS/Javascript standards so that the application maintains high-quality and consistent coding practices.
  - Acceptance Criteria:
    - Python code conforms to PEP8 standards.
    - HTML, CSS, Javascript code are validated.
  - Tasks:
    - Implement a code review process.
    - Use tools for Python, HTML, CSS, Javascript validation.
  - How Tasks were respectively completed:
    - The list of files to be checked was prepared, including all `*.html`, `*.css`, `*.js`, `*.py` files essential to this project.
    - Python code was checked with the Code Institute linter, HTML with the W3C Markup Validation Service, CSS with The W3C CSS Validation Service, Javascript with the JSHint JavaScript Code Quality Tool.

User Story 2.1: Build the Data Model and Database Structure (Must Have, Story Points: 5)
- Description: As a developer, I want to implement a database model that supports the application’s business logic and data manipulation needs.
  - Acceptance Criteria:
    - A well-structured data model exists for storing and retrieving data.
    - At least one custom model is implemented.
  - Tasks:
    - Design a database schema that fits the project domain.
    - Implement the database model.
    - Create migrations to initialize the database structure.
  - How Tasks were respectively completed:
    - An Entity-Relationship Diagram (ERD) was created to design a database schema that fits the project domain.
    - Database models were implemented through `models.py` files with field declarations in app folders.
    - Running the following commands in the terminal: `python manage.py makemigrations` and `python manage.py migrate` initialized the database structure. It executes the SQL commands through the migration files.

User Story 2.2: Implement CRUD Functionality (Must Have, Story Points: 5)
- Description: As a user, I want to create, update, read, and delete data so that I can manage my information within the application.
  - Acceptance Criteria:
    - All CRUD actions are functional.
    - Data changes are immediately reflected in the UI.
  - Tasks:
    - Build the back-end logic for CRUD operations.
    - Design forms for data input with validation.
    - Ensure changes to data are reflected on the front-end.
  - How Tasks were respectively completed:
    - Designing the back-end logic for CRUD operations involved defining `models.py` files to represent data structures, creating `views.py` files to handle the logic for displaying and processing data, `forms.py` for user input validation, setting up `urls.py` files to map requests to the appropriate views, and creating templates to render the HTML presentation.
    - The forms.py files were created and include a Meta class with attributes designed to validate data input.
    - The messages framework was imported with `from django.contrib import messages` in the views files in order to display notifications to users when data changes are made.