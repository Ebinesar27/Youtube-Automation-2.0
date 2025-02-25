class Line():



    def cut_lines(self,text):
        words = text.split()
        lines = [' '.join(words[i:i+5]) for i in range(0, len(words), 5)]
        return '\n'.join(lines)

# Example Usage
# text = "This is an example text that needs to be formatted with five words per line."
# formatted_text = cut_lines(text)
# print(formatted_text)