### This is the Take Home Assignment for the Role of Backend Intern at GrowthX

## Objective:
To Create an assignment submission portal.

### Technology Used:
- 1.Database:
   - Use MongoDB as your database.
   - MongoDB Compass

- 2.Language and Framework:
   - Python
   - FastAPI

- 3.Testing:
   - Used Postman for Testing Client URls.
 
## How to SetUp this project locally and Test the Results.
- 1.Fork/Clone this repo:
   - `git clone https://github.com/AviGawande/GrowthX-Backend`
- 2.In the same directory create a virtual environment(venv):
   - Install dependencies if not. `pip install virtualenv`
   - Create a new Virtual.Env name myenv. `python -m venv myenv`
   - Activate the Virtual-Environment(myenv). `myenv\Scripts\activate`
- 3.CD into the project directory of clonned project:
   - `cd GrowthX-Backend`
   - Install the Requirements file for project:
      - `pip install -r requirements. txt `
- 4.Run this command on the terminal(ensure to activate the virtualenv and install the dependencies):
   - `uvicorn main:app --reload`
   - visit this url `http://127.0.0.1:8000/` on browser.
- 5.And your backend system is running locally.


  # Results:
  I have attached the snapshots of the each enpoint working successfully along with Postman Urls each.

  - 1.Register a New User:
     - Method: POST
     - URL: `http://localhost:8000/register`
     - Body: Select "Raw" and then "JSON" from the dropdown in the Body tab:
       ```
       {
       "username": "testuser",
       "password": "testpassword",
       "user_type": "user"
       }
       ```
     - ![Screenshot 2024-10-09 213906](https://github.com/user-attachments/assets/e76c5bb0-6b36-4521-b459-0c228ce042e9)
   
   - 2.Register a New Admin:
     - Method: POST
     - URL: `http://localhost:8000/register`
     - Body: Select "Raw" and then "JSON" from the dropdown in the Body tab:
       ```
       {
       "username": "testadmin",
       "password": "adminpassword",
       "user_type": "admin"
       }
       ```
     - ![Screenshot 2024-10-09 214040](https://github.com/user-attachments/assets/dab0b114-344b-4f82-aaf2-14abf1a51e45)
    
   - 3.Login for (User and Admin Both):
     - Method: POST
     - URL: `http://localhost:8000/login`
     - Auth:
         - Select the "Authorization" tab.
         - Choose "Basic Auth" from the dropdown.
         - Enter:
         - Username: `testuser` or `testadmin` (based on the account you want to test)
         - Password: `testpassword` or `adminpassword` (based on the account you want to test)
     - Login as User:![Screenshot 2024-10-09 214628](https://github.com/user-attachments/assets/d559eb64-74df-4b60-807c-f01de1b82a0b)
     - Login as Admin:![Screenshot 2024-10-09 214758](https://github.com/user-attachments/assets/7ca6779e-0557-483e-a2f2-037df10bc2ca)
 
   - 4.Upload an Assignment (as a user):
     - Method: POST
     - URL: `http://localhost:8000/upload`
     - Auth:
         - Use "Basic Auth" (enter `testuser` and `testpassword`).
     - Body: Select "Raw" and then "JSON" from the dropdown in the Body tab:
       ```
       {
          "task": "Complete Python assignment",
           "admin_username": "testadmin"
        }
       ```
     - ![Screenshot 2024-10-09 215032](https://github.com/user-attachments/assets/603c9518-dc84-4cf1-8282-e055baaf5d59)

       
   - 5.Get All Admins:
     - Method: GET
     - URL: `http://localhost:8000/upload`
     - Auth:
         - Use "Basic Auth" (enter `testuser` and `testpassword`).
     - Body: Select "Raw" and then "JSON" from the dropdown in the Body tab:
       ```
       {
          "task": "Complete Python assignment",
           "admin_username": "testadmin"
        }
       ```








     

### Type of Users:
   - 1.Users.
      - a. Register and log in.
      - b. Upload assignments.
   - 2.Admin.
      - a. Register and log in.
      - b. View assignments tagged to them.
      - c. Accept or reject assignments.
