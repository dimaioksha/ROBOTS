
plot2d(fwData(:, 2), fwData(:, 1), 3);
xs = [fwData(1, 2), fwData(10, 2)]
ys = [R * xs(1), R * xs(2)]
plot2d(xs, ys, 2);

data = rvData'
plot2d(rvData(:, 2), rvData(:, 1), 3);
xs = [rvData(1, 2), rvData(10, 2)]
ys = [R * xs(1), R * xs(2)]
plot2d(xs, ys, 2);
