aim = [time, angle]';
deff('e=curve(k, z)', 'e=z(2)-k(1)*(z(1) - k(2) * (1-exp(-z(1)/k(2))))');
att=[15;0.06];

[koeffs, errs] = datafit(curve, aim, att);

Wnls = koeffs(1);
Tm = koeffs(2);

model = Wnls*(time-Tm*(1-exp(-time/Tm)));

J = 0.0023;
Mst = J*Wnls / Tm;
plot2d(time, model, 3);
