# Kvasir-SEG dataset
> The Kvasir-SEG dataset (size 46.2 MB) contains 1000 polyp images and their corresponding ground truth from the Kvasir Dataset v2. The resolution of the images contained in Kvasir-SEG varies from 332x487 to 1920x1072 pixels. The images and its corresponding masks are stored in two separate folders with the same filename. The image files are encoded using JPEG compression, and online browsing is facilitated. The bounding box (coordinate points) for the corresponding images are stored in a JSON file. https://datasets.simula.no/downloads/kvasir-seg.zip


```
wget https://datasets.simula.no/downloads/kvasir-seg.zip #(45M)
unzip kvasir-seg.zip
rm kvasir-seg.zip
```

## Converting images to video 
```
cd data/polyp-dataset/Kvasir-SEG/images
ffmpeg -framerate 30 -pattern_type glob -i 'Kvasir-SEG/images/ck*.jpg' -c:v libx264 out720x576.mp4


 #cp images/ck2bxknhjvs1x0794iogrq49k.jpg selected/
 #cp images/cju16jgnyzp970878melv7r25.jpg selected/
 #cp images/cju33w4sdcivk0855x879zht7.jpg selected/
 #cp images/cju85omszllp30850b6rm9mi3.jpg selected/


 #convert cju16jgnyzp970878melv7r25.jpg -resize 512x cju16jgnyzp970878melv7r25.jpg
 #convert cju33w4sdcivk0855x879zht7.jpg -resize 512x cju33w4sdcivk0855x879zht7.jpg
 #convert cju85omszllp30850b6rm9mi3.jpg -resize 512x cju85omszllp30850b6rm9mi3.jpg
 #convert ck2bxknhjvs1x0794iogrq49k.jpg -resize 512x ck2bxknhjvs1x0794iogrq49k.jpg

ffmpeg -framerate 30 -pattern_type glob -i 'Kvasir-SEG/selected-512x/*.jpg' -c:v libx264 out720x576-selection512x.mp4


```



## Using `convert_video_to_gxf_entities.py`  (Graph Execution Framework, GXF)
```
mamba activate cagxVE
#ffmpeg -i out.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python convert_video_to_gxf_entities.py --width 1920 --height 1080 --channels 3 --framerate 1 --basename out
#ffmpeg -i out.mp4 -pix_fmt yuvj422p -f rawvideo pipe:1 | python convert_video_to_gxf_entities.py --width 600 --height 500 --channels 3 --framerate 1 --basename out
ffmpeg -i out720x576.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python ../../nvidia-clara-agx/holoscan-sdk-scripts/convert_video_to_gxf_entities.py --width 720 --height 576 --channels 3 --framerate 30 --basename out720x576

ffmpeg -i out720x576-selection512x.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python ../../nvidia-clara-agx/holoscan-sdk-scripts/convert_video_to_gxf_entities.py --width 512 --height 484 --channels 3 --framerate 30 --basename out720x576-selection512x

```
https://github.com/nvidia-holoscan/holoscan-sdk/tree/main/scripts#convert_video_to_gxf_entitiespy
https://docs.nvidia.com/holoscan/sdk-user-guide/gxf/gxf_by_example.html  
https://docs.nvidia.com/clara-holoscan/archive/clara-holoscan-0.3.0/gxf/index.html


## Coping files to clara-agx
```
cd /workspace/holohub/data/colonoscopy_segmentation
cp ../../cmicHACKS2/data/polyp-dataset/out720x576.mp4 .
cp ../../cmicHACKS2/data/polyp-dataset/out720x576.gxf_* .
```




## Testing `raw.mp4` with `convert_video_to_gxf_entities.py`
```
mamba activate cagxVE

wget --content-disposition 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/clara-holoscan/holoscan_endoscopy_sample_data/20221121/files?redirect=true&path=video/raw.mp4' -O raw.mp4

wget --content-disposition 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/clara-holoscan/holoscan_colonoscopy_sample_data/20230222/files?redirect=true&path=colon_exam_720x576.mp4' -O colon_exam_720x576.mp4

ffmpeg -i raw.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python scripts/convert_video_to_gxf_entities.py --width 1920 --height 1080 --channels 3 --framerate 30 --basename raw

ffmpeg -i colon_exam_720x576.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python scripts/convert_video_to_gxf_entities.py --width 720 --height 576 --channels 3 --framerate 30 --basename colon_exam_720x576

```

errors

```

av_interleaved_write_frame(): Broken pipe
Error writing trailer of pipe:1: Broken pipeime=00:00:00.04 bitrate=248832.0kbits/s speed=1.83x    
frame=    1 fps=0.0 q=-0.0 Lsize=    1215kB time=00:00:00.04 bitrate=248832.0kbits/s speed=1.22x    
video:1215kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.000000%
Conversion failed!

```

https://catalog.ngc.nvidia.com/orgs/nvidia/teams/clara-holoscan/resources/holoscan_endoscopy_sample_data/files?version=20221121



## References 
https://stackoverflow.com/questions/22965569/convert-from-jpg-to-mp4-by-ffmpeg  
https://docs.nvidia.com/holoscan/sdk-user-guide/gxf/gxf_by_example.html   



