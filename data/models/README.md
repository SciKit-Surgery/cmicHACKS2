# Models

## `onnx` models

### Trained models

| Model (Size)  | Download | Notebook |
| -- |-- | -- |
| ColonSegNet-07112023-2359.onnx (20MB or 20,067,028) | [:link:](TOADD) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1s-eKu6QjaV54jva_ylG1VxwCj1B8nwJ3) |
| ColonSegNet_brightcontr.onnx (20MB) | [:link:](https://drive.google.com/file/d/1IoeDmH-nBcOrmrg1SBEx2wuMjRCuO0K_/view?usp=drive_link) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1CgdpeDY4SLpKddk6dFvXpFwcx0skF8dj#scrollTo=e7dn13rCydBf) |


### Examples to download models in your local machine
* ColonSegNet-07112023-2359.onnx
```
wget https://raw.githubusercontent.com/SciKit-Surgery/cmicHACKS2/main/data/ColonSegNet-07112023-2359.onnx
```

* Original model
```
wget --content-disposition 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/clara-holoscan/holoscan_colonoscopy_sample_data/20230222/files?redirect=true&path=colon.onnx' -O colon.onnx
```

```
wget --content-disposition 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/clara-holoscan/holoscan_colonoscopy_sample_data/20230222/files?redirect=true&path=colon_exam_720x576.mp4' -O colon_exam_720x576.mp4
```

## References 
https://catalog.ngc.nvidia.com/orgs/nvidia/teams/clara-holoscan/resources/holoscan_colonoscopy_sample_data/files


