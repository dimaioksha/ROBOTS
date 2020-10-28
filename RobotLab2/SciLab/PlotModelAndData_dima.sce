idx = string(currIdx * 10)

data = read(get_absolute_file_path("PlotModelAndData_dima.sce") + "..\Data\log" + idx + ".txt", -1, 2);
data(:, 1) = data(:, 1)*%pi/180

fprintfMat(get_absolute_file_path("PlotModelAndData_dima.sce") + "..\Sim\Theta_simply_Sim" + idx + ".txt",[Theta_simplified.values Theta_simplified.time], "%.5f");
fprintfMat(get_absolute_file_path("PlotModelAndData_dima.sce") + "..\Sim\ThetaDot_simply_Sim" + idx + ".txt",[W_simplified.values W_simplified.time], "%.5f");

plot2d(data(:, 2), data(:, 1), 3)
plot2d(Theta_simplified.time, Theta_simplified.values, 2)
plot2d(W_simplified.time, W_simplified.values, 2)
