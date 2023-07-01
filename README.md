# Locale

Locale is a developer tool for anyone who needs to know Nigeria, geographically at least. Locale's API shows you all of Nigeria's regions, 
states, and local government areas (LGAs). Locale is looking to be a very useful tool for the thousands of businesses building for Nigeria's 200M+ population size.

**Note**: Locale is still under development


### Usage
1. Visit [website](https://techystarr.pythonanywhere.com/) on your web browser


2. Create an account as an admin
    - Click "Auth" to reveal the authentication endpoints
    - Register with your preferred details


3. Sign in to your account
    - Input the details you registered with to generate a JWT token
    - Copy this access token without the quotation marks


4. Click on the "Authorize" button at the top right. Enter the JWT token prefixed with "Bearer" in the given format
    ```
    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlIj
    ```
    
5. Click "Authorize", then close the pop-up


6. Now authorized, you can use the endpoints by creating, viewing, updating and deleting both students and courses.


7. Click the 'Authorize' button, then logout to logout


## Testing Locally

Clone the repository


```console
git clone https://github.com/TechyStarr/Student-Management-API.git
```



Change the directory to the cloned folder

```console
cd student-mgt
```

Install the necessary dependencies to run the project

```console
pip install -r requirements.txt
```
Create a database from migration files 

```console
flask db migrate -m "your description"
```

```console
flask db upgrade
```
Run application

```console
flask run
```

or

```console
py runserver.py
```





## Available Endpoint

### Auth Endpoint
| ROUTE | METHOD | DESCRIPTION | AUTHORIZATION  | USER TYPE |  PLACEHOLDER | 
| ------- | ----- | ------------ | ------|------- | ----- |
|  `auth/signup` | _POST_ | It allows an admin to create an account  | Any | Any |  ---- | 
|  `auth/login` |  _POST_  | Generates an access and refresh token for user authentication | Any | Any | ---- | 
|  `auth/refresh` |  _POST_  | It is used to refresh expired tokens   | Authenticated | Any | ---- | 




### Admin Endpoint
| ROUTE | METHOD | DESCRIPTION | AUTHORIZATION  | USER TYPE |  PLACEHOLDER | 
| ------- | ----- | ------------ | ------|------- | ----- |
|  `admin/students` |  _GET_  | It allows the admin retrieve all registered students   | Authenticated | Admin | ---- |
|  `admin/students` |  _POST_  | It allows the admin register students   | Authenticated | Admin | ---- |
|  `admin/students/<student_id>` |  _GET_  | It allows the admin retrieve a student by id | Authenticated | Any | A student ID |
|  `admin/student/<student_id>` |  _DELETE_  | It allows the admin delete a student by id | Authenticated | Admin | A student ID |
|  `admin/courses` |  _POST_  | It allows the admin create courses   | Authenticated | Admin | ---- |
|  `admin/courses` |  _GET_  | It allows the admin retrieve registered courses   | Authenticated | Admin | ---- |
|  `admin/course/<course_id>` |  _DELETE_  | It allows the admin delete a course by id | Authenticated | Any | A course ID |
|  `admin/course/<course_id>` |  _PATCH_  | It allows the admin update a course by id | Authenticated | Any | A course ID |
|  `admin/students/<student_id>` |  _POST_  | It allows the admin register a student for a course  | Authenticated | Any | A student ID |
|  `admin/students/<student_id>/courses` |  _GET_  | The admin retrieves all courses a student is registered for   | Authenticated | ---- | A student ID |





### Students Endpoint
| ROUTE | METHOD | DESCRIPTION | AUTHORIZATION  | USER TYPE |  PLACEHOLDER | 
| ------- | ----- | ------------ | ------|------- | ----- |
|  `student/courses/<student_id>/scores` |  _GET_  | It allows the student retrieve their score and course details   | Authenticated | Student | A student ID |
|  `students/<student_id>/gpa` |  _GET_  | Calculate a student gpa score   | Authenticated | Student | A student ID |
|  `students/course/add_score` |  _PATCH_  | It allows student update profile | Authenticated | Student | ---- |



### Grades Endpoint
| ROUTE | METHOD | DESCRIPTION | AUTHORIZATION  | USER TYPE |  PLACEHOLDER | 
| ------- | ----- | ------------ | ------|------- | ----- |
|  `grades/student/courses/course_id` |  _PATCH_  | It allows the admin update student course details   | Authenticated | Admin | ---- |
|  `grades/student/student_id/courses` |  _GET_  | It allows the admin to retrieve all courses a student registered for   | Authenticated | Admin | ---- |
|  `grades/student/student_id/courses` |  _GET_  | It allows the admin to retrieve all courses a student is registered for   | Authenticated | Admin | ---- |

