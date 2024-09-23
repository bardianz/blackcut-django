
import re
 


def check_is_persian(text):
    pattern = r"^[\u0600-\u06FF\s]+$"
 
    if re.match(pattern, text):
        print("YESSSSSSSS")
        return True
    else:
        print("NO")
        return False
