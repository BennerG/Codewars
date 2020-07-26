# The rgb function is incomplete. Complete it so that passing in RGB decimal 
# values will result in a hexadecimal representation being returned. Valid 
# decimal values for RGB are 0 - 255. Any values that fall out of that range 
# must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 
# will not work here.
#

def rgb1(r, g, b):
    return "".join([f"{0:02X}" if x < 0 else f"{255:02X}" if x > 255 else f"{x:02X}" for x in (r,g,b)])

def rgb(r, g, b):
    return "".join(map(lambda x: f"{max(min(x,255), 0):02X}", (r,g,b)))

print("FFFFFF", rgb(255, 255, 255)) # returns FFFFFF
print("FFFFFF", rgb(255, 255, 300)) # returns FFFFFF
print("000000", rgb(0,0,0)) # returns 000000
print("9400D3", rgb(148, 0, 211)) # returns 9400D3

