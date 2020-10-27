plot2d(fwData(:, 2), fwData(:, 1), 2);
xs = [fwData(1, 2), 0]
ys = [R * xs(1), R * xs(2)]
plot2d(xs, ys, 5);



plot2d(rvData(:, 2), rvData(:, 1), 3);
xs = [0, rvData(10, 2)]
ys = [R * xs(1), R * xs(2)]
plot2d(xs, ys, 2);
