# 🚀 No More Ads Just to Find Your IP!

Ever get tired of opening a dozen tabs, watching 30‑second ads, and closing pop‑ups just to find out your external IP? Same here. Time to put an end to the madness.

This is your new best friend: fast, no‑nonsense, and copies your IP straight to the clipboard. No more wasted clicks!

## 🔍 What Is It?

A Python script that:

- Fetches your external IP (via `api.ipify.org`).
- Automatically copies it to the clipboard (with `pyperclip`).
- Offers a CLI interface with URL and timeout options.

## 🤔 Why Use It?

- **Ads-free**: Forget those annoying ads.
- **One command**: Run and get your IP instantly.
- **Cross-platform**: Works on Linux, macOS, Windows—anywhere Python runs.

## 🛠️ Requirements

- Python 3.6+
- `requests` library
- (Optional) `pyperclip` for clipboard support

## 🚀 Installation

```bash
pip install requests
# If you want clipboard support:
pip install pyperclip
```

## 🎯 Usage

```bash
python get_external_ip.py
```

**Options**:

- `-u`, `--url` : IP lookup service URL (default: `https://api.ipify.org`)
- `-t`, `--timeout` : Request timeout in seconds (default: 5)

Example:

```bash
python get_external_ip.py -u https://my-ip-service.com -t 3
```

## 🎉 Sample Output

```bash
$ python get_external_ip.py
INFO: External IP: 123.456.78.9
# And it’s already in your clipboard – just Ctrl+V to paste!
```

## 📝 License

MIT © You. Feel free to use, clone, and share with your penguin‑loving friends.

---

Made with love (and a pinch of laziness) by **Your Name Here**. ;) Now go paste that IP without the headache! 😎
