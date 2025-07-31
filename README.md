# Telegram OTP Bot (5sim-powered)

## Description
This bot allows users to buy virtual numbers from 5sim.net for any supported service (Telegram, WhatsApp, etc.) and receive OTP codes directly in Telegram.

## Setup & Deployment (Railway)
1. Fork or clone this repo to your GitHub.
2. Go to Railway.app → **New Project** → **Deploy from GitHub** → select this repo.
3. In Railway, set environment variables under Settings:
   - `TELEGRAM_TOKEN`
   - `FIVESIM_API_KEY`
4. Railway auto-build & start the bot.
5. Bot runs 24/7 — no sleep.

## Usage
- `/start` – welcome message  
- `/buy telegram` – purchase a Telegram number and wait for OTP
