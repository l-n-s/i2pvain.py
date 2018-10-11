# i2pvain.py

i2pvain.py generates a customized [I2P](https://geti2p.net/) destination, which base32 address starts with a word you choose.

For example, let's generate an address which starts with "cool" and save it to a file "cool.dat":

    ./i2pvain.py cool cool.dat
    cool672xmktk5ehyiccz2if76c6fhhhjdxxlfyftzhivnvhfkygq.b32.i2p
    5F8keASxnf-AorD75fGkJD271L51Wz~U2yrw3MNHc8qIh50ffg0QVIcvocNhDQO-9t4nVOZ2l2oQ6tztgdhx4u~P1zeIqhLWZaQT0idVx4Iv-6WqZUH0htstUa3yOi12KGBB2NfkMPBZPb02Zo9Jwo6Sa7Xtnr57x8PXuoil-WScCSeBd6kXDB63oia7FmRCtVe4EaUhrjIyeK4Nb0eqlN2ELA0jcY4kMNLjIyWdJ8nkqlGwVXl0vdu3eaEudydbW99Jv-6qhGeaCTbzSZJfl4A2GK7vO5xuOFVAYY06sBLIv1PguG8vqIiHyEPtZZ3gnjWZQbewl8xiGoG0ymhT~d7P8V8TcQBmZlfpLVGlpHeUD2jC4DnZiMyXIf6Rq8-3n3gLK5oxmcYR9Xd9unt-bv0aNtWMsXmjgD~qOECkeVgs9OJHCaU5HYbf6foyHLW4-rtJsKwIGwUhliZg5ne3yaR6SE3DewDuCjJFkDU12xJENLfYB1LKyKQoaP8gF4ZkBQAEAAcAAKfpqPr03P4NGjsb1TQ4-iesxeyV6fIvTc-uEfcG8Ljh94k~irK-Cw4HRrNx-79s8-UtcJm2awnNVc2lfrSo-0XWIaMlsHTg~R~GGau2iRi0WYaG~fnpuOyURwf84ZMw3fxLbTUSYtGsS24eT1Q9lpcrgQHseq~6dBl2BWzXcL20rmOKU8n07AY7bO2E-2a0V9WD2kSJv~ecQ9lttaANJ1hsTIOXws056mDrXP3akXodH93kcZEq7WKH8ucbfqL1XGgFh24ZX7LRSXjE6FgfGBq9IMyWVTVxwvjSO2n6gbEuEyptzFF45tnvVDyTjli6pT6mjdvwCALxJuA0db1AJ29LmEMuQOMZagmmXJbKfrOqLu55f~AvSwQdFJdlcPlSow==
    Key saved to --> cool.dat

Now you can use "cool.dat" key file to create a new I2P tunnel, and its base32 address will be "cool672xmktk5ehyiccz2if76c6fhhhjdxxlfyftzhivnvhfkygq.b32.i2p"

## requirements

- Python 3.4+ 
- I2P router with SAM API enabled
