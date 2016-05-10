

original_line = raw_input("Enter A line to reverse")

line_break = original_line.split()

reverse_line = []

for word in line_break:
    reverse_line.insert(0,word)


print " ".join(reverse_line)
