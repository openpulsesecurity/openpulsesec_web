# Open Pulse Security Website

Welcome to the official repository for the Open Pulse Security website. This website is built using **Python** and **Flask**, providing a modern and secure platform to showcase our services, solutions, and company information.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Home Page**: Introduction to Open Pulse Security and our mission.
- **Services**: Detailed information about our cybersecurity services.
- **Pricing**: Transparent pricing plans for our offerings.
- **Solutions**: Tailored solutions for businesses and individuals.
- **About Us**: Learn more about our team and values.
- **Privacy Policy**: Our commitment to protecting your data.
- **Terms of Service**: Legal terms for using our services.
- **Careers**: Explore job opportunities at Open Pulse Security.
- **Contact Form**: A secure and functional contact form for inquiries.

## Technologies Used
- **Python**: Backend programming language.
- **Flask**: Lightweight web framework for Python.
- **HTML/CSS**: Frontend structure and styling.
- **SMTP**: For sending emails via the contact form.
- **Environment Variables**: Secure configuration management using `.env`.

## Installation
1. Clone the repository:
   
   ```bash
   git clone https://github.com/openpulsesecurity/openpulsesec_web.git
   cd openpulsesec_web
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. Create a `.env` file in the root directory with the following variables:
   ```plaintext
   SMTP_SERVER=your.smtp.server
   SMTP_PORT=465
   SMTP_USER=your-smtp-username
   SMTP_PASSWORD=your-smtp-password
   SENDER_EMAIL=your-email@domain.com
   ```
2. Replace the placeholders with your actual SMTP and email credentials.

## Running the Application
1. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Run the Flask development server:
   ```bash
   flask run
   ```
3. Open your browser and navigate to `http://127.0.0.1:5000`.

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your commit message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request and describe your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Open Pulse Security** – Protecting your digital future.
