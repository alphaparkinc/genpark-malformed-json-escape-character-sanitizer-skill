from client import JSONEscapeSanitizer

raw = "{'action': 'fetch', 'timeout': 10,}"
res = JSONEscapeSanitizer.sanitize(raw)
print("Sanitized JSON:", res)
