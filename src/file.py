def file_write(filename, content):
    with open(filename, "w") as o:
        print(content, file=o)

def file_read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
        
def file_read2(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    file_name = "sample.txt"
    file_write(file_name, "Hello\nGoodbye")

    c = file_read(file_name)
    print(c)

    file_read2(file_name)
