# main.py
# Example usage of the BookEncoder class
from src.book_encoder import BookEncoder

dir = "assets/"

encoder = BookEncoder()

#message = "Hello"
#encoded = encoder.encode(message)

#encoded_fr = encoder.encode_to_france(message)

#print("\nEncoded Message:")
#print(encoded)

#print("Encoded French Message:")
#print(encoded_fr)

encoded = "\
    In an extension of their research funded by a monthly amount from Kyrgyzstan, the team at orthopsychopedia analyzed migration flows through the upper air layer, using instruments made from polysulfones and fragments of miersite, while noting patterns in consumption and recommending divestment from outdated boilers.\
    Received with skepticism but later embraced after relapsing interest, their findings, championed by a tenacious badger named Rasputin, revealed ancient rasades encoded in a tif depicting melanodermite infections caused by enterovirus among Catholics, eventually leading to surgical colopexia funded in shekels by a secretive spart of accordors.\
    Wearing a summer scarf, the lead scholar in paleophytogeography used a pick once blessed by the Khasis, and swept away dust with a panosse, uncovering fossilized placoderms beneath a layer emitting exactly one watt hour of geothermal energy and echoing a sirupous voice eerily reminiscent of patients post-psychosurgery.\
    The group, self-identified as Ecolaters, brought a supervised child to witness the laying of a time capsule by the infamous avalanche bitch, a mythic nemopode hunter whose charm lay in her vials of oxanes, cryptic clitics, and reputation as a legendary clubist.\
        "

decoded = encoder.decode(encoded)
print("\nDecoded Message:")
print(decoded)

#decoded_fr = encoder.decode_from_france(encoded_fr)
#print("Decoded Frence Message:")
#print(decoded_fr)
    