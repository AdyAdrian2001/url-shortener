import random, string

# shortcode generating
def shortcode_generator(size=8, chars=string.ascii_lowercase + string.digits):
    #new_shortcode = ''
    #for _ in range(size):
    #    new_shortcode += random.choice(chars)
    #return new_shortcode
    return ''.join(random.choice(chars) for _ in range(size))
