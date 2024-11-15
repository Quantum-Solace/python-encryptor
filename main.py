import sys
import pyzipper
import os

def encrypt_folder(input_folder, output_file, password):
    if not os.path.isdir(input_folder):
        print(f"Error: The folder '{input_folder}' does not exist.")
        return

    try:
        with pyzipper.AESZipFile(output_file, 'w', compression=pyzipper.ZIP_LZMA) as zf:
            zf.setpassword(password.encode('utf-8'))
            zf.setencryption(pyzipper.WZ_AES, nbits=256)

            for foldername, subfolders, filenames in os.walk(input_folder):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, input_folder)
                    zf.write(file_path, arcname=arcname)

        print(f"Folder '{input_folder}' has been encrypted as '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python encrypt.py <folder> <password>')
        sys.exit(1)

    input_folder = sys.argv[1]
    output_file = 'encrypted_folder.zip'
    password = sys.argv[2]

    encrypt_folder(input_folder, output_file, password)