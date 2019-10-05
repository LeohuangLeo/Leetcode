class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_ = []
        for i in emails:
            i = i.split('@')
            i[0] = i[0].replace('.','')
            if '+' in i[0]:
                i[0] = i[0][:i[0].index('+')]
                i = ','.join(i)
                emails_.append(i)
            else:
                i = ','.join(i)
                emails_.append(i)

        return len(set(emails_))
