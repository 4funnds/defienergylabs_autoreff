# DeFi Energy Labs Bot

## Overview
An automated registration bot for DeFi Energy Labs platform. This bot helps automate the account creation process using customizable parameters, proxy support, and credential management.

## Table of Contents
- [Overview](#overview)
- [Quickstart](#quickstart)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)

## Quickstart
1. Clone this repository
2. Install the required dependencies:
```bash
pip install requests
```
3. Add your proxies to `proxies.txt` (optional)
4. Run the bot:
```bash
python bot.py
```

## Features
- 🤖 Automated account registration
- 📧 Random username and email generation
- 🔄 Proxy support for enhanced privacy
- 💾 Automatic credential saving
- 🍪 Cookie management
- ⏱️ Random delays between requests
- 📝 Detailed logging and progress tracking

### Key Components
- Credential storage in `credentials.txt`
- Cookie storage in `cookie.txt`
- Proxy list support via `proxies.txt`
- Customizable registration parameters