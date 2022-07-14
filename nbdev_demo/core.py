# AUTOGENERATED! DO NOT EDIT! File to edit: 01_core.ipynb (unless otherwise specified).

__all__ = ['HelloSayer', 'Scan']

# Cell
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): self.to = to

    def say(self):
        "Do the saying"
        return say_hello(self.to)

# Cell

class Scan:
    """Represents a medical imaging single 3D volume.

    Attributes:
        title: str represnting name of volume
        dcm_series: series of dcm files containing volume
    """

    def __init__(self, title, dcm_series):
        vol, pix_dim, affine = dicom_to_volume(dcm_series)
        self.title = title
        self.dcm_series = dcm_series
        self.vol = vol
        self.pix_dim = pix_dim
        self.affine = affine



    def getName(self):
        return self.__class__.__name__

    def write_nifti(self, output_path):
        """Writes a Nfiti file of 3D volume to a specified output path.

        Args:
            output_path (path): Nifti output path

        Returns:
            _path_: Nifti output path
        """

        nifti_file = nibabel.Nifti1Image(self.vol, self.affine)
        output_path = f"{output_path}/{self.title}.nii.gz"
        nibabel.save(nifti_file, output_path)

        return output_path