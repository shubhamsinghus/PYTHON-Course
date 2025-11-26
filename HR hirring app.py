import sys
import warnings
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QHBoxLayout, QTextEdit,
    QTabWidget, QFormLayout, QSpinBox, QComboBox, QDateEdit,
    QTextEdit, QGroupBox, QScrollArea, QMainWindow
)
from PyQt6.QtCore import Qt, QDate
import pyrebase
import datetime

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


# --- PROFILE WINDOW CLASS ---
class ProfileWindow(QMainWindow):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.user_data = user_data
        self.setWindowTitle("EduNova HR - User Profile Management")
        self.setGeometry(100, 100, 1000, 800)  # Set position and size
        self.init_ui()
        self.load_existing_data()

    def init_ui(self):
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Title
        title = QLabel("User Profile - Complete Your Professional Details")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #4E73DF; margin: 15px; text-align: center;")

        # Create tab widget
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #C4C4C4;
                border-radius: 8px;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #E9ECEF;
                padding: 12px 20px;
                margin-right: 3px;
                border: 1px solid #C4C4C4;
                border-bottom: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background-color: #4E73DF;
                color: white;
            }
            QTabBar::tab:hover {
                background-color: #3751C6;
                color: white;
            }
        """)

        # Personal Details Tab
        self.personal_tab = QWidget()
        self.create_personal_tab()
        self.tabs.addTab(self.personal_tab, "👤 Personal Details")

        # Education Tab
        self.education_tab = QWidget()
        self.create_education_tab()
        self.tabs.addTab(self.education_tab, "🎓 Education")

        # Experience Tab
        self.experience_tab = QWidget()
        self.create_experience_tab()
        self.tabs.addTab(self.experience_tab, "💼 Work Experience")

        # Job Preferences Tab
        self.preferences_tab = QWidget()
        self.create_preferences_tab()
        self.tabs.addTab(self.preferences_tab, "🎯 Job Preferences")

        # Buttons
        button_layout = QHBoxLayout()
        self.save_btn = QPushButton("💾 Save Profile")
        self.save_btn.setMinimumHeight(40)
        self.save_btn.clicked.connect(self.save_profile)

        self.clear_btn = QPushButton("🗑️ Clear Form")
        self.clear_btn.setMinimumHeight(40)
        self.clear_btn.clicked.connect(self.clear_form)

        self.close_btn = QPushButton("❌ Close")
        self.close_btn.setMinimumHeight(40)
        self.close_btn.clicked.connect(self.close)

        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.clear_btn)
        button_layout.addWidget(self.close_btn)

        # Status label
        self.status_label = QLabel("Ready to save your profile...")
        self.status_label.setStyleSheet("padding: 10px; background-color: #E9ECEF; border-radius: 5px;")

        # Add widgets to main layout
        layout.addWidget(title)
        layout.addWidget(self.tabs)
        layout.addWidget(self.status_label)
        layout.addLayout(button_layout)

        self.apply_styles()

    def create_personal_tab(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QFormLayout(content)

        # Personal Information Group
        personal_group = QGroupBox("Personal Information")
        personal_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        personal_layout = QFormLayout(personal_group)

        self.full_name = QLineEdit()
        self.full_name.setPlaceholderText("Enter your full name")
        self.full_name.setMinimumHeight(35)

        self.phone = QLineEdit()
        self.phone.setPlaceholderText("Enter your phone number with country code")
        self.phone.setMinimumHeight(35)

        self.age = QSpinBox()
        self.age.setRange(18, 70)
        self.age.setValue(25)
        self.age.setMinimumHeight(35)

        self.gender = QComboBox()
        self.gender.addItems(["Select Gender", "Male", "Female", "Other", "Prefer not to say"])
        self.gender.setMinimumHeight(35)

        self.dob = QDateEdit()
        self.dob.setCalendarPopup(True)
        self.dob.setDate(QDate(1995, 1, 1))
        self.dob.setMinimumHeight(35)

        self.address = QTextEdit()
        self.address.setMaximumHeight(100)
        self.address.setPlaceholderText("Enter your complete address...")

        personal_layout.addRow("Full Name:*", self.full_name)
        personal_layout.addRow("Phone Number:*", self.phone)
        personal_layout.addRow("Age:*", self.age)
        personal_layout.addRow("Gender:", self.gender)
        personal_layout.addRow("Date of Birth:", self.dob)
        personal_layout.addRow("Address:", self.address)

        # Contact Information Group
        contact_group = QGroupBox("Contact Information")
        contact_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        contact_layout = QFormLayout(contact_group)

        self.linkedin = QLineEdit()
        self.linkedin.setPlaceholderText("LinkedIn profile URL")
        self.linkedin.setMinimumHeight(35)

        self.github = QLineEdit()
        self.github.setPlaceholderText("GitHub profile URL (if applicable)")
        self.github.setMinimumHeight(35)

        self.portfolio = QLineEdit()
        self.portfolio.setPlaceholderText("Portfolio website URL")
        self.portfolio.setMinimumHeight(35)

        contact_layout.addRow("LinkedIn:", self.linkedin)
        contact_layout.addRow("GitHub:", self.github)
        contact_layout.addRow("Portfolio:", self.portfolio)

        layout.addWidget(personal_group)
        layout.addWidget(contact_group)
        layout.addStretch()

        scroll.setWidget(content)
        personal_tab_layout = QVBoxLayout(self.personal_tab)
        personal_tab_layout.addWidget(scroll)

    def create_education_tab(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)

        # Highest Education
        edu_group = QGroupBox("Highest Education")
        edu_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        edu_form = QFormLayout(edu_group)

        self.highest_degree = QComboBox()
        self.highest_degree.addItems([
            "Select Degree",
            "High School",
            "Diploma",
            "Associate Degree",
            "Bachelor's Degree",
            "Master's Degree",
            "PhD",
            "Post-Doctoral",
            "Other"
        ])
        self.highest_degree.setMinimumHeight(35)

        self.field_of_study = QLineEdit()
        self.field_of_study.setPlaceholderText(
            "e.g., Computer Science, Business Administration, Mechanical Engineering")
        self.field_of_study.setMinimumHeight(35)

        self.university = QLineEdit()
        self.university.setPlaceholderText("Name of university/college/institution")
        self.university.setMinimumHeight(35)

        self.graduation_year = QSpinBox()
        self.graduation_year.setRange(1970, 2030)
        self.graduation_year.setValue(2020)
        self.graduation_year.setMinimumHeight(35)

        self.gpa = QLineEdit()
        self.gpa.setPlaceholderText("e.g., 3.5/4.0 or 8.5/10 or 85%")
        self.gpa.setMinimumHeight(35)

        edu_form.addRow("Highest Degree:*", self.highest_degree)
        edu_form.addRow("Field of Study:*", self.field_of_study)
        edu_form.addRow("University/Institution:*", self.university)
        edu_form.addRow("Graduation Year:*", self.graduation_year)
        edu_form.addRow("GPA/Percentage:", self.gpa)

        # Additional Education
        add_edu_group = QGroupBox("Additional Education & Certifications")
        add_edu_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        add_edu_layout = QVBoxLayout(add_edu_group)

        self.additional_education = QTextEdit()
        self.additional_education.setMaximumHeight(150)
        self.additional_education.setPlaceholderText(
            "List any additional degrees, certifications, training programs, workshops, or online courses...\n\n"
            "Example:\n"
            "- Google Data Analytics Professional Certificate (2023)\n"
            "- AWS Certified Solutions Architect (2022)\n"
            "- Digital Marketing Certification from Coursera (2021)"
        )

        add_edu_layout.addWidget(self.additional_education)

        layout.addWidget(edu_group)
        layout.addWidget(add_edu_group)
        layout.addStretch()

        scroll.setWidget(content)
        education_tab_layout = QVBoxLayout(self.education_tab)
        education_tab_layout.addWidget(scroll)

    def create_experience_tab(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)

        # Current/Most Recent Job
        current_job_group = QGroupBox("Current/Most Recent Position")
        current_job_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        current_form = QFormLayout(current_job_group)

        self.job_title = QLineEdit()
        self.job_title.setPlaceholderText("e.g., Senior Software Engineer, Marketing Manager, Data Analyst")
        self.job_title.setMinimumHeight(35)

        self.company = QLineEdit()
        self.company.setPlaceholderText("Current/Previous company name")
        self.company.setMinimumHeight(35)

        self.industry = QComboBox()
        self.industry.addItems([
            "Select Industry",
            "IT & Software Development",
            "Finance & Banking",
            "Healthcare",
            "Education & Training",
            "Manufacturing",
            "Retail & E-commerce",
            "Marketing & Advertising",
            "Consulting",
            "Government",
            "Non-Profit",
            "Other"
        ])
        self.industry.setMinimumHeight(35)

        self.start_date = QDateEdit()
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QDate(2020, 1, 1))
        self.start_date.setMinimumHeight(35)

        self.end_date = QDateEdit()
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(QDate.currentDate())
        self.end_date.setMinimumHeight(35)

        self.currently_working = QComboBox()
        self.currently_working.addItems(["No", "Yes"])
        self.currently_working.setMinimumHeight(35)

        self.responsibilities = QTextEdit()
        self.responsibilities.setMaximumHeight(120)
        self.responsibilities.setPlaceholderText(
            "Describe your key responsibilities, achievements, and contributions...")

        current_form.addRow("Job Title:*", self.job_title)
        current_form.addRow("Company:*", self.company)
        current_form.addRow("Industry:*", self.industry)
        current_form.addRow("Start Date:*", self.start_date)
        current_form.addRow("End Date:*", self.end_date)
        current_form.addRow("Currently Working here?", self.currently_working)
        current_form.addRow("Key Responsibilities & Achievements:", self.responsibilities)

        # Total Experience & Skills
        exp_group = QGroupBox("Professional Summary")
        exp_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        exp_layout = QFormLayout(exp_group)

        self.total_experience = QComboBox()
        self.total_experience.addItems([
            "Select Experience",
            "Fresher (0-1 years)",
            "1-3 years",
            "3-5 years",
            "5-8 years",
            "8-12 years",
            "12-15 years",
            "15+ years"
        ])
        self.total_experience.setMinimumHeight(35)

        self.skills = QTextEdit()
        self.skills.setMaximumHeight(100)
        self.skills.setPlaceholderText(
            "List your key skills (comma separated)...\nExample: Python, JavaScript, Project Management, Data Analysis, Team Leadership")

        exp_layout.addRow("Total Professional Experience:*", self.total_experience)
        exp_layout.addRow("Key Skills & Technologies:*", self.skills)

        layout.addWidget(current_job_group)
        layout.addWidget(exp_group)
        layout.addStretch()

        scroll.setWidget(content)
        experience_tab_layout = QVBoxLayout(self.experience_tab)
        experience_tab_layout.addWidget(scroll)

    def create_preferences_tab(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)

        # Job Preferences
        job_pref_group = QGroupBox("Job Preferences")
        job_pref_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        job_form = QFormLayout(job_pref_group)

        self.desired_role = QLineEdit()
        self.desired_role.setPlaceholderText(
            "e.g., Senior Developer, Project Manager, Data Scientist, Business Analyst")
        self.desired_role.setMinimumHeight(35)

        self.preferred_industry = QComboBox()
        self.preferred_industry.addItems([
            "Select Preferred Industry",
            "IT & Software Development",
            "Finance & Banking",
            "Healthcare",
            "Education & Training",
            "Manufacturing",
            "Retail & E-commerce",
            "Marketing & Advertising",
            "Consulting",
            "Government",
            "Non-Profit",
            "Open to All Industries"
        ])
        self.preferred_industry.setMinimumHeight(35)

        self.job_type = QComboBox()
        self.job_type.addItems([
            "Select Job Type",
            "Full-time",
            "Part-time",
            "Contract",
            "Remote",
            "Hybrid",
            "Internship",
            "Freelance"
        ])
        self.job_type.setMinimumHeight(35)

        self.preferred_location = QLineEdit()
        self.preferred_location.setPlaceholderText("e.g., New York, USA or Remote or Bangalore, India")
        self.preferred_location.setMinimumHeight(35)

        self.expected_salary = QLineEdit()
        self.expected_salary.setPlaceholderText("e.g., 50000 USD, 8 LPA, 60000 EUR")
        self.expected_salary.setMinimumHeight(35)

        self.notice_period = QComboBox()
        self.notice_period.addItems([
            "Select Notice Period",
            "Immediately Available",
            "15 days",
            "30 days (1 month)",
            "60 days (2 months)",
            "90 days (3 months)",
            "More than 90 days"
        ])
        self.notice_period.setMinimumHeight(35)

        job_form.addRow("Desired Role/Position:*", self.desired_role)
        job_form.addRow("Preferred Industry:*", self.preferred_industry)
        job_form.addRow("Job Type:*", self.job_type)
        job_form.addRow("Preferred Location:*", self.preferred_location)
        job_form.addRow("Expected Salary:*", self.expected_salary)
        job_form.addRow("Notice Period:*", self.notice_period)

        # Additional Preferences
        add_pref_group = QGroupBox("Additional Preferences & Requirements")
        add_pref_group.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        add_pref_layout = QVBoxLayout(add_pref_group)

        self.additional_preferences = QTextEdit()
        self.additional_preferences.setMaximumHeight(120)
        self.additional_preferences.setPlaceholderText(
            "Any additional preferences, requirements, or notes for potential employers...\n\n"
            "Examples:\n"
            "- Prefer startup environment with growth opportunities\n"
            "- Looking for companies with good work-life balance\n"
            "- Interested in roles with international exposure\n"
            "- Flexible on salary for equity/stock options"
        )

        add_pref_layout.addWidget(self.additional_preferences)

        layout.addWidget(job_pref_group)
        layout.addWidget(add_pref_group)
        layout.addStretch()

        scroll.setWidget(content)
        preferences_tab_layout = QVBoxLayout(self.preferences_tab)
        preferences_tab_layout.addWidget(scroll)

    def load_existing_data(self):
        """Load existing profile data from Firebase"""
        try:
            self.status_label.setText("🔄 Loading your existing profile data...")
            uid = self.user_data['uid']
            profile_ref = db.child("user_profiles").child(uid).get()

            if profile_ref.val():
                profile_data = profile_ref.val()
                self.populate_form(profile_data)
                self.status_label.setText("✅ Profile data loaded successfully!")
                print("Existing profile data loaded")
            else:
                self.status_label.setText("ℹ️ No existing profile found. Please fill in your details.")
        except Exception as e:
            self.status_label.setText("❌ Error loading profile data")
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

            if 'dob' in personal:
                try:
                    dob = QDate.fromString(personal['dob'], Qt.DateFormat.ISODate)
                    self.dob.setDate(dob)
                except:
                    pass

            self.address.setPlainText(personal.get('address', ''))
            self.linkedin.setText(personal.get('linkedin', ''))
            self.github.setText(personal.get('github', ''))
            self.portfolio.setText(personal.get('portfolio', ''))

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

            if 'start_date' in experience:
                try:
                    start_date = QDate.fromString(experience['start_date'], Qt.DateFormat.ISODate)
                    self.start_date.setDate(start_date)
                except:
                    pass

            if 'end_date' in experience:
                try:
                    end_date = QDate.fromString(experience['end_date'], Qt.DateFormat.ISODate)
                    self.end_date.setDate(end_date)
                except:
                    pass

            currently_working = "Yes" if experience.get('currently_working', False) else "No"
            index = self.currently_working.findText(currently_working)
            if index >= 0:
                self.currently_working.setCurrentIndex(index)

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

            self.additional_preferences.setPlainText(preferences.get('additional_preferences', ''))

        except Exception as e:
            print(f"Error populating form: {e}")

    def save_profile(self):
        """Save profile data to Firebase"""
        try:
            # Validate required fields
            if not self.validate_required_fields():
                return

            self.status_label.setText("🔄 Saving your profile to database...")

            profile_data = {
                'personal': {
                    'full_name': self.full_name.text().strip(),
                    'phone': self.phone.text().strip(),
                    'age': self.age.value(),
                    'gender': self.gender.currentText(),
                    'dob': self.dob.date().toString(Qt.DateFormat.ISODate),
                    'address': self.address.toPlainText().strip(),
                    'linkedin': self.linkedin.text().strip(),
                    'github': self.github.text().strip(),
                    'portfolio': self.portfolio.text().strip(),
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
                    'start_date': self.start_date.date().toString(Qt.DateFormat.ISODate),
                    'end_date': self.end_date.date().toString(Qt.DateFormat.ISODate),
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
                    'notice_period': self.notice_period.currentText(),
                    'additional_preferences': self.additional_preferences.toPlainText().strip()
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

            self.status_label.setText("✅ Profile saved successfully to Firebase!")
            QMessageBox.information(self, "Success", "✅ Profile saved successfully to database!")

            if self.parent():
                self.parent().log_db_operation("✅ User profile saved successfully to Firebase")

        except Exception as e:
            error_msg = f"Failed to save profile:\n{str(e)}"
            self.status_label.setText("❌ Error saving profile")
            QMessageBox.critical(self, "Error", error_msg)
            print(f"Save error: {e}")

            if self.parent():
                self.parent().log_db_operation(f"❌ Profile save error: {str(e)}")

    def clear_form(self):
        """Clear all form fields"""
        reply = QMessageBox.question(self, "Clear Form",
                                     "Are you sure you want to clear all form data?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            # Personal Tab
            self.full_name.clear()
            self.phone.clear()
            self.age.setValue(25)
            self.gender.setCurrentIndex(0)
            self.dob.setDate(QDate(1995, 1, 1))
            self.address.clear()
            self.linkedin.clear()
            self.github.clear()
            self.portfolio.clear()

            # Education Tab
            self.highest_degree.setCurrentIndex(0)
            self.field_of_study.clear()
            self.university.clear()
            self.graduation_year.setValue(2020)
            self.gpa.clear()
            self.additional_education.clear()

            # Experience Tab
            self.job_title.clear()
            self.company.clear()
            self.industry.setCurrentIndex(0)
            self.start_date.setDate(QDate(2020, 1, 1))
            self.end_date.setDate(QDate.currentDate())
            self.currently_working.setCurrentIndex(0)
            self.responsibilities.clear()
            self.total_experience.setCurrentIndex(0)
            self.skills.clear()

            # Preferences Tab
            self.desired_role.clear()
            self.preferred_industry.setCurrentIndex(0)
            self.job_type.setCurrentIndex(0)
            self.preferred_location.clear()
            self.expected_salary.clear()
            self.notice_period.setCurrentIndex(0)
            self.additional_preferences.clear()

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
                color: #333333;
            }
            QWidget {
                background-color: #F8F9FC;
                color: #333333;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 14px;
            }
            QLineEdit, QSpinBox, QComboBox, QDateEdit {
                padding: 8px 12px;
                border: 2px solid #CED4DA;
                border-radius: 6px;
                background-color: white;
                font-size: 14px;
                min-height: 25px;
            }
            QLineEdit:focus, QSpinBox:focus, QComboBox:focus, QDateEdit:focus {
                border-color: #4E73DF;
                background-color: #F0F4FF;
            }
            QTextEdit {
                padding: 8px;
                border: 2px solid #CED4DA;
                border-radius: 6px;
                background-color: white;
                font-size: 14px;
            }
            QTextEdit:focus {
                border-color: #4E73DF;
                background-color: #F0F4FF;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #E9ECEF;
                border-radius: 8px;
                margin-top: 15px;
                padding-top: 15px;
                background-color: white;
                font-size: 14px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 10px 0 10px;
                color: #4E73DF;
            }
            QPushButton {
                background-color: #4E73DF;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: #3751C6;
            }
            QPushButton:pressed {
                background-color: #2A3EB1;
            }
            QLabel {
                font-size: 14px;
                color: #333333;
            }
        """)


