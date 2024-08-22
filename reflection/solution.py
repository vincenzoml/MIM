# %%
import SimpleITK as sitk
import os
import numpy as np

# %%
os.makedirs("output", exist_ok=True)
image_path = "sub-stroke0003_ses-01-ct+ax.nii.gz"
result_path = "output/result.nii.gz"

a, b, c, d = [0.9177152418942791, 0.08030779707443489,
              0.3890364925350529, -290.8034951038973]

# %%
input = sitk.ReadImage(image_path)

np_input = sitk.GetArrayViewFromImage(input)

# %%
z, y, x = np.mgrid[:np_input.shape[0],
                   :np_input.shape[1], :np_input.shape[2]]

plane = (np.abs(a * x + b * y + c * z + d) <= 1)

np_output = plane  # + np.where(plane, plane*1700, np_input)


image_output = sitk.GetImageFromArray(np_output)
image_output.CopyInformation(input)

sitk.WriteImage(image_output, result_path)
