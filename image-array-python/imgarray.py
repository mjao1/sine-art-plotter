from PIL import Image
import os

# Processes a selected image into a pixel array string
def process_image(file_path, width):
    try:
        # Opens image file
        image = Image.open(file_path)

        # Converts width input to integer and calculates height to maintain aspect ratio
        canvas_width = int(width)
        canvas_height = int((image.height * canvas_width) / image.width)
        
        resized_image = image.resize((canvas_width, canvas_height))
        pixels = resized_image.load()

        # Initializes an empty list to store pixel data
        output_array = []
        # Iterates over each row of pixels
        for y in range(canvas_height):
            row = []
            # Iterates over each column of ixels
            for x in range(canvas_width):
                # Gets RGB values of the pixel and averages it to convert to grayscale
                r, g, b = pixels[x, y][:3]
                avg = (r + g + b) // 3
                row.append(avg)
                
            # Adding row to the output array
            output_array.append(row)

        # Initializes string to store final output
        output_string = "let image = [\n"
        # Iterates over each row in output array
        for row in output_array:
            # Converts the row list to a string and adds it to the output string
            output_string += "[" + ", ".join(map(str, row)) + "],\n"
        # Removes the last comma and newline
        output_string = output_string[:-2] + "\n]"
        return output_string
        
    except Exception as e:
        return str(e)

def main():
    # Prompts user to enter file path of an image
    file_path = input("Enter image file path: ")
    if not os.path.exists(file_path):
        print("File not found")
        return
    #Promts user to enter requested width of the image
    width = input("Enter width: ")
    if not width.isdigit() or int(width) <= 0:
        print("Invalid width")
        return

    # Proccesses the image and prints the result
    result = process_image(file_path, width)
    print(result)

if __name__ == "__main__":
    main()
