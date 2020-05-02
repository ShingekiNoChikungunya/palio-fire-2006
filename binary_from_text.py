def sanitize(content):
  return content.replace(" ","").replace("\n","").replace("\r","")


def main():
  with open("binary_as_text", "r") as f:
    content = f.read()
    content = sanitize(content)

  bin_content = b''
  for i in range(len(content)//2):
    byte = content[i*2:i*2+2]
    bin_content += bytes([int(byte, 16)])

  with open("generated_binary", "wb") as dest:
    dest.write(bin_content)

if __name__ == '__main__':
    main()
