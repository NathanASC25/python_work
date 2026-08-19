html = '<p>See <a href="https://example.com/page">this page</a> and <a href="https://example.org/other">another</a>.</p>'

pos = html.find('href="')
start = pos + 6
end = html.find('"', start)
link = html[start:end]

# Prints: https://example.com/page

print(link)
