results = read(get_absolute_file_path("LoadData.sce") + "..\Data\log100.txt", -1, 2);
angle = results(:, 1)*%pi/180;
time = results(:, 2)/1000;
//qlines = size(results, 1);
plot2d(time, angle, 2);

/*aim = [time, angle];
aim = aim';
deff('e=func(k, z)', 'e=z(2)-k(1)*(z(1) - k(2) * (1-exp(-z(1)/k(2))))');
att=[15;0.06];

[koeffs, errs] = datafit(func, aim, att);

Wnls = koeffs(1);
Tm = koeffs(2);

model = Wnls*(time-Tm*(1-exp(-time/Tm)));

Mst = J*Wnls / Tm
plot2d(time, model, 3);
plot2d(A.time, A.values, 5);*/
