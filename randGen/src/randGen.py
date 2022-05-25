#Makes a set of random data based on provided inputs

#All the standard libs required for this script
import os
import argparse


#randGen genreates data for other processes and currently has no variants
class randGen:
 
    
    def __init__(self):
    """Init mostly sets the default variable settings and initializes the
       argparser
    """
        self.args = []
        self.KEY_SIZE_BYTES=64
        #OpenSSL args are case-sensitive so it's easier to just handle here
        self.KEY_TYPE  = "aes"
        self.KEY_MODE  = "ecb"
        self.KEY_PATH  = "keys"
        self.CYPH_PATH = "cipher"

        self.parser = argparse.ArgumentParser(
            description="Generates a series of keys, ciphertext, and plaintext \
                         useful for various testing cases. '-'s are required")
        self.parser.add_argument('--key_dir', default = "keys",
                                help='Parent path to place/find keys below')
        self.parser.add_argument('--ciph_dir', default = "cipher",
                                help='Parent path to place/find cipher blocks')
        self.parser.add_argument('--plain_dir', default = "plain",
                                help='Parent path to place/find plain blocks')


    def makePaths()
    """makePaths generates the necessary folders for data manipulation.
       It can't guarantee you've allocated enough space to run.
    """


    #There's no current need to more than parse the supplied arguments
    def __main__
        self.args = self.parser.parse_args()
        print(f"Args: {self.args.key_dir}\n  \
                      {self.args.ciph_dir}\n \
                      {self.args.plain_dir}")
