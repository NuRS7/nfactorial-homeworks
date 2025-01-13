from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from typing import List, Optional

app=FastAPI()


cars=[
    {"id": 1, "name": "Mercedes Maybach", "year": "2025"},
    {"id": 2, "name": "Toyota Corolla", "year": "2020"},
    {"id": 3, "name": "Honda Accord", "year": "2018"},

]

users=[
    {"id": 1, "email": "test@test.com", "first_name": "Nursultan", "last_name": "Yerbakytuly", "username": "deadly_knight95"},
    {"id": 2, "email": "Zhana.salamanova@gmail.com", "first_name": "Zhanna", "last_name": "Salamanova", "username": "jane_doe"},
    {"id": 3, "email": "john.doe@example.com", "first_name": "John", "last_name": "Doe", "username": "john_doe"},

]



@app.get("/cars", response_model=List[dict])
def get_cars(page: int = 1, limit: int = 10):
    start=(page - 1) * limit
    end=start + limit
    return cars[start:end]



@app.get("/cars/{car_id}", response_model=dict)
def get_car_by_id(car_id: int):
    car=next((car for car in cars if car["id"] == car_id), None)
    if not car:
        raise HTTPException(status_code=404, detail="Not found")
    return car



@app.get("/users", response_class=HTMLResponse)
def get_users(page: int = 1, limit: int = 10):
    start=(page - 1) * limit
    end=start + limit
    paginated_users=users[start:end]

    html_content="""
    <html>
    <head>
        <title>Users</title>
    </head>
    <body>
        <table border="1">
            <tr>
                <th>Username</th>
                <th>Full Name</th>
            </tr>
    """
    for user in paginated_users:
        html_content+=f"""
            <tr>
                <td>{user['username']}</td>
                <td><a href="/users/{user['id']}">{user['first_name']} {user['last_name']}</a></td>
            </tr>
        """
    html_content+="""
        </table>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/users/{user_id}", response_class=HTMLResponse)
def get_user_by_id(user_id: int):
    user=next((user for user in users if user["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")

    html_content=f"""
    <html>
    <head>
        <title>{user['username']}</title>
    </head>
    <body>
        <h1>User Details</h1>
        <ul>
            <li>ID: {user['id']}</li>
            <li>Email: {user['email']}</li>
            <li>First Name: {user['first_name']}</li>
            <li>Last Name: {user['last_name']}</li>
            <li>Username: {user['username']}</li>
        </ul>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
