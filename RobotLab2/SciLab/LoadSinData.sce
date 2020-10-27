sin1Data = read(get_absolute_file_path("LoadSinData.sce") + "..\Data\sin_log1pi.txt", -1, 2)
sin1Data(:, 1) = sin1Data(:, 1)*%pi/180

sin2Data = read(get_absolute_file_path("LoadSinData.sce") + "..\Data\sin_log2pi.txt", -1, 2)
sin2Data(:, 1) = sin2Data(:, 1)*%pi/180

sin3Data = read(get_absolute_file_path("LoadSinData.sce") + "..\Data\sin_log3pi.txt", -1, 2)
sin3Data(:, 1) = sin3Data(:, 1)*%pi/180
