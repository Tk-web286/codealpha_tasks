# Secure Coding Review – Flask Web Application

## Overview

This project was completed as part of the **CodeAlpha Cyber Security Internship Program**.

The objective of this task was to perform a secure coding review of a Flask-based web application by conducting both manual code inspection and automated static analysis. The assessment focused on identifying security weaknesses, evaluating secure coding practices, and recommending improvements to strengthen application security.

---

## Objectives

- Perform a security-focused code review.
- Identify potential security weaknesses.
- Analyze authentication mechanisms.
- Evaluate input validation practices.
- Review file upload security controls.
- Assess session management implementation.
- Examine error handling configurations.
- Conduct static application security testing (SAST).
- Provide remediation recommendations.

---

## Technologies Used

- Python 3
- Flask Framework
- Kali Linux
- Bandit Static Analysis Tool
- Git
- GitHub

---

## Project Structure

```text
codealpha_tasks
|
└─CodeAlpha_Secure_Code_Analysis/
   │
   ├── app.py
   ├── Screenshots/
   │   ├── application_running.png
   │   ├── bandit_scan.png
   │   ├── login_review.png
   │   ├── input_validation_review.png
   │   └── file_upload_review.png
   │
   ├── report/
   │   └── Secure_Coding_Review_Report.pdf
   │
   └── README.md
```

---

## Security Review Methodology

### 1. Manual Code Review

The source code was manually inspected to evaluate:

- Authentication security
- Input validation mechanisms
- File upload controls
- Session management
- Error handling practices

### 2. Static Code Analysis

Automated security analysis was performed using Bandit.

```bash
bandit app.py
```

The scan was used to identify common Python security issues and coding weaknesses.

---

## Application Features Reviewed

### Authentication Module

- Login functionality assessment
- Password security evaluation
- Authentication workflow analysis

### Input Validation

- User input handling review
- Validation and sanitization assessment

### File Upload Functionality

- Upload mechanism analysis
- File validation review
- Storage security assessment

### Session Security

- Session management evaluation
- Cookie security assessment

### Error Handling

- Application configuration review
- Debug settings verification

---

## Security Assessment Findings

| Security Area | Status | Observation |
|--------------|---------|-------------|
| Authentication | Needs Improvement | Password hashing not implemented |
| Input Validation | Partial | Limited validation controls |
| File Upload Security | Needs Improvement | No file restrictions enforced |
| Session Security | Not Implemented | Session management absent |
| Error Handling | Acceptable | Debug mode disabled |
| Static Analysis | Passed | No critical issues detected |

---

## Recommendations

### Authentication Security

- Implement password hashing using bcrypt or Argon2.
- Enforce strong password policies.
- Implement secure authentication mechanisms.

### Input Validation

- Validate all user inputs.
- Apply input sanitization.
- Use allow-list validation where possible.

### File Upload Security

- Restrict allowed file extensions.
- Enforce file size limitations.
- Validate MIME types before storage.

### Session Management

- Implement secure session handling.
- Enable Secure and HttpOnly cookie flags.
- Configure session expiration.

### Secure Development Practices

- Conduct regular code reviews.
- Integrate security testing into the development lifecycle.
- Keep dependencies updated.
- Follow OWASP Secure Coding Guidelines.

---

## Static Analysis Results

Bandit static analysis was successfully executed on the application source code.

### Command Used

```bash
bandit app.py
```

### Result

- Scan completed successfully.
- No critical security vulnerabilities detected.
- Manual review was used to identify additional areas for security improvement.

---

## Learning Outcomes

Through this project, the following cybersecurity concepts were explored:

- Secure Coding Practices
- Static Application Security Testing (SAST)
- Authentication Security
- Input Validation
- File Upload Security
- Session Management
- Security Risk Assessment
- Vulnerability Documentation
- Secure Software Development Lifecycle (SSDLC)

---

## Conclusion

The secure coding review successfully evaluated the Flask web application through both manual inspection and automated analysis techniques. While no critical vulnerabilities were identified by the static analysis tool, several areas for improvement were documented, including authentication, input validation, file upload security, and session management.

Implementing the recommended controls will improve the overall security posture of the application and support the development of more secure software systems.

---

## Author

**Thirukumaran S**  
Cyber Security Intern – CodeAlpha

---

## License

This project is intended for educational and cybersecurity learning purposes only.
