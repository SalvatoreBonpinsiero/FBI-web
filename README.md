<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/d/da/Seal_of_the_Federal_Bureau_of_Investigation.svg" width="100" alt="FBI-Web Logo">

# 🕸️ FBI-Web — OSINT Spider

**Minimal link-analysis tool for building visual spider webs of OSINT entities.**

[![Python](https://img.shields.io/badge/python-3.8%2B-F2C200?style=flat-square&labelColor=111)](#)
[![Flask](https://img.shields.io/badge/flask-2.0%2B-F2C200?style=flat-square&labelColor=111)](#)
[![D3.js](https://img.shields.io/badge/d3.js-v7-F2C200?style=flat-square&labelColor=111)](#)
[![License](https://img.shields.io/badge/license-MIT-F2C200?style=flat-square&labelColor=111)](#license)

<img src="https://raw.githubusercontent.com/SalvatoreBonpinsiero/FBI-web/refs/heads/main/prev.png" alt="Preview" width="100%">

</div>

---

## ✨ Features

- 🕸️ Interactive force-directed graph (D3.js)
- 🎯 Central target node
- 🧩 Typed entities: domain, ip, email, phone, person, username, org, url
- 🔗 Custom links between any two entities
- 🖱️ Drag, zoom, pan in real time
- 📄 TXT report export
- 🎨 Minimal design — white + yellow, Open Sans
- 🔒 Fully local — no APIs, no telemetry

---

## 🚀 Installation

```bash
git clone https://github.com/SalvatoreBonpinsiero/FBI-web.git
cd FBI-web
pip install -r requirements.txt
python app.py
