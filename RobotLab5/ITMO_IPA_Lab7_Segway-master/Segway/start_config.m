%% Init parameters
Psi0 = pi/12;                   % Initial body angle [Rad]
Psi_d0 = 0;                     % Initial body speed [Rad/sec]
Theta_d0 = 0;                   % Initial wheel speed [Rad/sec]
%% K parameters
Tp = 0.4;                       % Real transient time [sec]
Tp_z = 6.3;                     % Theoretical transient time  (n=3, Tp_z=6.3) [sec]
K_mode = 0;                     % K mode: 0-hand mode, 1- Ackerman mode, other - auto mode   