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





     

### Type of Users:
   - 1.Users.
      - a. Register and log in.
      - b. Upload assignments.
   - 2.Admin.
      - a. Register and log in.
      - b. View assignments tagged to them.
      - c. Accept or reject assignments.
