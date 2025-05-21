# Python-Extension-Automation
Firefox Extension Automation with Selenium (Educational Use Only)

This project is a Python automation script that interacts with a Firefox browser extension UI using Selenium WebDriver. It demonstrates how you can load a custom Firefox profile, access a locally installed extension, and simulate user input for learning and testing automation techniques.

⚠️ Disclaimer:
This project is intended strictly for educational purposes to learn about browser automation, Selenium interaction with Firefox extensions, and ethical automation practices.
Do NOT use this tool on unauthorized systems or services.
Misuse may violate platform terms and laws.

🚀 Features
Loads a Firefox extension using its moz-extension:// URL.

Injects a random combination of seed phrases from a local file.

Simulates user interaction by filling form fields and clicking buttons.

Saves any successful attempts to a result file.

🧰 Requirements
You need the following installed on your system:

Python 3.7+

GeckoDriver – WebDriver for Firefox

Mozilla Firefox (with the extension already installed)

selenium library

Install dependencies with:
pip install selenium
🔧 Setup Instructions
Clone this repository:

git clone https://github.com/your-username/Python-Extension-Automation.git
cd Python-Extension-Automation
Download GeckoDriver:

Download from: https://github.com/mozilla/geckodriver/releases

Make it executable and place it somewhere accessible (e.g., /usr/local/bin/ or reference it directly in the script as done here).

Set your paths in main.py:

Edit the following two lines with your actual local paths:
gecko_path = '/home/noname/Desktop/okx/geckodriver'
firefox_profile = '/home/noname/.mozilla/firefox/2ykusf7u.default-esr'
gecko_path is the path to the GeckoDriver binary.

firefox_profile is the path to your Firefox profile directory which contains your installed extension.

You can find your Firefox profile path using:

about:profiles
in Firefox address bar.

Update the extension URL:
target_url = 'moz-extension://<your-extension-id>/index.html'
This moz-extension:// URL is local to your machine and changes each time Firefox restarts. You will need to check this before each session.

🧪 How It Works
The script reads a list of words from cleaned.txt.

It picks 12 random words and attempts to insert them into all input fields with class mnemonic-words-inputs__container__input.

If the confirmation button becomes clickable (based on its class containing 'okui-btn'), it's considered a potential success.

That set of words is saved in successful_attempts_okx_1.txt.
