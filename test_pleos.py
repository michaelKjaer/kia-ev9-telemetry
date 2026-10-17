import json
import os
import sys
import urllib.error
import urllib.request

client_id = os.environ.get('PLEOS_CLIENT_ID')
client_secret = os.environ.get('PLEOS_CLIENT_SECRET')
if not client_id or not client_secret:
    sys.exit('Missing required GitHub Actions secrets.')

payload = json.dumps({'clientId': client_id, 'clientSecret': client_secret}).encode('utf-8')
request = urllib.request.Request(
    'https://api.pleos.ai/v1/auth/personal-token',
    data=payload,
    headers={'Brand': 'kia', 'Content-Type': 'application/json'},
    method='POST',
)
try:
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
        status = response.status
except urllib.error.HTTPError as exc:
    sys.exit(f'Pleos authentication failed with HTTP {exc.code} (response hidden).')
except urllib.error.URLError as exc:
    sys.exit(f'Connection failed: {type(exc.reason).__name__}')

if status == 200 and result.get('data', {}).get('accessToken'):
    print('SUCCESS: Pleos authentication works from GitHub Actions.')
else:
    sys.exit(f'Unexpected authentication response (HTTP {status}; sensitive response hidden).')
