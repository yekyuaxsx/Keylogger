# Keylogger

This project is a basic keylogger built using Python. It is designed to capture keystrokes and log them to a file for later review. It is intended for educational purposes only to understand how keylogging works and to help learn about cybersecurity practices.

## Features:

- Captures keystrokes from the user.
- Logs keypresses into a local file for analysis.
- Written in Python using libraries such as `pynput`.

**Disclaimer:** This project is for educational purposes only. It should not be used for malicious intent or without the consent of the target user. Unauthorized use of a keylogger can result in legal consequences.

---

## Troubleshooting

### If you encounter a `pynput` import error:

You should run the project in a virtual environment. To do this:

1. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**

   - **Windows:**

   ```bash
   venv\Scripts\activate
   ```

   - **Linux/macOS:**

   ```bash
   source venv/bin/activate
   ```

3. **Install the required library:**

   ```bash
   pip install pynput
   ```

By following these steps, you should be able to successfully install the `pynput` library and run your project.

---

### If you encounter an email error:

1. First, go to the settings section of your email account and enable two-factor authentication (2FA) from the security section.
2. Then, go to the **App Passwords** section, generate a password, and enter that password in the password field of your project.

This should resolve any email-related issues when using your project.
