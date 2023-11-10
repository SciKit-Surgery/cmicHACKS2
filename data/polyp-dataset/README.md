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
ffmpeg -framerate 1 -pattern_type glob -i 'Kvasir-SEG/images/ck*.jpg' -c:v libx264 out.mp4
```


## Using `convert_video_to_gxf_entities.py`
```
mamba activate cagxVE
#ffmpeg -i out.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python convert_video_to_gxf_entities.py --width 1920 --height 1080 --channels 3 --framerate 1 --basename out
#ffmpeg -i out.mp4 -pix_fmt yuvj422p -f rawvideo pipe:1 | python convert_video_to_gxf_entities.py --width 600 --height 500 --channels 3 --framerate 1 --basename out
ffmpeg -i out.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python convert_video_to_gxf_entities.py --width 600 --height 500 --channels 3 --framerate 1 --basename out
```
https://github.com/nvidia-holoscan/holoscan-sdk/tree/main/scripts#convert_video_to_gxf_entitiespy

## Testing `raw.mp4` with `convert_video_to_gxf_entities.py`
```
wget --content-disposition 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/clara-holoscan/holoscan_endoscopy_sample_data/20221121/files?redirect=true&path=video/raw.mp4' -O raw.mp4
ffmpeg -i raw.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python scripts/convert_video_to_gxf_entities.py --width 1920 --height 1080 --channels 3 --framerate 30 --basename raw
```
https://catalog.ngc.nvidia.com/orgs/nvidia/teams/clara-holoscan/resources/holoscan_endoscopy_sample_data/files?version=20221121



## References 
https://stackoverflow.com/questions/22965569/convert-from-jpg-to-mp4-by-ffmpeg  
https://docs.nvidia.com/holoscan/sdk-user-guide/gxf/gxf_by_example.html   



