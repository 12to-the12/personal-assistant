import hashlib

def quick_hash(text):
            m = hashlib.md5()
            m.update(text.encode("utf-8"))
            text_hash = str(int(m.hexdigest(), 16))[0:12]
            return text_hash