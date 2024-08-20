# %%
import SimpleITK as sitk
import os

os.makedirs("reflection/output", exist_ok=True)
image_path = "reflection/sub-stroke0003_ses-01-ct+ax.nii.gz"
result_path = "reflection/output/result.nii.gz"

image = sitk.ReadImage(image_path)

image2 = sitk.Threshold(image, 0, 10)

sitk.WriteImage(image2, result_path)
