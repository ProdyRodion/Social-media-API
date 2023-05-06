# Social Media API
This Django REST framework-based API serves as a RESTful interface for a social media platform. It empowers users to create profiles, follow other users, create and retrieve posts, manage likes and comments, and engage in various fundamental social media activities.
## How to run
```shell
git clone https://github.com/ProdyRodion/Social-media-API.git
cd Social_media_API
python3 -m venv venv
source venv/bin/activate # for linux or macOS
venv\Scripts\activate # for Windows
python manage.py runserver
```

 The API will be available at http://localhost:8000/.
 
### Features

<ul>
<li><strong>Authentication:</strong> Implement a secure method of accessing API endpoints by utilizing JWT token-based authentication.</li>
<li><strong>Post management:</strong> Enable comprehensive CRUD functionality to handle posts, including their creation, retrieval, updating, and deletion. Additionally, provide the ability to filter posts based on their title and content.</li>
<li><strong>User management:</strong> Allow users to register, modify their profile details (such as biography and avatar), and search for other users using their usernames.</li>
<li><strong>API documentation:</strong> Utilize Swagger UI to automatically generate interactive API documentation, which facilitates developers in effortlessly exploring and testing the API's endpoints.</li>
</ul>

## API Endpoints
The following endpoints are available:
### User Registration, Authentication and Following
- api/user/register: Register a new user by providing an email and password.
- api/user/token: Receive a token
- api/user/token/refresh/: Refresh a token
- api/user/token/verify/: Verify a token
- api/user/me/: User information
- api/user/<int:pk>/follow/: Follow/Unfollow another user by user ID.

### Documentations
- api/doc/swagger/: Documentations using Swagger

![img.png](readme%20image%2Fimg.png)