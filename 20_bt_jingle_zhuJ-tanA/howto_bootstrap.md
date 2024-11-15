# how-to :: BOOTSTRAP
---
## Overview
Bootstrap is a very useful CSS styling tool with prebuilt display functions (components, utilities, layout, etc.) that save developers the time to write intensive CSS codes. This guide will demonstrate some core features of Bootstrap, including 

### Estimated Time Cost: 1 hr

### Prerequisites:

- Create a html file with a header and body
- Install Bootstrap via package manager or include via CDN (Content Delivery Network) inside html file

### Procedure:
1. You can install via package manager:

    `$ npm install bootstrap@5.3.3`

    `$ gem install bootstrap -v 5.3.3`

   OR
   
    Include via CDN (Place the `<link>` tag in the `<head>`):
    ```
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Bootstrap demo</title>
      </head>
      <body>
        <h1>Hello, world!</h1>
      </body>
    </html>
    ```
1. If you plan to use dropdowns, popovers, or tooltips, place the `<script>` tag for JavaScript bundle before `</body>`:
    ```
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
    ```

### Creating a Navbar
1. Open and close nav tags: `<nav class="navbar"></nav>`
2. Vertically align (or stack) the navbar by adding `navbar-expand{-sm|-md|-lg|-xl}` as a class
    - Adding a size after "expand" will specify smaller than which sizes the navbar will collapse
    - Excluding a size will always collapse the navbar
3. Open and close div tags in the nav tags to contain links : `<div class=collapse navbar-collapse"></div>`
    - Assigning the collapse class will specify what collapses
4. Open an ordered list with ul tags indide the div tags: `<ul class="navbar-nav"></ul>`
    - Adding a `me-auto` class will auto-adjust margins
5. Create list objects for the nav bar with li and hyperlink tags inside the ul tags: `<li class="nav-item"><a class="nav-link"></a></li>`
     - Add the active class to the page currently open
     - Adding the "dropdown" class to an "li" tag will enable dropdown options:
         ```
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
         ```
6. A disabled link can be included by adding a `disabled` class and toggling `aria-disabled`:
    ```
    <li class="nav-item">
      <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
    </li>
    ```
8. Add text between corresponding tags to label links
9. Create a Search bar and Search button:
    ```
    <form class="d-flex">
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
    ```
    
### Creating a grid
- Add `<div class="row"></div>` for all content that will be horizontally aligned together
- Add `<div class="col"></div>` for all content that will be vertically aligned
- Rows and columns can be put inside each other and vice versa
    - The broader class will take precedence
- Sizes can be added to rows and columns with `-{numeric size}`

### Creating Buttons
- Create button tags: `<button type="button" class="btn"></button>`
- There are pre-built buttons styles in Bootstrap, including:
    ```
    <button type="button" class="btn btn-primary">Primary Button</button>
    <button type="button" class="btn btn-secondary">Secondary Button</button>
    <button type="button" class="btn btn-success">Success</button>
    <button type="button" class="btn btn-danger">Danger</button>
    <button type="button" class="btn btn-warning">Warning</button>
    <button type="button" class="btn btn-info">Info</button>
    <button type="button" class="btn btn-light">Light</button>
    <button type="button" class="btn btn-dark">Dark</button>
    ```
- `-outline` can be added between `btn` and `-{style}` to only display an outlined button with no color filling
- The size of buttons can be adjusted by adding `btn-sm` or `btn-lg` as a class
- Buttons can be disabled by toggling `disabled`:  `<button type="button" class="btn " disabled>Button</button>`

### Creating a Card
- Create a div class for a card: `<div class="card"></div>`
- Create a div class for a header and body:
    ```
    <div class="card-header">Header</div>
    <div class="card-body"></div>
    ```
- Fill tags with desired content

### Creating a Table
- Create a table with table tags: `<table class="table"></table>`
- A border can be added to the table by adding the class `table-bordered`
- A caption be be provided to the table with the caption tags: `<caption></caption>`
- Create a thead class to house the headers of the table
- A theme can be given to the thead with a class
    - Example: `<thead class="table-dark">` will create a dark theme
- Create tr tags to hold horizontal elements of the table: `<tr></tr>`
- Use th tags to for header elements and td tags for body elements
    - Open and close `tbody` tags to house `tr` and `td` tags outside the first row 

### Creating a Form
- Create and close form tags: `<form></form>`
- Create div classes for each form item: `<div class="form-group"></div>`
- Inside the above class, create label and input tags to add a text label and a form respectively
- Assign the value to the `for` attribute in the label tag and the id attriubute in the input tag to the corresponding variable in an elsewhere file
- Add the `"form-control"` class to the input tags
- Assign text the the `placeholder` attribute in the input tag to display text in the empty form

  ```
    <form>
      <div class="form-group">
        <label for="formGroupExampleInput">Example label</label>
        <input type="text" class="form-control" id="formGroupExampleInput" placeholder="Example input">
      </div>
      <div class="form-group mt-2">
        <label for="exampleFormControlInput1">Email address</label>
        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
      </div>
      <div class="form-group mt-2">
        <label for="inputPassword2" class="sr-only">Password</label>
        <input type="password" class="form-control" id="inputPassword2" placeholder="Password">
      </div>
    </form>
  ```
    
### Resources
* [Bootstrap](https://getbootstrap.com)
 
---

Accurate as of (last update): 2024-11-14

#### Contributors:  
Amanda Tan, pd4  
Michelle Zhu, pd4
