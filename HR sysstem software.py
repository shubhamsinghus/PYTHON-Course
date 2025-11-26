# import sys
# import warnings
# import json
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, QLabel, QLineEdit, QPushButton,
#     QVBoxLayout, QMessageBox, QHBoxLayout, QTextEdit,
#     QTabWidget, QFormLayout, QSpinBox, QComboBox, QDateEdit,
#     QTextEdit, QGroupBox, QScrollArea
# )
# from PyQt6.QtCore import Qt, QDate
# import pyrebase
# import datetime
#
# # --- SUPPRESS WARNINGS ---
# warnings.filterwarnings("ignore", category=UserWarning)
#
# # --- Firebase Configuration ---
# firebaseConfig = {
#     "apiKey": "AIzaSyAhmE1-nWOXS8sgwV9Eyi_0J13NDxQP3AU",
#     "authDomain": "edunova-hr--recruitmentsystem.firebaseapp.com",
#     "databaseURL": "https://edunova-hr--recruitmentsystem-default-rtdb.firebaseio.com",
#     "projectId": "edunova-hr--recruitmentsystem",
#     "storageBucket": "edunova-hr--recruitmentsystem.firebasestorage.app",
#     "messagingSenderId": "1087546413169",
#     "appId": "1:1087546413169:web:7a276d4a31c30d1f4c8bd0",
#     "measurementId": "G-KNJ7DPD6M9"
# }
#
# # --- Initialize Firebase ---
# try:
#     firebase = pyrebase.initialize_app(firebaseConfig)
#     auth = firebase.auth()
#     db = firebase.database()
#     print("Firebase initialized successfully")
# except Exception as e:
#     print(f"Firebase initialization error: {e}")
#     sys.exit(1)
#
#
# # --- PROFILE WINDOW CLASS ---
# class ProfileWindow(QWidget):
#     def __init__(self, user_data, parent=None):
#         super().__init__(parent)
#         self.user_data = user_data
#         self.setWindowTitle("EduNova HR - User Profile")
#         #self.setFixedSize(800, 700)
#         self.init_ui()
#         self.load_existing_data()
#
#     def init_ui(self):
#         layout = QVBoxLayout()
#
#         # Title
#         title = QLabel("User Profile - Personal Details")
#         title.setStyleSheet("font-size: 20px; font-weight: bold; color: #4E73DF; margin: 10px;")
#
#         # Create tab widget
#         self.tabs = QTabWidget()
#
#         # Personal Details Tab
#         self.personal_tab = QWidget()
#         self.create_personal_tab()
#         self.tabs.addTab(self.personal_tab, "Personal Details")
#
#         # Education Tab
#         self.education_tab = QWidget()
#         self.create_education_tab()
#         self.tabs.addTab(self.education_tab, "Education")
#
#         # Experience Tab
#         self.experience_tab = QWidget()
#         self.create_experience_tab()
#         self.tabs.addTab(self.experience_tab, "Work Experience")
#
#         # Job Preferences Tab
#         self.preferences_tab = QWidget()
#         self.create_preferences_tab()
#         self.tabs.addTab(self.preferences_tab, "Job Preferences")
#
#         # Buttons
#         button_layout = QHBoxLayout()
#         self.save_btn = QPushButton("Save Profile")
#         self.save_btn.clicked.connect(self.save_profile)
#         self.cancel_btn = QPushButton("Close")
#         self.cancel_btn.clicked.connect(self.close)
#
#         button_layout.addWidget(self.save_btn)
#         button_layout.addWidget(self.cancel_btn)
#
#         # Add widgets to main layout
#         layout.addWidget(title)
#         layout.addWidget(self.tabs)
#         layout.addLayout(button_layout)
#
#         self.setLayout(layout)
#         self.apply_styles()
#
#     def create_personal_tab(self):
#         layout = QFormLayout()
#
#         # Personal Information
#         self.full_name = QLineEdit()
#         self.full_name.setPlaceholderText("Enter your full name")
#
#         self.phone = QLineEdit()
#         self.phone.setPlaceholderText("Enter your phone number")
#
#         self.age = QSpinBox()
#         self.age.setRange(18, 70)
#         self.age.setValue(25)
#
#         self.gender = QComboBox()
#         self.gender.addItems(["Select Gender", "Male", "Female", "Other"])
#
#         self.dob = QDateEdit()
#         self.dob.setCalendarPopup(True)
#         self.dob.setDate(QDate(1995, 1, 1))
#
#         self.address = QTextEdit()
#         self.address.setMaximumHeight(80)
#         self.address.setPlaceholderText("Enter your complete address")
#
#         # Add to layout
#         layout.addRow("Full Name:*", self.full_name)
#         layout.addRow("Phone Number:*", self.phone)
#         layout.addRow("Age:*", self.age)
#         layout.addRow("Gender:", self.gender)
#         layout.addRow("Date of Birth:", self.dob)
#         layout.addRow("Address:", self.address)
#
#         self.personal_tab.setLayout(layout)
#
#     def create_education_tab(self):
#         layout = QVBoxLayout()
#
#         # Highest Education
#         edu_group = QGroupBox("Highest Education")
#         edu_form = QFormLayout()
#
#         self.highest_degree = QComboBox()
#         self.highest_degree.addItems([
#             "Select Degree",
#             "High School",
#             "Diploma",
#             "Bachelor's Degree",
#             "Master's Degree",
#             "PhD",
#             "Other"
#         ])
#
#         self.field_of_study = QLineEdit()
#         self.field_of_study.setPlaceholderText("e.g., Computer Science, Business Administration")
#
#         self.university = QLineEdit()
#         self.university.setPlaceholderText("Name of university/college")
#
#         self.graduation_year = QSpinBox()
#         self.graduation_year.setRange(1970, 2030)
#         self.graduation_year.setValue(2020)
#
#         self.gpa = QLineEdit()
#         self.gpa.setPlaceholderText("e.g., 3.5/4.0 or 8.5/10")
#
#         edu_form.addRow("Highest Degree:*", self.highest_degree)
#         edu_form.addRow("Field of Study:*", self.field_of_study)
#         edu_form.addRow("University:*", self.university)
#         edu_form.addRow("Graduation Year:*", self.graduation_year)
#         edu_form.addRow("GPA/CGPA:", self.gpa)
#
#         edu_group.setLayout(edu_form)
#
#         # Additional Education
#         add_edu_group = QGroupBox("Additional Education/Certifications")
#         add_edu_layout = QVBoxLayout()
#
#         self.additional_education = QTextEdit()
#         self.additional_education.setMaximumHeight(100)
#         self.additional_education.setPlaceholderText("List any additional degrees, certifications, or training...")
#
#         add_edu_layout.addWidget(self.additional_education)
#         add_edu_group.setLayout(add_edu_layout)
#
#         layout.addWidget(edu_group)
#         layout.addWidget(add_edu_group)
#         layout.addStretch()
#
#         self.education_tab.setLayout(layout)
#
#     def create_experience_tab(self):
#         layout = QVBoxLayout()
#
#         # Current/Most Recent Job
#         current_job_group = QGroupBox("Current/Most Recent Position")
#         current_form = QFormLayout()
#
#         self.job_title = QLineEdit()
#         self.job_title.setPlaceholderText("e.g., Software Engineer, Marketing Manager")
#
#         self.company = QLineEdit()
#         self.company.setPlaceholderText("Current/Previous company name")
#
#         self.industry = QComboBox()
#         self.industry.addItems([
#             "Select Industry",
#             "IT & Software",
#             "Finance & Banking",
#             "Healthcare",
#             "Education",
#             "Manufacturing",
#             "Retail",
#             "Marketing & Advertising",
#             "Other"
#         ])
#
#         self.start_date = QDateEdit()
#         self.start_date.setCalendarPopup(True)
#         self.start_date.setDate(QDate(2020, 1, 1))
#
#         self.end_date = QDateEdit()
#         self.end_date.setCalendarPopup(True)
#         self.end_date.setDate(QDate.currentDate())
#
#         self.currently_working = QComboBox()
#         self.currently_working.addItems(["No", "Yes"])
#
#         self.responsibilities = QTextEdit()
#         self.responsibilities.setMaximumHeight(100)
#         self.responsibilities.setPlaceholderText("Describe your key responsibilities and achievements...")
#
#         current_form.addRow("Job Title:*", self.job_title)
#         current_form.addRow("Company:*", self.company)
#         current_form.addRow("Industry:*", self.industry)
#         current_form.addRow("Start Date:*", self.start_date)
#         current_form.addRow("End Date:*", self.end_date)
#         current_form.addRow("Currently Working here?", self.currently_working)
#         current_form.addRow("Key Responsibilities:", self.responsibilities)
#
#         current_job_group.setLayout(current_form)
#
#         # Total Experience
#         exp_group = QGroupBox("Total Professional Experience")
#         exp_layout = QFormLayout()
#
#         self.total_experience = QComboBox()
#         self.total_experience.addItems([
#             "Select Experience",
#             "Fresher (0-1 years)",
#             "1-3 years",
#             "3-5 years",
#             "5-8 years",
#             "8-12 years",
#             "12+ years"
#         ])
#
#         self.skills = QTextEdit()
#         self.skills.setMaximumHeight(80)
#         self.skills.setPlaceholderText("List your key skills (comma separated)...")
#
#         exp_layout.addRow("Total Experience:*", self.total_experience)
#         exp_layout.addRow("Key Skills:*", self.skills)
#
#         exp_group.setLayout(exp_layout)
#
#         layout.addWidget(current_job_group)
#         layout.addWidget(exp_group)
#         layout.addStretch()
#
#         self.experience_tab.setLayout(layout)
#
#     def create_preferences_tab(self):
#         layout = QVBoxLayout()
#
#         # Job Preferences
#         job_pref_group = QGroupBox("Job Preferences")
#         job_form = QFormLayout()
#
#         self.desired_role = QLineEdit()
#         self.desired_role.setPlaceholderText("e.g., Senior Developer, Project Manager")
#
#         self.preferred_industry = QComboBox()
#         self.preferred_industry.addItems([
#             "Select Preferred Industry",
#             "IT & Software",
#             "Finance & Banking",
#             "Healthcare",
#             "Education",
#             "Manufacturing",
#             "Retail",
#             "Marketing & Advertising",
#             "Open to All"
#         ])
#
#         self.job_type = QComboBox()
#         self.job_type.addItems([
#             "Select Job Type",
#             "Full-time",
#             "Part-time",
#             "Contract",
#             "Remote",
#             "Hybrid",
#             "Internship"
#         ])
#
#         self.preferred_location = QLineEdit()
#         self.preferred_location.setPlaceholderText("e.g., New York, Remote, Anywhere")
#
#         self.expected_salary = QLineEdit()
#         self.expected_salary.setPlaceholderText("e.g., 50000 USD, 8 LPA")
#
#         self.notice_period = QComboBox()
#         self.notice_period.addItems([
#             "Select Notice Period",
#             "Immediately",
#             "15 days",
#             "30 days",
#             "60 days",
#             "90 days",
#             "More than 90 days"
#         ])
#
#         job_form.addRow("Desired Role:*", self.desired_role)
#         job_form.addRow("Preferred Industry:*", self.preferred_industry)
#         job_form.addRow("Job Type:*", self.job_type)
#         job_form.addRow("Preferred Location:*", self.preferred_location)
#         job_form.addRow("Expected Salary:*", self.expected_salary)
#         job_form.addRow("Notice Period:*", self.notice_period)
#
#         job_pref_group.setLayout(job_form)
#
#         # Additional Preferences
#         add_pref_group = QGroupBox("Additional Preferences")
#         add_pref_layout = QVBoxLayout()
#
#         self.additional_preferences = QTextEdit()
#         self.additional_preferences.setMaximumHeight(100)
#         self.additional_preferences.setPlaceholderText("Any additional preferences or requirements...")
#
#         add_pref_layout.addWidget(self.additional_preferences)
#         add_pref_group.setLayout(add_pref_layout)
#
#         layout.addWidget(job_pref_group)
#         layout.addWidget(add_pref_group)
#         layout.addStretch()
#
#         self.preferences_tab.setLayout(layout)
#
#     def load_existing_data(self):
#         """Load existing profile data from Firebase"""
#         try:
#             uid = self.user_data['uid']
#             profile_ref = db.child("user_profiles").child(uid).get()
#
#             if profile_ref.val():
#                 profile_data = profile_ref.val()
#                 self.populate_form(profile_data)
#                 print("Existing profile data loaded")
#         except Exception as e:
#             print(f"Error loading profile data: {e}")
#
#     def populate_form(self, data):
#         """Populate form with existing data"""
#         # Personal Details
#         self.full_name.setText(data.get('personal', {}).get('full_name', ''))
#         self.phone.setText(data.get('personal', {}).get('phone', ''))
#         self.age.setValue(data.get('personal', {}).get('age', 25))
#
#         gender = data.get('personal', {}).get('gender', 'Select Gender')
#         index = self.gender.findText(gender)
#         if index >= 0:
#             self.gender.setCurrentIndex(index)
#
#         if 'dob' in data.get('personal', {}):
#             dob = QDate.fromString(data['personal']['dob'], Qt.DateFormat.ISODate)
#             self.dob.setDate(dob)
#
#         self.address.setPlainText(data.get('personal', {}).get('address', ''))
#
#         # Education
#         degree = data.get('education', {}).get('highest_degree', 'Select Degree')
#         index = self.highest_degree.findText(degree)
#         if index >= 0:
#             self.highest_degree.setCurrentIndex(index)
#
#         self.field_of_study.setText(data.get('education', {}).get('field_of_study', ''))
#         self.university.setText(data.get('education', {}).get('university', ''))
#         self.graduation_year.setValue(data.get('education', {}).get('graduation_year', 2020))
#         self.gpa.setText(data.get('education', {}).get('gpa', ''))
#         self.additional_education.setPlainText(data.get('education', {}).get('additional_education', ''))
#
#         # Experience
#         self.job_title.setText(data.get('experience', {}).get('job_title', ''))
#         self.company.setText(data.get('experience', {}).get('company', ''))
#
#         industry = data.get('experience', {}).get('industry', 'Select Industry')
#         index = self.industry.findText(industry)
#         if index >= 0:
#             self.industry.setCurrentIndex(index)
#
#         if 'start_date' in data.get('experience', {}):
#             start_date = QDate.fromString(data['experience']['start_date'], Qt.DateFormat.ISODate)
#             self.start_date.setDate(start_date)
#
#         if 'end_date' in data.get('experience', {}):
#             end_date = QDate.fromString(data['experience']['end_date'], Qt.DateFormat.ISODate)
#             self.end_date.setDate(end_date)
#
#         currently_working = "Yes" if data.get('experience', {}).get('currently_working', False) else "No"
#         index = self.currently_working.findText(currently_working)
#         if index >= 0:
#             self.currently_working.setCurrentIndex(index)
#
#         self.responsibilities.setPlainText(data.get('experience', {}).get('responsibilities', ''))
#
#         total_exp = data.get('experience', {}).get('total_experience', 'Select Experience')
#         index = self.total_experience.findText(total_exp)
#         if index >= 0:
#             self.total_experience.setCurrentIndex(index)
#
#         self.skills.setPlainText(data.get('experience', {}).get('skills', ''))
#
#         # Preferences
#         self.desired_role.setText(data.get('preferences', {}).get('desired_role', ''))
#
#         pref_industry = data.get('preferences', {}).get('preferred_industry', 'Select Preferred Industry')
#         index = self.preferred_industry.findText(pref_industry)
#         if index >= 0:
#             self.preferred_industry.setCurrentIndex(index)
#
#         job_type = data.get('preferences', {}).get('job_type', 'Select Job Type')
#         index = self.job_type.findText(job_type)
#         if index >= 0:
#             self.job_type.setCurrentIndex(index)
#
#         self.preferred_location.setText(data.get('preferences', {}).get('preferred_location', ''))
#         self.expected_salary.setText(data.get('preferences', {}).get('expected_salary', ''))
#
#         notice_period = data.get('preferences', {}).get('notice_period', 'Select Notice Period')
#         index = self.notice_period.findText(notice_period)
#         if index >= 0:
#             self.notice_period.setCurrentIndex(index)
#
#         self.additional_preferences.setPlainText(data.get('preferences', {}).get('additional_preferences', ''))
#
#     def save_profile(self):
#         """Save profile data to Firebase"""
#         try:
#             # Validate required fields
#             if not self.validate_required_fields():
#                 return
#
#             profile_data = {
#                 'personal': {
#                     'full_name': self.full_name.text().strip(),
#                     'phone': self.phone.text().strip(),
#                     'age': self.age.value(),
#                     'gender': self.gender.currentText(),
#                     'dob': self.dob.date().toString(Qt.DateFormat.ISODate),
#                     'address': self.address.toPlainText().strip(),
#                     'updated_at': datetime.datetime.now().isoformat()
#                 },
#                 'education': {
#                     'highest_degree': self.highest_degree.currentText(),
#                     'field_of_study': self.field_of_study.text().strip(),
#                     'university': self.university.text().strip(),
#                     'graduation_year': self.graduation_year.value(),
#                     'gpa': self.gpa.text().strip(),
#                     'additional_education': self.additional_education.toPlainText().strip()
#                 },
#                 'experience': {
#                     'job_title': self.job_title.text().strip(),
#                     'company': self.company.text().strip(),
#                     'industry': self.industry.currentText(),
#                     'start_date': self.start_date.date().toString(Qt.DateFormat.ISODate),
#                     'end_date': self.end_date.date().toString(Qt.DateFormat.ISODate),
#                     'currently_working': self.currently_working.currentText() == "Yes",
#                     'responsibilities': self.responsibilities.toPlainText().strip(),
#                     'total_experience': self.total_experience.currentText(),
#                     'skills': self.skills.toPlainText().strip()
#                 },
#                 'preferences': {
#                     'desired_role': self.desired_role.text().strip(),
#                     'preferred_industry': self.preferred_industry.currentText(),
#                     'job_type': self.job_type.currentText(),
#                     'preferred_location': self.preferred_location.text().strip(),
#                     'expected_salary': self.expected_salary.text().strip(),
#                     'notice_period': self.notice_period.currentText(),
#                     'additional_preferences': self.additional_preferences.toPlainText().strip()
#                 },
#                 'profile_complete': True,
#                 'last_updated': datetime.datetime.now().isoformat()
#             }
#
#             # Save to Firebase
#             uid = self.user_data['uid']
#             db.child("user_profiles").child(uid).set(profile_data)
#
#             # Also update user record
#             db.child("users").child(uid).update({
#                 "profile_complete": True,
#                 "last_updated": datetime.datetime.now().isoformat()
#             })
#
#             QMessageBox.information(self, "Success", "Profile saved successfully!")
#             self.parent().log_db_operation("✅ User profile saved successfully")
#
#         except Exception as e:
#             QMessageBox.critical(self, "Error", f"Failed to save profile:\n{str(e)}")
#             self.parent().log_db_operation(f"❌ Profile save error: {str(e)}")
#
#     def validate_required_fields(self):
#         """Validate required fields"""
#         required_fields = [
#             (self.full_name.text().strip(), "Full Name"),
#             (self.phone.text().strip(), "Phone Number"),
#             (self.highest_degree.currentText(), "Highest Degree"),
#             (self.field_of_study.text().strip(), "Field of Study"),
#             (self.university.text().strip(), "University"),
#             (self.job_title.text().strip(), "Job Title"),
#             (self.company.text().strip(), "Company"),
#             (self.industry.currentText(), "Industry"),
#             (self.total_experience.currentText(), "Total Experience"),
#             (self.skills.toPlainText().strip(), "Skills"),
#             (self.desired_role.text().strip(), "Desired Role"),
#             (self.preferred_industry.currentText(), "Preferred Industry"),
#             (self.job_type.currentText(), "Job Type"),
#             (self.preferred_location.text().strip(), "Preferred Location"),
#             (self.expected_salary.text().strip(), "Expected Salary"),
#             (self.notice_period.currentText(), "Notice Period")
#         ]
#
#         missing_fields = []
#         for field_value, field_name in required_fields:
#             if not field_value or field_value.startswith("Select"):
#                 missing_fields.append(field_name)
#
#         if missing_fields:
#             QMessageBox.warning(self, "Missing Information",
#                                 f"Please fill in the following required fields:\n• " + "\n• ".join(missing_fields))
#             return False
#
#         return True
#
#     def apply_styles(self):
#         self.setStyleSheet("""
#             QWidget {
#                 background-color: #F8F9FC;
#                 color: #333;
#                 font-family: 'Segoe UI';
#                 font-size: 14px;
#             }
#             QTabWidget::pane {
#                 border: 1px solid #C4C4C4;
#                 background-color: white;
#             }
#             QTabBar::tab {
#                 background-color: #E9ECEF;
#                 padding: 8px 16px;
#                 margin-right: 2px;
#                 border: 1px solid #C4C4C4;
#             }
#             QTabBar::tab:selected {
#                 background-color: #4E73DF;
#                 color: white;
#             }
#             QLineEdit, QSpinBox, QComboBox, QDateEdit, QTextEdit {
#                 padding: 6px;
#                 border: 1px solid #CED4DA;
#                 border-radius: 4px;
#                 background-color: white;
#             }
#             QGroupBox {
#                 font-weight: bold;
#                 border: 1px solid #CED4DA;
#                 border-radius: 6px;
#                 margin-top: 10px;
#                 padding-top: 10px;
#             }
#             QGroupBox::title {
#                 subcontrol-origin: margin;
#                 left: 10px;
#                 padding: 0 5px 0 5px;
#             }
#             QPushButton {
#                 background-color: #4E73DF;
#                 color: white;
#                 border: none;
#                 padding: 8px 16px;
#                 border-radius: 4px;
#                 font-weight: bold;
#             }
#             QPushButton:hover {
#                 background-color: #3751C6;
#             }
#         """)
#
#
# # --- MAIN AUTH WINDOW CLASS (UPDATED) ---
# class AuthApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.current_user = None
#         self.user_token = None
#         self.setWindowTitle("EduNova HR - Login System")
#         self.setFixedSize(500, 550)
#         self.init_ui()
#
#     def init_ui(self):
#         # Widgets
#         self.title = QLabel("EduNova HR Portal")
#         self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#
#         self.email_label = QLabel("Email:")
#         self.email_input = QLineEdit()
#         self.email_input.setPlaceholderText("Enter your email")
#
#         self.password_label = QLabel("Password:")
#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Enter your password (min. 6 characters)")
#         self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
#
#         # Buttons
#         self.signup_btn = QPushButton("Sign Up")
#         self.login_btn = QPushButton("Login")
#         self.forgot_btn = QPushButton("Forgot Password?")
#         self.profile_btn = QPushButton("My Profile")
#         self.check_auth_btn = QPushButton("Check Auth Status")
#         self.test_db_btn = QPushButton("Test Database")
#         self.view_users_btn = QPushButton("View Users")
#         self.logout_btn = QPushButton("Logout")
#
#         # Database output area
#         self.db_output = QTextEdit()
#         self.db_output.setPlaceholderText("Database operations will be displayed here...")
#         self.db_output.setMaximumHeight(150)
#
#         # Layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.title)
#         layout.addWidget(self.email_label)
#         layout.addWidget(self.email_input)
#         layout.addWidget(self.password_label)
#         layout.addWidget(self.password_input)
#
#         # Button layouts
#         auth_btn_layout = QHBoxLayout()
#         auth_btn_layout.addWidget(self.signup_btn)
#         auth_btn_layout.addWidget(self.login_btn)
#         layout.addLayout(auth_btn_layout)
#
#         layout.addWidget(self.forgot_btn)
#         layout.addWidget(self.profile_btn)
#         layout.addWidget(self.check_auth_btn)
#
#         # Database operations section
#         db_btn_layout = QHBoxLayout()
#         db_btn_layout.addWidget(self.test_db_btn)
#         db_btn_layout.addWidget(self.view_users_btn)
#         db_btn_layout.addWidget(self.logout_btn)
#         layout.addLayout(db_btn_layout)
#
#         layout.addWidget(QLabel("Database Operations:"))
#         layout.addWidget(self.db_output)
#         layout.addStretch()
#
#         self.setLayout(layout)
#         self.apply_styles()
#
#         # Connect buttons
#         self.signup_btn.clicked.connect(self.signup)
#         self.login_btn.clicked.connect(self.login)
#         self.forgot_btn.clicked.connect(self.reset_password)
#         self.profile_btn.clicked.connect(self.open_profile)
#         self.logout_btn.clicked.connect(self.logout)
#         self.check_auth_btn.clicked.connect(self.check_auth_status)
#         self.test_db_btn.clicked.connect(self.test_database_operations)
#         self.view_users_btn.clicked.connect(self.view_all_users)
#
#         # Initialize UI state
#         self.update_ui_state()
#
#     def open_profile(self):
#         """Open profile window"""
#         if not self.current_user:
#             QMessageBox.warning(self, "Error", "Please login first to access your profile.")
#             return
#
#         self.profile_window = ProfileWindow(self.current_user, self)
#         self.profile_window.show()
#
#     # ... (rest of the AuthApp methods remain the same as previous version)
#     # Include all the previous methods: update_ui_state, log_db_operation, signup, login,
#     # logout, test_database_operations, view_all_users, reset_password,
#     # check_auth_status, validate_inputs, handle_auth_error, clear_inputs, apply_styles
#
#     def update_ui_state(self):
#         """Update UI based on authentication state"""
#         is_logged_in = self.current_user is not None
#
#         self.signup_btn.setEnabled(not is_logged_in)
#         self.login_btn.setEnabled(not is_logged_in)
#         self.forgot_btn.setEnabled(not is_logged_in)
#         self.profile_btn.setEnabled(is_logged_in)
#         self.check_auth_btn.setEnabled(True)
#         self.test_db_btn.setEnabled(is_logged_in)
#         self.view_users_btn.setEnabled(is_logged_in)
#         self.logout_btn.setEnabled(is_logged_in)
#
#         if is_logged_in:
#             self.title.setText(f"EduNova HR Portal - Welcome {self.current_user['email']}")
#         else:
#             self.title.setText("EduNova HR Portal")
#
#     def log_db_operation(self, message):
#         """Log database operations to the output area"""
#         timestamp = datetime.datetime.now().strftime("%H:%M:%S")
#         self.db_output.append(f"[{timestamp}] {message}")
#
#     def signup(self):
#         email = self.email_input.text().strip()
#         password = self.password_input.text().strip()
#
#         if not self.validate_inputs(email, password):
#             return
#
#         try:
#             self.log_db_operation(f"Attempting to create user: {email}")
#             user = auth.create_user_with_email_and_password(email, password)
#             uid = user['localId']
#             self.user_token = user['idToken']
#             self.current_user = {
#                 'email': email,
#                 'uid': uid,
#                 'idToken': self.user_token
#             }
#
#             self.log_db_operation(f"✅ Auth user created: {email} (UID: {uid})")
#
#             # Write user data to database
#             try:
#                 user_data = {
#                     "email": email,
#                     "created_at": datetime.datetime.now().isoformat(),
#                     "role": "candidate",
#                     "last_login": datetime.datetime.now().isoformat(),
#                     "profile_complete": False
#                 }
#
#                 db.child("users").child(uid).set(user_data)
#                 self.log_db_operation("✅ User data written to database")
#
#                 QMessageBox.information(self, "Success",
#                                         "✅ Account created successfully!\n"
#                                         f"Email: {email}\n"
#                                         f"UID: {uid}")
#                 self.clear_inputs()
#                 self.update_ui_state()
#
#             except Exception as db_error:
#                 self.log_db_operation(f"❌ Database error: {str(db_error)}")
#                 QMessageBox.warning(self, "Database Warning",
#                                     "User created but database write failed.\n"
#                                     "You can still login.")
#
#         except Exception as e:
#             self.handle_auth_error(e, "Signup")
#
#     def login(self):
#         email = self.email_input.text().strip()
#         password = self.password_input.text().strip()
#
#         if not self.validate_inputs(email, password):
#             return
#
#         try:
#             self.log_db_operation(f"Attempting login for: {email}")
#             user = auth.sign_in_with_email_and_password(email, password)
#
#             self.current_user = {
#                 'email': email,
#                 'uid': user['localId'],
#                 'idToken': user['idToken']
#             }
#             self.user_token = user['idToken']
#
#             self.log_db_operation(f"✅ Login successful: {email}")
#
#             # Update last login in database
#             try:
#                 db.child("users").child(user['localId']).update({
#                     "last_login": datetime.datetime.now().isoformat()
#                 })
#                 self.log_db_operation("✅ Last login updated")
#             except Exception as db_error:
#                 self.log_db_operation(f"⚠️ Could not update last login: {db_error}")
#
#             QMessageBox.information(self, "Login Success", f"Welcome back, {email}!")
#             self.clear_inputs()
#             self.update_ui_state()
#
#         except Exception as e:
#             self.handle_auth_error(e, "Login")
#
#     def logout(self):
#         self.current_user = None
#         self.user_token = None
#         self.log_db_operation("✅ User logged out")
#         self.db_output.clear()
#         self.update_ui_state()
#         QMessageBox.information(self, "Logout", "You have been logged out successfully.")
#
#     def test_database_operations(self):
#         """Test various database operations"""
#         if not self.current_user:
#             QMessageBox.warning(self, "Error", "Please login first.")
#             return
#
#         try:
#             uid = self.current_user['uid']
#             self.log_db_operation("--- Testing Database Operations ---")
#
#             # Test writing data
#             test_data = {
#                 "test_timestamp": datetime.datetime.now().isoformat(),
#                 "test_message": "This is a test from EduNova HR App",
#                 "random_number": 42
#             }
#
#             db.child("test_data").child(uid).set(test_data)
#             self.log_db_operation("✅ Test data written to database")
#
#             # Test reading data
#             result = db.child("test_data").child(uid).get()
#             if result.val():
#                 self.log_db_operation("✅ Test data read successfully")
#                 self.log_db_operation(f"   Data: {json.dumps(result.val(), indent=2)}")
#
#             # Test updating data
#             update_data = {
#                 "test_message": "Updated test message",
#                 "updated_at": datetime.datetime.now().isoformat()
#             }
#             db.child("test_data").child(uid).update(update_data)
#             self.log_db_operation("✅ Test data updated successfully")
#
#         except Exception as e:
#             self.log_db_operation(f"❌ Database error: {str(e)}")
#             QMessageBox.critical(self, "Database Error", f"Database operation failed:\n{str(e)}")
#
#     def view_all_users(self):
#         """View all users in the database"""
#         if not self.current_user:
#             QMessageBox.warning(self, "Error", "Please login first.")
#             return
#
#         try:
#             self.log_db_operation("--- Fetching All Users ---")
#             users = db.child("users").get()
#
#             if users.val():
#                 user_count = len(users.val())
#                 self.log_db_operation(f"✅ Found {user_count} user(s):")
#                 for uid, user_data in users.val().items():
#                     self.log_db_operation(
#                         f"   👤 {user_data.get('email', 'No email')} - Role: {user_data.get('role', 'No role')}")
#             else:
#                 self.log_db_operation("ℹ️ No users found in database")
#
#         except Exception as e:
#             self.log_db_operation(f"❌ Error fetching users: {str(e)}")
#
#     def reset_password(self):
#         email = self.email_input.text().strip()
#
#         if not email:
#             QMessageBox.warning(self, "Missing Email", "Please enter your email to reset password.")
#             return
#
#         try:
#             auth.send_password_reset_email(email)
#             self.log_db_operation(f"Password reset email sent to: {email}")
#             QMessageBox.information(self, "Reset Link Sent",
#                                     f"Password reset email sent to:\n{email}\n\nPlease check your inbox.")
#         except Exception as e:
#             self.handle_auth_error(e, "Password Reset")
#
#     def check_auth_status(self):
#         """Check current authentication status"""
#         if self.current_user:
#             self.log_db_operation(f"✅ Currently logged in as: {self.current_user['email']}")
#             QMessageBox.information(self, "Auth Status", f"Logged in as: {self.current_user['email']}")
#         else:
#             self.log_db_operation("ℹ️ Not currently logged in")
#             QMessageBox.information(self, "Auth Status", "Not logged in")
#
#     def validate_inputs(self, email, password):
#         if not email or not password:
#             QMessageBox.warning(self, "Error", "Please fill all fields.")
#             return False
#
#         if "@" not in email or "." not in email:
#             QMessageBox.warning(self, "Invalid Email", "Please enter a valid email address.")
#             return False
#
#         if len(password) < 6:
#             QMessageBox.warning(self, "Weak Password", "Password should be at least 6 characters long.")
#             return False
#
#         return True
#
#     def handle_auth_error(self, error, operation):
#         """Handle authentication errors gracefully"""
#         error_message = str(error)
#
#         try:
#             if hasattr(error, 'args') and len(error.args) > 1:
#                 error_json = error.args[1]
#                 error_data = json.loads(error_json)
#                 error_message = error_data.get('error', {}).get('message', str(error))
#         except:
#             pass
#
#         if "CONFIGURATION_NOT_FOUND" in error_message:
#             error_message = ("Firebase configuration error.\n\n"
#                              "Please check:\n"
#                              "1. Firebase Authentication is enabled in console\n"
#                              "2. Email/Password provider is enabled\n"
#                              "3. Project is properly configured")
#         elif "EMAIL_EXISTS" in error_message:
#             error_message = "This email is already registered. Please use login instead."
#         elif "INVALID_LOGIN_CREDENTIALS" in error_message:
#             error_message = "Invalid email or password. Please try again."
#         elif "TOO_MANY_ATTEMPTS_TRY_LATER" in error_message:
#             error_message = "Too many attempts. Please try again later."
#         elif "INVALID_EMAIL" in error_message:
#             error_message = "Please enter a valid email address."
#         elif "WEAK_PASSWORD" in error_message:
#             error_message = "Password should be at least 6 characters long."
#
#         self.log_db_operation(f"❌ {operation} Error: {error_message}")
#         QMessageBox.critical(self, f"{operation} Error", error_message)
#
#     def clear_inputs(self):
#         """Clear input fields"""
#         self.email_input.clear()
#         self.password_input.clear()
#
#     def apply_styles(self):
#         self.setStyleSheet("""
#             QWidget {
#                 background-color: #1E1E2F;
#                 color: white;
#                 font-family: 'Segoe UI';
#                 font-size: 14px;
#             }
#             QLineEdit {
#                 background-color: #2C2C3E;
#                 border: 1px solid #5A5A7E;
#                 border-radius: 8px;
#                 padding: 8px 12px;
#                 color: white;
#                 font-size: 14px;
#                 margin-bottom: 10px;
#             }
#             QLineEdit:focus {
#                 border: 1px solid #4E73DF;
#             }
#             QPushButton {
#                 background-color: #4E73DF;
#                 border-radius: 8px;
#                 color: white;
#                 padding: 8px;
#                 font-weight: bold;
#                 font-size: 13px;
#                 border: none;
#                 margin: 2px;
#             }
#             QPushButton:hover {
#                 background-color: #3751C6;
#             }
#             QPushButton:pressed {
#                 background-color: #2A3EB1;
#             }
#             QPushButton:disabled {
#                 background-color: #5A5A7E;
#                 color: #A0A0A0;
#             }
#             QTextEdit {
#                 background-color: #2C2C3E;
#                 border: 1px solid #5A5A7E;
#                 border-radius: 8px;
#                 padding: 8px;
#                 color: white;
#                 font-family: 'Consolas', 'Monaco', monospace;
#                 font-size: 12px;
#             }
#             QLabel[class="title"] {
#                 font-size: 22px;
#                 font-weight: bold;
#                 color: #fff;
#                 margin-bottom: 15px;
#                 text-align: center;
#             }
#         """)
#         self.title.setProperty("class", "title")
#
#
# # --- RUN APPLICATION ---
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyle('Fusion')
#
#     window = AuthApp()
#     window.show()
#
#     try:
#         sys.exit(app.exec())
#     except Exception as e:
#         print(f"Application error: {e}")
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QStackedWidget,
                             QLineEdit, QTextEdit, QComboBox, QDateEdit,
                             QMessageBox, QFrame, QSizePolicy, QScrollArea)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont, QPixmap, QIcon, QPainter


class ProfileWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My Profile")
        self.setGeometry(300, 100, 1000, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
        """)

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Left sidebar - Navigation
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)

        # Right content area
        content_area = self.create_content_area()
        main_layout.addWidget(content_area)

    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
                border-radius: 10px;
                margin: 10px;
            }
        """)

        layout = QVBoxLayout()
        sidebar.setLayout(layout)

        # Profile summary
        profile_summary = QWidget()
        profile_summary.setStyleSheet("""
            QWidget {
                background-color: #34495e;
                border-radius: 8px;
                padding: 15px;
            }
        """)
        profile_layout = QVBoxLayout()
        profile_summary.setLayout(profile_layout)

        # Profile picture placeholder
        profile_pic = QLabel()
        profile_pic.setFixedSize(80, 80)
        profile_pic.setStyleSheet("""
            QLabel {
                background-color: #ecf0f1;
                border-radius: 40px;
                border: 3px solid #3498db;
            }
        """)
        profile_pic.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Name label
        name_label = QLabel("John Doe")
        name_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 18px;
                font-weight: bold;
                margin-top: 10px;
            }
        """)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Role label
        role_label = QLabel("Software Developer")
        role_label.setStyleSheet("""
            QLabel {
                color: #bdc3c7;
                font-size: 14px;
            }
        """)
        role_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        profile_layout.addWidget(profile_pic, alignment=Qt.AlignmentFlag.AlignCenter)
        profile_layout.addWidget(name_label)
        profile_layout.addWidget(role_label)

        layout.addWidget(profile_summary)

        # Navigation buttons
        nav_buttons = [
            ("Personal Info", "personal"),
            ("Professional", "professional"),
            ("Education", "education"),
            ("Skills", "skills"),
            ("Projects", "projects"),
            ("Settings", "settings")
        ]

        for text, section in nav_buttons:
            btn = QPushButton(text)
            btn.setFixedHeight(45)
            btn.setProperty('section', section)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #ecf0f1;
                    border: none;
                    text-align: left;
                    padding-left: 20px;
                    font-size: 14px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #34495e;
                }
                QPushButton:pressed {
                    background-color: #3498db;
                }
            """)
            btn.clicked.connect(lambda checked, s=section: self.show_section(s))
            layout.addWidget(btn)

        layout.addStretch()

        # Logout button
        logout_btn = QPushButton("Logout")
        logout_btn.setFixedHeight(45)
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        logout_btn.clicked.connect(self.close)
        layout.addWidget(logout_btn)

        return sidebar

    def create_content_area(self):
        content_area = QWidget()
        content_area.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 10px;
                margin: 10px;
            }
        """)

        self.layout = QVBoxLayout()
        content_area.setLayout(self.layout)

        # Header
        header = QLabel("My Profile")
        header.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: #2c3e50;
                padding: 20px;
            }
        """)
        self.layout.addWidget(header)

        # Create stacked widget for different sections
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Create different sections
        self.create_personal_section()
        self.create_professional_section()
        self.create_education_section()
        self.create_skills_section()
        self.create_projects_section()
        self.create_settings_section()

        # Show personal section by default
        self.show_section('personal')

        return content_area

    def create_personal_section(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Personal info form
        form_layout = QVBoxLayout()

        fields = [
            ("Full Name", "John Doe"),
            ("Email", "john.doe@example.com"),
            ("Phone", "+1 (555) 123-4567"),
            ("Date of Birth", ""),
            ("Address", "123 Main St, City, State 12345")
        ]

        for label_text, placeholder in fields:
            field_layout = QVBoxLayout()
            label = QLabel(label_text)
            label.setStyleSheet("font-weight: bold; color: #2c3e50; margin-top: 10px;")

            if label_text == "Date of Birth":
                field = QDateEdit()
                field.setDate(QDate(1990, 1, 1))
            else:
                field = QLineEdit()
                field.setPlaceholderText(placeholder)

            field.setStyleSheet("""
                QLineEdit, QDateEdit {
                    padding: 10px;
                    border: 2px solid #ecf0f1;
                    border-radius: 5px;
                    font-size: 14px;
                }
                QLineEdit:focus, QDateEdit:focus {
                    border-color: #3498db;
                }
            """)

            field_layout.addWidget(label)
            field_layout.addWidget(field)
            form_layout.addLayout(field_layout)

        layout.addLayout(form_layout)

        # Save button
        save_btn = QPushButton("Save Changes")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        save_btn.clicked.connect(self.save_profile)
        layout.addWidget(save_btn)

        layout.addStretch()
        self.stacked_widget.addWidget(widget)

    def create_professional_section(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        title = QLabel("Professional Information")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)

        # Add professional info fields here
        info_label = QLabel("Professional details will be displayed here...")
        info_label.setStyleSheet("color: #7f8c8d; font-size: 16px;")
        layout.addWidget(info_label)

        layout.addStretch()
        self.stacked_widget.addWidget(widget)

    def create_education_section(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        title = QLabel("Education Background")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)

        # Add education info fields here
        info_label = QLabel("Education history will be displayed here...")
        info_label.setStyleSheet("color: #7f8c8d; font-size: 16px;")
        layout.addWidget(info_label)

        layout.addStretch()
        self.stacked_widget.addWidget(widget)

    def create_skills_section(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        title = QLabel("Skills & Expertise")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)

        # Add skills info here
        info_label = QLabel("Skills and expertise will be displayed here...")
        info_label.setStyleSheet("color: #7f8c8d; font-size: 16px;")
        layout.addWidget(info_label)

        layout.addStretch()
        self.stacked_widget.addWidget(widget)

    def create_projects_section(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        title = QLabel("Projects Portfolio")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)

        # Add projects info here
        info_label = QLabel("Projects portfolio will be displayed here...")
        info_label.setStyleSheet("color: #7f8c8d; font-size: 16px;")
        layout.addWidget(info_label)

        layout.addStretch()
        self.stacked_widget.addWidget(widget)

    def create_settings_section(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        title = QLabel("Account Settings")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)

        # Add settings options here
        info_label = QLabel("Account settings will be displayed here...")
        info_label.setStyleSheet("color: #7f8c8d; font-size: 16px;")
        layout.addWidget(info_label)

        layout.addStretch()
        self.stacked_widget.addWidget(widget)

    def show_section(self, section_name):
        section_map = {
            'personal': 0,
            'professional': 1,
            'education': 2,
            'skills': 3,
            'projects': 4,
            'settings': 5
        }
        self.stacked_widget.setCurrentIndex(section_map.get(section_name, 0))

    def save_profile(self):
        QMessageBox.information(self, "Success", "Profile changes saved successfully!")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main Application")
        self.setGeometry(200, 200, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Application title
        title = QLabel("Welcome to My Application")
        title.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: #2c3e50;
                padding: 40px;
                text-align: center;
            }
        """)
        layout.addWidget(title)

        # MY Profile button
        self.profile_button = QPushButton("MY Profile")
        self.profile_button.setFixedSize(200, 60)
        self.profile_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        self.profile_button.clicked.connect(self.open_profile_window)
        layout.addWidget(self.profile_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Additional content
        content = QLabel("This is the main application window.\nClick 'MY Profile' to open your profile.")
        content.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #7f8c8d;
                text-align: center;
                margin-top: 50px;
            }
        """)
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(content)

        layout.addStretch()

    def open_profile_window(self):
        print("Opening Profile Window...")  # Debug message
        self.profile_window = ProfileWindow()
        self.profile_window.show()
        self.profile_window.raise_()
        self.profile_window.activateWindow()


def main():
    # Enable high DPI scaling for better appearance
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QApplication {
            background-color: #ecf0f1;
        }
    """)

    # Create and show main window
    main_window = MainWindow()
    main_window.show()

    print("Application started successfully!")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()