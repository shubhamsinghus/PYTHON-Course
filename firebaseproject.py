import sys
import warnings
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QHBoxLayout, QTextEdit,
    QTabWidget, QFormLayout, QSpinBox, QComboBox, QDateEdit,
    QGroupBox, QScrollArea, QMainWindow
)
from PyQt6.QtCore import Qt, QDate
import pyrebase
import datetime
import re

# --- SUPPRESS WARNINGS ---
warnings.filterwarnings("ignore", category=UserWarning)

# --- Firebase Configuration ---
firebaseConfig = {
    "apiKey": "AIzaSyAhmE1-nWOXS8sgwV9Eyi_0J13NDxQP3AU",
    "authDomain": "edunova-hr--recruitmentsystem.firebaseapp.com",
    "databaseURL": "https://edunova-hr--recruitmentsystem-default-rtdb.firebaseio.com",
    "projectId": "edunova-hr--recruitmentsystem",
    "storageBucket": "edunova-hr--recruitmentsystem.firebasestorage.app",
    "messagingSenderId": "1087546413169",
    "appId": "1:1087546413169:web:7a276d4a31c30d1f4c8bd0",
    "measurementId": "G-KNJ7DPD6M9"
}

# --- Initialize Firebase ---
try:
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    db = firebase.database()
    print("Firebase initialized successfully")
except Exception as e:
    print(f"Firebase initialization error: {e}")
    sys.exit(1)


def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password(password):
    """Validate password (min 6 characters)"""
    return len(password) >= 6


