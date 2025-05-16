import requests
import random
import string
import time

# Function to generate random username
def generate_username(length=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# Function to generate random email
def generate_email(domain="gmail.com", length=8):
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{name}@{domain}"

# Load proxies from a file (proxies.txt)
def load_proxies(filename="proxies.txt"):
    try:
        with open(filename, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        print(f"[+] Loaded {len(proxies)} proxies.")
        return proxies
    except FileNotFoundError:
        print("[-] proxies.txt not found. No proxy will be used.")
        return []

# Main function
def main():
    referral_code = input("Enter your referral code: ")
    password = input("Enter your password: ")
    url = f"https://defienergylabs.com/index?ref={referral_code} "

    iterations = int(input("How many accounts you willing to create? "))
    use_proxy = input("Use proxies? (y/n): ").lower() == 'y'

    proxies_list = load_proxies() if use_proxy else []

    with open("credentials.txt", "a") as cred_file, open("cookie.txt", "a") as cookie_file:
        for i in range(iterations):
            username = generate_username()
            email = generate_email()

            payload = {
                'username': username,
                'email': email,
                'password': password,
                'confirm_password': password,
                'referral_code': referral_code,
                'register': ''
            }

            # Select a random proxy
            proxy = None
            if use_proxy and proxies_list:
                proxy_str = random.choice(proxies_list)
                proxy = {
                    "http": proxy_str,
                    "https": proxy_str
                }
                print(f"[*] Using proxy: {proxy_str}")
            else:
                print("[*] No proxy used.")

            try:
                response = requests.post(url, data=payload, proxies=proxy, timeout=10)

                # Save credentials
                cred_file.write(f"Username: {username} | Email: {email}\n")

                # Extract cookies
                cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
                cookie_line = '; '.join([f"{k}={v}" for k, v in cookie_dict.items()])
                cookie_file.write(cookie_line + "\n")

                print(f"[{i+1}/{iterations}] Registered: {username} | Cookies: {cookie_line[:50]}...")

            except requests.exceptions.RequestException as e:
                print(f"[!] Request failed: {e}")

            # Random delay between 2-7 seconds
            delay = random.uniform(2, 7)
            print(f"[*] Sleeping for {delay:.2f}s...\n")
            time.sleep(delay)

    print("\n[+] Done.")
    print("[+] Credentials saved to 'credentials.txt'")
    print("[+] Cookies saved to 'cookie.txt'")

if __name__ == "__main__":
    main()