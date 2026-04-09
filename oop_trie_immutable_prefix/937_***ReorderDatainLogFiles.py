class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        letter: content, identifiers (lexicographically)
        digits: maintain their relative ordering
        logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        sorting tuple: if letter and digit, >> letter, digit
        if letter and letter, >> (content, identifier)
        if digit and digt, >> relative order

        """
        def ordering_format(log):
            identifier, content = log.split(" ", 1)
            
            if content[0].isdigit():
                return ("Z",)
            else:
                return ("A", content, identifier)


        logs.sort(key=lambda word: ordering_format(word))

        return logs



class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort_key(log):
            identifier, rest = log.split(" ", 1)
            is_digit = rest[0].isdigit()
            if is_digit:
                return (1,)  # digit logs last, and all digits will PRESERVE their order
            return (0, rest, identifier)  # letter logs sorted by content then id

        return sorted(logs, key=lambda x: sort_key(x)) # return sorted(logs, key=sort_key)


# OOP way by defining __lt__()
# Note: In Python, Sorting is STABLE, so for __lt__(a, b) return True means a < b, but returning False doesn't mean b >= a, 
# instead, it means 'a is NOT less than b', so it will PRESERVE the original order !!!!
class Log:
    def __init__(self, log):
        self.log = log
        parts = log.split(" ", 1) # Split only into a maximum of two parts based on the first space character found
        # parts = log.split(" ", k) >> means split into maximum of K + 1 parts
        self.identifier = parts[0]
        self.contents = parts[1]
        self.is_digit = self.contents[0].isdigit()

    def __lt__(self, other):
        # Case 1: one letter-log, one digit-log
        if not self.is_digit and other.is_digit:
            return True
        if self.is_digit and not other.is_digit:
            return False

        # Case 2: both digit-logs → preserve original order
        if self.is_digit and other.is_digit:
            return False

        # Case 3: both letter-logs → compare by contents, then identifier
        if self.contents != other.contents:
            return self.contents < other.contents
        return self.identifier < other.identifier

class Solution2:

    def reorderLogFiles2(self, logs: List[str]) -> List[str]:
        """

        ["let1 art can",
         "let3 art zero",
         "let2 own kit dig",
         "dig1 8 1 5 1",
         "dig2 3 6"]
        """
        log_objects = [Log(log) for log in logs]
        log_objects.sort()
        return [obj.log for obj in log_objects]