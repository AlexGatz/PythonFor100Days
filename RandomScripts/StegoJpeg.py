"""
Created by: Alex J. Gatz
Date: 06/08/2018

Hide a zip file inside a JPEG
"""

import sys

# Start with a jpeg file
jpeg_file = open(sys.argv[1], 'rb') # Path to JPEG
jpeg_data = jpeg_file.read()
jpeg_file.close()

# And the zip file to embed in the jpeg
zip_file = open(sys.argv[2], 'rb') # Path to ZIP file
zip_data = zip_file.read()
zip_file.close()

# Combine the files
out_file = open('HiddenDataImage.jpg', 'wb') # Output file
out_file.write(jpeg_data)
out_file.write(zip_data)
out_file.close()

# The resulting output file appears like a normal jpeg but 
# can also be unzipped and used as an archive.
