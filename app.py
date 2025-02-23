import requests
import pyfiglet
import threading
from termcolor import colored

SECURITY_HEADERS = {
    "Strict-Transport-Security": "Protects against man-in-the-middle attacks by enforcing HTTPS.",
    "Content-Security-Policy": "Prevents XSS attacks by restricting resource loading sources.",
    "X-Content-Type-Options": "Prevents MIME-type sniffing to reduce risk of XSS attacks.",
    "X-Frame-Options": "Prevents clickjacking attacks by restricting iframe embedding.",
    "X-XSS-Protection": "Enables browser XSS protection (deprecated but still useful).",
    "Referrer-Policy": "Controls how much referrer information is sent with requests.",
    "Permissions-Policy": "Restricts access to browser features like mic, camera, etc.",
    "Cache-Control": "Controls caching behavior to prevent sensitive data exposure.",
    "Expect-CT": "Prevents use of misissued SSL certificates."
}

def print_banner():
    banner = pyfiglet.figlet_format("Header Scanner", font="slant")
    print(colored(banner, "green"))
    print(colored("Developed by Faizalimam", "yellow"))
    print("=" * 60)

def check_header(headers, header_name):
    """Check if a header is present and print appropriate message."""
    if header_name in headers:
        print(colored(f"[✔] {header_name} is present.", "green"))
    else:
        print(colored(f"[✘] Missing {header_name}.", "red"))
        print(colored(f"    ➜ Suggestion: {SECURITY_HEADERS[header_name]}", "cyan"))

def analyze_headers(url):
    """Fetch headers from a URL and analyze security best practices."""
    try:
        print(colored(f"\nScanning {url}...\n", "blue"))
        response = requests.get(url, timeout=10)
        headers = response.headers

        missing_headers = []
        threads = []

        for header in SECURITY_HEADERS.keys():
            thread = threading.Thread(target=check_header, args=(headers, header))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("\n" + "=" * 60)
        print(colored("Summary:", "magenta", attrs=["bold"]))

        for header in SECURITY_HEADERS.keys():
            if header not in headers:
                missing_headers.append(header)

        if missing_headers:
            print(colored("\n[⚠] The following security headers are missing:", "red", attrs=["bold"]))
            for header in missing_headers:
                print(colored(f"- {header}: {SECURITY_HEADERS[header]}", "yellow"))
        else:
            print(colored("\n[✔] All critical security headers are present!", "green", attrs=["bold"]))

    except requests.exceptions.RequestException as e:
        print(colored(f"Error: {e}", "red"))

def main():
    print_banner()
    url = input(colored("Enter target URL: ", "yellow"))
    analyze_headers(url)

if __name__ == "__main__":
    main()
