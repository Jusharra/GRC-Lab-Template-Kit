from src.lambda.modules import iam_findings, reporting

def test_iam_run_shape():
    data = iam_findings.run()
    assert isinstance(data, dict)
    assert "users_without_mfa" in data

def test_reporting_csv(tmp_path):
    path = reporting.to_csv({"iam": {"users_without_mfa": 1}}, out_dir=tmp_path.as_posix())
    assert path.endswith(".csv")
