# %%
import SimpleITK as sitk
import os
import numpy as np

os.makedirs("output", exist_ok=True)
image_path = "sub-stroke0003_ses-01-ct+ax.nii.gz"
result_path = "output/result.nii.gz"

input = sitk.ReadImage(image_path)
np_output = np.array(sitk.GetArrayViewFromImage(input))

z, y, x = np.mgrid[:np_output.shape[0],
                   :np_output.shape[1], :np_output.shape[2]]

a, b, c, d = [0.9177152418942791, 0.08030779707443489,
              0.3890364925350529, -290.8034951038973]


for index, pixel_value in np.ndenumerate(np_output):
    # index will contain the (z, y, x) coordinates for a 3D image
    # pixel_value will be the value at that coordinate
    cx, cy, cz = index
    if (a*cx + b*cy + c*cz + d < 1):
        np_output[index] = 17000

image_output = sitk.GetImageFromArray(np_output)
image_output.CopyInformation(input)

sitk.WriteImage(image_output, result_path)

# image_x = sitk.GetImageFromArray(x)
# image_y = sitk.GetImageFromArray(y)
# image_z = sitk.GetImageFromArray(z)
#
# image_x.CopyInformation(input)
# image_y.CopyInformation(input)
# image_z.CopyInformation(input)
#
# sitk.WriteImage(image_x, "x.nii.gz")
# sitk.WriteImage(image_y, "y.nii.gz")
# sitk.WriteImage(image_z, "z.nii.gz")
