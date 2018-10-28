class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        hash_table = {}
        for email in emails:
            key = ''
            for s in email:
                if s == '.':
                    continue
                if s == '+':
                    break
                else:
                    key += s
            at_index = email.index('@')
            key += email[at_index + 1:]
            if key not in hash_table:
                hash_table[key] = 1
        return len(hash_table)
            
