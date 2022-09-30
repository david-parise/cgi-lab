#!//usr/bin/env python3

import os
import json

# Print env variables as plain text
# print("Content-Type: text/plain\n")
# print(os.environ)

# Print env variables as JSON
print("Content-Type: application/json\n")
print(json.dumps(dict(os.environ), indent=2))

# Print query parameter data in HTML
# print("Content-Type: text/html\n")
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

