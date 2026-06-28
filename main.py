import sys
from asr import transcribe
from intent import detect_help_intent
from emergency import trigger_emergency
from vad import has_speech


def run_pipeline(audio_file):

    print(f"Processing: {audio_file}")

    # 1. VAD (placeholder)
    if not has_speech(audio_file):
        print("No speech detected.")
        return

    # 2. ASR
    text = transcribe(audio_file)
    print("Transcript:", text)

    # 3. Intent detection
    score = detect_help_intent(text)
    print("Help score:", score)

    # 4. Decision
    if score >= 1.0:
        trigger_emergency(text)
    else:
        print("No emergency triggered.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <audio_file>")
        exit(1)

    run_pipeline(sys.argv[1])
