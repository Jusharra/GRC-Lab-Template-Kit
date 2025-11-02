def send_email(subject: str, body: str, attachments=None):
    print(f"[EMAIL] {subject}: {body[:80]}...")
    if attachments:
        for a in attachments:
            print(f"[EMAIL] attached: {a}")
