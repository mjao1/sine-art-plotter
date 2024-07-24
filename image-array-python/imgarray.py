from PIL import Image
import os

def process_image(file_path, width):
    try:
        image = Image.open(file_path)
        canvas_width = int(width)
        canvas_height = int((image.height * canvas_width) / image.width)
        resized_image = image.resize((canvas_width, canvas_height))
        pixels = resized_image.load()

        output_array = []
        for y in range(canvas_height):
            row = []
            for x in range(canvas_width):
                r, g, b = pixels[x, y][:3]
                avg = (r + g + b) // 3
                row.append(avg)
            output_array.append(row)

        output_string = "let image = [\n"
        for row in output_array:
            output_string += "[" + ", ".join(map(str, row)) + "],\n"
        output_string = output_string[:-2] + "\n]"
        return output_string
    except Exception as e:
        return str(e)

def main():
    file_path = input("Enter image file path: ")
    if not os.path.exists(file_path):
        print("File not found")
        return
    
    width = input("Enter width: ")
    if not width.isdigit() or int(width) <= 0:
        print("Invalid width")
        return
    
    result = process_image(file_path, width)
    print(result)

if __name__ == "__main__":
    main()
