# Kvasir-SEG dataset
> The Kvasir-SEG dataset (size 46.2 MB) contains 1000 polyp images and their corresponding ground truth from the Kvasir Dataset v2. The resolution of the images contained in Kvasir-SEG varies from 332x487 to 1920x1072 pixels. The images and its corresponding masks are stored in two separate folders with the same filename. The image files are encoded using JPEG compression, and online browsing is facilitated. The bounding box (coordinate points) for the corresponding images are stored in a JSON file. https://datasets.simula.no/downloads/kvasir-seg.zip

```
wget https://datasets.simula.no/downloads/kvasir-seg.zip #(45M)
unzip kvasir-seg.zip
rm kvasir-seg.zip
```

## Converting images to video 
* converting ck images to video
```
cd data/polyp-dataset/Kvasir-SEG/images
ffmpeg -framerate 30 -pattern_type glob -i 'Kvasir-SEG/images/ck*.jpg' -c:v libx264 out720x576.mp4
```
* converting selected images to video
```
 #cp images/ck2bxknhjvs1x0794iogrq49k.jpg selected/
 #cp images/cju16jgnyzp970878melv7r25.jpg selected/
 #cp images/cju33w4sdcivk0855x879zht7.jpg selected/
 #cp images/cju85omszllp30850b6rm9mi3.jpg selected/
ffmpeg -framerate 30 -pattern_type glob -i 'Kvasir-SEG/selected-512x/*.jpg' -c:v libx264 out720x576-selection512x.mp4
```

* converting resized selected images to video
```
 #convert cju16jgnyzp970878melv7r25.jpg -resize 512x cju16jgnyzp970878melv7r25.jpg
 #convert cju33w4sdcivk0855x879zht7.jpg -resize 512x cju33w4sdcivk0855x879zht7.jpg
 #convert cju85omszllp30850b6rm9mi3.jpg -resize 512x cju85omszllp30850b6rm9mi3.jpg
 #convert ck2bxknhjvs1x0794iogrq49k.jpg -resize 512x ck2bxknhjvs1x0794iogrq49k.jpg
ffmpeg -framerate 30 -pattern_type glob -i 'Kvasir-SEG/selected-512x/*.jpg' -c:v libx264 out720x576-selection512x.mp4
```
* converting one selected image to video
```
cd $HOME/repositories/scikit-surgery/cmicHACKS2/data/polyp-dataset/Kvasir-SEG/
cp -r selected selected-ck2bxknhjvs1x0794iogrq49k-512x-01-frames #same for other frames
cp -r selected selected-ck2bxknhjvs1x0794iogrq49k-512x-05-frames #and create copies of the same image
convert *.jpg -resize 512x *.jpg #only height
convert *.jpg -resize 512x512! *.jpg #hegith and width

cd $HOME/repositories/scikit-surgery/cmicHACKS2/data/polyp-dataset

#ffmpeg -framerate 30 -pattern_type glob -i 'Kvasir-SEG/selected-ck2bxknhjvs1x0794iogrq49k-512x-01-frames/*.jpg' -c:v libx264 out512x448-selected-ck2bxknhjvs1x0794iogrq49k-01-frames.mp4 #don't work 4 1frame
ffmpeg -framerate 30 -pattern_type glob -i 'Kvasir-SEG/selected-ck2bxknhjvs1x0794iogrq49k-05-frames/*.jpg' -c:v libx264 -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" out602x528-selected-ck2bxknhjvs1x0794iogrq49k-05-frames.mp4

ffmpeg -framerate 30 -pattern_type glob -i 'Kvasir-SEG/selected-ck2bxknhjvs1x0794iogrq49k-512x-05-frames/*.jpg' -c:v libx264 -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" out512x448-selected-ck2bxknhjvs1x0794iogrq49k-05-frames.mp4

ffmpeg -framerate 30 -pattern_type glob -i 'Kvasir-SEG/selected-ck2bxknhjvs1x0794iogrq49k-512x-512x-05-frames/*.jpg' -c:v libx264 -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" out512x512-selected-ck2bxknhjvs1x0794iogrq49k-05-frames.mp4


## check video
vlc out602x528-selected-ck2bxknhjvs1x0794iogrq49k-05-frames.mp4 

```

