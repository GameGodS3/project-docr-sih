import json
import os

from subprocess import PIPE, Popen

def voodoomagic():

    print(' [ voodoomagic ]: called voodoomagic')

    command = f'''
    curl --request POST \
        -s \
        --url https://pen-to-print-handwriting-ocr.p.rapidapi.com/recognize/ \
        --header 'X-RapidAPI-Host: pen-to-print-handwriting-ocr.p.rapidapi.com' \
        --header 'X-RapidAPI-Key: 8cb6a74ffcmsh9ff81e0b74a2c4ep1aaee4jsne3817830bbf0' \
        --header 'content-type: multipart/form-data' \
        --form 'srcImg=@tmp/image.jpg' \
        --form Session=string
    '''

    with Popen(command, stdout=PIPE,  shell=True) as process:
        output = process.communicate()[0].decode("utf-8")
        output.replace('\n', '\\n')
        return json.loads(output)
