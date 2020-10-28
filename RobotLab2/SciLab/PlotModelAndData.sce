idx = string(currIdx * 10)

data = read(get_absolute_file_path("PlotModelAndData.sce") + "..\Data\log" + idx + ".txt", -1, 2);
data(:, 1) = data(:, 1)*%pi/180

fprintfMat(get_absolute_file_path("PlotModelAndData.sce") + "..\Sim\ThetaSim" + idx + ".txt",[Theta.values Theta.time], "%.5f");
fprintfMat(get_absolute_file_path("PlotModelAndData.sce") + "..\Sim\ThetaDotSim" + idx + ".txt",[ThetaDot.values ThetaDot.time], "%.5f");

plot2d(data(:, 2), data(:, 1), 3)
plot2d(Theta.time, Theta.values, 2)
plot2d(ThetaDot.time, ThetaDot.values, 2)
