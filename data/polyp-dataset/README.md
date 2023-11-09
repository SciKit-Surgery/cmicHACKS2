# Kvasir-SEG dataset
> The Kvasir-SEG dataset (size 46.2 MB) contains 1000 polyp images and their corresponding ground truth from the Kvasir Dataset v2. The resolution of the images contained in Kvasir-SEG varies from 332x487 to 1920x1072 pixels. The images and its corresponding masks are stored in two separate folders with the same filename. The image files are encoded using JPEG compression, and online browsing is facilitated. The bounding box (coordinate points) for the corresponding images are stored in a JSON file. https://datasets.simula.no/downloads/kvasir-seg.zip


```
wget https://datasets.simula.no/downloads/kvasir-seg.zip #(45M)
unzip kvasir-seg.zip
```

## Converting images to video 
```
cd data/polyp-dataset/Kvasir-SEG/images
ffmpeg -framerate 1 -pattern_type glob -i 'Kvasir-SEG/images/ck*.jpg' -c:v libx264 out.mp4
```


## References 
https://stackoverflow.com/questions/22965569/convert-from-jpg-to-mp4-by-ffmpeg  
