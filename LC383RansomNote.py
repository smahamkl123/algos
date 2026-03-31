
def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag_dict = {}

    for i, v in enumerate(list(magazine)):
        if(v in mag_dict):
            mag_dict[v] += 1
        else:
            mag_dict[v] = 1

    for i, v in enumerate(list(ransomNote)):
        if v not in mag_dict:
            return False
        else:
            mag_dict[v] -= 1
            if mag_dict[v] < 0:
                return False

    return True

ransomNote = "aa"
magazine = "aa"

print(canConstruct(ransomNote, magazine))