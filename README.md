# Movie Ticket Booking System

A Django-based academic project for movie ticket booking with user authentication, seat selection, and booking management.

## Features

### User Features
- User registration and authentication
- Browse available movies
- View movie details and showtimes
- Interactive seat selection
- Book tickets
- View booking history

### Admin Features
- Manage movies, theaters, and showtimes
- Monitor bookings
- Generate reports
- Manage seat availability

## Technical Stack

- Django 5.2
- Bootstrap 5
- SQLite (default database)
- Pillow for image handling
- Django Crispy Forms

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```
   python manage.py runserver
   ```

## Project Structure

```
ticketit/
├── accounts/          # User authentication app
├── movies/            # Movie and booking management app
├── static/           # Static files (CSS, JS, images)
├── templates/        # HTML templates
└── ticketit/         # Project configuration
```

## Usage

1. Access the admin panel at `/admin` to manage movies and theaters
2. Regular users can register and login through the main interface
3. Browse movies and select showtimes
4. Choose seats and complete bookings
5. View booking history in user dashboard

## Contributing

This is an academic project. Please follow the standard Django coding style and add appropriate comments for clarity.

## License

This project is created for academic purposes. Feel free to use and modify according to your needs. 