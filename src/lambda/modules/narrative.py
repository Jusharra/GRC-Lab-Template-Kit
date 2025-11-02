def build(results: dict) -> str:
    lines = ["Executive Narrative:"]
    if results.get("iam", {}).get("users_without_mfa", 0) > 0:
        lines.append("- Enforce MFA for all IAM users; residual key risk persists.")
    if results.get("securityhub", {}).get("findings_open", 0) > 0:
        lines.append("- Prioritize remediation of Security Hub findings by severity and service.")
    if not results.get("cloudtrail", {}).get("multi_region_trail", False):
        lines.append("- Enable multi-region CloudTrail for unified auditing.")
    return "\n".join(lines) or "No issues detected."
