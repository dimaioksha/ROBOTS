Theta_real = read(get_absolute_file_path("PlottingModelling.sce") + "..\Data\log100.txt", -1, 2)

plot2d(Theta.time, Theta.values, 3)
plot2d(Theta_real(:,1), Theta_real(:, 2), 5)
//plot2d()
//plot2d(Wdot.time, Wdot.values, 5)