# --- MAIN AUTH WINDOW CLASS ---
class AuthApp(QWidget):
    def __init__(self):
        super().__init__()
        self.current_user = None
        self.user_token = None
        self.profile_window = None  # Track profile window
        self.setWindowTitle("EduNova HR - Recruitment System")
        self.setFixedSize(500, 600)
        self.init_ui()

    def init_ui(self):
        # Widgets
        self.title = QLabel("EduNova HR Portal")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password (min. 6 characters)")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Buttons
        self.signup_btn = QPushButton("Sign Up")
        self.login_btn = QPushButton("Login")
        self.forgot_btn = QPushButton("Forgot Password?")
        self.profile_btn = QPushButton("📝 My Profile")
        self.check_auth_btn = QPushButton("🔍 Check Auth Status")
        self.test_db_btn = QPushButton("🧪 Test Database")
        self.view_users_btn = QPushButton("👥 View Users")
        self.logout_btn = QPushButton("🚪 Logout")

        # Database output area
        self.db_output = QTextEdit()
        self.db_output.setPlaceholderText("Database operations will be displayed here...")
        self.db_output.setMaximumHeight(150)

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
        db_btn_layout.addWidget(self.view_users_btn)
        db_btn_layout.addWidget(self.logout_btn)
        layout.addLayout(db_btn_layout)

        layout.addWidget(QLabel("Database Operations:"))
        layout.addWidget(self.db_output)
        layout.addStretch()

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
        self.view_users_btn.clicked.connect(self.view_all_users)

        # Initialize UI state
        self.update_ui_state()

    def open_profile(self):
        """Open profile window"""
        if not self.current_user:
            QMessageBox.warning(self, "Error", "Please login first to access your profile.")
            return

        # Close existing profile window if open
        if self.profile_window and self.profile_window.isVisible():
            self.profile_window.close()

