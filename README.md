🚗 Real-World Car Rental Web Application — Full Project Description

The Car Rental WebApp is a full-stack, production-grade Django application designed to manage car listings, bookings, user authentication, payments (optional), and admin operations.
This project closely simulates a real-world booking platform, integrating modern technologies such as PostgreSQL, OAuth authentication, Bootstrap, and Heroku deployment.

🧩 Project Overview

The Car Rental WebApp enables users to browse available cars, search by categories, view detailed car specifications, create accounts, log in through social media, and rent cars online.
Administrators have complete control over inventory, bookings, and user data through a customized Django admin panel.

This project demonstrates skills in backend development, database management, frontend integration, DevOps, authentication, and cloud deployment.

🛠 Tech Stack
Backend

Django 4+

Python 3.x

Django ORM

PostgreSQL

Frontend

HTML5 / CSS3

Bootstrap 5 Template (UI Theme)

JavaScript

Authentication

Django Authentication System

Google OAuth

Facebook OAuth

Deployment

Heroku Platform

Gunicorn

Whitenoise (static files)

Developer Tools

Git & GitHub

Virtual Environments (venv)

PostgreSQL CLI

Django Admin Customization

🧱 Key Functionalities Explained in Detail
1️⃣ Virtual Environment Setup

A separate Python environment is created using:

python -m venv env


Why?
To isolate project dependencies and ensure a clean development workflow.

2️⃣ Creating Django Project & Apps

A modular architecture:

Main apps

pages – manages static pages like home, about, services

cars – car listings, filtering, and car detail pages

accounts – registration, login, profile, social auth

contacts – rental requests, email notifications

Apps follow Django's MTV architecture.

3️⃣ Integrating Git & GitHub

Project tracked using Git

Pushed to GitHub for version control

Branching strategy implemented (main → feature branches)

4️⃣ Bootstrap Admin Template Integration

A professional car-rental Bootstrap UI is integrated into Django’s template engine.

Features:

Responsive navbar

Hero sliders

Car cards

Testimonials

Contact forms

All static assets (CSS, JS, images) are configured inside /static/.

5️⃣ PostgreSQL Database Setup

Database schema includes:

Tables

Users

Cars

Specifications (fuel type, gearbox, mileage)

Booking/Rental Requests

Testimonials

Admin user metadata


6️⃣ Static & Media File Handling

Static = CSS, JS, images

Media = Uploaded car photos

Django’s storage setup handles:

Uploading multiple car images

Secure access to uploaded files

7️⃣ Django Admin Customization

Admin panel is enhanced to look professional:

✔ Branded headers
✔ Car management with image previews
✔ User management
✔ Search fields
✔ Filters
✔ Custom list displays

8️⃣ Search Functionality

Users can search cars based on:

Car brand

Car model

City

Year

Price

Fuel type

Backend: Django QuerySet filters
Frontend: Dynamic search forms

9️⃣ Pagination

Large car lists are paginated


🔟 Django Messages (Success & Error Alerts)

Used after:

Login

Logout

Car booking

Profile update

Signup

1️⃣1️⃣ User Authentication (Django + Custom Logic)
Features:

User registration

Login

Logout

Password reset

Email verification (optional)

Profile management

Authentication middleware protects routes.

1️⃣2️⃣ Google & Facebook Login (OAuth)

Integrated using:

social-auth-app-django

Google Developer Console

Facebook Developer Dashboard

Users can sign in in 1 click.

1️⃣3️⃣ Email Sending System

Used to notify admins & users:

Contact form submissions

Booking confirmations

Password resets

Configured via:

SMTP (Gmail)

Django’s send_mail

1️⃣4️⃣ Database Dump & Load

Used for:

✔ Backup
✔ Migration
✔ Deployment

🧾 User Flow
1. Visitor lands on homepage

➡ Views trending cars, search bar, categories.

2. Searches for cars

➡ Filters by brand, model, fuel type, price.

3. Opens car details page

➡ Full specification + gallery.

4. Logs in / signs up

➡ Email/password
➡ OR Google login
➡ OR Facebook login

5. Requests for booking

➡ Email notification sent to admin.

6. Admin reviews in dashboard

➡ Approves or rejects booking.
