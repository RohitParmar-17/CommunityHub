# CommunityHub

## Overview
CommunityHub is a web platform built using Django that offers a comprehensive space for users to explore blogs, forums, and an integrated marketplace. It enables users to browse through shared ideas, discussions, and available products within a community-driven environment. Users cannot add their own content but can view existing blogs, forums, and marketplace listings.

## Screenshots

<img src="screenshots/home.png" alt="Home Page" width="100%">

## Features
- **Blogs**: Users can read blog posts on various topics.
- **Forums**: View interactive discussion boards where knowledge is shared.
- **Marketplace**: Browse products and services listed by admins.
- **User Authentication**: Secure login and signup system for personalized browsing.
- **Admin Dashboard**: Manage users, content, and transactions efficiently.

## Tech Stack
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite / PostgreSQL

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Virtual Environment (optional but recommended)

### Steps to Run Locally
1. **Clone the Repository**
   ```sh
   git clone https://github.com/RohitParmar-17/CommunityHub.git
   cd CommunityHub
   ```
2. **Create and Activate Virtual Environment (Optional)**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run Migrations**
   ```sh
   python manage.py migrate
   ```
5. **Start the Development Server**
   ```sh
   python manage.py runserver
   ```
   The app will be available at `http://127.0.0.1:8000/`

## Deployment
To deploy the project:
1. **Collect Static Files**
   ```sh
   python manage.py collectstatic
   ```
2. **Deploy on Platforms like Heroku, AWS, or DigitalOcean**
   - Use `gunicorn` for production-ready deployment.
   - Configure `settings.py` for production environment.

## Contributing
- Fork the repository
- Create a new branch (`git checkout -b feature-branch`)
- Make your changes and commit (`git commit -m "Added new feature"`)
- Push to the branch (`git push origin feature-branch`)
- Open a pull request

## Contact
For any issues or suggestions, feel free to reach out:
- **Email**: rohitghost5050@gmail.com

