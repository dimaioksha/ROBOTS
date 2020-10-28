Theta_real = read(get_absolute_file_path("PlottingModelling.sce") + "..\Data\log-20.txt", -1, 2)

Theta_real = Theta_real(1:112, :)
plot2d(Theta.time, Theta.values, 3)
plot2d(Theta_real(:,2), Theta_real(:, 1)*%pi/180, 5)
//plot2d()
//plot2d(Wdot.time, Wdot.values, 5)

