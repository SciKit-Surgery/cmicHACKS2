# Friday 10th Nov 2023

## 09:00 - 10:30 > Hacking: Evaluation of AI models with benchmarks
* Test segmentation models and convert `checkpoint.pth` to `colon.onnx` > [colon_seg_net_test.ipynb](colon_seg_net_test.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zNmljc-ppn_0RZvppI3Vz7rX3uA8msPd)

## 10:45 - 12:00 > Hacking: Optmise, test and deploy AI models in clara-agx
> How can choosing the right floating point precision improve performance with my application?  

* See [workflow](../../data/polyp-dataset/README.md) to convert your images to video and gxf format 
* See Inference Parameters (`backend` and `enable_fp16`=True/False) in [colonoscopy_segmentation.py](../../nvidia-clara-agx/colonoscopy_segmentation/colonoscopy_segmentation.py) and further descriptions in this [README](../../nvidia-clara-agx/colonoscopy_segmentation/README.md)
 
Models can also be optimised using tao-coverter
```
./tao-converter \
    -k tlt_encode \
    -d 3,544,960 \
    -w 40960M \
    -t fp16 \
    -o output_cov/Sigmoid,output_bbox/BiasAdd \
    -e engine.trt \
    resnet34_peoplenet_pruned_int8.etlt
```

* Parameters in tao-converter
```
-k: The key used to encode the .tlt model when doing the training. 
-d: Comma-separated list of input dimensions that should match the dimensions used for tao <model> export.
-w: Maximum workspace size for the TensorRT engine. The default value is 1073741824(1<<30).
-t: Desired engine data type, generates calibration cache if in INT8 mode. The default value is fp32. The options are {fp32, fp16, int8}.
-o: Comma-separated list of output blob names that should match the output configuration used for tao <model> export.
-e: Path to save the engine to. (default: ./saved.engine)
input_file
```

## 13:00 - 14:30 > Hacking: Clara AGX/IGX for intelligent Medical Instruments by Mikael Brudfors
* Mikael Brudfors introducing Clara AGX/IGX for intelligent Medical Instruments
* Q&As
* Keep hacking 

## 14:45 - 16:30 > Tidied up documentation and present results
* Prepare documentation and discuss results
* Create PRs
* Review and merge PRS
* Group photo

## References 

https://docs.nvidia.com/deeplearning/tensorrt/quick-start-guide/index.html#abstract


