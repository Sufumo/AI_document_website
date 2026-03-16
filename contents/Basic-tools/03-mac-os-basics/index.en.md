---
title: Mac OS Basics
draft: false
---

# Mac OS Basics

## Why Configure macOS?

macOS is already pretty developer-friendly out of the box, but there are a few hidden settings that can make your life significantly easier. From finding files to managing your workspace, this guide covers the essentials every developer should know.

---

## Quick Search: Spotlight

### The Built-in Superpower

macOS comes with **Spotlight Search** — and it's actually good. No need to install anything extra.

Press `Command + Space` and start typing. Spotlight searches apps, files, emails, contacts, even does calculations and currency conversions.

![](./images/Mac/file-20260107123351255.png)

![](./images/Mac/file-20260107123528095.png)

💡 **Pro Tip**: Spotlight learns from your usage. The more you use it, the smarter it gets at predicting what you're looking for.

---

## System Language Settings

Want to switch between English and Chinese? Here's how:

### Step 1: Open Language Settings

Go to **System Settings** → **General** → **Language & Region**.

![](./images/Mac/file-20260106175129911.png)

### Step 2: Add and Prioritize Your Language

Add **English** (or your preferred language) to "Preferred Languages" and drag it to the top. macOS will update after a restart or logout.

![](./images/Mac/file-20260106175220146.png)

---

## File Management Essentials

### Finder: Your File Command Center

**Finder** is the heart of file management on macOS. Click the smiley face icon in your Dock (bottom left by default) to open it.

![](./images/Mac/file-20260106180402157.png)

---

### Show File Extensions & Hidden Files

⚠️ **Critical for Developers**: By default, macOS hides file extensions and system files. When you're working with `.gitignore`, `.env`, `.zshrc`, you need to see these.

**Show File Extensions:**

1. Open **Finder** → **Settings** (or press `Command + ,`)

2. Click **Advanced** → Check **Show all filename extensions**

![](./images/Mac/file-20260106180156222.png)

**Show Hidden Files:**

Press `Command + Shift + .` to toggle hidden files visibility. Press it again to hide them.

💡 **Pro Tip**: Files starting with a dot (like `.gitignore`) are hidden by default on Unix-based systems. This shortcut is your best friend.

---

### The Path Bar

Knowing where you are in the file system is crucial. Let's enable the path bar:

**Step 1**: In Finder, go to **View** → **Show Path Bar**

![](./images/Mac/file-20260107163525369.png)

Now you'll see your current location at the bottom of every Finder window.

**Step 2**: Right-click anywhere in the path bar to open a terminal at that location

![](./images/Mac/file-20260109145541008.png)

Select **Open in Terminal** and you're ready to run commands.

![](./images/Mac/file-20260109145641593.png)

---

### File Compression Made Easy

**Compress**: Right-click any file or folder → Select **Compress "..."** → Creates a `.zip` file

![](./images/Mac/file-20260106180748623.png)

**Extract**: Just double-click any `.zip` file — macOS handles it natively

![](./images/Mac/file-20260107121928478.png)

No extra software needed. It just works.

---

## Keep Your Dock Clean

The Dock is prime real estate. A cluttered Dock means a cluttered workflow. Here's how to keep it organized:

**Remove Unused Apps:**

Right-click (or two-finger click) any Dock icon → **Options** → **Remove from Dock**

![](./images/Mac/file-20260106175556075.png)

| What to Keep | What to Remove |
|--------------|----------------|
| Daily apps (Terminal, VS Code, Browser) | Apps you rarely use |
| Apps you're learning | Duplicates or alternatives |
| Communication tools | Installers, one-time tools |

---

## Trackpad Optimization

The Mac trackpad is best-in-class. Let's make it even better.

### Enable Tap to Click

No more physically pressing down. A light tap is all you need.

Go to **System Settings** → **Trackpad** → Enable **Tap to click**

![](./images/Mac/file-20260107122542163.png)

You can also customize other trackpad behaviors to match your preferences.

![](./images/Mac/file-20260107124740080.png)

### Customize Gestures

| Feature | What It Does | Default |
|---------|--------------|---------|
| **Look up & data detectors** | Quick dictionary lookup | Three-finger tap on a word |
| **Secondary click** | Right-click functionality | Two-finger tap or click in corner |

![](./images/Mac/file-20260107180059440.png)

![](./images/Mac/file-20260107180237427.png)

💡 **Pro Tip**: Spend 5 minutes in System Settings → Trackpad exploring all the gestures. Muscle memory will thank you later.

---

## File Sharing with AirDrop

### The Apple Ecosystem Superpower

**AirDrop** lets you instantly share files between Mac, iPhone, and iPad — no internet required, no file size limits, no hassle.

### How to Use AirDrop

**Step 1**: Open AirDrop from the Control Center (top-right corner of your screen)

![](./images/Mac/file-20260107175549496.png)

**Step 2**: In any app, click the **Share** button and select **AirDrop**

![](./images/Mac/file-20260106180901363.png)

![](./images/Mac/file-20260107171018286.png)

**Step 3**: Select the recipient from the list of nearby devices

![](./images/Mac/file-20260107171354103.png)

### Find Your Mac's Name

To make sure people can find you, check your Mac's name:

Click the **Apple menu** → **About This Mac** → **More Info**

![](./images/Mac/file-20260107175634492.png)

![](./images/Mac/file-20260107175752932.png)

Your Mac's name appears here. This is what others will see when they try to AirDrop to you.

---

## Summary

1. **Spotlight Search**: `Command + Space` for instant search
2. **Language Settings**: System Settings → General → Language & Region
3. **Show file extensions**: Finder Settings → Advanced → Show all filename extensions
4. **Show hidden files**: `Command + Shift + .`
5. **Path bar**: View → Show Path Bar (right-click to open Terminal)
6. **Clean Dock**: Remove unused apps, keep only essentials
7. **Trackpad**: Enable "Tap to click" for efficiency
8. **AirDrop**: Instant file sharing across Apple devices

---

*Your Mac is now dialed in for developer productivity. These aren't just tips — they're the foundation of an efficient workflow.*
