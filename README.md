
# Header Scanner Tool
![Image](https://github.com/user-attachments/assets/e9caa375-ed8d-47c7-b05c-317521c1e4cf)
**Header Scanner** is a Python-based tool designed to scan website HTTP headers for critical security headers, ensuring your website is protected against common web vulnerabilities like XSS attacks, clickjacking, man-in-the-middle attacks, and more. 

Developed by **Faizalimam**, this tool identifies missing security headers and provides actionable suggestions on how to fix them.

---

## Features

- Scans HTTP response headers for important security headers.
- Identifies missing security headers like `Strict-Transport-Security`, `Content-Security-Policy`, and more.
- Provides clear suggestions for fixing missing headers.
- Built with **multithreading** for fast scanning and optimized performance.
- Easy-to-use command-line interface.

---

## Security Headers Checked

The following security headers are checked by the tool:

- **Strict-Transport-Security**: Protects against man-in-the-middle attacks by enforcing HTTPS.
- **Content-Security-Policy**: Prevents XSS attacks by restricting resource loading sources.
- **X-Content-Type-Options**: Prevents MIME-type sniffing to reduce the risk of XSS attacks.
- **X-Frame-Options**: Prevents clickjacking attacks by restricting iframe embedding.
- **X-XSS-Protection**: Enables browser-level XSS protection (deprecated but still useful).
- **Referrer-Policy**: Controls how much referrer information is sent with requests.
- **Permissions-Policy**: Restricts access to browser features like microphone, camera, etc.
- **Cache-Control**: Controls caching behavior to prevent sensitive data exposure.
- **Expect-CT**: Prevents the use of misissued SSL certificates.

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Faizalimam990/Header-scanner
    cd headerscanner
    ```

2. **Install required Python libraries**:
    ```bash
    pip install requests pyfiglet termcolor
    ```

---

## Usage

1. **Run the tool**:
    ```bash
    python headerscanner.py
    ```

2. **Enter the URL** when prompted, and the tool will scan the website’s headers:
    ```bash
    Enter target URL: https://example.com
    ```

The tool will display which security headers are present and which are missing, along with helpful suggestions for each missing header.

---

## Example Output

```bash
 Header Scanner     
    Developed by Faizalimam
 ==================================================
Enter target URL: https://example.com
Scanning https://example.com...

[✔] Strict-Transport-Security is present.
[✘] Missing Content-Security-Policy.
    ➜ Suggestion: Prevents XSS attacks by restricting resource loading sources.
[✔] X-Content-Type-Options is present.
[✘] Missing X-Frame-Options.
    ➜ Suggestion: Prevents clickjacking attacks by restricting iframe embedding.
[✔] X-XSS-Protection is present.
[✔] Referrer-Policy is present.

===============================================================
Summary:
[⚠] The following security headers are missing:
- Content-Security-Policy: Prevents XSS attacks by restricting resource loading sources.
- X-Frame-Options: Prevents clickjacking attacks by restricting iframe embedding.
