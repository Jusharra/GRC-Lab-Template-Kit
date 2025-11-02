"""Lambda entry point & local runner."""
import argparse
import json
import os
from .modules import (
    iam_findings,
    scp_findings,
    securityhub_findings,
    access_analyzer_findings,
    cloudtrail_findings,
    reporting,
    narrative,
    email_utils,
)

def handler(event, context):
    enable_ai = os.getenv("AI_ENABLE", "false").lower() == "true"
    results = {
        "iam": iam_findings.run(),
        "scp": scp_findings.run(),
        "access_analyzer": access_analyzer_findings.run(),
        "cloudtrail": cloudtrail_findings.run(),
        "securityhub": securityhub_findings.run(),
    }
    csv_path = reporting.to_csv(results, out_dir=".")
    narrative_txt = narrative.build(results) if enable_ai else "AI narrative disabled"
    if os.getenv("EMAIL_TO"):
        email_utils.send_email(subject="GRC Lab Report", body=narrative_txt, attachments=[csv_path])
    return {"statusCode": 200, "body": json.dumps({"csv": csv_path, "ai": enable_ai})}

def _local_run(args):
    resp = handler({}, {})
    print(resp)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", action="store_true")
    _local_run(parser.parse_args())
