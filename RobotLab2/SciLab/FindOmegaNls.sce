
Wnls = []

for i=1:10
    data = read(get_absolute_file_path("FindOmegaNls.sce") + "..\Data\log" + string(-i * 10) + ".txt", -1, 2);
    angle = data(:, 1)*%pi/180;
    time = data(:, 2);
    
    aim = [time, angle]';
    deff('e=curve(k, z)', 'e=z(2)-k(1)*(z(1) - k(2) * (1-exp(-z(1)/k(2))))');
    att=[-15;0.06];
    
    [koeffs, errs] = datafit(curve, aim, att);
    
    Wnls(i) = koeffs(1);
end
