from typing import List


def getSignature(s: str) -> str:
    myarr = [0] * 26
    for letter in list(s):
        myarr[ord('a') - ord(letter)] += 1
    
    result = ""
    for a in range(len(myarr)):
         if myarr[a] != 0:
              result += chr(a + ord('a')) + str(myarr[a])
    
    return result
            

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # first iterate through the strings and build a hashmap
    wordMap = {}

    for str in strs:
        sig = getSignature(str)
        if sig in wordMap:
            wordMap[sig].append(str)
        else:
            wordMap[sig] = list()
            wordMap[sig].append(str)

    result = []
    for key in wordMap.keys():
        result.append(list(wordMap[key]))
    return result

strs1 = ["eat","tea","tan","ate","nat","bat"]
strs1 = ["",""]
print(groupAnagrams(strs1))
