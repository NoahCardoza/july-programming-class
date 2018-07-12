# Exercise 3: Assignment

According to Suetonius in "De Vita XII Caesarum" published A.D. 121:

> Exstant et ad Ciceronem, item ad familiares domesticis de rebus, in quibus, si qua occultius perferenda erant, per notas scripsit, id est sic structo litterarum ordine, ut nullum verbum effici posset; quae si qui investigare et persequi velit, quartam elementorum litteram, id est D pro A et perinde reliquas commutet.

This is the first recorded case of encryption for security, and is today called the “Caesar Cipher” because Julius Caesar used it to encode sensitive information when communicating with his generals. Although not very secure by today’s standards, it was still used as recently as WW1 by the Russian Army.

###Mission:
Write a Caesar Cipher Encoder/Decoder using an arbitrary key.

1.  Print a statement welcoming the user to the Caesar encoder and decoder.

2.  Ask the user for the shift key, i.e. the number of letters to “shift” the
    alphabet to make the coded message. A key of 1, for example, means that A
    becomes B, B becomes C, and so forth to Z becoming A. A key of -2 means that
    A becomes Y, B becomes Z, C becomes A, and so forth.

3.  Ask the user for the message to be encoded/decoded.

4.  If the message is to be encoded, apply the shift key which was specified in
    (3) and print the encoded message. If the message is to be decoded, apply
    the reverse of the shift key which was specified in (3) and print the
    decoded message.

5.  Print a closing statement of some kind.

### Notes:
- Remember that the shift should “wrap around”, i.e. a shift that goes past the end of the alphabet should wrap back to the beginning and vice versa.

- You must use ASCII codes. These can be found here: http://www.ascii-code.com/

- The program need only accept messages in capitals. If your code does
  everything listed above AND can accommodate lowercase letters AND can leave
  punctuation untouched (i.e. does not encode spaces, periods, commas, etc.)
