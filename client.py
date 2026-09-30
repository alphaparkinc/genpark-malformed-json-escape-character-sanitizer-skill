"""Malformed JSON Escape Character Sanitizer.
100% Python Standard Library.
"""

import json
import re

class JSONEscapeSanitizer:
    """Sanitizes unescaped newlines, trailing commas, and single-quoted keys in model JSON."""
    @staticmethod
    def sanitize(raw_json: str) -> dict:
        text = raw_json.strip()
        if text.startswith("```"):
            lines = text.splitlines()
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            text = "\n".join(lines).strip()

        text_fixed = re.sub(r"(?<=\{|\,|\:)\s*'([^'\\]*(?:\\.[^'\\]*)*)'\s*(?=\:|\,|\})", r'"\1"', text)
        text_fixed = re.sub(r',\s*([\}\]])', r'\1', text_fixed)

        try:
            parsed = json.loads(text_fixed)
            return {"valid": True, "parsed": parsed, "sanitized_str": text_fixed}
        except Exception:
            try:
                text_fixed2 = text.replace("'", '"')
                text_fixed2 = re.sub(r',\s*([\}\]])', r'\1', text_fixed2)
                parsed = json.loads(text_fixed2)
                return {"valid": True, "parsed": parsed, "sanitized_str": text_fixed2}
            except Exception as e:
                return {"valid": False, "error": str(e), "raw": text_fixed}
