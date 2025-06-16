import zipfile
import itertools
import time

# Function for extracting zip files to test if the password works!


def extractFile(zip_file, password):
    try:
        zip_file.extractall(path='/tmp', pwd=password.encode())
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        pass


# Main code starts here...
# The file name of the zip file.
zipfilename = '/tmp/alien-zip-2092.zip'
alphabet = '1234567890'
zip_file = zipfile.ZipFile(zipfilename)

# We know they always have 3 characters
# For every possible combination of 3 letters from alphabet...
for c in itertools.product(alphabet, repeat=3):
    # Add the three letters to the first half of the password.
    password = ''.join(c)
    # Try to extract the file.
    print("Trying: %s" % password)
    # If the file was extracted, you found the right password.
    if extractFile(zip_file, password):
        print('*' * 20)
        print('Password found: %s' % password)
        print('Files extracted...')
        exit(0)

# If no password was found by the end, let us know!
print('Password not found.')
