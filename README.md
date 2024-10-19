The included `example.mp4` movie for 100 randomly distributed integer points was produced with `ffmpeg`:
```
$ffmpeg -framerate 8 -pattern_type glob -i './frames/*.png' -c:v libx264 -r 30 -pix_fmt yuv420p example.mp4
```

