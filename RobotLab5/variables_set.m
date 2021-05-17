%% Physical parametrs
g = 9.81;                       % Gravity acceleration [m/sec^2]
m = 0.024; %0.05; 						% Wheel weight [kg]
R = 0.028; %0.0275; 						% Wheel radius [m]
Jk = m * R^2 / 2;%0.000014; %m * R^2 / 2;				% Wheel inertial moment [kg*m^2]
M = 0.75; %0.8;                        % Body mass [kg]
h = 0.11;						% Body height [m]
l = h / 2;						% Distance from the center of mass to the wheel axle [m]
Jt = M * l^2 / 3; %0.006414; M * l^2 / 3;              % Body inertia moment [kg*m^2]
%% Motors parameters
Umax = 8.2;                     % DC motor voltage [V]
J = 0.00237;					% DC motor inertia moment [kgm^2]
r = 2.5; %3;                          % DC motor resistance [Om]
km = 0.4872;%0.274;                     % Motor coefficient
ke = 0.4872;%0.274;                     % Motor coefficient
