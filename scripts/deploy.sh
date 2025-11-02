#!/usr/bin/env bash
set -euo pipefail
STAGE=${1:-dev}
ARTIFACT=package-${STAGE}.zip
echo "[+] Packaging Lambda -> ${ARTIFACT}"
zip -r ${ARTIFACT} src/ > /dev/null
echo "[i] Customize CFN deploy for your account:"
echo "aws cloudformation deploy --template-file templates/access-review-real.yaml \  --stack-name grc-lab-${STAGE} \  --parameter-overrides ArtifactBucket=your-bucket ArtifactKey=${ARTIFACT} \  --capabilities CAPABILITY_NAMED_IAM"