# --- PROFILE WINDOW CLASS ---
class ProfileWindow(QMainWindow):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.user_data = user_data
        self.setWindowTitle("EduNova HR - User Profile Management")
        self.setGeometry(200, 100, 1300, 800)
        self.init_ui()

        # Load data after UI is initialized
        QApplication.processEvents()
        self.load_existing_data()

    def init_ui(self):
        try:
            # Central widget
            central_widget = QWidget()
            self.setCentralWidget(central_widget)

            layout = QVBoxLayout(central_widget)

            # Title
            title = QLabel("User Profile - Complete Your Professional Details")
            title.setStyleSheet("font-size: 18px; font-weight: bold; color: #4E73DF; margin: 10px; text-align: center;")

            # Create tab widget
            self.tabs = QTabWidget()
            self.tabs.setStyleSheet("""
                QTabWidget::pane {
                    border: 1px solid #C4C4C4;
                    border-radius: 5px;
                    background-color: white;
                }
                QTabBar::tab {
                    background-color: #E9ECEF;
                    padding: 8px 15px;
                    margin-right: 2px;
                    border: 1px solid #C4C4C4;
                    border-bottom: none;
                    border-top-left-radius: 4px;
                    border-top-right-radius: 4px;
                    font-weight: bold;
                }
                QTabBar::tab:selected {
                    background-color: #4E73DF;
                    color: white;
                }
            """)

            # Create tabs
            self.personal_tab = self.create_personal_tab()
            self.education_tab = self.create_education_tab()
            self.experience_tab = self.create_experience_tab()
            self.preferences_tab = self.create_preferences_tab()

            self.tabs.addTab(self.personal_tab, "Personal Details")
            self.tabs.addTab(self.education_tab, "Education")
            self.tabs.addTab(self.experience_tab, "Work Experience")
            self.tabs.addTab(self.preferences_tab, "Job Preferences")

            # Buttons
            button_layout = QHBoxLayout()
            self.save_btn = QPushButton("Save Profile")
            self.save_btn.setMinimumHeight(35)
            self.save_btn.clicked.connect(self.save_profile)

            self.clear_btn = QPushButton("Clear Form")
            self.clear_btn.setMinimumHeight(35)
            self.clear_btn.clicked.connect(self.clear_form)

            self.close_btn = QPushButton("Close")
            self.close_btn.setMinimumHeight(35)
            self.close_btn.clicked.connect(self.close)

            button_layout.addWidget(self.save_btn)
            button_layout.addWidget(self.clear_btn)
            button_layout.addWidget(self.close_btn)

            # Status label
            self.status_label = QLabel("Ready to save your profile...")
            self.status_label.setStyleSheet("padding: 8px; background-color: #E9ECEF; border-radius: 4px;")

            # Add widgets to main layout
            layout.addWidget(title)
            layout.addWidget(self.tabs)
            layout.addWidget(self.status_label)
            layout.addLayout(button_layout)

            self.apply_styles()

        except Exception as e:
            print(f"Error initializing ProfileWindow UI: {e}")
            QMessageBox.critical(self, "Error", f"Failed to initialize profile window: {str(e)}")

    def create_personal_tab(self):
        try:
            tab = QWidget()
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            content = QWidget()
            layout = QFormLayout(content)

            # Personal Information Group
            personal_group = QGroupBox("Personal Information")
            personal_layout = QFormLayout(personal_group)

            self.full_name = QLineEdit()
            self.full_name.setPlaceholderText("Enter your full name")

            self.phone = QLineEdit()
            self.phone.setPlaceholderText("Enter your phone number")

            self.age = QSpinBox()
            self.age.setRange(18, 70)
            self.age.setValue(25)

            self.gender = QComboBox()
            self.gender.addItems(["Select Gender", "Male", "Female", "Other", "Prefer not to say"])

            self.dob = QDateEdit()
            self.dob.setCalendarPopup(True)
            self.dob.setDate(QDate(1995, 1, 1))

            self.address = QTextEdit()
            self.address.setMaximumHeight(80)
            self.address.setPlaceholderText("Enter your complete address...")

            personal_layout.addRow("Full Name:*", self.full_name)
            personal_layout.addRow("Phone Number:*", self.phone)
            personal_layout.addRow("Age:*", self.age)
            personal_layout.addRow("Gender:", self.gender)
            personal_layout.addRow("Date of Birth:", self.dob)
            personal_layout.addRow("Address:", self.address)

            # Contact Information Group
            contact_group = QGroupBox("Contact Information")
            contact_layout = QFormLayout(contact_group)

            self.linkedin = QLineEdit()
            self.linkedin.setPlaceholderText("LinkedIn profile URL")

            self.github = QLineEdit()
            self.github.setPlaceholderText("GitHub profile URL")

            self.portfolio = QLineEdit()
            self.portfolio.setPlaceholderText("Portfolio website URL")

            contact_layout.addRow("LinkedIn:", self.linkedin)
            contact_layout.addRow("GitHub:", self.github)
            contact_layout.addRow("Portfolio:", self.portfolio)

            layout.addWidget(personal_group)
            layout.addWidget(contact_group)
            layout.addStretch()

            scroll.setWidget(content)
            tab_layout = QVBoxLayout(tab)
            tab_layout.addWidget(scroll)

            return tab

        except Exception as e:
            print(f"Error creating personal tab: {e}")
            return QWidget()

    def create_education_tab(self):
        try:
            tab = QWidget()
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            content = QWidget()
            layout = QVBoxLayout(content)

            # Highest Education
            edu_group = QGroupBox("Highest Education")
            edu_form = QFormLayout(edu_group)

            self.highest_degree = QComboBox()
            self.highest_degree.addItems([
                "Select Degree", "High School", "Diploma", "Associate Degree",
                "Bachelor's Degree", "Master's Degree", "PhD", "Other"
            ])

            self.field_of_study = QLineEdit()
            self.field_of_study.setPlaceholderText("e.g., Computer Science, Business Administration")

            self.university = QLineEdit()
            self.university.setPlaceholderText("Name of university/college/institution")

            self.graduation_year = QSpinBox()
            self.graduation_year.setRange(1970, 2030)
            self.graduation_year.setValue(2020)

            self.gpa = QLineEdit()
            self.gpa.setPlaceholderText("e.g., 3.5/4.0 or 8.5/10")

            edu_form.addRow("Highest Degree:*", self.highest_degree)
            edu_form.addRow("Field of Study:*", self.field_of_study)
            edu_form.addRow("University:*", self.university)
            edu_form.addRow("Graduation Year:*", self.graduation_year)
            edu_form.addRow("GPA/Percentage:", self.gpa)

            # Additional Education
            add_edu_group = QGroupBox("Additional Education & Certifications")
            add_edu_layout = QVBoxLayout(add_edu_group)

            self.additional_education = QTextEdit()
            self.additional_education.setMaximumHeight(100)
            self.additional_education.setPlaceholderText("List any additional degrees, certifications...")

            add_edu_layout.addWidget(self.additional_education)

            layout.addWidget(edu_group)
            layout.addWidget(add_edu_group)
            layout.addStretch()

            scroll.setWidget(content)
            tab_layout = QVBoxLayout(tab)
            tab_layout.addWidget(scroll)

            return tab

        except Exception as e:
            print(f"Error creating education tab: {e}")
            return QWidget()

    def create_experience_tab(self):
        try:
            tab = QWidget()
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            content = QWidget()
            layout = QVBoxLayout(content)

            # Current Job
            current_job_group = QGroupBox("Current/Most Recent Position")
            current_form = QFormLayout(current_job_group)

            self.job_title = QLineEdit()
            self.job_title.setPlaceholderText("e.g., Senior Software Engineer")

            self.company = QLineEdit()
            self.company.setPlaceholderText("Company name")

            self.industry = QComboBox()
            self.industry.addItems([
                "Select Industry", "IT & Software", "Finance", "Healthcare",
                "Education", "Manufacturing", "Retail", "Other"
            ])

            self.start_date = QDateEdit()
            self.start_date.setCalendarPopup(True)
            self.start_date.setDate(QDate(2020, 1, 1))

            self.end_date = QDateEdit()
            self.end_date.setCalendarPopup(True)
            self.end_date.setDate(QDate.currentDate())

            self.currently_working = QComboBox()
            self.currently_working.addItems(["No", "Yes"])

            self.responsibilities = QTextEdit()
            self.responsibilities.setMaximumHeight(80)
            self.responsibilities.setPlaceholderText("Describe your key responsibilities...")

            current_form.addRow("Job Title:*", self.job_title)
            current_form.addRow("Company:*", self.company)
            current_form.addRow("Industry:*", self.industry)
            current_form.addRow("Start Date:*", self.start_date)
            current_form.addRow("End Date:*", self.end_date)
            current_form.addRow("Currently Working?", self.currently_working)
            current_form.addRow("Responsibilities:", self.responsibilities)

            # Professional Summary
            exp_group = QGroupBox("Professional Summary")
            exp_layout = QFormLayout(exp_group)

            self.total_experience = QComboBox()
            self.total_experience.addItems([
                "Select Experience", "Fresher (0-1 years)", "1-3 years", "3-5 years",
                "5-8 years", "8-12 years", "12+ years"
            ])

            self.skills = QTextEdit()
            self.skills.setMaximumHeight(80)
            self.skills.setPlaceholderText("List your key skills...")

            exp_layout.addRow("Total Experience:*", self.total_experience)
            exp_layout.addRow("Key Skills:*", self.skills)

            layout.addWidget(current_job_group)
            layout.addWidget(exp_group)
            layout.addStretch()

            scroll.setWidget(content)
            tab_layout = QVBoxLayout(tab)
            tab_layout.addWidget(scroll)

            return tab

        except Exception as e:
            print(f"Error creating experience tab: {e}")
            return QWidget()

    def create_preferences_tab(self):
        try:
            tab = QWidget()
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            content = QWidget()
            layout = QVBoxLayout(content)

            # Job Preferences
            job_pref_group = QGroupBox("Job Preferences")
            job_form = QFormLayout(job_pref_group)

            self.desired_role = QLineEdit()
            self.desired_role.setPlaceholderText("e.g., Senior Developer, Project Manager")

            self.preferred_industry = QComboBox()
            self.preferred_industry.addItems([
                "Select Industry", "IT & Software", "Finance", "Healthcare",
                "Education", "Open to All Industries"
            ])

            self.job_type = QComboBox()
            self.job_type.addItems([
                "Select Job Type", "Full-time", "Part-time", "Contract",
                "Remote", "Hybrid", "Internship"
            ])

            self.preferred_location = QLineEdit()
            self.preferred_location.setPlaceholderText("e.g., New York or Remote")

            self.expected_salary = QLineEdit()
            self.expected_salary.setPlaceholderText("e.g., 50000 USD or 8 LPA")

            self.notice_period = QComboBox()
            self.notice_period.addItems([
                "Select Notice Period", "Immediately", "15 days", "30 days",
                "60 days", "90 days"
            ])

            job_form.addRow("Desired Role:*", self.desired_role)
            job_form.addRow("Preferred Industry:*", self.preferred_industry)
            job_form.addRow("Job Type:*", self.job_type)
            job_form.addRow("Preferred Location:*", self.preferred_location)
            job_form.addRow("Expected Salary:*", self.expected_salary)
            job_form.addRow("Notice Period:*", self.notice_period)

            layout.addWidget(job_pref_group)
            layout.addStretch()

            scroll.setWidget(content)
            tab_layout = QVBoxLayout(tab)
            tab_layout.addWidget(scroll)

            return tab

        except Exception as e:
            print(f"Error creating preferences tab: {e}")
            return QWidget()

    def load_existing_data(self):
        """Load existing profile data from Firebase"""
        try:
            self.status_label.setText("Loading your existing profile data...")
            QApplication.processEvents()

            uid = self.user_data['uid']
            profile_ref = db.child("user_profiles").child(uid).get()

            if profile_ref and profile_ref.val():
                profile_data = profile_ref.val()
                self.populate_form(profile_data)
                self.status_label.setText("Profile data loaded successfully!")
                print("Existing profile data loaded")
            else:
                self.status_label.setText("No existing profile found. Please fill in your details.")

        except Exception as e:
            self.status_label.setText("Error loading profile data")
            print(f"Error loading profile data: {e}")

    def populate_form(self, data):
        """Populate form with existing data"""
        try:
            # Personal Details
            personal = data.get('personal', {})
            self.full_name.setText(personal.get('full_name', ''))
            self.phone.setText(personal.get('phone', ''))
            self.age.setValue(personal.get('age', 25))

            gender = personal.get('gender', 'Select Gender')
            index = self.gender.findText(gender)
            if index >= 0:
                self.gender.setCurrentIndex(index)

            # Education
            education = data.get('education', {})
            degree = education.get('highest_degree', 'Select Degree')
            index = self.highest_degree.findText(degree)
            if index >= 0:
                self.highest_degree.setCurrentIndex(index)

            self.field_of_study.setText(education.get('field_of_study', ''))
            self.university.setText(education.get('university', ''))
            self.graduation_year.setValue(education.get('graduation_year', 2020))
            self.gpa.setText(education.get('gpa', ''))
            self.additional_education.setPlainText(education.get('additional_education', ''))

            # Experience
            experience = data.get('experience', {})
            self.job_title.setText(experience.get('job_title', ''))
            self.company.setText(experience.get('company', ''))

            industry = experience.get('industry', 'Select Industry')
            index = self.industry.findText(industry)
            if index >= 0:
                self.industry.setCurrentIndex(index)

            self.responsibilities.setPlainText(experience.get('responsibilities', ''))

            total_exp = experience.get('total_experience', 'Select Experience')
            index = self.total_experience.findText(total_exp)
            if index >= 0:
                self.total_experience.setCurrentIndex(index)

            self.skills.setPlainText(experience.get('skills', ''))

            # Preferences
            preferences = data.get('preferences', {})
            self.desired_role.setText(preferences.get('desired_role', ''))

            pref_industry = preferences.get('preferred_industry', 'Select Preferred Industry')
            index = self.preferred_industry.findText(pref_industry)
            if index >= 0:
                self.preferred_industry.setCurrentIndex(index)

            job_type = preferences.get('job_type', 'Select Job Type')
            index = self.job_type.findText(job_type)
            if index >= 0:
                self.job_type.setCurrentIndex(index)

            self.preferred_location.setText(preferences.get('preferred_location', ''))
            self.expected_salary.setText(preferences.get('expected_salary', ''))

            notice_period = preferences.get('notice_period', 'Select Notice Period')
            index = self.notice_period.findText(notice_period)
            if index >= 0:
                self.notice_period.setCurrentIndex(index)

        except Exception as e:
            print(f"Error populating form: {e}")

    def save_profile(self):
        """Save profile data to Firebase"""
        try:
            if not self.validate_required_fields():
                return

            self.status_label.setText("Saving your profile to database...")

            profile_data = {
                'personal': {
                    'full_name': self.full_name.text().strip(),
                    'phone': self.phone.text().strip(),
                    'age': self.age.value(),
                    'gender': self.gender.currentText(),
                    'updated_at': datetime.datetime.now().isoformat()
                },
                'education': {
                    'highest_degree': self.highest_degree.currentText(),
                    'field_of_study': self.field_of_study.text().strip(),
                    'university': self.university.text().strip(),
                    'graduation_year': self.graduation_year.value(),
                    'gpa': self.gpa.text().strip(),
                    'additional_education': self.additional_education.toPlainText().strip()
                },
                'experience': {
                    'job_title': self.job_title.text().strip(),
                    'company': self.company.text().strip(),
                    'industry': self.industry.currentText(),
                    'currently_working': self.currently_working.currentText() == "Yes",
                    'responsibilities': self.responsibilities.toPlainText().strip(),
                    'total_experience': self.total_experience.currentText(),
                    'skills': self.skills.toPlainText().strip()
                },
                'preferences': {
                    'desired_role': self.desired_role.text().strip(),
                    'preferred_industry': self.preferred_industry.currentText(),
                    'job_type': self.job_type.currentText(),
                    'preferred_location': self.preferred_location.text().strip(),
                    'expected_salary': self.expected_salary.text().strip(),
                    'notice_period': self.notice_period.currentText()
                },
                'profile_complete': True,
                'last_updated': datetime.datetime.now().isoformat()
            }

            # Save to Firebase
            uid = self.user_data['uid']
            db.child("user_profiles").child(uid).set(profile_data)

            # Also update user record
            db.child("users").child(uid).update({
                "profile_complete": True,
                "last_updated": datetime.datetime.now().isoformat()
            })

            self.status_label.setText("Profile saved successfully!")
            QMessageBox.information(self, "Success", "Profile saved successfully to database!")

            if self.parent():
                self.parent().log_db_operation("User profile saved successfully")

        except Exception as e:
            error_msg = f"Failed to save profile:\n{str(e)}"
            self.status_label.setText("Error saving profile")
            QMessageBox.critical(self, "Error", error_msg)
            print(f"Save error: {e}")

    def clear_form(self):
        """Clear all form fields"""
        reply = QMessageBox.question(self, "Clear Form",
                                     "Are you sure you want to clear all form data?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            # Clear all fields
            self.full_name.clear()
            self.phone.clear()
            self.age.setValue(25)
            self.gender.setCurrentIndex(0)
            self.dob.setDate(QDate(1995, 1, 1))
            self.address.clear()
            self.linkedin.clear()
            self.github.clear()
            self.portfolio.clear()

            self.highest_degree.setCurrentIndex(0)
            self.field_of_study.clear()
            self.university.clear()
            self.graduation_year.setValue(2020)
            self.gpa.clear()
            self.additional_education.clear()

            self.job_title.clear()
            self.company.clear()
            self.industry.setCurrentIndex(0)
            self.start_date.setDate(QDate(2020, 1, 1))
            self.end_date.setDate(QDate.currentDate())
            self.currently_working.setCurrentIndex(0)
            self.responsibilities.clear()
            self.total_experience.setCurrentIndex(0)
            self.skills.clear()

            self.desired_role.clear()
            self.preferred_industry.setCurrentIndex(0)
            self.job_type.setCurrentIndex(0)
            self.preferred_location.clear()
            self.expected_salary.clear()
            self.notice_period.setCurrentIndex(0)

            self.status_label.setText("Form cleared. Fill in your details and save.")

    def validate_required_fields(self):
        """Validate required fields"""
        required_fields = [
            (self.full_name.text().strip(), "Full Name"),
            (self.phone.text().strip(), "Phone Number"),
            (self.highest_degree.currentText(), "Highest Degree"),
            (self.field_of_study.text().strip(), "Field of Study"),
            (self.university.text().strip(), "University/Institution"),
            (self.job_title.text().strip(), "Job Title"),
            (self.company.text().strip(), "Company"),
            (self.industry.currentText(), "Industry"),
            (self.total_experience.currentText(), "Total Experience"),
            (self.skills.toPlainText().strip(), "Skills"),
            (self.desired_role.text().strip(), "Desired Role"),
            (self.preferred_industry.currentText(), "Preferred Industry"),
            (self.job_type.currentText(), "Job Type"),
            (self.preferred_location.text().strip(), "Preferred Location"),
            (self.expected_salary.text().strip(), "Expected Salary"),
            (self.notice_period.currentText(), "Notice Period")
        ]

        missing_fields = []
        for field_value, field_name in required_fields:
            if not field_value or field_value.startswith("Select"):
                missing_fields.append(field_name)

        if missing_fields:
            QMessageBox.warning(self, "Missing Information",
                                f"Please fill in the following required fields:\n\n• " + "\n• ".join(missing_fields))
            return False

        return True

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F8F9FC;
            }
            QLineEdit, QSpinBox, QComboBox, QDateEdit {
                padding: 6px 10px;
                border: 1px solid #CED4DA;
                border-radius: 4px;
                background-color: white;
                min-height: 20px;
            }
            QTextEdit {
                padding: 6px;
                border: 1px solid #CED4DA;
                border-radius: 4px;
                background-color: white;
            }
            QGroupBox {
                font-weight: bold;
                border: 1px solid #E9ECEF;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
                background-color: white;
            }
            QPushButton {
                background-color: #4E73DF;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3751C6;
            }
        """)


# --- MAIN AUTH WINDOW CLASS ---
class AuthApp(QWidget):
    def __init__(self):
        super().__init__()
        self.current_user = None
        self.user_token = None
        self.profile_window = None
        self.setWindowTitle("EduNova HR - Recruitment System")
        self.setFixedSize(450, 500)
        self.init_ui()

    def init_ui(self):
        # Widgets
        self.title = QLabel("EduNova HR Portal")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 20px; font-weight: bold; margin: 10px;")

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setText("test@example.com")  # Default test email

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password (min. 6 characters)")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setText("123456")  # Default test password

        # Buttons
        self.signup_btn = QPushButton("Sign Up")
        self.login_btn = QPushButton("Login")
        self.forgot_btn = QPushButton("Forgot Password?")
        self.profile_btn = QPushButton("My Profile")
        self.check_auth_btn = QPushButton("Check Auth Status")
        self.test_db_btn = QPushButton("Test Database")
        self.logout_btn = QPushButton("Logout")

        # Database output area
        self.db_output = QTextEdit()
        self.db_output.setPlaceholderText("Database operations will be displayed here...")
        self.db_output.setMaximumHeight(120)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Button layouts
        auth_btn_layout = QHBoxLayout()
        auth_btn_layout.addWidget(self.signup_btn)
        auth_btn_layout.addWidget(self.login_btn)
        layout.addLayout(auth_btn_layout)

        layout.addWidget(self.forgot_btn)
        layout.addWidget(self.profile_btn)
        layout.addWidget(self.check_auth_btn)

        # Database operations section
        db_btn_layout = QHBoxLayout()
        db_btn_layout.addWidget(self.test_db_btn)
        db_btn_layout.addWidget(self.logout_btn)
        layout.addLayout(db_btn_layout)

        layout.addWidget(QLabel("Database Operations:"))
        layout.addWidget(self.db_output)

        self.setLayout(layout)
        self.apply_styles()

        # Connect buttons
        self.signup_btn.clicked.connect(self.signup)
        self.login_btn.clicked.connect(self.login)
        self.forgot_btn.clicked.connect(self.reset_password)
        self.profile_btn.clicked.connect(self.open_profile)
        self.logout_btn.clicked.connect(self.logout)
        self.check_auth_btn.clicked.connect(self.check_auth_status)
        self.test_db_btn.clicked.connect(self.test_database_operations)

        # Initialize UI state
        self.update_ui_state()

    def open_profile(self):
        """Open profile window"""
        if not self.current_user:
            QMessageBox.warning(self, "Error", "Please login first to access your profile.")
            return

        try:
            # Close existing profile window if open
            if self.profile_window and self.profile_window.isVisible():
                self.profile_window.close()

            # Create new profile window
            self.profile_window = ProfileWindow(self.current_user, self)
            self.profile_window.show()
            self.log_db_operation("Profile window opened")

        except Exception as e:
            error_msg = f"Failed to open profile window:\n{str(e)}"
            QMessageBox.critical(self, "Error", error_msg)
            self.log_db_operation(f"Error opening profile: {str(e)}")

    def signup(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Please fill all fields.")
            return

        # Validate email format
        if not validate_email(email):
            QMessageBox.warning(self, "Invalid Email", "Please enter a valid email address.")
            return

        # Validate password length
        if not validate_password(password):
            QMessageBox.warning(self, "Invalid Password", "Password must be at least 6 characters long.")
            return

        try:
            # Show loading message
            self.log_db_operation("Creating account...")
            QApplication.processEvents()

            # Create user with email and password
            user = auth.create_user_with_email_and_password(email, password)
            uid = user['localId']

            # Store user data
            self.current_user = {
                'uid': uid,
                'email': email
            }
            self.user_token = user['idToken']

            # Write to database
            db.child("users").child(uid).set({
                "email": email,
                "created_at": datetime.datetime.now().isoformat(),
                "profile_complete": False
            })

            QMessageBox.information(self, "Success", "Account created successfully!")
            self.log_db_operation("New user registered successfully")
            self.update_ui_state()

        except Exception as e:
            error_msg = self.parse_firebase_error(e)
            QMessageBox.critical(self, "Signup Error", error_msg)
            self.log_db_operation(f"Signup error: {error_msg}")

    def login(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Please fill all fields.")
            return

        # Validate email format
        if not validate_email(email):
            QMessageBox.warning(self, "Invalid Email", "Please enter a valid email address.")
            return

        try:
            # Show loading message
            self.log_db_operation("Logging in...")
            QApplication.processEvents()

            # Sign in with email and password
            user = auth.sign_in_with_email_and_password(email, password)
            self.current_user = {
                'uid': user['localId'],
                'email': email
            }
            self.user_token = user['idToken']

            QMessageBox.information(self, "Login Success", f"Welcome back, {email}!")
            self.log_db_operation(f"User {email} logged in successfully")
            self.update_ui_state()

        except Exception as e:
            error_msg = self.parse_firebase_error(e)
            QMessageBox.critical(self, "Login Error", error_msg)
            self.log_db_operation(f"Login error: {error_msg}")

    def parse_firebase_error(self, error):
        """Parse Firebase authentication errors"""
        try:
            # Pyrebase returns error as a tuple (exception, response)
            if hasattr(error, 'args') and len(error.args) > 1:
                error_json = error.args[1]
                error_data = json.loads(error_json)
                error_message = error_data.get('error', {}).get('message', str(error))

                # Map common Firebase error messages to user-friendly messages
                error_mapping = {
                    'INVALID_EMAIL': 'The email address is badly formatted.',
                    'EMAIL_NOT_FOUND': 'No account found with this email address.',
                    'INVALID_PASSWORD': 'The password is invalid.',
                    'USER_DISABLED': 'This user account has been disabled.',
                    'EMAIL_EXISTS': 'An account with this email already exists.',
                    'OPERATION_NOT_ALLOWED': 'Password sign-in is disabled for this project.',
                    'TOO_MANY_ATTEMPTS_TRY_LATER': 'Too many unsuccessful login attempts. Please try again later.'
                }

                for key, message in error_mapping.items():
                    if key in error_message:
                        return message

                return error_message
            else:
                return str(error)
        except:
            return str(error)

    def reset_password(self):
        email = self.email_input.text().strip()

        if not email:
            QMessageBox.warning(self, "Missing Email", "Please enter your email to reset password.")
            return

        if not validate_email(email):
            QMessageBox.warning(self, "Invalid Email", "Please enter a valid email address.")
            return

        try:
            auth.send_password_reset_email(email)
            QMessageBox.information(self, "Reset Link Sent", f"Password reset email sent to:\n{email}")
            self.log_db_operation(f"Password reset email sent to {email}")
        except Exception as e:
            error_msg = self.parse_firebase_error(e)
            QMessageBox.critical(self, "Error", error_msg)
            self.log_db_operation(f"Password reset error: {error_msg}")

    def logout(self):
        self.current_user = None
        self.user_token = None
        if self.profile_window:
            self.profile_window.close()
            self.profile_window = None

        QMessageBox.information(self, "Logout", "You have been logged out successfully.")
        self.log_db_operation("User logged out")
        self.update_ui_state()

    def check_auth_status(self):
        if self.current_user:
            self.log_db_operation(f"Auth Status: Logged in as {self.current_user['email']}")
        else:
            self.log_db_operation("Auth Status: Not logged in")

    def test_database_operations(self):
        try:
            if not self.current_user:
                self.log_db_operation("Test DB: Please login first")
                return

            # Test write operation
            test_data = {
                "test_timestamp": datetime.datetime.now().isoformat(),
                "test_message": "Database connection test successful"
            }
            db.child("test_operations").child(self.current_user['uid']).set(test_data)
            self.log_db_operation("Test DB: Write operation successful")

        except Exception as e:
            self.log_db_operation(f"Test DB Error: {str(e)}")

    def log_db_operation(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.db_output.append(f"[{timestamp}] {message}")

    def update_ui_state(self):
        """Update UI based on authentication state"""
        is_logged_in = self.current_user is not None

        # Enable/disable buttons based on login state
        self.profile_btn.setEnabled(is_logged_in)
        self.test_db_btn.setEnabled(is_logged_in)
        self.logout_btn.setEnabled(is_logged_in)

        # Update title
        if is_logged_in:
            self.title.setText(f"EduNova HR Portal\nWelcome, {self.current_user['email']}!")
        else:
            self.title.setText("EduNova HR Portal")

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E2F;
                color: white;
                font-family: 'Segoe UI';
                font-size: 14px;
            }
            QLineEdit {
                background-color: #2C2C3E;
                border: 1px solid #5A5A7E;
                border-radius: 6px;
                padding: 8px;
                color: white;
            }
            QPushButton {
                background-color: #4E73DF;
                border: none;
                border-radius: 6px;
                color: white;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3751C6;
            }
            QPushButton:disabled {
                background-color: #6C757D;
                color: #ADB5BD;
            }
            QTextEdit {
                background-color: #2C2C3E;
                border: 1px solid #5A5A7E;
                border-radius: 6px;
                padding: 8px;
                color: white;
                font-size: 12px;
            }
        """)


# --- RUN APPLICATION ---
if __name__ == "__main__":
    app = QApplication(sys.argv)

    try:
        window = AuthApp()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Application error: {e}")
        QMessageBox.critical(None, "Fatal Error", f"The application encountered a fatal error:\n{str(e)}")
        sys.exit(1)