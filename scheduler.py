import json
from datetime import datetime

def run_due_once():
    try:
        with open("schedule.json", "r", encoding="utf-8") as f:
            jobs = json.load(f)
    except:
        print("schedule.json bulunamadı")
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    for job in jobs:
        if job["publish_at"] == now:
            print("Video gönderiliyor:", job["file"])
            print("Caption:", job["caption"])
            print("OK (şimdilik mock sistem)")