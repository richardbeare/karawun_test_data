# Test data for Karawun

This repository contains a set of nifti files (in the Images folder) for conversion to Brainlab compatible DICOM images
using Karawun (). Karawun users can use this dataset to satisfy themselves that nifti data
is converted sensibly, independent of the data stride pattern in the input nifti file,
or anisotopic slicing.

## Image Data

The source data is the standard MNI atlas with left/right markings distributed with FSL.

Several different versions of this image have been created:

1. Reslicing to produce anisotropic voxels. For example thicker axial slices.

1. Reformatting data layout - i.e modifying the stride pattern

Masks or labelled versions of the MNI atlas have also been created that include the "L" and "R" markers only. Each
letter is a separate connected component and will be displayed in a different colour in Brainlab.

These images were also resliced and reformatted.

## Streamline data

A set of synthetic "tracts" have been created using mrtrix streamline files. The streamlines are
best viewed in the axial direction and form a pair of letter ("L" and "R") and are aligned with
the original markers.

## Creating the data

See Images/README for commands used to create the images

### Naming conventions

The images have name prefixes of either `mni` or `LR`, with `mni` indicating graylevel
images and `LR` indicating mask images. Suffixes are of the form `2_2_4` indicating voxel
dimensions and `A` through `E` indicating different stride patterns.

Details can be queried further using `fslinfo` or `mrinfo`. The images and tck files can
also be viewed using `mrview`

## Conversion

The test dataset can be converted to Brainlab compatible using the Karawun command:

```
mkdir brainlabdicom

importTractography -d ./Dicom/1.3.12.2.1107.5.2.43.167031.2019040213095021814319052.dcm --nifti Images/MNI152_T1_2mm_LR-masked.nii.gz mni_* --label-files Images/LR* --tract-files Images/letters.tck -o brainlabdicom

```

## Verify

All data in this test set has been derived from a single image using steps that preserve geometry. i.e the location
of any chosen landmark should be the same across all versions of the same image, and the position of the
tracts and 3D objects should remain consistent across all combinations of image versions, irrespective
of original stride pattern or slicing.

