# Colonoscopy Polyp Segmentation
> Full workflow including a generic visualization of segmentation results from a polyp segmentation models.

* See [Holohub repo](https://github.com/nvidia-holoscan/holohub/) to either setup  your connection or just connect to clara-agx


* Run container
```
cd ~/holohub
./dev_container launch --ssh_x11
```

* Copy data
```
cd /workspace/holohub/data/colonoscopy_segmentation
cp ../../cmicHACKS2/data/models/ColonSegNet-07112023-2359.onnx .
cp ../../cmicHACKS2/data/polyp-dataset/out720x576.mp4 .
cp ../../cmicHACKS2/data/polyp-dataset/out720x576.gxf_* .


cp ../../cmicHACKS2/data/polyp-dataset/*gxf_entities .
cp ../../cmicHACKS2/data/polyp-dataset/*gxf_index .
cp ../../cmicHACKS2/data/polyp-dataset/*mp4 .
```


* Running in our own repository
```
cd /workspace/holohub/cmicHACKS2/nvidia-clara-agx/colonoscopy_segmentation
python colonoscopy_segmentation.py --data /workspace/holohub/data/colonoscopy_segmentation
```



* Build application (mainly download data)
```
./run build colonoscopy_segmentation
```

* Run application
in cagx 
```
./run launch colonoscopy_segmentation 
```

```
cd /workspace/holohub/applications/colonoscopy_segmentation/
python colonoscopy_segmentation.py --data /workspace/holohub/data/colonoscopy_segmentation
```




* log
```

root@cagx-ucl:/workspace/holohub# ./run launch colonoscopy_segmentation       
[command] export PYTHONPATH=/opt/nvidia/holoscan/lib/cmake/holoscan/../../../python/lib:/workspace/holohub/build/python/lib:/workspace/holohub
[command] cd /workspace/holohub/applications/colonoscopy_segmentation
[command] python3 colonoscopy_segmentation.py --data /workspace/holohub/data/colonoscopy_segmentation
[info] [gxf_executor.cpp:210] Creating context
[warning] [inference.cpp:114] Values for model ultrasound_seg not in list form.
[info] [inference.cpp:115] HoloInfer in Holoscan SDK 0.6 onwards expects a list of tensor names for models in the parameter set.
[info] [inference.cpp:118] Converting input tensor names for model ultrasound_seg to list form for backward compatibility.
[info] [gxf_executor.cpp:1595] Loading extensions from configs...
[info] [gxf_executor.cpp:1741] Activating Graph...
[info] [resource_manager.cpp:79] ResourceManager cannot find Resource of type: nvidia::gxf::GPUDevice for entity [eid: 00002, name: __entity_2]
[info] [resource_manager.cpp:106] ResourceManager cannot find Resource of type: nvidia::gxf::GPUDevice for component [cid: 00003, name: cuda_stream]
[info] [resource.hpp:44] Resource [type: nvidia::gxf::GPUDevice] from component [cid: 3] cannot find its value from ResourceManager
[info] [resource_manager.cpp:79] ResourceManager cannot find Resource of type: nvidia::gxf::GPUDevice for entity [eid: 00004, name: __entity_4]
[info] [resource_manager.cpp:106] ResourceManager cannot find Resource of type: nvidia::gxf::GPUDevice for component [cid: 00005, name: block_memory_pool]
[info] [resource.hpp:44] Resource [type: nvidia::gxf::GPUDevice] from component [cid: 5] cannot find its value from ResourceManager
[info] [resource_manager.cpp:79] ResourceManager cannot find Resource of type: nvidia::gxf::GPUDevice for entity [eid: 00006, name: __entity_6]
[info] [resource_manager.cpp:106] ResourceManager cannot find Resource of type: nvidia::gxf::GPUDevice for component [cid: 00007, name: block_memory_pool]
[info] [resource.hpp:44] Resource [type: nvidia::gxf::GPUDevice] from component [cid: 7] cannot find its value from ResourceManager
[info] [resource_manager.cpp:79] ResourceManager cannot find Resource of type: nvidia::gxf::GPUDevice for entity [eid: 00008, name: __entity_8]
[info] [resource_manager.cpp:106] ResourceManager cannot find Resource of type: nvidia::gxf::GPUDevice for component [cid: 00009, name: block_memory_pool]
[info] [resource.hpp:44] Resource [type: nvidia::gxf::GPUDevice] from component [cid: 9] cannot find its value from ResourceManager
[info] [gxf_executor.cpp:1771] Running Graph...
[info] [gxf_executor.cpp:1773] Waiting for completion...
[info] [gxf_executor.cpp:1774] Graph execution waiting. Fragment: Colonoscopy App
[info] [greedy_scheduler.cpp:190] Scheduling 6 entities
[info] [inference.cpp:202] Inference Specifications created
[info] [core.cpp:46] TRT Inference: converting ONNX model at /workspace/holohub/data/colonoscopy_segmentation/colon.onnx
[info] [utils.cpp:85] Engine file missing at /workspace/holohub/data/colonoscopy_segmentation/colon.QuadroRTX6000.7.5.72.trt.8.2.3.0.engine.fp32. Starting generation process.
NOTE: This could take a couple of minutes depending on your model size and GPU!
[info] [utils.hpp:44] parsers/onnx/onnx2trt_utils.cpp:364: Your ONNX model has been generated with INT64 weights, while TensorRT does not natively support INT64. Attempting to cast down to INT32.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_647 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_648 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_651 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_652 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_655 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_656 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_659 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_660 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_663 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_664 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_667 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_668 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_671 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_672 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_675 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_676 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.cpp:165] Engine file generated, saved as: /workspace/holohub/data/colonoscopy_segmentation/colon.QuadroRTX6000.7.5.72.trt.8.2.3.0.engine.fp32
[info] [core.cpp:79] Loading Engine: /workspace/holohub/data/colonoscopy_segmentation/colon.QuadroRTX6000.7.5.72.trt.8.2.3.0.engine.fp32
[info] [core.cpp:122] Engine loaded: /workspace/holohub/data/colonoscopy_segmentation/colon.QuadroRTX6000.7.5.72.trt.8.2.3.0.engine.fp32
[info] [infer_manager.cpp:343] HoloInfer buffer created for inference_output_tensor
[info] [inference.cpp:213] Inference context setup complete
[info] [context.cpp:50] _______________
[info] [context.cpp:50] Vulkan Version:
[info] [context.cpp:50]  - available:  1.2.131
[info] [context.cpp:50]  - requesting: 1.2.0
[info] [context.cpp:50] ______________________
[info] [context.cpp:50] Used Instance Layers :
[info] [context.cpp:50] 
[info] [context.cpp:50] Used Instance Extensions :
[info] [context.cpp:50] VK_KHR_surface
[info] [context.cpp:50] VK_KHR_xcb_surface
[info] [context.cpp:50] VK_EXT_debug_utils
[info] [context.cpp:50] VK_KHR_external_memory_capabilities
[info] [context.cpp:50] ____________________
[info] [context.cpp:50] Compatible Devices :
[info] [context.cpp:50] 0: Quadro RTX 6000
[info] [context.cpp:50] Physical devices found : 
[info] [context.cpp:50] 1
[info] [context.cpp:50] ________________________
[info] [context.cpp:50] Used Device Extensions :
[info] [context.cpp:50] VK_KHR_swapchain
[info] [context.cpp:50] VK_KHR_external_memory
[info] [context.cpp:50] VK_KHR_external_memory_fd
[info] [context.cpp:50] VK_KHR_external_semaphore
[info] [context.cpp:50] VK_KHR_external_semaphore_fd
[info] [context.cpp:50] VK_KHR_push_descriptor
[info] [context.cpp:50] VK_EXT_line_rasterization
[info] [context.cpp:50] 
[info] [vulkan_app.cpp:777] Using device 0: Quadro RTX 6000 (UUID aa494f54ba4286b71c9ddc3f846)
[info] [holoviz.cpp:1425] Input spec:
- type: color
  name: ""
  opacity: 1.000000
  priority: 0
- type: color_lut
  name: out_tensor
  opacity: 1.000000
  priority: 0

[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 1 , delay: -1481048427 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 2 , delay: -3427814262 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 3 , delay: -5656653792 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 4 , delay: -8256425419 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 5 , delay: -10492869462 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 6 , delay: -12897712352 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 7 , delay: -16672821035 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 8 , delay: -18985618966 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 9 , delay: -21744952480 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 10 , delay: -24156342059 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 11 , delay: -26525140726 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 12 , delay: -28739639136 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 13 , delay: -30937116747 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 14 , delay: -33356354614 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 15 , delay: -35726835936 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 16 , delay: -38064017163 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 17 , delay: -40084710390 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 18 , delay: -42261973760 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 19 , delay: -44463402251 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 20 , delay: -47709392182 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 21 , delay: -50304766816 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 22 , delay: -52472258123 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 23 , delay: -54943806070 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 24 , delay: -57263775968 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 25 , delay: -59591485067 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 26 , delay: -61874361430 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 27 , delay: -64265720480 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 28 , delay: -67119868235 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 29 , delay: -69311360470 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 30 , delay: -72476480128 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 31 , delay: -74598171019 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 32 , delay: -77757672022 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 33 , delay: -81366001120 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 34 , delay: -83464158283 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 35 , delay: -86267267542 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 36 , delay: -88066675648 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 37 , delay: -90189997995 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 38 , delay: -90200843766 ns)
[info] [video_stream_replayer.cpp:261] Playing video stream is lagging behind (count: % 39 , delay: -93029044224 ns)
[info] [greedy_scheduler.cpp:369] Scheduler stopped: Some entities are waiting for execution, but there are no periodic or async entities to get out of the deadlock.
[info] [greedy_scheduler.cpp:398] Scheduler finished.
[info] [gxf_executor.cpp:1783] Graph execution deactivating. Fragment: Colonoscopy App
[info] [gxf_executor.cpp:1784] Deactivating Graph...
[info] [gxf_executor.cpp:1787] Graph execution finished. Fragment: Colonoscopy App
[info] [gxf_executor.cpp:229] Destroying context

```

## Optmise model

```
[info] [core.cpp:46] TRT Inference: converting ONNX model at /workspace/holohub/data/colonoscopy_segmentation/colon.onnx
[info] [utils.cpp:85] Engine file missing at /workspace/holohub/data/colonoscopy_segmentation/colon.QuadroRTX6000.7.5.72.trt.8.2.3.0.engine.fp32. Starting generation process.
NOTE: This could take a couple of minutes depending on your model size and GPU!
[info] [utils.hpp:44] parsers/onnx/onnx2trt_utils.cpp:364: Your ONNX model has been generated with INT64 weights, while TensorRT does not natively support INT64. Attempting to cast down to INT32.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_647 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_648 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_651 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_652 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_655 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_656 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_659 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_660 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_663 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_664 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_667 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_668 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_671 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_672 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_675 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.hpp:44] parsers/onnx/ShapedWeights.cpp:171: Weights onnx::MatMul_676 has been transposed with permutation of (1, 0)! If you plan on overwriting the weights with the Refitter API, the new weights must be pre-transposed.
[info] [utils.cpp:165] Engine file generated, saved as: /workspace/holohub/data/colonoscopy_segmentation/colon.QuadroRTX6000.7.5.72.trt.8.2.3.0.engine.fp32
[info] [core.cpp:79] Loading Engine: /workspace/holohub/data/colonoscopy_segmentation/colon.QuadroRTX6000.7.5.72.trt.8.2.3.0.engine.fp32
[info] [core.cpp:122] Engine loaded: /workspace/holohub/data/colonoscopy_segmentation/colon.QuadroRTX6000.7.5.72.trt.8.2.3.0.engine.fp32

```

## Inference Parameters
### backend
backend parameter is set to either trt for TensorRT, onnxrt for Onnx runtime, or torch for libtorch.

### enable_fp16
`enable_fp16`: Generation of the TensorRT engine files with FP16 option
If backend is set to trt, and if the input models are in onnx format, then users can generate the engine file with fp16 option to accelerate inferencing.



## Data
* Download 
```
wget -q --show-progress --content-disposition https://api.ngc.nvidia.com/v2/resources/nvidia/clara-holoscan/holoscan_colonoscopy_sample_data/versions/20230222/zip -O /workspace/holohub/data/colonoscopy_segmentation.zip
```


* size of data 
```
-rw-r--r-- 1 root root  51099580 Nov  3 14:28  colon.QuadroRTX6000.7.5.72.trt.8.2.3.0.engine.fp32
-rw-r--r-- 1 root root  20056152 Mar 17  2023  colon.onnx
-rw-r--r-- 1 root root 502716592 Nov  3 14:25  colon_exam_720x576.gxf_entities
-rw-r--r-- 1 root root      9696 Nov  3 14:25  colon_exam_720x576.gxf_index
-rw-r--r-- 1 root root   2697869 Mar 17  2023  colon_exam_720x576.mp4
```




## Reference 
https://github.com/nvidia-holoscan/holohub/tree/main/applications/colonoscopy_segmentation    
https://catalog.ngc.nvidia.com/orgs/nvidia/teams/clara-holoscan/resources/holoscan_colonoscopy_sample_data   
https://docs.nvidia.com/holoscan/sdk-user-guide/inference.html   



