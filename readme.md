<div align="center">

# 🐧 The Free Wiki

**A curated, open-source knowledge base for Linux system administration, shell scripting, FFmpeg mastery, and power-user workflows.**

[![Live Site](https://img.shields.io/badge/Live-FreeWiki-38bdf8?style=for-the-badge&logo=githubpages&logoColor=white)](https://soimuen11.github.io/FreeWiki/)
[![Build with Jekyll](https://img.shields.io/badge/Jekyll-Theme_Midnight-121620?style=for-the-badge&logo=ruby&logoColor=red)](https://jekyllrb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## 💡 About The Project

**The Free Wiki** is a personal and open collection of solutions, command-line cheatsheets, custom shell scripts, and media processing recipes compiled by Phil Wayne. Started in June 2020, it serves as a battle-tested reference guide for resolving real-world Linux desktop & server issues, boosting daily terminal productivity, and organizing essential open-source tools.

---

## 🌟 Key Topics & Highlights

- **🐧 Linux System Administration**: Disk partitioning, `iptables` firewall rules, `dmesg` diagnostics, and distros reference.
- **⚡ Command-Line & Terminal Mastery**: Vim productivity tricks, fuzzy finders (`fzf`), Ranger file manager, `curl` recipes, and shell customisation.
- **🎥 FFmpeg & Screencasting**: Field-tested commands for high-performance screen recording, audio processing, and video transcoding.
- **📜 Automation Scripts**: Custom Linux scripts for daily maintenance, batch conversions, and automated desktop tasks.
- **🎨 Glassmorphic Responsive Interface**: Ultra-fast static site powered by Jekyll with a modern dark midnight UI designed for high contrast and readability across all devices.

---

## 🗺️ Wiki Structure

| Section | Description |
| :--- | :--- |
| 🏠 **[Home](https://soimuen11.github.io/FreeWiki/index.html)** | Introduction to the project, author bio, and quick links. |
| 🛠️ **[Issues](https://soimuen11.github.io/FreeWiki/issues.html)** | Diagnosed Linux errors, hardware compatibility notes, and step-by-step fixes. |
| 💡 **[Tips & Tricks](https://soimuen11.github.io/FreeWiki/tips-and-tricks.html)** | Comprehensive command-line cheatsheets, Vim configurations, and networking guides. |
| 🎬 **[FFmpeg](https://soimuen11.github.io/FreeWiki/ffmpeg.html)** | Essential screencasting, video cutting, audio extract, and stream encoding commands. |
| 📚 **[Resources](https://soimuen11.github.io/FreeWiki/resources.html)** | Hand-picked online learning resources, documentation links, and tech blogs. |
| 📜 **[Scripts](https://soimuen11.github.io/FreeWiki/scripts.html)** | Custom Bash and shell scripts for system automation and workflow enhancement. |

---

## 🛠️ Local Development & Setup

To run and preview **The Free Wiki** locally on your machine:

### Option A: Using Jekyll (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/soimuen11/FreeWiki.git
cd FreeWiki

# 2. Install dependencies
bundle install

# 3. Start local development server
bundle exec jekyll serve
```
Open `http://localhost:4000` in your web browser.

### Option B: Using Python (Automatic Build & Server)

Because Jekyll projects use `.markdown` templates and layouts, running `http.server` directly in the root directory serves raw markdown files. Use the included `build.py` helper script to compile and serve the site automatically:

```bash
# Compile markdown files into HTML and start local server
python3 build.py
```
Open `http://localhost:8000` in your web browser.

*Alternatively, if you already have the compiled `_site/` directory:*
```bash
python3 -m http.server 8000 -d _site
```

---

## 🤝 Contributing & Feedback

Suggestions, fixes, and contributions are always welcome!
- Found a bug or an outdated command? Feel free to open an **[Issue](https://github.com/soimuen11/FreeWiki/issues)**.
- Want to add a new tip or script? Fork the repository, make your changes, and submit a **Pull Request**.

---

## 👨‍💻 Credits & Authors

- **Phil Wayne** ([@soimuen11](https://github.com/soimuen11)) - Project Creator & Content Maintainer
  - **Blog**: [madlibrarianwriting.poetry.blog](https://madlibrarianwriting.poetry.blog/)
  - **Portfolio**: [portfolio.phiannetta.xyz](https://portfolio.phiannetta.xyz)
- **Semplicemente.io** ([@Semplicementeio](https://github.com/Semplicementeio)) - Modern UI/UX Redesign & Documentation

