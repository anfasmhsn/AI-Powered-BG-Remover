from rembg import remove
from PIL import Image
input_path = 'input.png'
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
print(f'Removed background from {input_path} and saved to {output_path}.')  
