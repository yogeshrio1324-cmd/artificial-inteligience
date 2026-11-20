
# Web Blog using HTML Tags
# Demonstration of Anchor Tag, Title Tag, etc.

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>My Personal Web Blog</title>
    <style>
        body {
            font-family: Arial;
            background-color: lightblue;
            margin: 30px;
        }
        h1 {
            color: darkblue;
            text-align: center;
        }
        h2 {
            color: green;
        }
        p {
            font-size: 17px;
        }
        img {
            width: 300px;
        }
    </style>
</head>

<body>

    <h1>Welcome to My Web Blog</h1>

    <h2>About My Blog</h2>
    <p>
        Welcome to my personal web blog.
        This blog shares information about technology,
        education and programming.
    </p>

    <h2>HTML Tags Demonstration</h2>

    <p><b>Bold Tag:</b> This is bold text.</p>

    <p><i>Italic Tag:</i> This is italic text.</p>

    <p><u>Underline Tag:</u> This is underlined text.</p>

    <h2>Anchor Tag</h2>
    <p>Visit Google Website:</p>
    <a href="https://www.google.com" target="_blank">
        Click Here to Visit Google
    </a>

    <h2>Image Tag</h2>
    <img src="https://via.placeholder.com/300"
         alt="Sample Blog Image">

    <h2>List Tag</h2>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>Python</li>
        <li>WordPress</li>
    </ul>

    <h2>Contact Information</h2>
    <p>Email: example@gmail.com</p>

    <hr>

    <footer>
        <p>Copyright 2026 My Personal Web Blog</p>
    </footer>

</body>
</html>
"""

# Save HTML file
with open("myblog.html", "w", encoding="utf-8") as file:
    file.write(html_code)

print("Web Blog created successfully!")
print("Open myblog.html in your web browser.")