References: 
* https://www.networkworld.com/article/3697731/resizing-images-on-the-linux-command-line.html
* https://stackoverflow.com/questions/20847674/ffmpeg-libx264-height-not-divisible-by-2 

## Using `ffmeg` and `convert_video_to_gxf_entities.py`  (Graph Execution Framework, GXF)
```
mamba activate cagxVE
#ffmpeg -i *.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python ../../nvidia-clara-agx/holoscan-sdk-scripts/convert_video_to_gxf_entities.py --width 512 --height 484 --channels 3 --framerate 30 --basename *
#ffmpeg -i out.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python convert_video_to_gxf_entities.py --width 1920 --height 1080 --channels 3 --framerate 1 --basename out
#ffmpeg -i out.mp4 -pix_fmt yuvj422p -f rawvideo pipe:1 | python convert_video_to_gxf_entities.py --width 600 --height 500 --channels 3 --framerate 1 --basename out
ffmpeg -i out720x576.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python ../../nvidia-clara-agx/holoscan-sdk-scripts/convert_video_to_gxf_entities.py --width 720 --height 576 --channels 3 --framerate 30 --basename out720x576

ffmpeg -i out720x576-selection512x.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python ../../nvidia-clara-agx/holoscan-sdk-scripts/convert_video_to_gxf_entities.py --width 512 --height 484 --channels 3 --framerate 30 --basename out720x576-selection512x


ffmpeg -i out602x528-selected-ck2bxknhjvs1x0794iogrq49k-05-frames.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python ../../nvidia-clara-agx/holoscan-sdk-scripts/convert_video_to_gxf_entities.py --width 602 --height 528 --channels 3 --framerate 30 --basename out602x528-selected-ck2bxknhjvs1x0794iogrq49k-05-frames


ffmpeg -i out512x448-selected-ck2bxknhjvs1x0794iogrq49k-05-frames.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python ../../nvidia-clara-agx/holoscan-sdk-scripts/convert_video_to_gxf_entities.py --width 602 --height 528 --channels 3 --framerate 30 --basename out512x448-selected-ck2bxknhjvs1x0794iogrq49k-05-frames

ffmpeg -i out512x512-selected-ck2bxknhjvs1x0794iogrq49k-05-frames.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python ../../nvidia-clara-agx/holoscan-sdk-scripts/convert_video_to_gxf_entities.py --width 602 --height 528 --channels 3 --framerate 30 --basename out512x512-selected-ck2bxknhjvs1x0794iogrq49k-05-frames


```
https://github.com/nvidia-holoscan/holoscan-sdk/tree/main/scripts#convert_video_to_gxf_entitiespy
https://docs.nvidia.com/holoscan/sdk-user-guide/gxf/gxf_by_example.html  
https://docs.nvidia.com/clara-holoscan/archive/clara-holoscan-0.3.0/gxf/index.html




## Testing `raw.mp4` with `convert_video_to_gxf_entities.py`
```
mamba activate cagxVE

wget --content-disposition 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/clara-holoscan/holoscan_endoscopy_sample_data/20221121/files?redirect=true&path=video/raw.mp4' -O raw.mp4

wget --content-disposition 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/clara-holoscan/holoscan_colonoscopy_sample_data/20230222/files?redirect=true&path=colon_exam_720x576.mp4' -O colon_exam_720x576.mp4

ffmpeg -i raw.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python scripts/convert_video_to_gxf_entities.py --width 1920 --height 1080 --channels 3 --framerate 30 --basename raw

ffmpeg -i colon_exam_720x576.mp4 -pix_fmt rgb24 -f rawvideo pipe:1 | python scripts/convert_video_to_gxf_entities.py --width 720 --height 576 --channels 3 --framerate 30 --basename colon_exam_720x576

```

https://catalog.ngc.nvidia.com/orgs/nvidia/teams/clara-holoscan/resources/holoscan_endoscopy_sample_data/files?version=20221121

## References 
https://stackoverflow.com/questions/22965569/convert-from-jpg-to-mp4-by-ffmpeg  
https://docs.nvidia.com/holoscan/sdk-user-guide/gxf/gxf_by_example.html   

