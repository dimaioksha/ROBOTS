results = read(get_absolute_file_path("LoadData.sce") + "..\Data\log" + currIdx + ".txt", -1, 2);
angle = results(:, 1)*%pi/180;
time = results(:, 2)/1000;
plot2d(time, angle, 2);
