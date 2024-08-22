# %%
import SimpleITK as sitk
import os
import numpy as np

# %%
os.makedirs("output", exist_ok=True)
image_path = "sub-stroke0003_ses-01-ct+ax.nii.gz"
result_path = "output/result.nii.gz"

coefficients = np.array([0.9177152418942791, 0.08030779707443489,
                         0.3890364925350529, -290.8034951038973])

# %%
input = sitk.ReadImage(image_path)

np_input = sitk.GetArrayViewFromImage(input)

# %%
vect_coords = np.mgrid[:np_input.shape[0],
                       :np_input.shape[1],
                       :np_input.shape[2]]

coords = vect_coords.reshape(vect_coords.shape[0], -1)

denom = coefficients[0]**2 + coefficients[1]**2 + coefficients[2]**2

factor = 2 * (np.dot(coefficients[0:3], coords) + coefficients[3])/denom

mfactor = np.array([coefficients[0] * factor,
                    coefficients[1] * factor,
                    coefficients[2] * factor])

coords_prime = np.round(coords - mfactor)

output = np.reshape(coords_prime[0], np_input.shape)

# %%

image_output = sitk.GetImageFromArray(output)
image_output.CopyInformation(input)

sitk.WriteImage(image_output, result_path)


# %%
