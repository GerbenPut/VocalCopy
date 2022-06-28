eval "./youtube-dl.exe -x --audio-format wav --restrict-filenames $1"
wait
temp=`eval "./youtube-dl.exe --get-filename --restrict-filenames $1"`
file=${temp::-4}
echo $file
eval "python fastfourier.py $file"