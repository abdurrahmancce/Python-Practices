# Name with whitespace, tab, and newline
name = "\t   Abdur Rahman\n   "

# Print with whitespace visible
print("Original name with whitespace:",name)

# Use lstrip() - removes leading whitespace
print("Using lstrip():",name.lstrip())

# Use rstrip() - removes trailing whitespace
print("Using rstrip():",name.rstrip())

# Use strip() - removes both leading and trailing whitespace
print("Using strip():",name.strip())
