import os, csv
from datetime import datetime

def to_csv(results: dict, out_dir: str = ".") -> str:
    path = os.path.join(out_dir, f"grc_report_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["domain", "metric", "value"])
        for domain, metrics in results.items():
            for k, v in metrics.items():
                w.writerow([domain, k, v])
    return path
