from PIL import Image

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.8
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayscale_image(image):
    return image.convert('L')

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def image_to_ascii_html(image_path, output_path='index.html', width=80):
    image = Image.open(image_path)
    image = resize_image(image, width)
    image = grayscale_image(image)
    
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    
    ascii_art = []
    for i in range(0, len(ascii_str), img_width):
        ascii_art.append(ascii_str[i:i + img_width])
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ASCII Art</title>
    <style>
        body {{
            background: #0d1117;
            color: #f0f6fc;
            font-family: monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }}
        pre {{
            font-size: 10px;
            line-height: 10px;
        }}
    </style>
</head>
<body>
<pre>
"""
    for line in ascii_art:
        html += line + '\n'
    
    html += """</pre>
</body>
</html>"""
    
    with open(output_path, 'w') as f:
        f.write(html)
    print(f"Created {output_path}")

if __name__ == '__main__':
    image_to_ascii_html('picture.png')
