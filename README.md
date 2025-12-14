# 📡 SiteSentry: Automated Uptime Monitor

A Python automation script that periodically checks the health of specified websites. If a website goes down (status code != 200), it automatically sends an **Email Alert** to the administrator.



## 🚀 Features

* **Automated Scheduling:** Runs checks every 5 minutes (configurable) using the `schedule` library.
* **Status Inspection:** Detects 404 (Not Found), 500 (Server Error), and Connection Timeouts.
* **Email Alerts:** Uses Python's built-in `smtplib` to send real-time notifications via Gmail when a failure is detected.
* **Exception Handling:** Robust error catching for DNS failures or network drops.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **HTTP Requests:** `requests` library.
* **Scheduling:** `schedule` library.
* **Notifications:** `smtplib` (Standard Library).

