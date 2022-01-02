<h1 align= center><b>⭐️ Green_Player ⭐️</b></h1>
<h3 align = center> A Telegram Music Bot written in Python using Pyrogram and Py-Tgcalls </h3>

<p align="center">
<a href="https://python.org"><img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python"></a>
<br>
    <img src="https://img.shields.io/github/license/g-r-e-e-n/Music_player?style=for-the-badge" alt="LICENSE">
    <img src="https://img.shields.io/github/contributors/g-r-e-e-n/Music_player?style=for-the-badge" alt="Contributors">
    <img src="https://img.shields.io/github/repo-size/g-r-e-e-n/Music_player?style=for-the-badge" alt="Repository Size"> <br>
    <img src="https://img.shields.io/github/forks/g-r-e-e-n/Music_player?style=for-the-badge" alt="Forks">
    <img src="https://img.shields.io/github/stars/g-r-e-e-n/Music_player?style=for-the-badge" alt="Stars">
    <img src="https://img.shields.io/github/watchers/g-r-e-e-n/Music_player?style=for-the-badge" alt="Watchers">
    <img src="https://img.shields.io/github/commit-activity/w/g-r-e-e-n/Music_player?style=for-the-badge" alt="Commit Activity">
    <img src="https://img.shields.io/github/issues/g-r-e-e-n/Music_player?style=for-the-badge" alt="Issues">
</p>

## ✨ <a name="features"></a>Features

### ⚡️ Fast & Light

Starts streaming your inputs while downloading and converting them. Also, it
doesn't make produce files.

### 👮🏻‍♀️ Safe and handy

Restricts control and sensitive commands to admins.

### 🗑 Clean and spam free

Deletes old playing trash to keep your chats clean.

### 😎 Has cool controls

Lets you switch stream mode, loop, pause, resume, mute, unmute anytime.

### 🖼 Has cool thumbnails

Response your commands with cool thumbnails on the chat.

### 😉 Streams whatever you like

You can stream audio or video files, YouTube videos with any duration,
YouTube lives, YouTube playlists and even custom live streams like radios or m3u8 links or files in
the place it is hosted!

### 📊 Streams in multiple places

Allows you to stream different things in multiple chats simultaneously. Each
chat will have its own song queue.

### 🗣 Speaks different languages

Music Player is multilingual and speaks [various languages](#languages),
thanks to the translators.

## 🚀 <a name="deploy"></a>Deploy

[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Note: `First Fork The Repo Then Click On Deploy To Heroku Button!`


## ☁️ <a name="self_host"></a>Self Host

```bash
$ git clone https://github.com/g-r-e-e-n/MusicPlayer
$ cd MusicPlayer
$ cp sample.env .env
< edit .env with your own values >
$ sudo docker build . -t musicplayer
$ sudo docker run musicplayer
```

## ⚒ <a name="configs"></a>Configs

- `API_ID`: Telegram app id.
- `API_HASH`: Telegram app hash.
- `SESSION`: Pyrogram string session. You can generate from string generator.
- `SUDOERS`: ID of sudo users (separate multiple ids with space).
- `QUALITY`: Custom stream quality for the userbot in vc. Default: `medium`
- `PREFIX`: Commad prefixes (separate multiple prefix with space). Eg: `! /`
- `LANGUAGE`: An [available](#languages) bot language (can change it anytime). Default: `en`

## 📄 <a name="commands"></a>Commands

Command | Description
:--- | :---
• /ping | Check if alive or not
• /start / /help | Show the help for commands
• /mode / /switch | Switch the stream mode (audio/video)
• /p / /play [song name or youtube link] | Play a song in vc, if already playing add to queue
• /radio / /stream [radio url or stream link] | Play a live stream in vc, if already playing add to queue
• /playlist [youtube playlist link] | Play the whole youtube playlist at once
• /skip / /next | Skip to the next song
• /mute | Mute the current stream
• /unmute | Unmute the muted stream
• /pause | Pause the current stream
• /resume | Resume the paused stream
• /list / /queue | Show the songs in the queue
• /mix / /shuffle | Shuflle the queued playlist
• /loop / /repeat | Enable or disable the loop mode
• /lang / /language [language code] | Set the bot language in group
• /import | Import queue from exported file
• /export | Export the queue for import in future
• /stop / /leave | Leave from vc and clear the queue

## 🗣 <a name="languages"></a>Languages

```text
en    English
```

## 💜 <a name="contribute"></a>Contribute

New languages, bug fixes and improvements following
[our contribution guidelines](./CONTRIBUTING.md) are warmly welcomed!

## 📃 <a name="license"></a>License

Music Player is licenced under the GNU Affero General Public License v3.0.
Read more [here](./LICENSE).
