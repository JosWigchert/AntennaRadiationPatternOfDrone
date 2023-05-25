import math

# Function to extract bits from a list of symbols based on the modulation scheme
def extract_bits(symbols, modulation):
    if modulation == 'BPSK':
        bits = []
        for symbol in symbols:
            bit = 0 if symbol < 0 else 1
            bits.append(bit)
        return bits
    elif modulation == 'QPSK':
        bits = []
        for symbol in symbols:
            real = 0 if symbol[0] < 0 else 1
            imag = 0 if symbol[1] < 0 else 1
            bits.extend([real, imag])
        return bits
    # Add more cases for other modulation schemes if needed

# Function to parse the IQ sample file and extract bits, bytes, and RSS
def parse_iq_samples_file(file_path, modulation):
    bits = []
    bytes = []
    rss_values = []

    with open(file_path, 'r') as file:
        current_bits = 0
        for line in file:
            try:
                iq = eval(line.strip())  # Convert string representation to tuple

                # Normalize I/Q values
                max_value = max(abs(iq[0]), abs(iq[1]))
                if max_value != 0:
                    normalized_iq = (iq[0] / max_value, iq[1] / max_value)
                else:
                    normalized_iq = (0, 0)

                rss = 10 * math.log10(iq[0] ** 2 + iq[1] ** 2)  # Calculate RSS

                symbols = [normalized_iq]  # Assuming one symbol per IQ sample
                symbol_bits = extract_bits(symbols, modulation)
                bits.extend(symbol_bits)

                if len(bits)-current_bits >= 8:
                    byte_bits = bits[-8:]  # Assuming 8 bits per byte
                    byte_value = int(''.join(str(bit) for bit in byte_bits), 2)
                    bytes.append(byte_value)
                    current_bits = len(bits)

                rss_values.append(rss)
            except:
                pass
                # print(f"Error parsing line: {line.strip()}")

    return bits, bytes, rss_values

# Example usage
file_path = 'data_drone_gain20'  # Replace with your file path
modulation_scheme = 'QPSK'  # Replace with the modulation scheme used in your samples

bits, bytes, rss_values = parse_iq_samples_file(file_path, modulation_scheme)

# print("Bits:", bits)
# print("Bytes:", bytes)


byte_arrays = []
for i in range(8):
    offset = i * 1
    byte_array = bytearray()
    for j in range(offset, len(bits), 8):
        byte_array.append(bits[j])
    byte_arrays.append(byte_array)


for byte_array in byte_arrays:
    text = ''.join(chr(byte) for byte in bytes)
    print(text)
print("RSS Values:", rss_values)


