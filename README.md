
<a name="readme-top"></a>

<!--
*** Thank you for checking out and/or using this README Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "improvement".
*** Adapt appropriately and replace all placeholder text with accurate information relating to your project.
*** Do not forget to take the asset folder along with the README.md file so that the icons link will not be broken.
*** Remove all *N/B* comments!
*** Don't forget to give the project a star!
-->

<!-- PROJECT LOGO (N/B: Replace logo url and image to match your project)-->
<br />
<div align="center">
  <a href="https://github.com/IkennaEgwim/README-Template">
    <img src="./assets/images/logo.png" alt="Project Logo" width="80" height="80">
    </div>
  </a>

  <h1 align="center">NURISHED</h1>

  <p align="center">
 This documentation is a detailed step-by-step breakdown of the planning, design, development, testing & validation, and deployment of Nurished, the ultimate online platform for culinary enthusiasts. Built with Django, HTML, CSS and PostgreSQL, Nurished is designed to create a vibrant community where every recipe is a new adventure.
    <br />
    <br />
    <a href="https://github.com/path-to-readme-file"><strong>Explore the docs »</strong></a>
    <br />
    <br />

<!-- TABLE OF CONTENTS -->

Table of Contents

<!-- INTRODUCTION SECTION -->

  <details>
  <summary><a href="#introduction">SECTION 1: INTRODUCTION</a></summary>
        <li><a href="#about-the-project">About The Project</a>
        <li><a href='#ux'>User Experience (UX)</a></li>
        <li><a href='#user-stories'>User Stories</a></li>
        <li><a href="#technology-stack">Technology Stack</a></li>
        <li><a href="#languages-frameworks-libraries">Languages, Frameworks and Libraries</a></li>
        <li><a href="#management-and-development">Project Management and Development Approach</a></li>
    </details>
    <!-- PROJECT SETUP SECTION -->
    <details>
    <summary><a href="#project-setup">SECTION 2: PROJECT SETUP</a>
</summary>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
    </details>
    <details>
    <summary><a href="#features-and-structure">SECTION 3: PROJECT FEATURES AND STRUCTURE</summary>
    <li><a href="#features">Features</a></li>
        <li><a href="#structure-and-navigation">Structure and Navigation</a></li>
        <li><a href="#wireframes">Wireframes</a></li>
         <li><a href="#design-and-styling">Design and Styling</a>
        <ol>
            <li><a href="#design">Design</a></li>
            <li><a href="#color">Color</a></li>
            <li><a href="#font">font</a></li>
            <li><a href="#media">media</a></li>
        </ol>
        </li>
</details>
<details>
<summary><a href="#testing-and-validation">SECTION 4: TESTING AND VALIDATION</a>
</summary>
    <li><a href="#testing">Testing</a></li>
        <li><a href="#validation">Validation</a>
        <ol>
        <li><a href="#html-validator-report">HTML Validator Report</a></li>
        <li><a href="#css-validator-report">CSS Validator Report</a></li>
        </ol>
        </li>
        <li><a href="#user-story-testing">User Story Testing</a></li>
        <li><a href="#bugs-and-issues">Bugs and Issues</a></li>
</details>
<details>
<summary><a href="#deployment-and-credits">SECTION 5: DEPLOYMENT AND CREDITS</a>
</summary>
        <li><a href="#final-product">Final Product</a></li>
        <li>
            <a href="#credits">Credits</a>
            <ol>
                <li><a href="#template">Template</a></li>
                <li><a href="#content">Content</a></li>
                <li><a href="#media2">Media</a></li>
            </ol>
        </li>
<li><a href="#acknowledgments">Acknowledgments</a></li>
<li><a href="#contact">Contact</a></li>
</details>

<!-- INTRODUCTION -->

#

<section>
<h1 id="introduction">SECTION 1: INTRODUCTION </h1>

This section contains summary information about the project, the user expections and tools used in building this solution.

<h2 id="about-the-project">About The Project</h2>

