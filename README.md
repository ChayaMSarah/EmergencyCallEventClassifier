# Voice Emergency Request System

## Overview

This system provides a voice-based alternative to a physical emergency button, enabling users to request help through natural speech. It is designed for deployment on a low-power Android tablet provided by a health organization.

The goal is to reliably detect user requests for assistance while remaining efficient in terms of battery and compute usage.

---

## System Architecture

The system is composed of three sequential stages:
Audio Input
→ 
Audio Activity Filter
→ 
Help Intent Detection
→ 
Emergency Action Handler

---

## 1. Audio Activity Filter

### Purpose
To filter out irrelevant audio and reduce unnecessary processing.

### Functionality
This stage determines whether the incoming audio is likely to contain human vocal activity.

It filters out:
- Silence
- Background noise
- Non-speech sounds (e.g., barking, whistling, humming)

### Output
- `PASS`: Potential human speech detected
- `DROP`: No relevant vocal activity

### Notes
This stage is a lightweight pre-processing step and does not perform any semantic or intent analysis.

---

## 2. Help Intent Detection (Core Component)

### Purpose
To determine whether the user is attempting to request emergency assistance.

### Functionality
This stage analyzes short audio segments for indicators of help intent, including:

- Explicit requests (e.g., “help”, “call an ambulance”)
- Implicit requests (e.g., “I fell”, “I need assistance”)
- Partial or interrupted speech (e.g., “he…lp”)
- Short contextual patterns over a limited time window

### Output
A continuous score: help_score ∈ [0.0, 1.0]

### Decision Thresholds
- `≥ 0.8` → Trigger emergency workflow
- `0.5 – 0.8` → Uncertain; continue monitoring or optional confirmation
- `< 0.5` → No action

---

## 3. Emergency Action Handler

### Purpose
To execute the emergency response workflow once a help request is confirmed.

### Functionality
Depending on organizational configuration, this stage may:

- Notify emergency response services or backend systems
- Send device identifiers and location data (if available)
- Initiate live communication channels
- Trigger escalation procedures defined by the organization

---

## Design Principles

### Safety-First Behavior
The system is optimized to avoid missing valid help requests, even in cases of partial or imperfect speech.

### No Fixed Wake Word Requirement
Users are not required to use predefined activation phrases. Help requests are recognized from natural speech.

### On-Device Optimization
The system is designed to operate under constraints typical of tablet hardware:
- Limited CPU
- Limited battery
- Intermittent connectivity

### Separation of Concerns
Each stage is independent:
- Audio filtering handles signal validity
- Intent detection handles meaning
- Action handler handles emergency response

---

## Key Design Decision

The system uses **natural help-intent detection** instead of a fixed wake-word mechanism, allowing users to request assistance in a flexible and natural manner.

---

## Future Extensions (Optional)

- Multilingual support
- Improved noise robustness
- User-specific adaptation
- Optional confirmation flow for medium-confidence cases

# Voice Emergency MVP

Minimal end-to-end prototype for a voice-based emergency request system.

## Pipeline

Audio File → VAD → Hebrew ASR → Help Intent Detection → Emergency Trigger

## Run

```bash
pip install -r requirements.txt
python main.py sample.wav
🚀 How to run
git init
git add .
git commit -m "Initial voice emergency MVP"
pip install -r requirements.txt
python main.py sample.wav
🔧 What this is (important)

This is NOT production logic.

It gives you:

full working pipeline
Hebrew ASR integration
plug-in points for ML later
🧠 What you upgrade later

Replace:

intent.py → ML model (Hebrew fine-tuned)
vad.py → real audio VAD
threshold logic → probabilistic scoring system
