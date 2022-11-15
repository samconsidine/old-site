import sys


preamble = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sam's site</title>
</head>
<body>

<style>
    body {
        margin-left: 1.5%;
        margin-right: 1.5%;
    }
    p {
        margin-bottom: 0; 
        margin-top: 0; 
        font-family: Georgia, 'Times New Roman', Times, serif;     
    }
</style>
"""

print(preamble)

with open(sys.argv[1]) as f:
    lines = f.readlines()
    
    for line in lines:
        if line.strip() == '':
            print('<br>')
        else:
            formatted_line = line.strip()
            formatted_line = formatted_line.replace("'", '&#39')
            print('<p>' + formatted_line.replace('\n', '') + '</p>')

postamble = """</body>
</html>
"""

print(postamble)