<p align="center"><a href="https://path-to-deployed-site.com"><strong>Nurished</strong></a></p>

<a href="https://github.com/scientistigwe/README-Template">
<img src="./assets/images/screenshot.png" alt="Product Screenshot" width="600" height="600">
</a>

<h2 id="ux">User Experience (UX)</h2>

**Nurished**is an innovative online platform designed to bring together a vibrant community of culinary enthusiasts. The primary goal of Nurished is to allow users to discover, share, and discuss a wide variety of recipes tailored to their dietary preferences, cuisines, and cooking skills. Users can explore new recipes and contribute their own culinary creations, complete with detailed instructions and ingredient lists.

Key features of the project that makes it unique includes:

- Comprehensive Recipe Management: Nurished offers a robust system for users to upload, edit, delete, and manage their recipes, providing a flexible and user-friendly experience.

- Advanced Search and Filter Options: The platform’s advanced search and filtering capabilities make it easy for users to find recipes that match their specific dietary preferences, ingredients, and cooking skill levels.

- Educational Resources: Access to ingredient substitutions and cooking tips helps users improve their culinary skills and adapt recipes to their needs, enhancing the overall cooking experience.

- Organized Recipe Collections: Users can organize their saved recipes into collections (e.g., Breakfast, Desserts) for easier access and management, helping them keep their favorite recipes neatly categorized.

- Personalized Content: From weekly newsletters to personalized feeds, Nurished ensures that users receive content tailored to their interests and preferences.
  
