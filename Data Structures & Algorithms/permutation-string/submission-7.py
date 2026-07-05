class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        t = 0
        freq = {}
        for i in s2[:len(s1)]:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        tar_freq = {}
        for i in s1:
            if i in tar_freq:
                tar_freq[i] += 1
            else:
                tar_freq[i] = 1
        new_char = 0
        for i in range(len(s2)):
            if freq == tar_freq:
                return True

            else:
                if freq[s2[i]] == 1:
                    del freq[s2[i]]
                else:
                    freq[s2[i]] -= 1

                if i+len(s1) < len(s2):
                    new_char = s2[i + len(s1)]

                    if new_char in freq:
                        freq[new_char] += 1
                    else:
                        freq[new_char] = 1

            print(new_char, freq)

        return False