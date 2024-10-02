import base64

def decode_base64_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'wb') as outfile:
        for line in infile:
            decoded_line = base64.b64decode(line.strip())
            outfile.write(decoded_line)

if __name__ == "__main__":
    input_file = 'encoded.txt'  # Replace with your input file name
    output_file = 'decoded_output.bin'  # Replace with your desired output file name
    decode_base64_file(input_file, output_file)
    print(f"Decoded content written to {output_file}")
