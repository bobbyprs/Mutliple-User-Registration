# Mutliple-User-Registration(Django)
The is the just like flipkart registration form where Customer form is different from Seller form so normally in amazon both customer and seller have same registration 
form in the outher words it uses only one user models but in our case it not possible so i have  used only one custom user model with two proxy user models

# For Customer Registration
  As a customer I want to register my self to the platform , so that I can access info specific to me. 
  
Given I am not a registered user 

When I provide following valid details 

- Full Name  (Mandatory)

- e-mail address (Mandatory)

- mobile number (Mandatory)

- Password (Mandatory)

- Repeat password (Mandatory)

Than The user should get a successfully registration message

And should be routed to login page

Given I am already registered user 

When user click on submit after providing the details

then user should get an error message stating that the user already registered with the given e-mail address.

****************************************************
# For Seller user Registration


Then the screen with following input should be presented

  - Name of the brand/shop 

  - Supervisor / Owner name

  - email id: 

  - Mobile number (Supervisor / Owner name)

  - Auto generated password

  - Category

 

Given all the tenant details are provided

When user user click on create button

Then e-mail should be sent to the e-mail id provided on step 1 with the instruction and details to login.


