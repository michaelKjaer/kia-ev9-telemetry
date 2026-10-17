# Kia EV9 Telemetry

First step: Test Pleos authentication from GitHub Actions without exposing credentials or tokens.

1. Create a private GitHub repository.
2. Add repository Actions secrets `PLEOS_CLIENT_ID` and `PLEOS_CLIENT_SECRET`.
3. Upload `test_pleos.py` and `.github/workflows/test-pleos.yml` preserving their paths.
4. Open Actions → Test Pleos connection → Run workflow.
5. Check the log for `SUCCESS: Pleos authentication works from GitHub Actions.`

This initial workflow is manual only; it does not yet collect or store vehicle data.
