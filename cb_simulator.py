import numpy as np

import matplotlib.pyplot as plt

from skimage import exposure, data, io, img_as_float
from skimage.color import rgb2hed


filters = {
'normal':[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
'protanopia':[[.56667, .43333, 0], [.55833, ]]
}
red_multiplier = [1.56667, 1.43333, 1]
green_multiplier = [1.55833, 1.44167, 1]
blue_multiplier = [1, 1.24167, 1.75833]

def filter_image(image):
    colorblind_image = image
    colorblind_image = red_multiplier * image
    colorblind_image = green_multiplier * colorblind_image
    colorblind_image = blue_multiplier * colorblind_image

    return colorblind_image

# image = img_as_float(data.astronaut()[::2, ::2])
image = io.imread("hawaii_flowers.jpg")
io.imshow(image)
io.show()
image = exposure.rescale_intensity(filter_image(image))
io.imshow(image)
io.show()

red_channel = image[:,:,0] * .56667 + image[:,:,1] * .43333
print(red_channel)
green_channel = image[:,:,0] * .55833 + image[:,:,1] * .44167
blue_channel = image[:,:,1] * .24167 + image[:,:,2] * .75833
print(red_channel.shape)
colorblind_rgb = np.dstack((red_channel, green_channel, blue_channel))
colorblind_image = colorblind_rgb
exposure.rescale_intensity(colorblind_image)
io.imshow(colorblind_image)
io.show()
# fig, (ax1, ax2) = plt.subplots(figsize=(8, 4), ncols=2,  sharex=True, sharey=True)
# ax1.imshow(image)
# ax2.imshow(image)
# ax1.set_adjustable('box-forced')
# ax2.set_adjustable('box-forced')
#
# fig.show()