You can view the deployed website [here](https://nurished-0e1f46f5e548.herokuapp.com/)

<h2 id="user-stories">User Stories</h2>

- As a user, I want to create a profile so that I can manage my recipes and interact with the community.
- As a user, I want to upload my own recipes, including ingredients, preparation steps, cooking time, and serving size so that I can share my culinary creations with others.
- As a user, I want to search for recipes based on ingredients, cuisine, dietary preferences, cooking time, and difficulty level so that I can find recipes that suit my needs.
- As a user, I want to save my favorite recipes to my profile so that I can easily find and revisit them later.
- As a user, I want to view ratings and reviews for a recipe so that I can determine if it’s worth trying.
- As a user, I want to rate recipes I have tried so that I can share my opinion and help others decide if they want to try the recipe.
- As a user, I want to write reviews for recipes I have tried so that I can provide detailed feedback to the recipe creator and other users.
- As a user, I want to follow other users so that I can see their new recipes and updates in my feed.
- As a user, I want to comment on recipes to ask questions or share tips with the recipe creator and other users.
- As a user, I want to edit my recipes after uploading so that I can make corrections or improvements.

<h2 id="technology-stack">Technology Stack</h2>
This subsection outlines the technologies, frameworks, libraries, and tools used in the development of this project. It provides insight into the foundational components that power "**Nurished**". Add-ons ad plugins are captured in the acknowledgements subsection.

<h2 id="languages-frameworks-libraries">Languages, Frameworks and Libraries</h2>

- <img src="./assets/icons/html5.svg" width="20px" align="top"><a href="https://en.wikipedia.org/wiki/HTML5"> HTML5</a> - Used for designing the structure of the project.

- <img src="./assets/icons/css3-alt.svg" width="20px" align="top"><a href="https://en.wikipedia.org/wiki/CSS"> CSS3</a> - Used for styling the project.

- <img src="./assets/icons/Django.png" width="20px" align="top"><a href="https://djangoproject.com/"> Django</a> - Provides the Python framework used for the project development.

- <img src="assets/img/google font.png" width="20px" align="top"><a href="https://fonts.google.com/"> Google Fonts</a> - Provides all of the fonts for this website.

- <img src="./assets/icons/font_awesome.png" width="20px" align="top"><a href="https://fontawesome.com/"> Font Awesome</a> - Used for the site icons.

- <img src="./assets/icons/github.png" width="20px" align="top"><a href="https://github.com/IrisSmok"> Github</a> - Used to store the project code.

- <img src="./assets/icons/gitpod.png" width="20px" align="top"><a href="https://www.gitpod.io/"> Gitpod</a> - An IDE Used for coding.

- <img src="./assets/icons/balsamiq.png" width="20px" align="top"><a href="https://balsamiq.com/"> Balsamiq</a> - Used to create site wireframes.

- <img src="./assets/icons/shutterstock.png" width="20px" align="top"><a href="https://www.shutterstock.com/home"> Shutterstock</a> and <img src="./assets/icons/unsplash.png" width="20px" align="top"><a href="https://unsplash.com/"> Unsplash photo</a> - Used for all images on the website.

- <img src="./assets/icons/responsive-devices.png" width="20px" align="top"><a href="http://ami.responsivedesign.is/"> Am I Responsive</a> - Used to check if the site is responsive on different screen sizes.

- <img src="./assets/icons/IMG2GO.png" width="20px" align="top"><a href="https://www.img2go.com/compress-image#j=f26cc008-23b4-4d4e-9934-96877fa9a7e7"> IMG2GO</a> and <img src="./assets/icons/Tiny_PNG.png" width="20px" align="top"><a href="https://tinypng.com/"> Tiny PNG</a> - Used to help compress the images.

- <img src="./assets/icons/bootstrap.png" width="20px" align="top"><a href="[Bootstrap-url]"> Bootstrap</a> - Used for building responsive and mobile-first websites and web applications.

<h2 id="management-and-development">Project Management and Development Approach</h2>


This project was implemented using the Agile Manifesto methodology. Below are the ways this project adhered to the 4 core values and 12 core principles of the aforementioned method:

<strong>Four Values of the Agile Manifesto:</strong>

- Vision 1: Customer collaboration over contract negotiation: The Team held **16** Hurdles through Slack Platform, ensuring alignment with user needs and prioritizing features through user story mapping.

<p align="center"><strong>A screenshot of a one of the team's huddles through slack.</strong></p>
<img src="assets/img/meeting screenshot.jpg" alt="Screenshot of the team's huddle" width="600" height="100%">
<br>
<br>

- Vision 2: Responding to change over following a plan: Throughout the project, the team managed
  [![GitHub issues](https://img.shields.io/github/issues-closed/Diana-is-Coding/R-P-S)](https://github.com/Diana-is-Coding/R-P-S/issues) + [![GitHub issues](https://img.shields.io/github/issues/Diana-is-Coding/R-P-S)](https://github.com/Diana-is-Coding/R-P-S/issues) GitHub issues, adapting to changing requirements and feedback iteratively.

- Vision 3: Working software over comprehensive documentation: We achieved **16 story points** across **1 sprint**, emphasizing the focus on delivering functional software increments.
<p align="center"><strong>A screenshot of Github activities ilustrating collaborative environment.</strong></p>
<p align="center"><strong>A screenshot of Kanban Board.</strong></p>
<img src="assets/img/kanban-board.PNG" alt="Screenshot of the team's huddle" width="600" height="100%">
<br>
<br>

- Vision 4: Individuals and interactions over processes and tools: Daily interactions on GitHub led to **29 commits**, fostering collaboration and knowledge sharing among team members.

<br>
<br>

<strong>Twelve Principles of the Agile Manifesto</strong>

- Satisfy the customer: Held regular meetings to ensure alignment with user stories.
- Deliver working software: Prioritized delivering functional increments in each sprint, allowing for early feedback.
- Welcome changing requirements: Maintained open communication channels and adapted plans iteratively.
- Collaborate daily: Conducted daily standup, catchup and stand-down to facilitate collaboration and problem-solving.
- Face-to-face conversation: Utilized over 15 virtual meetings through slack huddle to enhance clarity and understanding.
- Motivated individuals: Empowered team members through skill development and recognition.
- Measure progress through working product: Evaluated progress based on delivered functionality in each sprint.
- Promote sustainable development: Prioritized sustainability practices to ensure long-term success.
- Simplicity is essential: Used MoSCoW prioritization and focused on MVP delivery to avoid unnecessary complexity.
- Continuous attention to technical excellence: Adopted show and tell technique to ensure all team members learn while collaborating.
- Self-organizing team: Encouraged autonomy and collaboration within the team.
- Regular reflection on continuous improvement: Conducted regular retrospectives to identify areas for improvement.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- PROJECT SETUP -->

#

<h1 id="project-setup">SECTION 2: PROJECT SETUP</h1>

In this section, a detailed account of all requirements needed for Quid Pro to be setup and running. It also includes installation instructions and a link to all necessary documentations for these tools.

<h2 id="prerequisites">Prerequisites</h2>

Quid Pro does not rely on any external dependencies or services.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#

<h1 id="features-and-structure">SECTION 3: PROJECT FEATURES AND STRUCTURE</h1>

This section encompasses the various elements and functionalities aimed at enhancing the user experience and achieving the goals of Nurished. It outlines the key features and structural components intended to provide users with a seamless and informative journey through the platform.

<h1 id="features">Features</h1>

Nurished is packed with several key features that make it a unique. Here are the main features that define the Nurished experience:

### 1. User Profiles:

- Users can create and customize profiles to manage recipes and interact with the community.
- Profile customization includes adding a picture and bio for personalization.

### 2. Recipe Management:

- Upload, edit, and delete recipes with detailed information on ingredients, preparation steps, cooking time, and serving size.

### 3. Search and Filter:

- Advanced search capabilities allow users to find recipes based on ingredients, cuisine, dietary preferences, cooking time, and difficulty level.
- Filters enable quick navigation through search results.

### 4. Recipe Interaction:

- Save favorite recipes for easy access.
- Organize saved recipes into collections like Breakfast or Desserts.
- Rate and review recipes to share feedback and help others decide on recipes to try.
- View ratings and reviews to assess recipe popularity and quality.

### 5. Social Features:

- Comment on recipes to engage with creators and other users.
- Follow other users to stay updated on their new recipes and activities.
- Personalized user feed showcasing updates from followed users.

### 6. Additional Features:

- Subscribe to a weekly newsletter featuring new and popular recipes.
- Share recipes via social media platforms directly from the site.
- Report inappropriate content to maintain a positive community environment.
- Access ingredient substitutions and cooking tips to enhance culinary skills.

<h2 id="structure-and-navigation">Structure and Navigation</h2>
- **Project Structure**

### 1.  Backend:

- Built with Django, handling server-side logic, database management (PostgreSQL), and user authentication.
- Utilizes Django REST Framework for creating APIs.

### 2. Frontend:

-  Developed without React for a dynamic and responsive user interface.
-  UI components designed using Bootstrap for a visually appealing experience across devices.

### 3. Deployment:

-  Deployed on Heroku for scalability and accessibility.
-  Uses SQLite PostgreSQL for database storage.

- **File Organisation**

  - The files where structured into folders and clustered based on functionality. Also file naming convention that reflects the functions of the conetent of the file was adopted.

<h2 id="wireframes">Wireframes</h2>

### _File Organisation Tree_

<p align="center">
<img src="assets/img/New Wireframe 1.png" width="600" height="700">
</p>

### _Home Page_

<p align="center">
<img src="assets/img/New Wireframe 2.png" width="600" height="700">
</p>

<img src="assets/img/New Wireframe 3.png" width="600" height="900">
</p>

### _Mobile View - Home Page_

<p align="center">
<img src="assets/img/New Wireframe mobile1.png" width="400" height="1000">
</p>

<h2 id="design-and-styling">Design and Styling</h2>

<h3 id="design">Design</h3>

**Nurished** provides a comprehensive platform for culinary enthusiasts to explore, share, and discuss recipes. With a focus on user-friendly features like robust recipe management, advanced search options, and interactive social capabilities, Nurished fosters a vibrant community centered around culinary creativity and discovery.

<h3 id="color">Color</h3>

- #dac4fb (Purple) - We chose this color to have a welcominng background.

<h3 id="font">Font</h3>

- main font: Reddit Mono
- Secondary font - Monospace


<p align="right">(<a href="#readme-top">back to top</a>)</p>

#

<h1 id="testing-and-validation">SECTION 4: TESTING AND VALIDATION</h1>
- In this section, the functionalities of the final product was tested and validated to ensure consistency with user stories.
<h2 id="testing">Testing</h2>

- **Browser Compatibility Testing:** Ensured compatibility with Chrome, Opera, Microsoft Edge, and Firefox desktop browsers.

- **Responsiveness Testing:** Utilized Chrome Developer Tools to verify responsiveness across multiple devices: Desktop, Laptop, Moto G4, Galaxy S5, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPad, iPad Pro, Galaxy Fold

h2 id="validation">Validation</h2>

The W3C Markup Validator and W3C CSS Validator Services were used to check my code for syntax errors in this project.

- [HTML W3C Validator](https://validator.w3.org/#validate_by_input): I checked each page by direct input method on HTML validator site.

<p align="center">
<img src="assets/img/html_check.PNG" width="600" height="100%">
</p>

- [CSS W3C Validator](https://jigsaw.w3.org/css-validator/): I checked each page by direct input method on HTML validator site. No error or warning message was encountered following this test.

<p align="center">
<img src="assets/img/css-check.PNG" width="600" height="100%">
</p>



<h3 id="html-validator-report">HTML Validator Report</h3>

- No error or warning message was encountered following this test.
- We did have some errors originaly but we fixed them as it was as simple as "change image to img"

<h3 id="css-validator-report">CSS Validator Report</h3>

- No error or warning message was encountered following this test.


#

<h2 id="deployment-and-credits">SECTION 5: DEPLOYMENT AND CREDITS</h2>

-In this section, the tested and validated product will be deployed and external resources used during this exercise will be mentioned.

<h2 id="final-product">Final Product</h2>

- The website is live and can be seen on https://nurished-0e1f46f5e548.herokuapp.com/

### _Home Page on various screens_

<p align="center">
<img src="assets/img/responsive-home.PNG" width="600" height="100%">
</p>

- Add images of various sections of the final product as above.

<h2 id="credits">Credits</h2>

<h3 id="template">Template</h3>

- This template was adopted and adapted from README.md templates published by <a href="https://github.com/IkennaEgwim/README-Template" alt="Github page of Ikenna Egwim" target="_blank">Ikenna Egwim</a>, <a href="https://github.com/Iris-Smok/Vannas-Beauty-Salon_PP1" alt="Github page of Iris Smok" target="_blank">Iris Smok</a> and <a href="https://github.com/othneildrew/Best-README-Template" alt="Github page of Othneil Drew" target="_blank">Othneil Drew</a>.

<h3 id="content">Content</h3>

- All content was written by **Ikenna Egwim**.


<h3 id="media2">Media</h3>

- All images were taken from [Shutterstock](https://www.shutterstock.com/home) and [Unsplash photo](https://unsplash.com/)

<!-- ACKNOWLEDGMENTS -->
<h2 id="acknowledgments">Acknowledgments</h2>

Use this space to list individuals, groups or resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [GitHub Pages](https://pages.github.com)
- [Font Awesome](https://fontawesome.com)

<!-- CONTACT -->

<h2 id="contact">Contact</h2>

- Ikenna Egwim - [Email Address](egwimik@gmail.com); 

- Safi Hasan - [Email Address](egwimik@gmail.com);

- Diana Labode - [Email Address](egwimik@gmail.com);

- Nidhal Zarrad  - [Email Address](egwimik@gmail.com); 

- Project Link: [https://github.com/NZDevelopment/Nurished)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
</section>
