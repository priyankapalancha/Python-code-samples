import uuid
import secrets
import base64

uuid = str(uuid.uuid4().fields[-1])[:8]

print(uuid)