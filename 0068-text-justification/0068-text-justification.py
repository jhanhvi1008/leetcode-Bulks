class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0

        while i < len(words):
            # Find how many words fit in the current line
            line_len = len(words[i])
            j = i + 1

            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i

            # Total characters without spaces
            total_chars = sum(len(word) for word in line_words)

            # Last line OR single word -> left justified
            if j == len(words) or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                # Fully justify
                total_spaces = maxWidth - total_chars
                gaps = num_words - 1

                even_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]

                    # Left slots get extra spaces
                    spaces = even_spaces + (1 if k < extra_spaces else 0)
                    line += " " * spaces

                line += line_words[-1]

            res.append(line)
            i = j

        return res
        