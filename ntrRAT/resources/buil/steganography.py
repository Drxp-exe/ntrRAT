
from PIL import Image

def hide_message(image_path, message, output_path):
    image = Image.open(image_path)
    encoded_image = image.copy()
    width, height = image.size
    message += '###'  # End marker

    data_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            for n in range(3):  # R, G, B channels
                if data_index < len(message):
                    pixel[n] = pixel[n] & ~1 | int(bin(ord(message[data_index]))[2:][-1])
                    data_index += 1
            encoded_image.putpixel((x, y), tuple(pixel))
            if data_index >= len(message):
                encoded_image.save(output_path)
                print(f"Message hidden in {output_path}")
                return

if __name__ == "__main__":
    img = input("Enter image path: ")
    msg = input("Enter secret message: ")
    output = input("Enter output image path: ")
    hide_message(img, msg, output)
    